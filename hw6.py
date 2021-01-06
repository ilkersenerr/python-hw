import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class SPX(unittest.TestCase):

    CATEGORY_PAGE = (By.CSS_SELECTOR, ".navigation__desktop-item")
    PRODUCT_PAGE = (By.CLASS_NAME, "product-card")
    CHOOSE_SIZE = (By.CSS_SELECTOR, ".mb-3.js-variant")
    ADD_TO_CART = (By.CSS_SELECTOR, ".js-add-to-cart")
    CART_PAGE = (By.CSS_SELECTOR, ".go-basket-btn")
    MAIN_PAGE = (By.CSS_SELECTOR, '.header__icon')
    website = "https://spx.com.tr"
    IS_ON_CAT_PAGE = (By.CSS_SELECTOR, ".pz-breadcrumb__link")
    IS_ON_PRODUCT_PAGE = (By.CSS_SELECTOR, ".pz-breadcrumb__link")

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.website)
        self.wait = WebDriverWait(self.driver, 15)

    def test_navigate(self):
        assert "SPX - Sport Point Extreme" in self.driver.title
        self.wait.until(ec.presence_of_all_elements_located(self.CATEGORY_PAGE))[1].click()
        assert self.wait.until(ec.presence_of_all_elements_located(self.IS_ON_CAT_PAGE))[1].text == "ERKEK", True
        self.wait.until(ec.presence_of_all_elements_located(self.PRODUCT_PAGE))[3].click()
        assert len(self.wait.until(ec.presence_of_all_elements_located(self.IS_ON_PRODUCT_PAGE)))>2
        self.wait.until(ec.presence_of_all_elements_located(self.CHOOSE_SIZE))[0].click()
        assert self.wait.until(ec.presence_of_all_elements_located(self.CHOOSE_SIZE))[0].text == "M", True
        self.wait.until(ec.element_to_be_clickable(self.ADD_TO_CART)).click()
        assert self.wait.until(ec.presence_of_all_elements_located(self.ADD_TO_CART))[0].text == "SEPETE EKLE", True
        self.wait.until(ec.element_to_be_clickable(self.CART_PAGE)).click()
        assert self.wait.until(ec.presence_of_all_elements_located(self.CART_PAGE)).text == "SEPETE GİT", True
        self.wait.until(ec.element_to_be_clickable(self.MAIN_PAGE)).click()
        assert self.wait.until(ec.presence_of_all_elements_located(self.MAIN_PAGE)).text == "", True
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()