"""
This module contains DemoblazeHomePage,
the page object for the Demoblaze home page.
"""

from playwright.sync_api import Page
from faker import Faker
from utils.locator_decorator import LocatorDecorator
from utils.logger import logger
import random


# UtilityMethods.decorate_locator_methods()

class DemoblazeHomePage:
    URL = 'https://www.demoblaze.com/index.html'

    def __init__(self, page: Page) -> None:
        self.page = page
        self.login_button = page.locator('a#login2')
        self.signin_button = page.locator('a#signin2')
        self.cart_button = page.locator('a#cartur')
        self.home_navigation_button = page.locator('a#nava')
        self.login_username_input = page.locator('input#loginusername')
        self.login_password_input = page.locator('input#loginpassword')
        self.login_button_modal = page.locator('div#logInModal > div[role="document"] .btn.btn-primary')
        self.welcome_user_text = page.locator('a#nameofuser')
        self.logout_button = page.locator('a#logout2')
        self.signin_username_input = page.locator('input#sign-username')
        self.signin_password_input = page.locator('input#sign-password')
        self.signin_modal_button = page.locator('div#signInModal > div[role="document"] .btn.btn-primary')
        self.galaxy_s6_link = page.locator('div#tbodyid > div:nth-of-type(1) .hrefch')
        self.product_add_to_cart_button = page.locator('.btn.btn-lg.btn-success')
        self.first_product_in_cart = page.locator('tr > td:nth-of-type(2)')
        self.place_order_button = page.locator('.btn.btn-success')
        self.order_name_input = page.locator('input#name')
        self.order_country_input = page.locator('input#country')
        self.order_city_input = page.locator('input#city')
        self.order_credit_cart_input = page.locator('input#card')
        self.order_month_input = page.locator('input#month')
        self.order_year_input = page.locator('input#year')
        self.order_purchase_button = page.locator("div#orderModal > div[role='document'] .btn.btn-primary")
        self.order_alert_message = page.locator('.showSweetAlert.sweet-alert.visible > h2')

    def load(self) -> None:
        logger.info("Navigating to " + self.URL)
        try:
            self.page.goto(self.URL)
            logger.info("Navigated successfully.")
        except Exception as err:
            logger.info("Navigation to page failed. Exception message->" + str(err))

    def open_login_modal(self):
        logger.info("Clicking on login button")
        try:
            self.login_button.click()
            logger.info("Clicked successfully")
        except Exception as err:
            logger.info("Failed to click. Exception message->" + str(err))

    def click_login_button_modal(self):
        logger.info("Clicking on login button located in the login modal")
        try:
            self.login_button_modal.click()
            logger.info("Clicked successfully")
        except Exception as err:
            logger.info("Failed to click. Exception message->" + str(err))

    def user_login(self, username, password):
        self.open_login_modal()
        logger.info("Filling userinfo: " + username + ", " + password)
        try:
            self.login_username_input.fill(username)
            self.login_password_input.fill(password)
            logger.info("Filled userinfo successfully")
        except Exception as err:
            logger.info("Failed to fill. Exception message->" + str(err))
        self.click_login_button_modal()

    def generate_random_credentials(self):
        return Faker().name().replace(" ", "") + str(random.randint(1, 99))

    def open_signup_modal(self):
        logger.info("Clicking on singup button")
        try:
            self.signin_button.click()
            logger.info("Clicked successfully")
        except Exception as err:
            logger.info("Failed to click. Exception message->" + str(err))

    def click_sign_up_button_in_modal(self):
        logger.info("Clicking on sign up button located in the sign up modal")
        try:
            self.signin_modal_button.click()
            logger.info("Clicked successfully")
        except Exception as err:
            logger.info("Failed to click. Exception message->" + str(err))

    def close_alert(self):
        logger.info("Closing the alert box")
        try:
            self.page.on("dialog", lambda dialog: dialog.accept())
            logger.info("Alert box closed successfully")
        except Exception as err:
            logger.info("Failed to close alert box. Exception message->" + str(err))

    def user_signup(self, username, password):
        self.open_signup_modal()
        logger.info("Filling userinfo: " + username + ", " + password)
        try:
            self.signin_username_input.fill(username)
            self.signin_password_input.fill(password)
            logger.info("Filled userinfo successfully")
        except Exception as err:
            logger.info("Failed to fill. Exception message->" + str(err))
        self.click_sign_up_button_in_modal()
        self.close_alert()

    def find_product_in_cart(self, position):
        return f"tr:nth-of-type({position}) > td:nth-of-type(2)"

    def open_galaxy_s6_product_description(self):
        logger.info("Opening galaxy s6 product description")
        try:
            self.galaxy_s6_link.click()
            logger.info("Galaxy s6 product opened")
        except Exception as err:
            logger.info("Failed to open galaxy s6 product page. Exception message->" + str(err))

    def open_cart(self):
        logger.info("Navigating to cart page")
        try:
            self.cart_button.click()
            logger.info("Navigated to cart page successfully")
        except Exception as err:
            logger.info("Failed to navigate to cart page. Exception message->" + str(err))

    def add_product_to_cart(self):
        logger.info("Adding product to cart")
        try:
            self.product_add_to_cart_button.click()
            logger.info("Product added successfully")
        except Exception as err:
            logger.info("Product wasn't added. Exception message->" + str(err))

    def click_place_order_button(self):
        logger.info("Clicking on place order button")
        try:
            self.place_order_button.click()
            logger.info("Clicked successfully")
        except Exception as err:
            logger.info("Failed to click. Exception message->" + str(err))

    def fill_order_info(self):
        logger.info("Filling order info")
        try:
            self.order_name_input.fill('DummyName123')
            self.order_country_input.fill('Bulgaria')
            self.order_city_input.fill('Ruse')
            self.order_credit_cart_input.fill('374245455400126')
            self.order_month_input.fill('03')
            self.order_year_input.fill('2025')
            logger.info("Filled order info successfully")
        except Exception as err:
            logger.info("Failed to fill. Exception message->" + str(err))

    def click_purchase_button(self):
        logger.info("Clicking on purchase button")
        try:
            self.order_purchase_button.click()
            logger.info("Clicked successfully")
        except Exception as err:
            logger.info("Failed to click. Exception message->" + str(err))
