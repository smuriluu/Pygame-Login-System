import pygame
import requests
from scripts.gui import Label, Button, TextBox
from scripts.assets import COURIER_PRIME, COURIER_PRIME_BOLD
from scripts.dotenv import API_NEW_USER

class Registration():
    '''
    Handles the game menu, including buttons, sliders, and user interactions.
    '''
    def __init__(self, game):
        '''
        Initializes the menu, creating a new screen and menu elements.
        '''
        # Reference to the main game instance.
        self.game = game
        # Access game settings.
        self.settings = game.settings
        # Access the game's screen.
        self.screen = game.screen
        # Setup a new menu screen.
        self.new_screen()
    
    def new_screen(self):
        '''
        Creates a new surface for the menu and initializes menu components.
        '''
        # Create a menu surface with the same size as the game screen.
        self.menu_screen = pygame.Surface((self.screen.WIDTH, self.screen.HEIGHT))

        # Create text and button elements for the menu.
        self.title = Label(self.menu_screen, font_size=65, font=COURIER_PRIME_BOLD)
        self.text = Label(self.menu_screen, font_size=50, font=COURIER_PRIME)
        self.send_button = Button(self.menu_screen, pos=(self.screen.WIDTH/2, 600), text_font_size=50, text_font=COURIER_PRIME, border_radius=20)
        self.username_text_box = TextBox(self.menu_screen, (self.screen.WIDTH/2, 200), size=(500, 50), border=2, transparency=-1, border_radius=20, text_font_size=30, text_font=COURIER_PRIME)
        self.password_text_box = TextBox(self.menu_screen, (self.screen.WIDTH/2, 350), size=(500, 50), border=2, transparency=-1, border_radius=20, password=True, text_font_size=30, text_font=COURIER_PRIME)
        self.confirm_password_text_box = TextBox(self.menu_screen, (self.screen.WIDTH/2, 500), size=(500, 50), border=2, transparency=-1, border_radius=20, password=True, text_font_size=30, text_font=COURIER_PRIME)
        self.footer_text = ''

    def run(self):
        '''
        Main loop to handle menu logic.
        '''
        # Process events.
        self.events()
        # Update logic (if any).
        self.update()
        # Render menu elements.
        self.draw()
        # Handle user interactions.
        self.inputs()
    
    def update(self):
        '''
        Update menu components (currently unused).
        '''
        pass

    def events(self):
        '''
        Handle pygame events, including quitting the game.
        '''
        for event in pygame.event.get():
            # Quit the game if the window is closed.
            if event.type == pygame.QUIT:
                self.game.running = False
            self.username_text_box.event(event)
            self.password_text_box.event(event)
            self.confirm_password_text_box.event(event)
        
    def draw(self):
        '''
        Draw the menu on the screen.
        '''
        # Scale the menu surface to fit the display surface.
        self.screen.scale_screen(self.menu_screen)
        # Fill the menu background with white.
        self.menu_screen.fill((255,255,255))
        self.title.write(self.settings.game_texts['create_account'], (int(self.screen.WIDTH/2), 0), center_w=True)
        self.send_button.draw(self.settings.game_texts['sing_up'])
        self.text.write(self.settings.game_texts['username'], (int(self.screen.WIDTH/2), 100), center_w=True)
        self.username_text_box.draw()
        self.text.write(self.settings.game_texts['password'], (int(self.screen.WIDTH/2), 250), center_w=True)
        self.password_text_box.draw()
        self.text.write(self.settings.game_texts['confirm_password'], (int(self.screen.WIDTH/2), 400), center_w=True)
        self.confirm_password_text_box.draw()

        self.text.write(self.footer_text, (int(self.screen.WIDTH/2), 650), center_w=True)

    def inputs(self):
        '''
        Handle inputs, such as button clicks and slider interactions.
        '''
        # Handle resolution buttons.
        if self.send_button.click(self.screen.aspect_ratio):
            if self.password_text_box.text == '' or self.confirm_password_text_box.text == '' or self.username_text_box.text == '':
                self.footer_text = 'Preencha todos os campos'
            elif self.password_text_box.text != self.confirm_password_text_box.text:
                self.footer_text = 'As senhas devem ser identicas'
            else:
                json = {
                    'username': self.username_text_box.text,
                    'password': self.password_text_box.text
                }
                response = requests.post(API_NEW_USER, json=json)
                if response.status_code == 201:
                    self.footer_text = response.json().get('message')
                    self.password_text_box.text = ''
                    self.confirm_password_text_box.text = ''
                    self.username_text_box.text = ''
                else:
                    self.footer_text = response.json().get('error')

        # Handle text_box interaction.
        self.username_text_box.click(self.screen.aspect_ratio)
        self.password_text_box.click(self.screen.aspect_ratio)
        self.confirm_password_text_box.click(self.screen.aspect_ratio)
