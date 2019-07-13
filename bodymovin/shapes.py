from typing import List, Union, Any
from dataclasses import dataclass
from enum import Enum

from . import properties, helpers

MDProperty = Union[properties.MultiDimensional, properties.MultiDimensionalKeyframed]
Value = Union[properties.Value, properties.ValueKeyframed]


@dataclass
class Ellipse:
    mn: str  # Match Name
    nm: str  # Name
    d: int  # Direction
    p: MDProperty  # Position
    s: MDProperty  # Size
    ty: str = 'el'  # Type


@dataclass
class Fill:
    mn: str  # Match Name
    nm: str  # Name
    o: Value  # Opacity
    c: MDProperty  # Color
    ty: str = 'fl'  # Type


class GradientType(Enum):
    Linear = 1
    Radial = 2


@dataclass
class GFill:
    mn: str  # Match Name
    nm: str  # Name
    o: Value  # Opacity
    s: MDProperty  # Start Point
    e: MDProperty  # End Point
    t: GradientType  # Gradient Type
    h: Value  # Highlight Length
    a: Value  # Highlight Angle
    g: Any  # Gradient Colors
    ty: str = 'gf'


@dataclass
class Group:
    mn: str  # Match Name
    nm: str  # Name
    np: int  # Number of Properties
    it: List['AnyShape']
    ty: str = 'gr'  # Type


@dataclass
class GStroke:
    mn: str  # Match Name
    nm: str  # Name
    o: Value  # Opacity
    s: MDProperty  # Start Point
    e: MDProperty  # End Point
    t: GradientType  # Gradient Type
    h: Value  # Highlight Length
    a: Value  # Highlight Angle
    g: Any  # Gradient Colors
    w: Value  # Stroke Width
    lc: helpers.LineCap  # Line Cap
    lj: helpers.LineJoin  # Line Join
    ml: int  # Miter Limit
    ty: str = 'gs'


@dataclass
class Merge:
    mn: str  # Match Name
    nm: str  # Name
    mm: int  # Merge Mode
    ty: str = 'mm'


@dataclass
class Rect:
    mn: str  # Match Name
    nm: str  # Name
    d: int  # Direction
    p: MDProperty  # Position
    s: MDProperty  # Size
    r: Value  # Rounded corners
    ty: str = 'rc'


@dataclass
class Repeater:
    mn: str  # Match Name
    nm: str  # Name
    c: Value  # Number of Copies
    o: Value  # Offset of Copies
    m: helpers.Composite  # Composite of copies
    tr: helpers.Transform  # Transform for each copy
    ty: str = 'rp'


@dataclass
class Round:
    mn: str  # Match Name
    nm: str  # Name
    r: Value  # Radius
    ty: str = 'rd'


@dataclass
class Shape:
    mn: str  # Match Name
    nm: str  # Name
    d: int  # Direction
    ks: Union[properties.Shape, properties.ShapeKeyframed]  # Vertices
    ty: str = 'sh'


class StarType(Enum):
    Star = 1
    Polygon = 2


@dataclass
class Star:
    mn: str  # Match Name
    nm: str  # Name
    d: int  # Direction
    p: MDProperty  # Position
    ir: Value  # Inner Radius
    is_: Value  # Inner Roundness
    or_: Value  # Outer Radius
    os: Value  # Outer Roundedness
    r: Value  # Rotation
    pt: Value  # Points
    sy: StarType  # Star Type
    ty: str = 'sr'


@dataclass
class Stroke:
    mn: str  # Match Name
    nm: str  # Name
    lc: helpers.LineCap  # Line Cap
    lj: helpers.LineJoin  # Line Join
    ml: int  # Miter Limit
    o: Value  # Opacity
    w: Value  # Stroke Width
    c: MDProperty  # Stroke Color
    ty: str = 'st'


@dataclass
class Transform:
    nm: str  # Name
    a: MDProperty  # Anchor Point
    p: MDProperty  # Position
    s: MDProperty  # Scale
    r: Value  # Rotation
    o: Value  # Opacity
    sk: Value  # Skew
    sa: Value  # Skew Axis


@dataclass
class Trim:
    mn: str  # Match Name
    nm: str  # Name
    s: Value  # Start
    e: Value  # End
    o: Value  # Offset
    ty: str = 'tm'


AnyShape = Union[
    Shape, Rect, Ellipse, Star, Fill,
    GFill, GStroke, Stroke, Merge, Trim,
    Group, Round, Repeater
]
