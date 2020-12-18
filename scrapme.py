def next_chapter():
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import (ElementNotVisibleException)
    from urllib.request import urlopen, Request, urlretrieve
    import sys
    import warnings
    from bs4 import BeautifulSoup
    import shutil
    import wget
    import requests
    import time
    import urllib.parse
    import random
    from lxml.html import fromstring
    from requests import get
    # import driver
    import re


    driver = webdriver.Firefox()



    class find_user():  # Copy other classes that aims to do the same but for the user name
        def __init__(self):
            pass

        def any(self):
            pass

        def find_gg(self, urls):  # USE GOOGLE TO FIND USERNAME SCRAPDED FROM IG
            driver.get("https://www.google.com/search?q=" + urls)
            driver.implicitly_wait(5)
            driver.maximize_window()

        def find_ya(self, urls):  # USE YANDEX TO FIND USERNAME SCRAPDED FROM IG
            driver.get("https://yandex.com/search/?text=" + urls)
            driver.implicitly_wait(5)
            driver.maximize_window()

        def all_normal(self):  # use url to get yandex result

            self.my_results2 = list()  # LIST WHERE ALL LINKS

            urll = driver.current_url

            A = ("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
                 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
                 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
                 )

            Agent = A[random.randrange(len(A))]

            headers = {'user-agent': Agent}
            r = requests.get(urll, headers=headers)
            # BeautifulSoup
            soup = BeautifulSoup(r.text, 'lxml')
            search_div = soup.find_all(class_='rc')  # find all divs tha contains search result
            for result in search_div:  # loop result list
                self.my_results2.append('Title: %s' % result.h3.string)  # geting h3
                self.my_results2.append('.........')
                self.my_results2.append('Url: %s' % result.a.get('href'))  # geting a.href
                self.my_results2.append('.........')
                self.my_results2.append('Description: %s' % result.find(class_='st'))  # description
                self.my_results2.append('\n###############\n')

        def save_us(self):  # It runs the method SOUP_FS and then save all links in a file
            self.all_normal()
            f = open("gg.txt", "a+", encoding="utf-8")
            for word in self.my_results2:
                f.write(word)
            f.close()

        def save_us1(self):  # It runs the method SOUP_FS and then save all links in a file
            self.all_normal()
            f = open("yan.txt", "a+", encoding="utf-8")
            for word in self.my_results2:
                f.write(word)
            f.close()

    ab3 = find_user()
    ab4 = find_user()
    f = open("user.txt", "r")
    ff = f.read()
    f1 = list()
    f1.append(ff)



    print("Scraping now , all results will be saved on nick_gg.txt")
    for item1 in f1:  # Try to find for the username before scraped on IG

        my_url = urllib.parse.quote(item1)
        ab3.find_gg(my_url)
        driver.implicitly_wait(3)
        ab3.save_us()

    print("Scraping now , all results will be saved on nick_ya.txt")
    for item2 in f1:  # Try to find for the username before scraped on IG

        my_url = urllib.parse.quote(item2)
        ab4.find_ya(my_url)
        driver.implicitly_wait(3)
        ab4.save_us()


next_chapter()