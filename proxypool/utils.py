import requests
import asyncio
import aiohttp
from bs4 import BeautifulSoup
from requests.exceptions import ConnectionError
from proxypool.setting import HEADERS


def get_page(url, options={}):
    print('Getting', url)
    try:
        r = requests.get(url, headers=HEADERS)
        print('Getting result', url, r.status_code)
        if r.status_code == 200:
            return r.text
    except ConnectionError:
        print('Crawling Failed', url)
        return None

def get_soup(url):
    """
    将网页解析为BeautifulSoup对象并返回
    :param url: target url
    :return: BeautifulSoup Object
    """
    html = requests.get(url, headers=HEADERS)
    try:
        soup = BeautifulSoup(html.content.decode('utf-8'), 'lxml')
    except UnicodeDecodeError:
        soup = BeautifulSoup(html.text, 'lxml')
    return soup

class Downloader(object):
    """
    一个异步下载器，可以对代理源异步抓取，但是容易被BAN。
    """

    def __init__(self, urls):
        self.urls = urls
        self._htmls = []

    async def download_single_page(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                self._htmls.append(await resp.text())

    def download(self):
        loop = asyncio.get_event_loop()
        tasks = [self.download_single_page(url) for url in self.urls]
        loop.run_until_complete(asyncio.wait(tasks))

    @property
    def htmls(self):
        self.download()
        return self._htmls
