import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

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

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()


    def _check_events(self):
        """ Watch for keyword and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._key_down(event)
            elif event.type == pygame.KEYUP:
                self._key_up(event)


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


        # Make the most recent screen visible
        pygame.display.flip()


    def _manage_bullets(self):
        """Showing, updating positions and clearing off bullets"""
        # Clearing off bullets
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # print(len(self.bullets))

        # Showing and updating positions
        self.bullets.update()


    def _fire_bullet(self):
        """Create a new Bullet object and add it to bullets sprite group"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    def run_game(self):
        """Start the main game loop"""
        while True:
            self._check_events()
            self.ship.update()
            self._manage_bullets()
            self._update_screen()


if __name__ == '__main__':
    # Make a game instance and run it
    mygame = AlienAttack()
    mygame.run_game()