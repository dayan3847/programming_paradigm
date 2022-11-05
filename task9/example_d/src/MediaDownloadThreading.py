import concurrent.futures
import threading
import requests
from MediaDownload import MediaDownload


class MediaDownloadThreading(MediaDownload):
    __thread_local = threading.local()

    def get_session(self):
        if not hasattr(MediaDownloadThreading.__thread_local, "session"):
            MediaDownloadThreading.__thread_local.session = requests.Session()
        return self.__thread_local.session

    def download_site(self, url):
        session = self.get_session()
        with session.get(url) as response:
            print(f"Read {len(response.content)} from {url}")

    def download_all_sites(self, sites):
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            executor.map(self.download_site, sites)
