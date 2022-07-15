from selenium.webdriver.common.by import By

class LoginPage:
    inputUser = By.ID, "txtUsername"
    inputPass = By.ID, "txtPassword"
    btnLogin = By.ID, "btnLogin"
    txtWelcome = By.ID, "welcome"

    def __init__(self, driver):
        self.driver = driver
        driver.maximize_window()
        driver.get("https://opensource-demo.orangehrmlive.com/")
        title = "OrangeHRM"
        assert title == driver.title

    def enter_login(self, user, password):
        self.driver.find_element(*self.inputUser).send_keys(user)
        self.driver.find_element(*self.inputPass).send_keys(password)
        self.driver.find_element(*self.btnLogin).click()

    def validate_welcome(self):
        return self.driver.find_element(*self.txtWelcome)