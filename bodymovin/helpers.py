from typing import Union, Optional
from dataclasses import dataclass
from enum import Enum

from . import properties

MDProperty = Union[properties.MultiDimensional, properties.MultiDimensionalKeyframed]
Value = Union[properties.Value, properties.ValueKeyframed]
Shape = Union[properties.Shape, properties.ShapeKeyframed]


class BlendMode(Enum):
    Normal = 0
    Multiply = 1
    Screen = 2
    Overlay = 3
    Darken = 4
    Lighten = 5
    ColorDodge = 6
    ColorBurn = 7
    HardLight = 8
    SoftLight = 9
    Difference = 10
    Exclusion = 11
    Hue = 12
    Saturation = 13
    Color = 14
    Luminosity = 15


class Composite(Enum):
    Above = 1
    Below = 2


class LineCap(Enum):
    Butt = 1
    Round = 2
    Square = 3


class LineJoin(Enum):
    Miter = 1
    Round = 2
    Bevel = 3


class MaskMode(Enum):
    None_ = 'n'
    Additive = 'a'
    Subtract = 's'
    Intersect = 'i'
    Lighten = 'l'
    Darken = 'd'
    Difference = 'f'


class Mask:
    inv: bool  # Inverted
    nm: str  # Name
    pt: Shape  # Mask verts
    o: Value  # Opacity


@dataclass
class Transform:
    """A transform"""

    a: MDProperty  # Anchor Point
    p: MDProperty  # Position
    s: MDProperty  # Scale
    r: Value  # Rotation
    o: Value  # Opacity
    px: Optional[Value] = None  # Position X
    py: Optional[Value] = None  # Position Y
    pz: Optional[Value] = None  # Position Z
    sk: Optional[Value] = None  # Skew
    sa: Optional[Value] = None  # Skew Axis
