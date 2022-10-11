from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGGIN_BUTTON = (By.CSS_SELECTOR, '[id="bottom-nav"] [data-bs-toggle="modal"]')
    EMAIL_FIELD = (By.ID, 'email')
    PASSWORD_FIELD = (By.ID, 'password')
    LOGGIN_BUTTON_FINAL = (By.ID, 'log_btn')
    ALERT = (By.CSS_SELECTOR, '[class="alert-body"]')
