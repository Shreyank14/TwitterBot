from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
import random

class TwitterBot:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.bot=webdriver.Firefox()

    def closeBrowser(self):
        self.bot.close()
    
    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/') #opening twitter on moziila
        print("Opening twitter on mozilla")
        time.sleep(3)
        email = bot.find_element_by_class_name('email-input')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        print("Entering username and password")
        password.send_keys(Keys.RETURN)
        print("loggin!!!")
        time.sleep(8)
    
    def like_tweet(self,hastag):
        bot = self.bot
        bot.get('https://twitter.com/search?q='+hastag+'&src=typd')
        print('searching for hastag')
        time.sleep(5)
        for i in range(1,5):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            print('scrolling to the bottom')
            time.sleep(3)
            tweets = bot.find_elements_by_xpath('//div[@data-testid="tweet"]')
            print(tweets)
            #links = [elem.get_attribute('data-permalink-path') for elem in tweets]
            for tweet in tweets:
                try:
                    bot.find_element_by_xpath('//div[@data-testid="like"]').click()
                    time.sleep(random.randint(5, 30))
                    #time.sleep(3)
                except Exception as ex:
                    time.sleep(60)
        print("Done Scrolling")


username = ""
password = ""

twitter= TwitterBot(username,password)
twitter.login()
#twitter.like_tweet('StockMarket')

hashtags=['StockMarket','economy','Bitcoin','crypto','wallstreet']

while True:
        try:
            # Choose a random tag from the list of tags
            tag = random.choice(hashtags)
            twitter.like_tweet(tag)
        except Exception:
            twitter.closeBrowser()
            time.sleep(60)
            twitter = TwitterBot(username,password)
            twitter.login()


 
