import requests

from loguru import logger

from src.core.util import find_jsons, find_single_item, find_args_from_url
from src.service.proxy import Proxy


class Bot:

    def __init__(self, live_ids: list):
        self.live_ids = live_ids
        self.proxy = Proxy()

    def test(self):
        live_id = self.live_ids[0]

        session = requests.session()
        headers = {
            'Host': 'm.youtube.com',
            'Proxy-Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Accept-Encoding': 'gzip, deflate'
        }

        logger.info(f"Started GET for watch url of Youtube Video {live_id}")
        response = session.get(
            f"https://m.youtube.com/watch?v={live_id}",
            headers=headers,
            proxies=self.proxy.next_proxy(),
            verify=False
        )
        logger.info(f"Ended GET for watch watch url of Youtube Video {live_id}")
        data = response.text

        # find few args
        jsons = find_jsons(data)
        watch_url = find_single_item(jsons, "videostatsWatchtimeUrl")
        base_url = find_single_item(watch_url, "baseUrl")
        args = find_args_from_url(base_url, ("cl", "ei", "of", "vm"))

        # call api for watch time
        cl = args.get("cl")
        ei = args.get("ei")
        of = args.get("of")
        vm = args.get("vm")

        headers = {
            'Host': 's.youtube.com',
            'Proxy-Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1',
            'Accept': 'image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5',
            'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
            "Referer": f"https://m.youtube.com/watch?v={live_id}"
        }
        url = f"https://s.youtube.com/api/stats/watchtime?ns=yt&el=detailpage&cpn=isWmmj2C9Y2vULKF&docid={live_id}&ver=2&cmt=7334&ei={ei}&fmt=133&fs=0&rt=1003&of={of}&euri&lact=4418&live=dvr&cl={cl}&state=playing&vm={vm}&volume=100&c=MWEB&cver=2.20200313.03.00&cplayer=UNIPLAYER&cbrand=apple&cbr=Safari%20Mobile&cbrver=12.1.15E148&cmodel=iphone&cos=iPhone&cosver=12_2&cplatform=MOBILE&delay=5&hl=ru&cr=GB&rtn=1303&afmt=140&lio=1556394045.182&idpj=&ldpj=&rti=1003&muted=0&st=7334&et=7634"
        session.get(
            url,
            headers=headers,
            proxies=self.proxy.next_proxy(),
            verify=False
        )

        if base_url:
            logger.info(args)
            # logger.info(base_url)
