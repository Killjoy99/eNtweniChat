import logging
from kivymd.uix.list import MDListItem
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import ObjectProperty, StringProperty, OptionProperty
from kivymd.uix.card import MDCard


# COMPONENTS
class ThemeDialog(MDDialog):
    pass

class ChatBubble(MDBoxLayout):
    msg = StringProperty()
    time = StringProperty()
    sender = StringProperty()
    isRead = OptionProperty("waiting", options=["read", "delivered", "waiting"])
    
class Message(MDLabel):
    """ Adaptive text for the chat bubble"""
    

class ColorDialog(MDDialog):
    pass

class ChatTextField(MDCard):
    pass

class CallLogItem(MDListItem):
    avatar = ObjectProperty()
    contact_name = StringProperty()
    timestamp = StringProperty()
    call_type = StringProperty()


class ChatListItem(MDListItem):
    avatar = ObjectProperty("data/images/profile.jpg")
    contact_name = StringProperty("Test")
    timestamp = StringProperty()
    last_message = StringProperty()
        
    def goto_chat(self):
        self.root.manager.push("chat_screen")
        print("Chat Activated")


class ContactListItem(MDListItem):
    avatar = ObjectProperty()
    name = StringProperty()
    phone_number = StringProperty()
    status = StringProperty()

    def select_contact(self, name):
        logging.info(f"Contact {name} selected")


class UpdatesListItem(MDListItem):
    avatar = ObjectProperty()
    sender_name = StringProperty()
    timestamp = StringProperty()
