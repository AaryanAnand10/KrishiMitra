from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty


class LoginScreen(Screen):
    email_input = ObjectProperty(None)
    password_input = ObjectProperty(None)
    result_label = ObjectProperty(None)

    credentials = {
        "user1@example.com": "password1",
        "user2@example.com": "password2",
        "user3@example.com": "password3",
        "user4@example.com": "password4"
    }

    def check_login(self):
        email = self.email_input.text
        password = self.password_input.text
        
        if email in self.credentials and self.credentials[email] == password:
            self.result_label.text = "Logging in..."
            self.result_label.color = (0, 1, 0, 1)  # Green color
        else:
            self.result_label.text = "Invalid user, Sign up?"
            self.result_label.color = (1, 0, 0, 1)  # Red color


class SignUpScreen(Screen):
    username_input = ObjectProperty(None)
    email_input = ObjectProperty(None)
    password_input = ObjectProperty(None)
    confirm_password_input = ObjectProperty(None)
    result_label = ObjectProperty(None)
    
    def sign_up(self):
        username = self.username_input.text.strip()
        email = self.email_input.text.strip()
        password = self.password_input.text.strip()
        confirm_password = self.confirm_password_input.text.strip()
        
        if password == confirm_password:
            self.result_label.text = "Signed up successfully!"
            self.result_label.color = (0, 1, 0, 1)  # Green color
        else:
            self.result_label.text = "Passwords do not match!"
            self.result_label.color = (1, 0, 0, 1)


class Krishi(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('login.kv')

if __name__ == "__main__":
    Krishi().run()