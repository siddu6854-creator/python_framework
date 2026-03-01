# from selenium import webdriver
from selenium import webdriver


class  LoginPage:
    textbox_username_id="Email"
    textbox_password_id="Password"
    link_text_loginin="Log in"
    lought_linkText="Logout"

    def __init__(self,driver):
        self.driver=driver

    def setusername(self, username):
        # clear the field before typing to avoid leftover text
        self.driver.find_element("id", self.textbox_username_id).clear()
        self.driver.find_element("id", self.textbox_username_id).send_keys(username)
        

    def setpassword(self, password):
        self.driver.find_element("id", self.textbox_password_id).clear()
        self.driver.find_element("id", self.textbox_password_id).send_keys(password)

    def login(self):
        # we can simply target the submit button by its visible text
        self.driver.find_element("xpath", "//button[normalize-space()='Log in']").click()

    def logout(self):
        self.driver.find_element("link text", self.lought_linkText).click()