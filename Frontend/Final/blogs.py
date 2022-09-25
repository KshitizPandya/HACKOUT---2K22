import requests
from bs4 import BeautifulSoup
import webbrowser
# from django.http import HttpResponse
# from django.shortcuts import render
# from datetime import datetime


def singhania():
    # fetching all href links
    url = "https://singhania.in/blog"
    # print(urls)
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    list = []
    for link in soup.find_all('a'):
        list.append(link.get('href'))

    # filtering the none values from the list
    filtered_list = []
    for ele in list:
        if ele != None:
            filtered_list.append(ele)

    # cleaning the href link for the required data
    urls = []
    for i in filtered_list:
        if "blog/" in i:
            # print(i)
            urls.append(i)
    proper = []
    for u in urls:
        tag = "https://singhania.in/" + u
        proper.append(tag)

    return proper

def singhania_present(s):
    new = []
    for i in s:
        q = i.replace("https://singhania.in/","").replace("blog/", "").replace("-", " ")
        new.append(q)

    return new



def vidhikarya():
    # fetching all hred links
    url = "https://www.vidhikarya.com/legal-blog"
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    list = []
    for link in soup.find_all('a'):
        list.append(link.get('href'))


    # filtering the none values from the list
    filtered_list = []
    for ele in list:
        if ele != None:
            filtered_list.append(ele)

    # cleaning the href link for the required data
    urls = []
    for i in filtered_list:
        if "/legal-blog/" in i:
            urls.append(i)

    proper = []
    for u in urls:
        tag = "https://www.vidhikarya.com/" + u
        proper.append(tag)

    res = [*set(proper)]
    # print(res)
    return res


def vidhikaria_present(v):
    new = []
    for i in v:
        q = i.replace("https://www.vidhikarya.com//legal-blog/", "").replace("-", " ")
        new.append(q)
    # print(new)
    return new


def myadvo():
    # fetching all hred links
    url = "https://www.myadvo.in/blog/"
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    list = []
    for link in soup.find_all('a'):
        list.append(link.get('href'))


    # filtering the none values from the list
    filtered_list = []
    for ele in list:
        if ele != None:
            filtered_list.append(ele)


    # cleaning the href link for the required data
    urls = []
    for i in filtered_list:
        if "/blog/" in i:
            urls.append(i)

    proper = []
    for u in urls:
        tag = "https://www.myadvo.in" + u
        proper.append(tag)
    res = [*set(proper)]
    return res

def myavdo_present(c):
    new = []
    for i in c:
        q = i.replace("https://www.myadvo.in/blog/", "").replace("-", " ")
        new.append(q)

    return new

# def django_call(request):
#     # asse = input("GIVE THE INPUT OF THE BLOG U WANT TO READ: ")
#     # asse = int(asse)
#     o = n
#     print(o)
#     return render(request, "index.html", {"o": o})
#     # webbrowser.open(o)


s = singhania()
v = vidhikarya()
c = myadvo()
x = singhania_present(s)
y = vidhikaria_present(v)
z = myavdo_present(c)
# print(s)
# print(v)
# print(c)
# print(x)
# print(y)
# print(z)
links = s+v+c
print(links)
print(len(links))
data = x+y+z
print(data)
print(len(data))

#
for ff in data:
    print(data.index(ff),".", ff)

take = input("Give input: ")
take = int(take)
n = links[take]