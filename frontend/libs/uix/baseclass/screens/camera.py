from kivy.uix.video import Video
from kivymd.uix.screen import MDScreen

import time
from libs.applibs import constants

class CameraScreen(MDScreen):
    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png(f"{constants.PROJECT_DIR}/data/temp/IMG_{timestr}.png")
        print("Captured")
