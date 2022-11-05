import multiprocessing

import requests

from MediaDownload import MediaDownload


class MediaDownloadMultiprocessing(MediaDownload):

    def download_site(self, url):
        with requests.Session().get(url) as response:
            name = multiprocessing.current_process().name
            print(f"{name}:Read {len(response.content)} from {url}")

    def download_all_sites(self, sites):
        with multiprocessing.Pool() as pool:
            pool.map(self.download_site, sites)
