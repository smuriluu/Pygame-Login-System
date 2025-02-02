import pygame
import requests
from scripts.gui import Label, Button, TextBox, Panel
from scripts.assets import COURIER_PRIME, COURIER_PRIME_BOLD
from scripts.dotenv import *

class Login():
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
        self.surface = pygame.Surface((self.screen.WIDTH, self.screen.HEIGHT))

        # Create text and button elements for the menu.
        self.title = Label(self.surface, font_size=50, font=COURIER_PRIME_BOLD)
        self.msg_text_text = Label(self.surface, font_size=25, font=COURIER_PRIME)
        self.sing_in_button = Button(self.surface, self.screen.aspect_ratio, (self.screen.WIDTH/4, (self.screen.HEIGHT - self.screen.HEIGHT/4)), size=(280, 70), text_font_size=25, text_font=COURIER_PRIME_BOLD, border_radius=30, text_color=(255,255,255), text_hover_color=(255,255,255))
        self.sing_up_button = Button(self.surface, self.screen.aspect_ratio, (self.screen.WIDTH - self.screen.WIDTH/4, (self.screen.HEIGHT - self.screen.HEIGHT/5)), size=(280, 70), text_font_size=25, text_font=COURIER_PRIME_BOLD, border_radius=30, text_color=(255,255,255), text_hover_color=(255,255,255), visible=False)
        self.sing_in_username_tb = TextBox(self.surface, self.screen.aspect_ratio, (self.screen.WIDTH/4,  self.screen.HEIGHT/2.8), size=(460, 70), tb_color=(200, 200, 200), text_font_size=25, display_text_color=(120,120,120), text_font=COURIER_PRIME, display_text=self.settings.game_texts['username'])
        self.sing_up_username_tb = TextBox(self.surface, self.screen.aspect_ratio, (self.screen.WIDTH - self.screen.WIDTH/4,  self.screen.HEIGHT/2.5), size=(460, 70), tb_color=(200, 200, 200), text_font_size=25, display_text_color=(120,120,120), text_font=COURIER_PRIME, display_text=self.settings.game_texts['username'], visible=False)
        self.sing_in_password_tb = TextBox(self.surface, self.screen.aspect_ratio, (self.screen.WIDTH/4, self.screen.HEIGHT/2), size=(460, 70), tb_color=(200, 200, 200), text_font_size=25, display_text_color=(120,120,120), password=True, text_font=COURIER_PRIME, display_text=self.settings.game_texts['password'])
        self.sing_up_password_tb = TextBox(self.surface, self.screen.aspect_ratio, (self.screen.WIDTH - self.screen.WIDTH/4, self.screen.HEIGHT - self.screen.HEIGHT/2.2), size=(460, 70), tb_color=(200, 200, 200), text_font_size=25, display_text_color=(120,120,120), password=True, text_font=COURIER_PRIME, display_text=self.settings.game_texts['password'], visible=False)
        self.sing_up_confirm_password_tb = TextBox(self.surface, self.screen.aspect_ratio, (self.screen.WIDTH - self.screen.WIDTH/4, self.screen.HEIGHT - self.screen.HEIGHT/3.2), size=(460, 70), tb_color=(200, 200, 200), text_font_size=25, display_text_color=(120,120,120), password=True, text_font=COURIER_PRIME, display_text=self.settings.game_texts['confirm_password'], visible=False)
        self.forgot_password_button = Button(self.surface, self.screen.aspect_ratio, (self.screen.WIDTH/4, (self.screen.HEIGHT - self.screen.HEIGHT/2.8)), size=(300, 75), text_font_size=25, text_font=COURIER_PRIME, transparency=-1, text_color=(100,100,100))
        self.panel = Panel(self.surface, self.screen.aspect_ratio, (self.screen.WIDTH/2,0), size=(self.screen.WIDTH/2,self.screen.HEIGHT))
        self.panel_sing_up_button = Button(self.surface, self.screen.aspect_ratio, (self.screen.WIDTH - self.screen.WIDTH/4, (self.screen.HEIGHT - self.screen.HEIGHT/3)), size=(280, 70), text_font_size=25, text_font=COURIER_PRIME_BOLD, border_radius=30, text_color=(255,255,255), text_hover_color=(255,255,255), transparency=-1, border=2, border_color=(255,255,255))
        self.panel_sing_in_button = Button(self.surface, self.screen.aspect_ratio, (self.screen.WIDTH/4, (self.screen.HEIGHT - self.screen.HEIGHT/3)), size=(280, 70), text_font_size=25, text_font=COURIER_PRIME_BOLD, border_radius=30, text_color=(255,255,255), text_hover_color=(255,255,255), transparency=-1, border=2, border_color=(255,255,255), visible=False)
        self.msg_text = ''
        self.msg_pos_x = self.screen.WIDTH/4
    
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
        self.panel.update(self.screen.dt)
        if self.panel.panel_rect.left < 0:
            self.panel_sing_in_button.visible = True
            self.panel.panel_rect.left = 0
            self.panel.stop()

            self.sing_in_username_tb.text = ''
            self.sing_in_username_tb.visible = False
            self.sing_in_password_tb.text = ''
            self.sing_in_password_tb.visible = False
            self.forgot_password_button.visible = False
            self.sing_in_button.visible = False
            self.msg_text = ''
            self.msg_pos_x = self.screen.WIDTH - self.screen.WIDTH/4
        
        if self.panel.panel_rect.right > self.screen.WIDTH:
            self.panel_sing_up_button.visible = True
            self.panel.panel_rect.right = self.screen.WIDTH
            self.panel.stop()

            self.sing_up_password_tb.text = ''
            self.sing_up_password_tb.visible = False
            self.sing_up_username_tb.text = ''
            self.sing_up_username_tb.visible = False
            self.sing_up_confirm_password_tb.text = ''
            self.sing_up_confirm_password_tb.visible = False
            self.sing_up_button.visible = False
            self.msg_text = ''
            self.msg_pos_x = self.screen.WIDTH/4

    def events(self):
        '''
        Handle pygame events, including quitting the game.
        '''
        for event in pygame.event.get():
            # Quit the game if the window is closed.
            if event.type == pygame.QUIT:
                self.game.running = False
            self.sing_in_username_tb.event(event)
            self.sing_up_username_tb.event(event)
            self.sing_in_password_tb.event(event)
            self.sing_up_password_tb.event(event)
            self.sing_up_confirm_password_tb.event(event)
        
    def draw(self):
        '''
        Draw the menu on the screen.
        '''
        self.screen.scale_screen(self.surface)
        self.surface.fill((255,255,255))

        self.title.write(self.settings.game_texts['title'], (int(self.screen.WIDTH/4), int(self.screen.HEIGHT/4)), center_w=True, center_h=True)
        self.title.write(self.settings.game_texts['create_account'], (int(self.screen.WIDTH - self.screen.WIDTH/4), int(self.screen.HEIGHT/4)), center_w=True, center_h=True)
        self.sing_in_username_tb.draw()
        self.sing_up_username_tb.draw()
        self.sing_in_password_tb.draw()
        self.sing_up_password_tb.draw()
        self.sing_up_confirm_password_tb.draw()
        self.forgot_password_button.draw(self.settings.game_texts['forgot_password'])
        self.sing_in_button.draw(self.settings.game_texts['btn_sing_in'])
        self.sing_up_button.draw(self.settings.game_texts['btn_sing_up'])
        self.msg_text_text.write(self.msg_text, (self.msg_pos_x, self.screen.HEIGHT - self.screen.HEIGHT/10), center_w=True)
        self.panel.draw()
        self.panel_sing_up_button.draw(self.settings.game_texts['btn_sing_up'])
        self.panel_sing_in_button.draw(self.settings.game_texts['btn_sing_in'])
        

    def inputs(self):
        '''
        Handle inputs, such as button clicks and slider interactions.
        '''

        if self.panel_sing_in_button.click():
            self.panel.velocity.x = 2000
            self.panel_sing_in_button.visible = False
            self.sing_in_username_tb.visible = True
            self.sing_in_password_tb.visible = True
            self.forgot_password_button.visible = True
            self.sing_in_button.visible = True
        
        if self.panel_sing_up_button.click():
            self.panel.velocity.x = -2000
            self.panel_sing_up_button.visible = False
            self.sing_up_password_tb.visible = True
            self.sing_up_confirm_password_tb.visible = True
            self.sing_up_username_tb.visible = True
            self.sing_up_button.visible = True
            
        if self.forgot_password_button.click():
            pass
        
        if self.sing_in_button.click():
            if self.sing_in_username_tb.text == '' or self.sing_in_password_tb.text == '':
                self.msg_text = self.settings.game_texts['error_code07']
            else:
                json = {
                    'username': self.sing_in_username_tb.text,
                    'password': self.sing_in_password_tb.text
                }
                response = requests.post(API_SING_IN, json=json)
                if response.status_code == 500:
                    self.msg_text = self.settings.game_texts[f'error_code{response.json().get('error_code')}']
                elif response.status_code == 200:
                    if response.json().get('id'):
                        self.msg_text = response.json().get('id')
                    if response.json().get('msg_code'):
                        self.msg_text = self.settings.game_texts[f'msg_code{response.json().get('msg_code')}']

        if self.sing_up_button.click():
            if self.sing_up_confirm_password_tb.text == '' or self.sing_up_password_tb.text == '' or self.sing_up_username_tb.text == '':
                self.msg_text = self.settings.game_texts['error_code02']
            elif self.sing_up_password_tb.text != self.sing_up_confirm_password_tb.text:
                self.msg_text = self.settings.game_texts['error_code03']
            elif any(char in self.sing_up_username_tb.text for char in  ' !@#$%^&*()/?:"<>|,.;'):
                self.msg_text = self.settings.game_texts['error_code04']
            elif self.sing_up_username_tb.text[0] in '0123456789':
                self.msg_text = self.settings.game_texts['error_code05']
            else:
                json = {
                    'username': self.sing_up_username_tb.text,
                    'password': self.sing_up_password_tb.text,
                    'confirm_password': self.sing_up_confirm_password_tb.text
                }
                response = requests.post(API_NEW_USER, json=json)
                if response.status_code == 201:
                    self.msg_text = self.settings.game_texts[f'msg_code{response.json().get('msg_code')}']
                    self.sing_up_confirm_password_tb.text = ''
                    self.sing_up_password_tb.text = ''
                    self.sing_up_username_tb.text = ''
                elif response.status_code in (400, 422, 500):
                    self.msg_text = self.settings.game_texts[f'error_code{response.json().get('error_code')}']

        # Handle text_box interaction.
        self.sing_in_username_tb.click()
        self.sing_up_username_tb.click()
        self.sing_in_password_tb.click()
        self.sing_up_password_tb.click()
        self.sing_up_confirm_password_tb.click()
