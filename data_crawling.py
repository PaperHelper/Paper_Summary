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

    pubs = {
            'cs.ai': ['nips','ieee','eccv','cvpr','iccv','aaai','icml','aamas','cibb','ecai','ecml pkdd','iclr','ijcai','iswc','neurlps','elsevier'],
            'cs.db': ['sigkdd','sigmod','cikm','acm','ieee','elsevier','cidr','ecir','ecis','icdt','icis','iswc',,'jcdl','kdd','pods','sigir','vldb'],
            'cs.os': ['atc','usenix','acm','middleware','sosp','systor'],
            'cs.dc': ['acm','disc','dsn','ieee','debs','icdcs','icpads','ipdps','podc','ppopp','sirocco','spaa','srds','hipc','sc','elsevier']
            
            }
    fields = ['cs.ai']

    # driver = webdriver.Chrome('./chromedriver')
    # driver.implicitly_wait(3)
    URL = f"https://arxiv.org/search/advanced"
    param = {
            'advanced' : '',
            'classification-computer_science' : 'y',
            'date-date_type' : 'submitted_date',
            'abstracts' : 'show',
            'size' : '50',
            'order' : '-announced_date_first'
            }

    cnt = 0
    for i, field in enumerate(fields):
        for pub in pubs[i]:
            param[f'terms-{cnt}-operator'] = 'AND' if cnt==0 else 'OR'
            param[f'terms-{cnt}-term'] = field+' '+pub
            param[f'terms-{cnt}-field'] = 'all'
            cnt += 1

    response = requests.get(URL,params=param)
    print(response)
    print(response.url)
    print(response.status_code)
    # html = driver.page_source
    res = requests.get(URL)
    soup = BeautifulSoup(html, 'html.parser')

    
