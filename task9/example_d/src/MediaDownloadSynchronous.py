import requests

from MediaDownload import MediaDownload


class MediaDownloadSynchronous(MediaDownload):

    def download_site(self, url):
        with requests.Session().get(url) as response:
            print(f"Read {len(response.content)} from {url}")

    def download_all_sites(self, sites):
        for url in sites:
            self.download_site(url)
