from selenium import webdriver
from selenium.webdriver.common.by import By



class SeleniumActions:

    def __init__(self,  path):
        self.c_path = path

    def load_url(self, url):
        try:
            driver = webdriver.Chrome(executable_path=self.c_path)
            driver.set_page_load_timeout(30)
            # assign web page url
            driver.get(url)
            driver.maximize_window()
            # find web links
            links = driver.find_elements(By.TAG_NAME, 'a')
            print("The number of links in the webpage is", len(links))
        except Exception as e:
            print(str(e))


