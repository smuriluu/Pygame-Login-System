import pygame
import os

class Sprites:
    def __init__(self, path):
        '''
        Initializes the Sprites class, setting up the directory for loading images.

        Parameters:
        - path: The base directory path where the 'images' folder is located.
        '''
        # Set the path to the 'images' directory by joining the base path with 'images'.
        self.images_dir = os.path.join(path, 'images')

    def load_sprite(self):
        '''
        Loads a sprite image from the 'images' directory.

        Functionality:
        - Loads an image file named 'sprite.png' located in the 'images' folder;
        - Uses `pygame.image.load` to load the image;
        - Applies `convert_alpha()` to the loaded image to preserve transparency (useful for PNG images with alpha channels);

        Note:
        - The method assumes that 'sprite.png' exists in the specified directory.
        '''
        # Load the image sprite.png from the images directory.
        # The convert_alpha() method optimizes the image for transparency and faster blitting.
        self.sprite = pygame.image.load(os.path.join(self.images_dir, 'sprite.png')).convert_alpha()
