import bs4 as bs
import sys
import schedule
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
import requests

tag = "job"
hashtagurl = "https://www.linkedin.com/feed/hashtag/" +  tag + "/"
print(hashtagurl)


class Page(QWebEnginePage):
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebEnginePage.__init__(self)
        self.html = ''
        self.loadFinished.connect(self._on_load_finished)
        self.load(QUrl(url))
        self.app.exec_()

    def _on_load_finished(self):
        self.html = self.toHtml(self.Callable)
        print('Load finished')

    def Callable(self, html_str):
        self.html = html_str
        self.app.quit()


def jprint(data_dict):
    print(json.dumps(data_dict, indent=4))

def mainprogram():
    page = Page(hashtagurl)
    soup = bs.BeautifulSoup(page.html, 'html.parser')
    for i in soup.find_all('span'):
      print(type(i))




mainprogram()