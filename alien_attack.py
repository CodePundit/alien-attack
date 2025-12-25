import sys
import pygame
from time import sleep

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


class AlienAttack:
    """Main class to manage the game"""

    def __init__(self):
        """Init the pygame system and create resources"""
        pygame.init()

        self.settings = Settings()
        # self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Attack")

        self.game_stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_alien_fleet()

        # Making the Play button
        self.play_button = Button(self, "Play")


    def _check_events(self):
        """ Watch for keyword and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._key_down(event)
            elif event.type == pygame.KEYUP:
                self._key_up(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                self._check_Play_clicked(mouse_position)


    def _key_down(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()


    def _key_up(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.built_me()

        # Drawing each bullet
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)

        # Draw the scores on the screen
        self.sb.draw()

        # Draw the Play button if the game is in active
        if not self.game_stats.is_game_active():
            self.play_button.draw_button()

        # Make the most recent screen visible
        pygame.display.flip()


    def _update_bullets(self):
        """Showing, updating positions and clearing off bullets"""
        # Clearing off bullets
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        # Showing bullets and updating their positions
        self.bullets.update()

        self._check_collisions()


    def _fire_bullet(self):
        """Create a new Bullet object and add it to bullets sprite group"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    def _check_collisions(self):
        # Checking if any bullets has hit an alien, if yes remove them both
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if collisions:
            for alien_list in collisions.values():
                self.game_stats.score += self.settings.alien_killing_score * len(alien_list)
            self.sb.update_score()

        if not self.aliens:
            """Destroy existing bullets on screen and create a new fleet"""
            self.bullets.empty()
            self._create_alien_fleet()
            self.settings.level_up()
            self.game_stats.level_up()
            self.sb.update_level_number()


    def _update_aliens(self):
        """check if the fleet is hitting game screen edge, then update position of all aliens"""
        self._check_fleet_edges()
        # Updating positions of all aliens via Sprite group
        self.aliens.update()

        # Check if any alien hit our ship
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # checking if any alien has reached to the bottom if screen - game over
        self._check_alien_bottom()


    def _ship_hit(self):
        """Responding to the ship hit by an alien"""
        self.game_stats.lost_a_game()
        self.bullets.empty()
        self.aliens.empty()

        self._create_alien_fleet()
        self.ship.center_ship()

        sleep(self.settings.delay)

        self.sb.update_remaining_ships()

        if not self.game_stats.is_game_active():
            pygame.mouse.set_visible(True)


    def _check_alien_bottom(self):
        """Check if any alien has reached at the bottom of the screen"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # treat this same as an alien hit the ship
                self._ship_hit()
                break


    def _create_alien_fleet(self):
        """Create a fleet of Aliens and add it to aliens sprite group"""
        # Create an Alien and find how many we can fit in a row
        # space between two aliens is same as their width
        temp_alien = Alien(self)
        alien_width, alien_height = temp_alien.rect.size

        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_of_aliens_in_a_row = available_space_x // (2 * alien_width)

        # Determine the number of alien rows that can fit on screen
        ship_height = self.ship.rect.height
        available_space_y = self.settings.screen_height - ship_height - (3 * alien_height)
        number_of_aliens_rows = available_space_y // (2 * alien_height)

        # Create all alien rows (full fleet)
        for row_number in range(number_of_aliens_rows):
            for alien_number_in_row in range(number_of_aliens_in_a_row):
                self._create_alien(alien_number_in_row, row_number)


    def _create_alien(self, alien_number_in_row: int, row_number: int):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.rect.x = alien_width + (2 * alien_width * alien_number_in_row)
        alien.x_position = alien.rect.x
        alien.rect.y = alien_height + (2 * alien_height * row_number)
        self.aliens.add(alien)


    def _check_fleet_edges(self):
        """Checking if any alien is hitting edge and changing direction on first encounter"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break


    def _change_fleet_direction(self):
        """Drop the entire fleet and change its direction"""
        for alien in self.aliens.sprites():
            alien.drop_alien_location()

        self.settings.alien_fleet_direction *= -1


    def _check_Play_clicked(self, mouse_position):
        """Start a new game if the player clicked play"""
        if self.play_button.rect.collidepoint(mouse_position) and not self.game_stats.is_game_active():
            self.game_stats.reset()
            self.settings.init_dynamic_settings()
            # Hide the mouse curser
            pygame.mouse.set_visible(False)
            # Clear the previous game score from screen
            self.sb.update_score()
            self.sb.update_level_number()
            self.sb.update_remaining_ships()


    def run_game(self):
        """Start the main game loop"""
        while True:
            self._check_events()

            if self.game_stats.is_game_active():
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()


if __name__ == '__main__':
    # Make a game instance and run it
    mygame = AlienAttack()
    mygame.run_game()
