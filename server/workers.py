from abc import ABC, abstractmethod
from typing import Type, Literal, Optional, final
import kuropy.kuro_fs as kuro_fs
from utils import *


# This one's very specific for this use case, but in the future, will be moved into the kuro_utils module
_ClassType = TypeVar("_ClassType")


def abstractclass(cls: Type[_ClassType]) -> _ClassType:
    cls_dict = dict(cls.__dict__)

    if "__init__" in cls_dict:
        cls_dict["__init__"] = abstractmethod(cls_dict["__init__"])

    return type(cls.__name__, (ABC,), cls_dict)


@abstractclass
class PageStoreWorker(kuro_fs.KuroFileHandler):
    def __init__(self):
        self._load_file = self.read
        self._write_file = self.write

        self.collected_pages = []


@abstractclass
class _TemplateParserWorker(PageStoreWorker):
    def __init__(self):
        pass

    def parse_infobox(self):
        pass

    def __custom_template(self):
        pass


# These namespaces sufficent enough for showing the bare necessities for analytics
_Namespace_Literals = Literal["User", "NamedWiki", "File",
                              "MediaWiki", "Template", "Help", "Category", "Forum"]


BASE_FANDOM_URL = "fandom.com"


@final
class CrawlWorker(_TemplateParserWorker, PageStoreWorker):
    def __init__(self, base_prefix: str, *,
                 increment_page_cap: int = 50,
                 crawl_timeout: int = 10):
        if base_prefix is None:
            raise ValueError("base_url is required")

        self._increment_page_cap = increment_page_cap
        self._crawl_timeout = crawl_timeout

        # Check if wiki is up and operational
        main_page = request_soup(f"https://{base_prefix}.{BASE_FANDOM_URL}", verbose=True)  # noqa

        if main_page.ok:
            raise ConnectionRefusedError("Wiki closed for: <reason>")

        self._base_wiki_prefix = base_prefix

    def get_n_pages(self, namespaces: Optional[list[_Namespace_Literals]]):
        """Crawls all available namespaces such as `Template:*` or `File:`*"""
        if namespaces is None:
            return

        NAMESPACE_MAP: dict[_Namespace_Literals, int] = {
            "User": 2,
            "NamedWiki": 4,
            "File": 6,
            "MediaWiki": 8,
            "Template": 10,
            "Help": 12,
            "Category": 14,
            "Forum": 110,
        }

    # @protected
    def _iterate_pages(self):
        """Iterate pages from `Special:AllPages`"""
        _apage_from: str | None = None
        _apage_to: str | None = None

    def get_raw_page_content(self, *,
                             include_raw=False,
                             raw_only=False):
        """Gets and parses the raw page content, be it only text content"""
        pass

    def get_page_history(self, *,
                         limit=500,
                         include_protected_status=False):
        """Gets the page history, optionally including its protection status"""
        pass
