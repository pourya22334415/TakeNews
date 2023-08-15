from selenium.webdriver.support import select, select, expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
import json
import time
import os


class NewsScraper():
    def __init__(self, driver_path, start_url, json_file_path):
        self.driver_path = driver_path
        self.start_url = start_url
        self.json_file_path = json_file_path
        self.driver = None
        self.wait = None

    def start_service(self):
        os.system('echo -n "starting service ... "')
        service = Service(executable_path=driver_path)
        self.driver = webdriver.Chrome(service=service)

        self.driver.get(start_url)
        self.wait = WebDriverWait(self.driver, 10)
        
        os.system('echo "Ok"')
        self.load_pages()
        urls = self.get_news_urls()
        data = self.get_data_from_urls(urls)
        
        os.system('echo "saving loaded urls:"')
        self.store_data_in_json_file(json_file_path, data)
        
        os.system('echo "All data saved successfully"')
        self.driver.quit()

    def load_pages(self):
        os.system('echo -n "loading news ... "')
        button_xpath = 'button[class="button__Base-kwkpzw-0 fpijDs BrowseArticleData___StyledButton-sc-1qvnay0-0 eByvXQ"]'
        
        button = self.driver.find_element(By.CSS_SELECTOR, button_xpath)
        for _ in range(20):
            self.wait.until(EC.element_to_be_clickable(button)).click()
        os.system('echo "Ok"')

    def get_news_urls(self):
        urls = []
        os.system('echo -n "getting urls ... "')
        links_xpath = 'a[class="link__CustomNextLink-sc-1r7l32j-0 iCQspp"]'
 
        links = self.driver.find_elements(By.CSS_SELECTOR, links_xpath)
        for link in links:
            href = link.get_attribute('href')
            urls.append(href)
        
        os.system('echo "Ok"')
        return urls

    def get_data_from_urls(self, urls):
        os.system('echo "start extracting data"')
        zoomit2_urls = []
        zoomgi_urls = []
        pedal_urls = []
        data = []
        
        counter = 0

        for url in urls:
            self.driver.get(url)
            prev = counter

            if (url.startswith("https://www.zoomg.ir")):
                zoomgi_urls.append(url)
            elif (url.startswith("https://www.pedal.ir")):
                pedal_urls.append(url)
            else:
                try:
                    title_xpath = '//h1[@class="typography__StyledDynamicTypographyComponent-t787b7-0 eNoCZh"]'
                    content_xpath = '//div[@class="BlockContainer__InnerArticleContainer-i5s1rc-1 dfnkIg"]//p'
                    tags_xpath = '//span[@class="typography__StyledDynamicTypographyComponent-t787b7-0 eMeOeL"]'
                    
                    title = self.wait.until(EC.presence_of_element_located(
                                                (By.XPATH, title_xpath)
                                                )).text
                    content = self.get_text_elements(xpath= content_xpath)
                    tags = self.get_text_elements(xpath= tags_xpath),
                    

                    obj = {
                        'title': title,
                        'content': content,
                        'tags': tags,
                        'source': url
                    }
                    
                    counter += 1
                    data.append(obj)
                except:
                    zoomit2_urls.append(url)

                if (counter != prev):
                    os.system('echo -ne "data received: %s\r"' %counter)

        skipped = len(zoomgi_urls) + len(pedal_urls) + len(zoomit2_urls)
        os.system('echo "data received: %s\r"' %counter)
        os.system('echo "%d data skipped"' %skipped)
        os.system('echo -n "extracting skipped data ... "')
        
        # zoomgi
        self.get_skipped_data(data,
                         zoomgi_urls,
                         title_xpath= '//span[@class="row"]', 
                         content_xpath= '//div[@id="bodyContainer"]//p', 
                         tags_xpath= '//div[@id="bodyContainer"]//h3')

        # pedal
        self.get_skipped_data(data,
                         pedal_urls, 
                         title_xpath= '//h1[@class="post-title entry-title"]', 
                         content_xpath= '//div[@class="entry-content entry clearfix"]//p', 
                         tags_xpath= '//span[@class="tagcloud"]//a')
        
        # zoomit2
        self.get_skipped_data(data,
                         zoomit2_urls, 
                         title_xpath= '//h1[@class="typography__StyledDynamicTypographyComponent-t787b7-0 krllpu"]', 
                         content_xpath= '//div[@class="BlockContainer__InnerArticleContainer-i5s1rc-1 dfnkIg"]//p',
                         tags_xpath= '//span[@class="typography__StyledDynamicTypographyComponent-t787b7-0 jaRosJ"]') 

            
        os.system('echo "Done"')
        return data
    
    def get_skipped_data(self, 
                         data,
                         urls, 
                         title_xpath, 
                         content_xpath, 
                         tags_xpath):
        for url in urls:
            self.driver.get(url)

            try:
                title = self.wait.until(EC.presence_of_element_located(
                                            (By.XPATH, title_xpath)
                                            )).text                         
                content = self.get_text_elements(xpath= content_xpath)
                tags = self.get_text_elements(xpath= tags_xpath)
                

                obj = {
                    'title': title,
                    'content': content,
                    'tags': tags,
                    'source': url
                }
                
                data.append(obj)
            except:
                pass

    def get_text_elements(self, xpath):
        text = []
        elements = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, xpath)))
        for e in elements:
            t = e.text
            if (t != ""):
                text.append(t)
        return text
        print("Ok")

    def store_data_in_json_file(self, json_file_path, data):
        os.system('echo -n "saving informations ... "')
        with open(json_file_path, "w", encoding='utf8') as file:
            json.dump(data, file, indent=4)
            file.close()
        os.system('echo "Ok"')



driver_path = './chromedriver'
start_url = 'https://www.zoomit.ir/archive/?sort=Newest&skip=20'
json_file_path = './data.json'

scraper = NewsScraper(driver_path, start_url, json_file_path)
scraper.start_service()