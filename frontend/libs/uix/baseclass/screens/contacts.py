from kivymd.uix.screen import MDScreen

class NewContactScreen(MDScreen):
    pass


class CreateContactScreen(MDScreen):
    # firstname = app.root.ids
    def save_contact(self, firstname, lastname, phonenumber):
        logging.info(f"contact saved {firstname}")
