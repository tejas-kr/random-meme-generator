import requests
from bs4 import BeautifulSoup

class Meme:
    """Meme"""
    soup: BeautifulSoup
    url: str

    def __init__(self, logger: object, count: int = 1) -> None:
        """__init__

        Args:
            logger (object): Logger Object
            count (int, optional): Number of memes to get. Defaults to 1.
        """
        self.logger = logger
        self.url = "https://www.generatormix.com/random-memes?number=%d"%(count)
        proxies = { 
            "http": 'http://34.142.51.21:443'
        }

        try:
            web_code = requests.get(self.url, proxies=proxies)
            self.soup = BeautifulSoup(web_code.content, 'html.parser')
            self.logger.info("Soup Initialized")
        except Exception as e:
            self.logger.exception(e)

    def get_memes(self):
        """get_memes

        Yields:
            tuple: ('Meme Title', 'Meme Link')
        """

        imgs = self.soup.find('div', id='output').find_all('img')
        for img in imgs:
            yield (img['alt'], img['data-src'])
