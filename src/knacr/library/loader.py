from typing import Final, TypeVar

import requests
from knacr.container.acr_db import AcrDb
from knacr.container.fun.acr_db import create_acr_db
from knacr.errors.custom_exceptions import ReqURIEx, ValJsonEx
from knacr.library.validate import validate_acr_db_schema


LATEST_VER: Final[str] = "latest"


def load_acr_db(version: str = LATEST_VER, /) -> dict[int, AcrDb]:
    req = f"https://raw.githubusercontent.com/artdotlis/knAcr/{version}/data/acr_db.json"
    print("downloading from github collection")
    if (res := requests.get(req, timeout=60)).ok:
        con = res.json()
        return parse_acr_db(con)
    else:
        raise ReqURIEx(f"Could not get {req}")


_TJ = TypeVar("_TJ")


def parse_acr_db(acr_db: _TJ) -> dict[int, AcrDb]:
    if not isinstance(acr_db, dict):
        raise ValJsonEx("JSON is not a dictionary")
    validate_acr_db_schema(acr_db)
    return create_acr_db(acr_db)
