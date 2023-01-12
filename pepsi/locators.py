from selenium.webdriver.common.by import By


class Locators:
    LOCATOR_CREATE_ACCOUNT_BUTTON = (By.XPATH, "//div[@class='shadow-box-hero__content text-center']/a[@class='mic-btn']")
    LOCATOR_CREATE_ACCOUNT_LINK = (By.XPATH, "//a[@class='create-account btn-text']")
    LOCATOR_FIRST_NAME_FIELD = (By.XPATH, "//input[@name='firstName']")
    LOCATOR_LAST_NAME_FIELD = (By.XPATH, "//input[@name='lastName']")
    LOCATOR_EMAIL_FIELD = (By.XPATH, "//input[@name='email']")
    LOCATOR_STREET_FIELD = (By.XPATH, "//input[@name='address1']")
    LOCATOR_CITY_FIELD = (By.XPATH, "//input[@name='city']")
    LOCATOR_STATE_FIELD = (By.XPATH, "//input[@name='state']")
    LOCATOR_POSTAL_CODE_FIELD = (By.XPATH, "//input[@name='zipcode']")
    LOCATOR_COUNTRY_FIELD = (By.XPATH, "//select[@name='countryCode']")
    LOCATOR_WALLET_ADDRESS_FIELD = (By.XPATH, "//input[@name='wallet_address']")
    LOCATOR_PRIVACY_POLICY_CHECKBOX = (By.XPATH, "//input[@name='termsCondition']")
    LOCATOR_CREATE_ACCOUNT_SECOND_BUTTON = (By.XPATH, "//button[@class='btn btn-yellow btn-block ']")
    LOCATOR_CREATE_ACCOUNT_THIRD_BUTTON = (By.XPATH, "//button[@class='btn btn-yellow btn-block']")
    LOCATOR_NEW_PASSWORD_FIELD = (By.XPATH, "//input[@name='newPassword']")
    LOCATOR_CONFIRM_PASSWORD_FIELD = (By.XPATH, "//input[@name='confirmPassword']")
