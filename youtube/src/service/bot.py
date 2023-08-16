import requests

from loguru import logger

from src.core.util import find_jsons, find_single_item


class Bot:

    def __init__(self, live_ids: list):
        self.live_ids = live_ids

    def test(self):
        session = requests.session()
        headers = {
            'Host': 'm.youtube.com',
            'Proxy-Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Accept-Encoding': 'gzip, deflate'
        }

        response = session.get(
            f"https://m.youtube.com/watch?v={self.live_ids[0]}",
            headers=headers,
            # proxies=proxy1.FormatProxy()
        )
        data = response.text
        # base_url_parts = data.split(r'videostatsWatchtimeUrl\":{\"baseUrl\":\"')
        # logger.info(len(base_url_parts))
        # logger.info(base_url_parts)
        # url = base_url_parts[1].split(r'\"}')[0].replace(r"\\u0026", r"&").replace('%2C', ",").replace("\/", "/")

        jsons = find_jsons(data)
        #jsons = [json for json in jsons if "videostatsWatchtimeUrl" in json]
        json = find_single_item("videostatsWatchtimeUrl", jsons)

        if json:
            logger.info(json)
