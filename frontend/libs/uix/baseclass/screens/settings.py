from kivymd.uix.screen import MDScreen

from libs.uix.baseclass.components.components import ThemeDialog, ColorDialog

class SettingsScreen(MDScreen):
    # changing screens also can be done in python
    # def goto_home_screen(self):
    #     self.manager.push_replacement("home")
    avatar = "data/images/profile.jpg"

class SettingsAccountScreen(MDScreen):
    avatar = "data/images/profile.jpg"
    avatar2 = "data/images/profile.jpg"
    avatar3 = "data/images/profile3.jpg"


class SettingsChatsScreen(MDScreen):
    def change_theme_dialog(self):
        dialog = ThemeDialog()
        dialog.open()

    def change_color_dialog(self):
        dialog = ColorDialog()
        dialog.open()


class SettingsHelpScreen(MDScreen):
    version = "0.0.1.dev0"
    
class NotImplemented(MDScreen):
    pass