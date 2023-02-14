"""
These tests cover Demoblaze home page.
"""
import pytest
from pages.home_page import DemoblazeHomePage
from utils.logger import logger
from playwright.sync_api import expect, Page


@pytest.mark.smoke
def test_demoblaze_home_page_is_displayed(home_page: DemoblazeHomePage):
    logger.info("Verify home page is displayed")
    home_page.load()
    expect(home_page.home_navigation_button).to_have_text("PRODUCT STORE")


@pytest.mark.smoke
def test_login_modal_is_displayed(home_page: DemoblazeHomePage):
    logger.info("Verify login modal is displayed")
    home_page.load()
    home_page.open_login_modal()
    expect(home_page.login_button_modal).to_be_visible()


@pytest.mark.smoke
def test_valid_user_login(home_page: DemoblazeHomePage):
    logger.info("Verify user can log in successfully")
    home_page.load()
    home_page.user_login("testuser3211", '1234')
    expect(home_page.welcome_user_text).to_have_text('Welcome testuser3211')


@pytest.mark.regression
def test_invalid_user_login(page: Page, home_page: DemoblazeHomePage):
    logger.info("Verify user can not log in with invalid credentials")
    home_page.load()
    home_page.user_login("wronguser232", '1234')
    page.on("dialog", lambda dialog: dialog.accept())
    expect(home_page.welcome_user_text).to_be_hidden()


@pytest.mark.regression
def test_user_logout(home_page: DemoblazeHomePage):
    logger.info("Verify user can log out successfully")
    home_page.load()
    home_page.user_login("testuser3211", '1234')
    home_page.logout_button.click()
    expect(home_page.logout_button).to_be_hidden()


@pytest.mark.smoke
def test_user_signup(home_page: DemoblazeHomePage):
    logger.info("Verify user can register/signup successfully")
    home_page.load()
    username = home_page.generate_random_credentials()
    password = home_page.generate_random_credentials()
    home_page.user_signup(username, password)
    home_page.user_login(username, password)
    expect(home_page.welcome_user_text).to_have_text('Welcome ' + username)


@pytest.mark.smoke
def test_adding_product_to_cart(page: Page, home_page: DemoblazeHomePage):
    logger.info("Verify user can add product to the cart")
    home_page.load()
    home_page.open_galaxy_s6_product_description()
    home_page.add_product_to_cart()
    home_page.open_cart()
    expect(page.locator(home_page.find_product_in_cart(1))).to_have_text("Samsung galaxy s6")


@pytest.mark.smoke
def test_place_valid_order(home_page: DemoblazeHomePage):
    logger.info("Verify user place an order successfully")
    home_page.load()
    home_page.user_login("testuser3211", '1234')
    home_page.load()
    home_page.open_galaxy_s6_product_description()
    home_page.add_product_to_cart()
    home_page.open_cart()
    home_page.click_place_order_button()
    home_page.fill_order_info()
    home_page.click_purchase_button()
    expect(home_page.order_alert_message).to_have_text('Thank you for your purchase!')
