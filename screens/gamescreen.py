import pygame
pygame.init()
from .base import BaseScreen
from components.player import Player
from components.zombie import Zombie
from globalvars import WIDTH, HEIGHT

class GameScreen(BaseScreen):
    """Screen for the game

    Args:
        BaseScreen (screen): base screen of the game
    """
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        
        # Keep username and final score as None - nothing to do with them here
        self.username = None
        self.password = None
        self.final_score = None

        self.start_time = pygame.time.get_ticks() // 1000

        # Manage player timer
        self.counter = 300
        pygame.time.set_timer(pygame.USEREVENT, 1000) # Set the time counter

        # Create the player and manage movements
        self.player = Player(WIDTH // 2, 350, 0.2, speed=5)
        self.move_left = False
        self.move_right = False
        self.shoot = False
        self.score = -1 # Start with -1 to avoid the first jump = 0 score

        # Create zombie group and spawn timer
        self.zombie_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.zombie_timer, 1500) # Every 1.5s, a zombie will spawn
        self.zombie_group = pygame.sprite.Group()

        # Create player group
        self.player_group = pygame.sprite.Group() # For collision and methods
        self.player_group.add(self.player)

    def display_score(self):
        """Method to display the score
        """
        score_font = pygame.font.Font("fonts/minecraft.ttf", 50)
        score_text_surface = score_font.render(f"Score: {self.score}", False, "Black")
        self.window.blit(score_text_surface, (WIDTH // 96, 490))

    def display_health(self):
        """Method to display the health point
        """
        health_font = pygame.font.Font("fonts/minecraft.ttf", 50)
        health_text_surface = health_font.render(f"Health: {self.player.health}", False, "Green")
        self.window.blit(health_text_surface, (720, 490))

    def display_timer(self):
        """Method to display game timer
        """
        counter_font = pygame.font.Font("fonts/minecraft.ttf", 50)
        timer_text_surface = counter_font.render(f"Time left: {self.counter}", False, "Red")
        self.window.blit(timer_text_surface, (585, 20))

    def draw(self):
        """Keep drawing the player, zombie, the score, and the health point
        """
        if self.player.is_alive:
            # Shoot bullets
            if self.shoot:
                self.player.shoot()

            if self.player.in_the_air:
                # Add score for jumping
                self.score += 1
                # Jump animation
                self.player.update_action(2)

            elif self.move_left or self.move_right:
                # Run animation
                self.player.update_action(1)

            else:
                # Stand animation
                self.player.update_action(0)

            self.player.move(self.move_left, self.move_right)
        
        # Draw the player and the zombie
        self.player.draw(self.window)
        self.zombie_group.update()
        self.zombie_group.draw(self.window)
        
        # Draw the score, the health point, and the timer
        self.display_score()
        self.display_health()
        self.display_timer()

    def update(self):
        """Keep updating any changes made during the game
        """
        self.player_group.update()

        # Check collision - kill kill zombie sprite and reduce player hp
        if pygame.sprite.groupcollide(self.player_group, self.zombie_group, 0, 1).keys():
            take_dmg = pygame.mixer.Sound("audio/hurt.mp3")
            take_dmg.set_volume(1)
            take_dmg.play()
            self.player.health -= 1
        
        # Go to game over screen if player dies
        if self.player.health == 0:
            self.start_time += pygame.time.get_ticks() // 1000
            # Move to game over screen
            self.final_score = self.score
            self.next_screen = "game_over"
            self.running = False
        
        # Check collision - kill zombie sprite on bullet collision
        if pygame.sprite.groupcollide(self.zombie_group, self.player.bullet_group, 1, 1).keys():
            zombie_sound = pygame.mixer.Sound("audio/zombie.mp3")
            zombie_sound.set_volume(0.5)
            zombie_sound.play()
            self.score += 55
        
    def manage_event(self, event):
        """Manage all events done during the game screen

        Args:
            event (event): a pygame event
        """

        # Decrease the game timer
        if event.type == pygame.USEREVENT:
            if self.counter > 0:
                self.counter -= 1
            else:
                self.final_score = self.score
                self.next_screen = "game_over"
                self.running = False

        # Spawn zombie every 1.5s and add it to the zombie group
        if event.type == self.zombie_timer:
            self.zombie_group.add(Zombie(0.3))

        # Manage player movement upon pressing the keys
        if event.type == pygame.KEYDOWN:
            # If player presses left key
            if event.key == pygame.K_a:
                self.move_left = True
            # If player presses right key
            if event.key == pygame.K_d:
                self.move_right = True
            # If player presses L key
            if event.key == pygame.K_l:
                self.shoot = True
            # If player presses space key
            if event.key == pygame.K_SPACE and self.player.is_alive:
                self.player.jump = True
    
        # Manage player movement upon lifting the keys
        if event.type == pygame.KEYUP:
            # If player lets go of left key
            if event.key == pygame.K_a:
                self.move_left = False
            # If player lets go of right key
            if event.key == pygame.K_d:
                self.move_right = False
            # If player lets go of the L key
            if event.key == pygame.K_l:
                self.shoot = False