from selenium.common.exceptions import (
    TimeoutException,
    ElementClickInterceptedException,
    StaleElementReferenceException
)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    # =========================================================
    # AD / GOOGLE VIGNETTE HANDLING
    # =========================================================

    def is_google_vignette(self):
        """
        Check whether Google Vignette has taken over the current URL.
        Example:
        https://automationexercise.com/#google_vignette
        """
        try:
            return "google_vignette" in self.driver.current_url.lower()
        except Exception:
            return False

    def close_google_vignette(self):
        """
        Try to recover from Google Vignette.

        Google Vignette can appear between page navigations.
        The safest recovery for automation is to go back first.
        """

        if not self.is_google_vignette():
            return False

        try:
            self.driver.back()

            self.wait.until(
                lambda driver: not self.is_google_vignette()
            )

            return True

        except Exception:
            return False

    # =========================================================
    # ELEMENT METHODS
    # =========================================================

    def find_element(self, locator):
        return self.wait.until(
            EC.presence_of_element_located(locator)
        )

    def click(self, locator):
        """
        Click an element safely.

        If the element is an <a> tag and Google Vignette
        interrupts navigation, use the original href as fallback.
        """

        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )

        # -----------------------------------------------------
        # Save href before clicking
        # -----------------------------------------------------

        href = None

        try:
            tag_name = element.tag_name.lower()

            if tag_name == "a":
                href = element.get_attribute("href")

        except StaleElementReferenceException:
            element = self.wait.until(
                EC.element_to_be_clickable(locator)
            )

            try:
                if element.tag_name.lower() == "a":
                    href = element.get_attribute("href")
            except Exception:
                pass

        # -----------------------------------------------------
        # Scroll element into view
        # -----------------------------------------------------

        self.driver.execute_script(
            """
            arguments[0].scrollIntoView({
                block: 'center',
                inline: 'center'
            });
            """,
            element
        )

        # -----------------------------------------------------
        # Normal click
        # -----------------------------------------------------

        try:
            element.click()

        except ElementClickInterceptedException:

            # Sometimes an ad/overlay intercepts the click.
            # JavaScript click bypasses the visual overlay.

            self.driver.execute_script(
                "arguments[0].click();",
                element
            )

        # -----------------------------------------------------
        # Google Vignette recovery
        # -----------------------------------------------------

        if self.is_google_vignette() and href:

            print(
                f"\n[INFO] Google Vignette detected. "
                f"Recovering navigation to: {href}"
            )

            self.driver.get(href)

            self.wait.until(
                lambda driver: not self.is_google_vignette()
            )

    def type_text(self, locator, text):
        element = self.find_element(locator)

        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        element = self.find_element(locator)

        return element.text

    def is_visible(self, locator):

        try:
            self.wait.until(
                EC.visibility_of_element_located(locator)
            )

            return True

        except TimeoutException:

            # If an ad appeared while checking the element,
            # try recovering once.

            if self.is_google_vignette():

                self.close_google_vignette()

                try:
                    self.wait.until(
                        EC.visibility_of_element_located(locator)
                    )

                    return True

                except TimeoutException:
                    pass

            return False

    def wait_for_url_contains(self, text):

        self.wait.until(
            EC.url_contains(text)
        )