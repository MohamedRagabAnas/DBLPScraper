from bs4 import BeautifulSoup
import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
import lxml.html
import sys
import csv
#options
STRINGS_FOR_TEST = ["Sherif Sakr"]
DBLP_BASE_URL = 'http://dblp.uni-trier.de/'
PUB_SEARCH_URL = DBLP_BASE_URL + "search?q="


def query_db(authorName=STRINGS_FOR_TEST):
    '''
    returns the BeautifulSoup object of a query to DBLP
    :param pub_string: A list of strings of keywords
    :return: BeautifulSoup: A BeautifulSoup Object
    '''
    driver = webdriver.Chrome()
    driver.get(PUB_SEARCH_URL+""+authorName)
    html = driver.page_source
    time.sleep(1)
    elem = driver.find_element_by_tag_name("body")
    no_of_pagedowns = 20
    while no_of_pagedowns:
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.2)
        no_of_pagedowns-=1

    html = driver.page_source    
    return BeautifulSoup(html,"lxml")

def get_co_Authors(authorNames):
    authors = []
    for authorName in authorNames:
        soup = query_db(authorName)
        for author in soup.findAll('span', attrs={"itemprop": "author"}):
            authors.append(author.text)
    authors=list(set(authors))
    return authors

def main():
    authors=get_co_Authors(authorNames=["mohamed ragab moaawad","noha mohamed osman","hosam zaghloul"])
    with open('Co-Authors.csv', "wb") as csvfile:
        for authorName in authors:
           csvfile.write(str(authorName)+"\n")
    print authors
    
if __name__ == '__main__':
        main()
