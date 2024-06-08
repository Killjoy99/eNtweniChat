from kivymd.uix.dropdownitem import MDDropDownItem
from kivy.uix.accordion import StringProperty
from kivymd.uix.screen import MDScreen
from kivymd.uix.menu import MDDropdownMenu

import logging

from kivy.properties import StringProperty, ObjectProperty

from libs.uix.baseclass.components.components import ChatBubble, ChatListItem


class ChatsScreen(MDScreen):
    def menu(self):
        # pass
        menu_items = [
            {"text": "New group", "on_release": lambda x="x": logging.info("New Group Screen")},
            {"text": "New broadcast", "on_release": lambda x="x": logging.info("New broadcast Screen")},
            {"text": "Linked devices", "on_release": lambda x="x": logging.info("Linked devices Screen")},
            {"text": "Starred messages", "on_release": lambda x="x": logging.info("Starred messages Screen")},
            {"text": "Settings", "on_release": lambda x="settings": root.manager.push(x, "up")}
        ]
        
        menu = MDDropdownMenu(
            items = menu_items,
            caller = self.ids.menu_caller,
            # width_mult = 4
        )
        self.menu = menu
        return self.menu
            
    def load_chats(self):
        self.ids.chat_list_container.add_widget(ChatListItem(avatar="data/images/profile.jpg"))


class ChatScreen(MDScreen):
    user_name = StringProperty()
    avatar = StringProperty()

    def set_username(self, name):
        self.user_name = name
        logging.info(self.user_name)

    def send_message(self, message, contact):
        if message == "":
            return
        else:
            # ui to display the message sent, the status as well.
            # icon: str = "clock"
            icon_color: str = "red"
            status = "waiting"
            icon = "clock"

            chat_bubble = ChatBubble()
            chat_bubble.ids.message_container.text = message
            chat_bubble.ids.message_status.icon = icon
            chat_bubble.ids.message_status.icon_color_disabled = icon_color
            # chat_bubble.ids.message_sent_recv_time.text = self.get_current_time()
            self.ids.chat_items.add_widget(chat_bubble)
            self.ids.message.text = ""

            # actually do the message sending logic
            self.send_message_logic(message, contact)

    def send_message_logic(self, message, contact):
        response = self.receive_message(message)
        logging.info(response)

    def receive_message(self, message: str):
        greeting = ["hello", "hie", "hie there"]
        if message.lower() in greeting:
            response = "Hie, are you doing ok. I ask because I am very sure that things are not going well between you and me."
        else:
            response = "I do not understand the command"

        chat_bubble = ChatBubble()
        chat_bubble.ids.message_container.text = response
        # chat_bubble.ids.message_sent_recv_time.text = self.get_current_time()
        chat_bubble.ids.time_container_card.pos_hint = {"bottom": 1, "right": 0.99}
        self.ids.chat_items.add_widget(chat_bubble)

class NewChatScreen(MDScreen):
    pass
