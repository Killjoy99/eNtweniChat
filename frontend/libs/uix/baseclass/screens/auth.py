from kivy.uix.accordion import ObjectProperty
from kivymd.uix.screen import MDScreen
from kivy.storage.jsonstore import JsonStore


class WelcomeScreen(MDScreen):
    logo = ObjectProperty("data/images/logo.png")

class RegisterScreen(MDScreen):
    def __init__(self):
        super().__init__()
        self.store = JsonStore("config.json")
    # changing screens also can be done in python
    # def goto_home_screen(self):
    #     self.manager.push_replacement("home")
    def register(self, phone_number):
        self.store.put("SETTINGS",registered = "True")
        self.store.put("ACCOUNT", phone_number = phone_number)
        self.manager.push_replacement("home")

class ChooseCountryScreen(MDScreen):
    """ A Screen with a list of all supported countries that can register on the app"""
    pass

class AuthScreen(MDScreen):
    # changing screens also can be done in python
    # def goto_home_screen(self):
    #     self.manager.push_replacement("home")
    pass
