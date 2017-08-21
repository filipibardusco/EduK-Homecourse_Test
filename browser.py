from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException        
import time
class Browser(object):

    base_url = 'http://beta.eduk.com.br'
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    def close(self):
        """
        close the webdriver instance
        """
        self.driver.quit()

    def visit(self, location=''):
        """
        navigate webdriver to different pages
        """
        url = self.base_url + location
        self.driver.get(url)

    def find_by_id(self, selector):
        """
        find a page element in the DOM
        """
	return self.driver.find_element_by_id(selector)

    def find_by_xpath(self, selector):
        """
        find a page element in the DOM
        """
	return self.driver.find_element_by_xpath(selector)

    def find_by_class(self, selector):
        """
        find a page element in the DOM
        """
	return self.driver.find_element_by_class_name(selector)

    def find_elements_by_xpath(self, selector):
	return self.driver.find_elements_by_xpath(selector)

    def check_exists_by_xpath(self, xpath):
        try:
            self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True 

    def click_point(self, x, y, xpath):
        el=self.driver.find_element_by_xpath(xpath)
        print("=======================>{} {} {} {}".format(x,y,xpath,el))
        action = webdriver.common.action_chains.ActionChains(self.driver)
        action.move_to_element_with_offset(el, x, y)
        time.sleep(0.5)
        action.click()
        action.perform()

    def wait_click(self, xpath):
        element = WebDriverWait(self.driver, 10).until(
        	EC.element_to_be_clickable((By.XPATH, xpath))
	);
        element.click()

    def wait(self, xpath, excon):
        element = WebDriverWait(self.driver, 20).until(
        EC.excon((By.XPATH, xpath)));

    def switch_to(self):
        self.driver.switch_to.frame(self.driver.find_element_by_tag_name("iframe"))
