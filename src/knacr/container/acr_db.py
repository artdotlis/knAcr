from dataclasses import dataclass, field
from enum import Enum
from typing import final


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class AcrChaCon:
    id: int
    type: str


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class AcrDb:
    acr: str
    code: str
    name: str
    active: bool
    regex_ccno: str
    regex_id: str
    homepage: str = ""
    catalogue: str = ""
    acr_changed_to: list[AcrChaCon] = field(default_factory=list)
    acr_syn: list[str] = field(default_factory=list)


# TODO increase
class AcrChaT(Enum):
    unk = "unknown"
    syn = "synonym"
    dep = "transfer"


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class CatArgs:
    acr: str
    id: str
    pre: str
    core: str
    suf: str
