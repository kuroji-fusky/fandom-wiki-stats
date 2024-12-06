from typing import Any, Optional
from bs4 import BeautifulSoup
import requests


rs = requests.Session()
_soup_headers = {
    "User-Agent": "FWS/Docker+scraper@kurojifusky.com"
}


def request_soup(url: str, *,
                 params: Optional[dict[str, Any]], verbose=False) -> (dict[str, BeautifulSoup | int | bool] | BeautifulSoup):
    _req = rs.get(url, params=params, timeout=25, headers=_soup_headers)
    _soup = BeautifulSoup(_req.text, "html.parser")

    if verbose:
        return {'soup': _soup, 'status': _req.status_code, 'ok': _req.ok}

    return _soup
