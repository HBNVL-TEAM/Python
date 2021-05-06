from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from modules.crawler import *
import requests as rq
from bs4 import BeautifulSoup
import urllib.parse as urlparse
import os
import urllib3
from concurrent.futures import ThreadPoolExecutor
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) 
import threading
class Test(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main = QUiLoader().load('main.ui',self)
        self.main.btnscan.clicked.connect(self.Sthread)
        self.main.show()
    def Sthread(self):
        t = threading.Thread(target=self.show)
        t.start()

    def show(self):
        listscan=self.main.listscan
        url=self.main.lineurl.text()
        self.crawler_links(url,45)

    def GetHref(html):
        soup= BeautifulSoup(html, "lxml")
        hreflist = []
        for link in soup.findAll('a'):
            href = link.get('href')
            if href and "#" not in href and "mailto" not in href and "javascript:" not in href:
                hreflist.append(href)
        return set(hreflist)

    def GetCurrentDir(url):
        urllen = len(url)
        for i in range(1, urllen):
            if "/" in url[-i:]:
                return url[:urllen - i + 1]
            elif "." in url[-i:]:
                while "/" not in url[-i:]:
                    i += 1
                return url[:urllen - i + 1]
        return False

    def CraftURL(url, href):
        href = href.replace("./", "")
        if url[-1:] != "/" and os.path.splitext(urlparse.urlparse(url).path)[0] == "":
            url = url + "/"
        urlsplited = urlparse.urlsplit(url)
        if href[:1] == "/":
            return urlsplited.scheme + "://" + urlsplited.netloc + href
        else:
            return GetCurrentDir(urlsplited.scheme + "://" + urlsplited.netloc + urlsplited.path) + href

    def GetLinks(url, html):
        hrefset = GetHref(html)
        links = []
        urlsplited = urlparse.urlsplit(url)
        baseurl = urlsplited.scheme + "://" + urlsplited.netloc
        for href in hrefset:
            if href[:7] != "http://" and href[:8] != "https://":
                links.append(CraftURL(url, href))
            elif href[:len(baseurl)] == baseurl:
                links.append(href)
        return links
    def crawler_links(self,url,total):
        listcrawler=[]
        listcrawler.append('Web Crawler Process: ')
        a=rq.get(url)
        b=ThreadPoolExecutor().submit(GetLinks,url,a.text).result()
        dem=0
        for i in b:
            if total==0:
                break
            d=rq.get(i)
            c=ThreadPoolExecutor(max_workers=len(b)).submit(GetLinks,i,d.text).result()
            total-=1
            for j in c:
                if j not in b:
                    b.append(j)
            dem+=1
            listcrawler.append(i)
            listscan=self.main.listscan
            item=QListWidgetItem(i,listscan)
        listcrawler.append('Total Links: '+str(dem))
        listcrawler.append("FINISH Crawler")
        return listcrawler
        #return b

app=QApplication()
frame=Test()
app.exec_()

