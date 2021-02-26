from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
#driver = webdriver.Chrome(r'chromedriver.exe')

#test begin(opening):
class MYLittleTest(unittest.TestCase):
    @classmethod #It is a class function, a label
    def setUpClass(cls): #reach the driver
        cls.driver = webdriver.Chrome(r'chromedriver.exe') #csak a lapokat nyitja meg, nem mindig újra a böngészőt
        cls.driver.implicitly_wait(10) #waiting for cls opening
        cls.driver.maximize_window() # always open the browser in full screen
    
#test cases (tests begin with :test_ e.g: test_FirstTest()):
    # def test_runTest(self):
    #     self.driver.get("http://www.lorumipse.hu/") LorumIpse
    
    # def test_MybuttonTest(self):
    #     self.driver.get("http://www.lorumipse.hu/") 
    #     self.driver.find_elements_by_class_name('') 
    #     self.driver.find_element_by_id('more').click() ButtonClick 

#Youtube automatization:
    #test cases:
    def test_Youtube(self):
        self.driver.get("https://www.youtube.com")
        #self.driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/paper-dialog/yt-upsell-dialog-renderer/div/div[3]/div[1]/yt-button-renderer/a/paper-button').click()
        
        #if the user is not logged in, the login pop-up iframe will be skipped
        #and then accept cookies
        try:
            self.driver.find_element_by_xpath('//*[@id="dismiss-button"]/yt-button-renderer').click() 
            self.driver.find_element_by_id('iframe') #find iframe by id
            self.driver.switch_to_frame('iframe') #switch to iframe
            self.driver.find_element_by_id('introAgreeButton').click()

            self.driver.switch_to_default_content() #switch from iframe to default site
        except Exception as e:
            print('No iframe'+e)
        
        self.driver.find_element_by_id('search').send_keys('WAP' + Keys.ENTER) 
        #typing video what you want (here: WAP) to searchbar then pressing Enter to search

        #play the video automatically:
        result_videos = self.driver.find_elements_by_class_name('style-scope ytd-video-renderer')
        result_videos[0].click() #play the first video, wich the youtube found

        #full screen video playing/watching:
        self.driver.find_element_by_xpath('//*[@id="movie_player"]/div[24]/div[2]/div[2]/button[10]').click()

        #click skip button, to skip ads:
        try:
            time.sleep(5)
            self.driver.find_element_by_xpath('//*[@id="skip-button:6"]/span/button').click()#first skip button click
            try:
                time.sleep(5)
                self.driver.find_element_by_xpath('//*[@id="skip-button:6"]/span/button').click()#second skip button click
            except Exception as e:
                print('No second ad: '+e)
        except Exception as e:
            print('No ad(s): '+e)

    # closing
    @classmethod 
    def tearDownClass(cls):
        print("\n Test done!")

unittest.main() #call the class 

