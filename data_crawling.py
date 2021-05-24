from requests import get  # to make GET request
from selenium import webdriver
import requests
import time
from bs4 import BeautifulSoup



def download(url, file_name):
    with open(file_name, "wb") as file:   # open in binary mode
        response = get(url)               # get request
        file.write(response.content)      # write to file

if __name__ == '__main__':

    driver = webdriver.Chrome('/Users/shinnahyun/Desktop/chromedriver')
    driver.implicitly_wait(3)
    URL = f"https://arxiv.org/list/cs.DB/recent"
    driver.get(URL)
    html = driver.page_source
    res = requests.get(URL)
    soup = BeautifulSoup(html, 'html.parser')

    all_nums = soup.find_all('a', {"title": "Download PDF"})

    #print(all_nums)
    for a in all_nums:
        href = a.attrs['href']
        print(href)
        url = "https://arxiv.org{}.pdf".format(href)
        href = href.replace('/pdf/', '')
        download(url,"{}.pdf".format(href))
