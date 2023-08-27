from selenium.webdriver.support import select, expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver



class NewsScraper():
    def __init__(self, start_url):
        self.driver_path = "/usr/lib/chromium/chromedriver"
        self.start_url = start_url
        self.driver = None
        self.wait = None

    def get_data(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_prefs = {}
        chrome_options.experimental_options["prefs"] = chrome_prefs
        chrome_prefs["profile.default_content_settings"] = {"images": 2}     

        service = Service(executable_path=self.driver_path)
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

        self.driver.get(self.start_url)
        self.wait = WebDriverWait(self.driver, timeout=20)
        self.load_pages()
        urls = self.get_news_urls()
        data = self.get_data_from_urls(urls)

        self.driver.quit()
        return data

    def load_pages(self):
        button_xpath = 'button[class="button__Base-kwkpzw-0 fpijDs BrowseArticleData___StyledButton-sc-1qvnay0-0 eByvXQ"]'
        
        button = self.driver.find_element(By.CSS_SELECTOR, button_xpath)
        for _ in range(32):
            self.wait.until(EC.element_to_be_clickable(button)).click()

    def get_news_urls(self):
        urls = []
        links_xpath = 'a[class="link__CustomNextLink-sc-1r7l32j-0 iCQspp"]'
 
        links = self.driver.find_elements(By.CSS_SELECTOR, links_xpath)
        for link in links:
            href = link.get_attribute('href')
            urls.append(href)
        
        return urls

    def get_data_from_urls(self, urls):
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
                    content_xpath = '//p[@class="typography__StyledDynamicTypographyComponent-t787b7-0 lddBNw ParagraphElement__ParagraphBase-sc-1soo3i3-0 gOVZGU"]'
                    tags_xpath = '//span[@class="typography__StyledDynamicTypographyComponent-t787b7-0 eMeOeL"]'
                    
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
                    
                    counter += 1
                    data.append(obj)
                except:
                    zoomit2_urls.append(url)

        # zoomgi
        self.get_skipped_data(data,
                         zoomgi_urls,
                         title_xpath= '//span[@class="row"]', 
                         content_xpath= '//div[@id="bodyContainer"]//p', 
                         tags_xpath= '//a[@class="GroupName"]',
                         is_zoomgi = True)

        # pedal
        self.get_skipped_data(data,
                         pedal_urls, 
                         title_xpath= '//h1[@class="post-title entry-title"]', 
                         content_xpath= '//div[@class="entry-content entry clearfix"]//p', 
                         tags_xpath= '//a[@rel="tag"]')
        
        # zoomit2
        self.get_skipped_data(data,
                         zoomit2_urls, 
                         title_xpath= '//h1[@class="typography__StyledDynamicTypographyComponent-t787b7-0 krllpu"]', 
                         content_xpath= '//p[@class="typography__StyledDynamicTypographyComponent-t787b7-0 lddBNw ParagraphElement__ParagraphBase-sc-1soo3i3-0 gOVZGU"]',
                         tags_xpath= '//span[@class="typography__StyledDynamicTypographyComponent-t787b7-0 jaRosJ"]') 

        return data
    
    def get_skipped_data(self, 
                         data,
                         urls, 
                         title_xpath, 
                         content_xpath, 
                         tags_xpath,
                         is_zoomgi = False):
        for url in urls:
            self.driver.get(url)

            try:
                title = self.wait.until(EC.presence_of_element_located(
                                            (By.XPATH, title_xpath)
                                            )).text
                
                content = self.get_text_elements(xpath= content_xpath)
                
                if (is_zoomgi):
                    tags = self.wait.until(EC.presence_of_elements_located(
                                            (By.XPATH, tags_xpath)
                                            )).text
                    tags = [tags]
                else:
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