import asyncio
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.storage.jsonstore import JsonStore
from kivy.utils import platform

from libs.uix.root import Root


if platform != "android":
    Window.size = (400, 840)


class EntweniChatApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.light_theme_color = "#008080"
        
        # set theme
        self.store = JsonStore("config.json")
        self.title = "eNtweniChat - Lazy Loading"
        self.icon = "data/images/logo.png"
        self.registered = self.check_registered()

        Window.keyboard_anim_args = {"d": 0.2, "t": "linear"}
        Window.softinput_mode = "below_target"
        
    async def async_init(self):
        pass

    def build(self):
        # Don't change self.root to self.some_other_name
        # refer https://kivy.org/doc/stable/api-kivy.app.html#kivy.app.App.root
        asyncio.ensure_future(self.async_init())
        
        self.root = Root()
        
        if self.registered:
            self.root.push("home")
        else:
            self.root.push("welcome")
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Teal"
        if platform == "android":
            from android.permission import Permission, request_permissions
            request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
        # if self.theme_cls.theme_style == "Light":
        #     self.light_theme_color = "#008080"
        # else:
        #     self.light_theme_color = "#000000"

    def check_registered(self):
        reg = self.store.get("SETTINGS")["registered"]
        return eval(reg)
        

if __name__ == "__main__":
    app = EntweniChatApp()
    app.run()
    # loop = asyncio.new_event_loop()
    # loop.run_until_complete(app.async_run(async_lib="asyncio"))