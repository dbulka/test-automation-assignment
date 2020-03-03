import pytest
import time
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager

from project import site_URL, registation_URL, start_main_button, second_start_button, login_button, name_field, \
    last_name, email, company, register, skip_wizard, settings_drop_down, setting, user_email, user_password, login, password, login_page_button
from utils.base_fixtures import BaseFixture


@pytest.fixture
def browser():
    driver = Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    yield driver
    time.sleep(30)
    driver.quit()


def test_main_button(browser):
    browser.get(site_URL)
    browser.find_element_by_xpath(start_main_button).click()
    assert browser.title == "Register | Blazemeter"
    browser.find_element_by_xpath(login_button).click()
    assert browser.title == "Log In | Blazemeter"


def test_second_button(browser):
    browser.maximize_window()
    browser.get(site_URL)
    browser.find_element_by_xpath(second_start_button).click()
    assert browser.title == "Register | Blazemeter"
    browser.find_element_by_xpath(login_button).click()
    assert browser.title == "Log In | Blazemeter"


def test_registration(browser):
    browser.maximize_window()
    browser.get(registation_URL)
    input_name = browser.find_element_by_xpath(name_field)
    input_name.send_keys(BaseFixture.get_valid_string())
    input_last_name = browser.find_element_by_xpath(last_name)
    input_last_name.send_keys(BaseFixture.get_valid_string())
    input_email = browser.find_element_by_xpath(email)
    input_email.send_keys(BaseFixture.get_valid_string() + "@gmail.com")
    input_company = browser.find_element_by_xpath(company)
    input_company.send_keys(BaseFixture.get_valid_string())
    browser.find_element_by_xpath(register).click()
    i = 0
    while i < 15:
        if browser.title == "Welcome Wizard":
            break
        time.sleep(1)
        i += 1
    current_url = browser.current_url
    assert current_url[-20:] == "/welcome-wizard/http"
    browser.find_element_by_xpath(skip_wizard).click()
    assert browser.title == "Workspace Dashboard"

def test_update_settings(browser):
    browser.maximize_window()
    browser.get(registation_URL)
    browser.find_element_by_xpath(login_button).click()
    input_login = browser.find_element_by_xpath(login)
    input_login.send_keys(user_email)
    input_password = browser.find_element_by_xpath(password)
    input_password.send_keys(user_password)
    browser.find_element_by_xpath(login_page_button).click()
    assert browser.title == "Workspace Dashboard"
    i = 0
    while i < 15:
        time.sleep(1)
        i += 1
        browser.find_element_by_class_name("dropdown-toggle").selectByValue("Dzmitry Bulka")

