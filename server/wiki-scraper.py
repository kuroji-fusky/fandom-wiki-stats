from typing import Any, Optional
from bs4 import BeautifulSoup
import requests


rs = requests.Session()
_soup_headers = {
    "User-Agent": "FWS/Docker+scraper@kurojifusky.com"
}


def request_soup(url: str, params: Optional[dict[str, Any]]) -> BeautifulSoup:
    _req = rs.get(url, params=params, timeout=25, headers=_soup_headers)
    return BeautifulSoup(_req.text, "html.parser")
