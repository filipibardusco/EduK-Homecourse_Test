from selenium import webdriver


class Browser(object):

    base_url = 'http://stg-beta.eduk.com.br'
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

 
