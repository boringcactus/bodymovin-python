from typing import List, Optional
from dataclasses import dataclass, field

from . import helpers, effects, shapes


class Image:
    def __init__(self):
        raise NotImplementedError()


class Null:
    def __init__(self):
        raise NotImplementedError()


class Comp:
    def __init__(self):
        raise NotImplementedError()


@dataclass
class Shape:
    ks: helpers.Transform  # transform
    ao: int  # auto-orient
    ind: int  # layer index
    ip: int  # in point (first frame)
    op: int  # out point (last frame)
    st: float  # start time (?????)
    nm: str  # name
    shapes: List[shapes.AnyShape]  # items
    cl: Optional[str] = None  # HTML class
    ln: Optional[str] = None  # HTML ID
    hasMask: int = 0  # has a mask?
    parent: Optional[int] = None  # parent layer
    bm: helpers.BlendMode = helpers.BlendMode.Normal  # blend mode
    ddd: int = 0  # 3D?
    sr: int = 1  # time stretching
    masksProperties: List[helpers.Mask] = field(default_factory=list)  # masks
    ef: List[effects.Index] = field(default_factory=list)  # effects
    ty: int = 4


@dataclass
class Solid:
    ks: helpers.Transform
    ao: bool
    ind: int
    cl: str
    ln: str
    ip: int
    op: int
    st: float
    nm: int
    hasMask: bool
    masksProperties: List[helpers.Mask]
    ef: List[effects.Index]
    parent: int
    sc: str
    sh: int
    sw: int
    bm: helpers.BlendMode = 0
    ddd: bool = False
    sr: int = 1
    ty: int = 1


class Text:
    def __init__(self):
        raise NotImplementedError()
