from pepsi.base_page import BasePage
from pepsi.locators import Locators


class MainPage(BasePage):
    def start_create_account(self):
        self.find_element(Locators.LOCATOR_CREATE_ACCOUNT_BUTTON).click()
        self.find_element(Locators.LOCATOR_CREATE_ACCOUNT_LINK).click()

    def fill_in_the_fields(self, human):
        self.find_element(Locators.LOCATOR_FIRST_NAME_FIELD).send_keys(human.first_name)
        self.find_element(Locators.LOCATOR_LAST_NAME_FIELD).send_keys(human.last_name)
        self.find_element(Locators.LOCATOR_EMAIL_FIELD).send_keys(human.email)
        self.find_element(Locators.LOCATOR_STREET_FIELD).send_keys(human.street)
        self.find_element(Locators.LOCATOR_CITY_FIELD).send_keys(human.city)
        self.find_element(Locators.LOCATOR_STATE_FIELD).send_keys(human.state)
        self.find_element(Locators.LOCATOR_POSTAL_CODE_FIELD).send_keys(human.postal_code)
        self.select_element(self.find_element(Locators.LOCATOR_COUNTRY_FIELD))
        self.find_element(Locators.LOCATOR_WALLET_ADDRESS_FIELD).send_keys(human.public_address)

        self.find_element(Locators.LOCATOR_PRIVACY_POLICY_CHECKBOX).click()

    def end_create_account(self):
        self.find_element(Locators.LOCATOR_CREATE_ACCOUNT_SECOND_BUTTON).click()

    def set_password(self, password='Sergo07012!'):
        self.find_element(Locators.LOCATOR_NEW_PASSWORD_FIELD).send_keys(password)
        self.find_element(Locators.LOCATOR_CONFIRM_PASSWORD_FIELD).send_keys(password)

        self.find_element(Locators.LOCATOR_CREATE_ACCOUNT_THIRD_BUTTON).click()
