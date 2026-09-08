from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class DriverFactory:

    @staticmethod
    def create_driver(browser="chrome"):

        if browser.lower() == "chrome":

            options = Options()

            # Không chờ toàn bộ tài nguyên của trang tải xong
            options.page_load_strategy = "eager"

            options.add_argument("--start-maximized")
            options.add_argument("--disable-notifications")
            options.add_argument("--disable-popup-blocking")

            prefs = {
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False,
                "profile.default_content_setting_values.notifications": 2
            }

            options.add_experimental_option("prefs", prefs)

            driver = webdriver.Chrome(options=options)

            # Nếu trang tải quá 30 giây thì Selenium timeout
            driver.set_page_load_timeout(30)

            return driver

        else:
            raise ValueError(
                f"Browser '{browser}' is not supported. "
                "Use: chrome"
            )