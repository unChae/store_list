from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

class Chrome:

    # 크롬창 생성
    def __init__(self, name):
        self.name = name

        #chromedriver path setting
        CHROMEDRIVER_PATH = './chromedriver.exe'

        chrome_options = Options()
        # hide windows
        chrome_options.add_argument('headless')
        chrome_options.add_argument('window-size=1920x1080')
        chrome_options.add_argument("disable-gpu")

        # run browser
        self.driver = webdriver.Chrome( executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options )
    
    # url 이동
    def set_url(self, url):
        self.driver.get(url)

    def get_driver(self):
        return self.driver
