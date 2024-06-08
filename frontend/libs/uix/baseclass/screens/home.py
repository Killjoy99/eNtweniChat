from kivymd.uix.bottomsheet.bottomsheet import MDLabel
import logging

from kivymd.uix.screen import MDScreen
from kivymd.uix.tab import MDTabsItem, MDTabsItemText, MDTabsItemIcon
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.navigationbar import MDNavigationBar, MDNavigationItem


from libs.uix.baseclass.screens.communities import CommunitiesScreen
from libs.uix.baseclass.screens.chats import ChatsScreen
from libs.uix.baseclass.screens.updates import UpdatesScreen
from libs.uix.baseclass.screens.calls import CallsScreen


# from libs.uix.root import Root

from kivy.lang import Builder

home_screens = ["chats", "communities", "updates", "calls"]
for screen in home_screens:
    Builder.load_file(f"libs/uix/kv/screens/{screen}/{screen}.kv")


class HomeScreen(MDScreen):
    def __init__(self):
        super().__init__()
            
        
    def on_switch_tabs(self, bar: MDNavigationBar, item: MDNavigationItem, item_icon: str, item_text: str,):
        # load the screen with builder and display item
        self.ids.home_screen_manager.current = item_text
        
        # self.manager.current = item_text
        # self.manager.push(item_text.lower())
       
    def tabs_dropdown_menu(self):
        # tab_id = self.ids.tabs.get_current_tab().id
        
        menu_items = {
            "communities_tab": [
                {"text": "Settings", "on_release": lambda x="settings": self.change_screen_with_dismiss(x, "up")}
            ],
            "chats_tab": [
                {"text": "New group", "on_release": lambda x="x": logging.info("New Group Screen")},
                {"text": "New broadcast", "on_release": lambda x="x": logging.info("New broadcast Screen")},
                {"text": "Linked devices", "on_release": lambda x="x": logging.info("Linked devices Screen")},
                {"text": "Starred messages", "on_release": lambda x="x": logging.info("Starred messages Screen")},
                {"text": "Settings", "on_release": lambda x="settings": self.change_screen_with_dismiss(x, "up")}
            ],
            "updates_tab": [
                {"text": "Settings", "on_release": lambda x="settings": self.change_screen_with_dismiss(x, "up")}
                
            ],
            "calls_tab": [
                {"text": "Clear call logs", "on_release": lambda x="x": logging.info("Clear call logs")},
                {"text": "Settings", "on_release": lambda x="settings": self.change_screen_with_dismiss(x, "up")},
            ]
        }
        
        # select menu items based on the current tab
        # current_menu_items = menu_items.get(tab_id, [])
        
        menus = [
            {"text": "Clear call logs", "on_release": lambda x="x": logging.info("Clear call logs")},
            {"text": "Settings", "on_release": lambda x="settings": self.change_screen_with_dismiss(x, "up")},
        ]
        # create a dropdown menu
        self.home_screen_tabs_dropdown_menu = MDDropdownMenu(
            items = menus,
            caller = self.ids.menu_caller,
            # width_mult = 4
        )
        self.home_screen_tabs_dropdown_menu.open()
        
    def change_screen_with_dismiss(self, screen_name, direction="left"):
        # change the screen and dismiss the dropdown menu
        self.manager.push(screen_name, direction)
        if self.home_screen_tabs_dropdown_menu:
            self.home_screen_tabs_dropdown_menu.dismiss()
            return
        
class TestScreen(MDScreen):
    def __init__(self):
        super().__init__()
        
        _tabs = {
            "message-text-outline": "Chats",
            "chat-processing-outline": "Updates",
            "account-group-outline": "Communities",
            "phone-outline": "Calls",
        }
        for tab_icon, tab_name in _tabs.items():
            self.ids.tabs.add_widget(
                MDTabsItem(MDTabsItemIcon(icon=tab_icon,), MDTabsItemText(text=tab_name,),)
            )
            self.ids.tab_content.add_widget(
                MDLabel(text=tab_name, halign="center",md_bg_color="red", pos_hint={"center_x": 0.5, "center_y": 0.5})
            )
            
            # Switch to the chats tab
            # self.ids.tabs.switch_tab(text="Updates")
    
    def home_back(self):
        print(self.ids.tabs.get_current_related_content())