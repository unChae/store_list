from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

class Chrome:

    # 크롬창 생성
    def __init__(self, name):
        self.name = name

        #chromedriver 경로 설정
        CHROMEDRIVER_PATH = './chromedriver.exe'

        chrome_options = Options()

        #브라우저 실행 및 탭 추가
        self.driver = webdriver.Chrome( executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options )
    
    # url 이동
    def set_url(self, url):
        self.driver.get(url)

    def get_driver(self):
        return self.driver
        
    # 크롬창 종료
    def close(self):
        self.driver.close()