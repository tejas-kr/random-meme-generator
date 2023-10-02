import requests
from bs4 import BeautifulSoup

class Meme:
    """Meme"""
    soup: BeautifulSoup
    url: str

    def __init__(self, count: int = 1) -> None:
        """__init__

        Args:
            count (int, optional): Number of memes to get. Defaults to 1.
        """

        self.url = "https://www.generatormix.com/random-memes?number=%d"%(count)
        proxies = { 
            "http": 'http://34.142.51.21:443'
        }

        web_code = requests.get(self.url, proxies=proxies)
        self.soup = BeautifulSoup(web_code.content, 'html.parser')

    def get_memes(self):
        """get_memes

        Yields:
            tuple: ('Meme Title', 'Meme Link')
        """

        imgs = self.soup.find('div', id='output').find_all('img')
        for img in imgs:
            yield (img['alt'], img['data-src'])
