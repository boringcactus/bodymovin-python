from typing import List, Union
from dataclasses import dataclass, field

from . import layers, sources

AnyLayer = Union[layers.Shape, layers.Solid, layers.Comp, layers.Image, layers.Null, layers.Text]
AnySource = Union[sources.Image, sources.Precomp]


@dataclass
class Animation:
    ip: int  # in point (first frame)
    op: int  # out point (last frame)
    fr: int  # frame rate
    w: int  # width
    ddd: int  # 3D?
    h: int  # height
    v: str  # Bodymovin version
    nm: str  # composition name
    layers: List[AnyLayer]
    assets: List[AnySource] = field(default_factory=list)
    chars: List[sources.Chars] = field(default_factory=list)
