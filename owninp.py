def www():
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
    import regme
    # import driver


    import colorama
    from colorama import Back, Fore, Style

    colorama.init()

    slist = list()
    print(Fore.MAGENTA)
    print(Back.LIGHTWHITE_EX)

    a = input("Please input a website:")
    for i in a:
        slist.append(i)




    #driver = webdriver.Firefox(executable_path="C:\\Users\\Win10\\Desktop\\ax\\geckodriver.exe")
    driver = webdriver.Firefox()

    nerolist = list()



    class gg_in():  # Class to all interactions with the google page

        def __init__(self):

            pass

        def get_start(self):  # simple get the driver to instagram page
            pass

        def sel_img(self, urls):  # that the url from  a list made by the first script
            driver.get("https://www.google.com/searchbyimage?image_url=" + urls)
            driver.implicitly_wait(5)
            driver.maximize_window()

        def soup_fs(self):  # that do most of the program it scrape  google search and it append everything to the list
            self.my_results = list()  # LIST WHERE ALL LINKS
            urll = driver.current_url

            A = ("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
                 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
                 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
                 )

            Agent = A[random.randrange(len(A))]  # Randomize the headers to not be blocked by google

            headers = {'user-agent': Agent}
            r = requests.get(urll, headers=headers)
            # BeautifulSoup
            soup = BeautifulSoup(r.text, 'lxml')
            search_div = soup.find_all(class_='rc')  # find all divs tha contains search result
            for result in search_div:  # loop result list
                self.my_results.append('Title: %s' % result.h3.string)  # geting h3
                self.my_results.append('.........')
                self.my_results.append('Url: %s' % result.a.get('href'))  # geting a.href
                self.my_results.append('.........')
                self.my_results.append('Description: %s' % result.find(class_='st'))  # description
                self.my_results.append('\n###############\n')

        def save_list(self):  # It runs the method SOUP_FS and then save all links in a file
            self.soup_fs()
            f = open("google.txt", "a", encoding="utf-8")
            for word in self.my_results:
                f.write(word)
            f.close()

        def save_user(self, urls):
            # https://www.google.com/search?q=
            # that the url from  a list made by the first script
            driver.get("https://www.google.com/search?q=" + urls)
            driver.implicitly_wait(5)
            driver.maximize_window()


    class yandex_in():

        def __init__(self):
            pass

        def getyan(self):  # get yandex main page
            pass

        def sel_img(self, urls):  # that the url from  a list made by the first script
            driver.get("https://yandex.com/images/search?rpt=imageview&url=" + urls)
            driver.implicitly_wait(5)
            driver.maximize_window()

        def yan_soup(self):  # use url to get yandex result

            self.my_results1 = list()  # LIST WHERE ALL LINKS

            urll = driver.current_url

            A = ("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
                 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
                 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
                 )

            Agent = A[random.randrange(len(A))]  # Randomize the headers to not be blocked by Yandex

            headers = {'user-agent': Agent}
            r = requests.get(urll, headers=headers)
            # BeautifulSoup
            soup = BeautifulSoup(r.text, 'lxml')
            search_div = soup.find_all(class_='rc')  # find all divs tha contains search result
            for result in search_div:  # loop result list
                self.my_results1.append('Title: %s' % result.h3.string)  # geting h3
                self.my_results1.append('.........')
                self.my_results1.append('Url: %s' % result.a.get('href'))  # geting a.href
                self.my_results1.append('.........')
                self.my_results1.append('Description: %s' % result.find(class_='st'))  # description
                self.my_results1.append('\n###############\n')

        def save_yan(self):  # It runs the method SOUP_FS and then save all links in a file
            self.yan_soup()
            f = open("yandex.txt", "a", encoding="utf-8")
            for word in self.my_results1:
                f.write(word)
            f.close()
            pass

        def save_user2(self, urls):
            # that the url from  a list made by the first script
            driver.get("https://yandex.com/search/?text=" + urls)
            driver.implicitly_wait(5)
            driver.maximize_window()


    # Logic usend on selenium

    # Google Logic
    ab1 = gg_in()  # Start google class
    ab1.get_start()  # does nothing

    ab2 = yandex_in()  # Start yandex class
    ab2.getyan()  # Does nothing
    # Links Scraped from instagram
    int_f = open("in_links.txt", "r")
    int_r = int_f.read()

    b = open("usr.txt", "a", encoding="utf-8")
    for word in nerolist:
        b.write(word)
    b.close()

    print("Scraping now Google , all results will be saved on google.txt")
    for item in slist:  # iteration for google scraping

        my_url = urllib.parse.quote(item)
        ab1.sel_img(my_url)
        driver.implicitly_wait(3)
        ab1.save_list()

    for item1 in nerolist:  # Try to find for the username before scraped on IG

        my_url = urllib.parse.quote(item1)
        ab1.save_user(my_url)
        driver.implicitly_wait(3)
        ab1.save_list()

    for item15 in nerolist:  # Try to find for the username before scraped on IG

        my_url = urllib.parse.quote(item15)
        ab2.save_user2(my_url)
        driver.implicitly_wait(3)
        ab2.save_yan()

    print("Scraping now Yandex , all results will be saved on yandex.txt")
    for item2 in slist:  # Same but for yandex
        my_url = urllib.parse.quote(item2)
        ab2.sel_img(my_url)
        driver.implicitly_wait(3)
        ab2.save_yan()

    regme.regme()