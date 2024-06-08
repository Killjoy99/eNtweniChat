from kivymd.uix.screen import MDScreen


class CallsScreen(MDScreen):
    def go_to_screen(self, screen):
        self.manager.push(screen)
        

class CallInfoScreen(MDScreen):
    avatar = "data/images/profile.jpg"
    avatar2 = "data/images/profile.jpg"
    avatar3 = "data/images/profile3.jpg"


class NewCallScreen(MDScreen):
    avatar = "data/images/profile.jpg"
    avatar2 = "data/images/profile.jpg"
    avatar3 = "data/images/profile3.jpg"


class CallLinkScreen(MDScreen):
    call_type = "phone"  # using icons here
    call_url = f"https:call.eNtweniChat.com/{call_type}/hj6GUS7jjjMd"
    avatar = "data/images/profile.jpg"
    avatar2 = "data/images/profile.jpg"
    avatar3 = "data/images/profile3.jpg"