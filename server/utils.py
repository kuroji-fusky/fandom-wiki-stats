from typing import Optional, TypeVar, TypedDict, overload
from bs4 import BeautifulSoup
import requests


rs = requests.Session()
_soup_headers = {
    "User-Agent": "FWS/Docker+scraper@kurojifusky.com"
}

_Params_T = TypeVar("_Params_T", bound=str)
_VerboseSoup = TypedDict("_Verbose_Req", {
    "soup": BeautifulSoup,
    "status": int,
    "ok": bool
})


@overload
def request_soup(url: str, *,
                 params: Optional[dict[str, _Params_T]], verbose=False) -> BeautifulSoup: ...


@overload
def request_soup(url: str, *,
                 params: Optional[dict[str, _Params_T]], verbose=True) -> _VerboseSoup: ...


def request_soup(url: str, *,
                 params: Optional[dict[str, _Params_T]], verbose=False) -> _VerboseSoup | BeautifulSoup:
    _req = rs.get(url, params=params, timeout=25, headers=_soup_headers)
    _soup = BeautifulSoup(_req.text, "html.parser")

    if verbose:
        return {'soup': _soup, 'status': _req.status_code, 'ok': _req.ok}

    return _soup
