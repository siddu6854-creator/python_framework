"""Login tests for the nopCommerce demo application.

The test modules need to import helpers from the sibling
``pageObjects`` package.  When pytest loads this file it may not have the
``python_framework`` directory on ``sys.path`` which results in
``ModuleNotFoundError``.  Add the framework directory explicitly so the
imports succeed regardless of the current working directory used to invoke
pytest.  The adjustment happens before any other imports are attempted.
"""

import os
import sys

# make sure the parent package (python_framework) is on the import path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage


class Test_001_Login:
    baseURL= "https://admin-demo.nopcommerce.com/"
    username= "admin@yourstore.com"
    password= "admin"

    def test_homepage_Title(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        assert "nopCommerce demo store. Login" in act_title
        # placeholder login code; uncomment when validation of the page
        # object methods is required.
        self.log = LoginPage(self.driver)
        self.log.setusername(self.username)
        self.log.setpassword(self.password)
        self.log.login()

    def teardown_method(self, method):
        if hasattr(self, "driver") and self.driver:
            try:
                self.driver.quit()
            except Exception:
                pass