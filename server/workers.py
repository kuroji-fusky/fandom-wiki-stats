from typing import Literal, final
from abc import ABC, abstractmethod


class _FandomTemplateParser(ABC):
    @abstractmethod
    def __init__(self):
        pass

    def parse_infobox(self):
        pass

    def __custom_template(self):
        pass


@final
class CrawlWorker(_FandomTemplateParser):
    def __init__(self,
                 base_url: str,
                 *,
                 increment_page_cap: int = 50,
                 crawl_timeout: int = 10):
        if base_url is None:
            raise ValueError("base_url is required")

        self._base_url = base_url
        self._increment_page_cap = increment_page_cap
        self._crawl_timeout = crawl_timeout

    def get_all_pages(self):
        """Crawls from `Special:AllPages`, including redirects"""
        pass

    _NS_Literals = Literal["Template", "File", "Category"]

    def get_namespace_pages(self, namespaces: list[_NS_Literals]):
        """Crawls all available namespaces such as `Template:*` or `File:`*"""
        if namespaces is None:
            return

        pass

    def get_page_content(self, *,
                         include_raw=False,
                         raw_only=False,
                         get_history=False):
        """Gets and parses the page content"""
        pass
