import pygame
from scripts.screen import Screen
from scripts.settings import Settings
from canvas.login import Login

class Main():
    '''
    Manages the main loop and game states for the application.
    '''
    def __init__(self):
        '''
        Initializes the game by setting up required components like settings, screen, and login.
        '''
        # Initialize Pygame.
        pygame.init()
        # Create an instance of the Settings class to manage configuration.
        self.settings = Settings()
        # Create an instance of the Screen class, passing the settings to configure the display.
        self.screen = Screen(self.settings)
        # A flag to control the main game loop.
        self.running = True
        # Set the initial game state to 'login'.
        self.game_state = 'login'
        # Create an instance of the login class, passing the current Main instance for access to shared resources.
        self.login = Login(self)
    
    def run(self):
        '''
        Runs the main game loop. 
        Continuously updates the game state and renders the screen until the game is exited.
        '''
        while self.running:
            # Calculate the time elapsed since the last frame (delta time) for consistent animations and logic.
            self.screen.delta_time()
            # Handle user inputs and manage transitions between game states.
            self.controller()
            # Refresh the screen to reflect changes.
            self.screen.screen_update()
        # Exit the game and clean up resources.
        pygame.quit()

    def controller(self):
        '''
        Manages the game state and directs control to the appropriate handler for the current state.
        '''
        # If the game is currently in the 'login' state, execute the login logic.
        if self.game_state == 'login':
            self.login.run()

# Ensure the script runs only if executed directly, not when imported.
if __name__ == '__main__':
    Main().run()
