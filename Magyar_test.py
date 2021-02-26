from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
#driver = webdriver.Chrome(r'chromedriver.exe')

#teszt kezdete:
class MYLittleTest(unittest.TestCase):
    @classmethod #osztályfüggvény ez ilyen kis cimke
    def setUpClass(cls): #driver eléréshez használjuk
        cls.driver = webdriver.Chrome(r'chromedriver.exe') #csak a lapokat nyitja meg, nem mindig újra a böngészőt
        cls.driver.implicitly_wait(10) #várunk a cls megnyitásra
        cls.driver.maximize_window() #a böngészőt mindig nagy ablakban nyitja meg
    
#tesztesetek (A teszteket mindig test_ -al kezdődnek):
    # def test_runTest(self):
    #     self.driver.get("http://www.lorumipse.hu/") LorumIpse megnyitás
    
    # def test_MybuttonTest(self):
    #     self.driver.get("http://www.lorumipse.hu/") 
    #     self.driver.find_elements_by_class_name('') 
    #     self.driver.find_element_by_id('more').click() gombkattintás 

#Youtube teszt:
    #tesztesetek:
    def test_Youtube(self):
        self.driver.get("https://www.youtube.com")
        #self.driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/paper-dialog/yt-upsell-dialog-renderer/div/div[3]/div[1]/yt-button-renderer/a/paper-button').click()
        
        #ha nincs bejelentkezve a felhasználó, akkor a bejelentkezési felugró iframet átugorja
        #majd elfogadja a cookie-k használatát
        try:
            self.driver.find_element_by_xpath('//*[@id="dismiss-button"]/yt-button-renderer').click() 
            self.driver.find_element_by_id('iframe') #iframe megtalálás id alapján
            self.driver.switch_to_frame('iframe') #iframe-re váltás
            self.driver.find_element_by_id('introAgreeButton').click()

            self.driver.switch_to_default_content() #az iframebe váltás miatt az alap oldalra kell váltani
        except Exception as e:
            print('Nincs iframe'+e)
        
        self.driver.find_element_by_id('search').send_keys('WAP' + Keys.ENTER)
        #beírja a keresőbe a videó nevét (WAP), majd Entert nyom és keres is

        #videó elindítása:
        result_videos = self.driver.find_elements_by_class_name('style-scope ytd-video-renderer')
        result_videos[0].click() #az első találatot nyitja meg a videók közül

        #teljes képernyős videónézés:
        self.driver.find_element_by_xpath('//*[@id="movie_player"]/div[24]/div[2]/div[2]/button[10]').click()

        #youtube skip gomb megnyomása, ha van:
        try:
            time.sleep(5)
            self.driver.find_element_by_xpath('//*[@id="skip-button:6"]/span/button').click() #skip/átugró gombra kattint
            try:
                time.sleep(5)
                self.driver.find_element_by_xpath('//*[@id="skip-button:6"]/span/button').click()#skip/átugró gombra kattint
            except Exception as e:
                print('Nincs második reklám: '+e)
        except Exception as e:
            print('Nincs reklám: '+e)

    # Mi történjen a teszt lezárásakor:
    @classmethod 
    def tearDownClass(cls):
        print("\n Test befejezve!")

unittest.main() #osztály meghívása

