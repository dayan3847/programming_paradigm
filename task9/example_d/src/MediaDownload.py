from abc import ABC, abstractmethod

import requests


class MediaDownload(ABC):
    _session = None

    def __int__(self):
        self._session = requests.Session()

    @abstractmethod
    def download_site(self, url):
        pass

    @abstractmethod
    def download_all_sites(self, sites):
        pass
