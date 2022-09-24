import requests
from bs4 import BeautifulSoup

def myadvo():
    # fetching all hred links
    url = "https://www.myadvo.in/blog/"
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    list = []
    for link in soup.find_all('a'):
        list.append(link.get('href'))
    print(list)


    # filtering the none values from the list
    filtered_list = []
    for ele in list:
        if ele != None:
            filtered_list.append(ele)
    print(filtered_list)


    # cleaning the href link for the required data
    urls = []
    for i in filtered_list:
        if "/blog/" in i:
            urls.append(i)
    print(urls)

    proper = []
    for u in urls:
        tag = "https://www.myadvo.in" + u
        proper.append(tag)
    print(proper)

    # print(len(proper))
    # print(proper)
    res = [*set(proper)]
    # print(res)
    return res

myadvo()