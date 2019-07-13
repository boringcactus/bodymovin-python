from typing import List, Union, Any, Optional
from dataclasses import dataclass

Number = Union[int, float]


@dataclass
class Bezier:
    x: Number  # X axis
    y: Number  # Y axis


@dataclass
class MDBezier:
    x: List[Number]  # X axis
    y: List[Number]  # Y axis


@dataclass
class OffsetKeyframe:
    s: List[Number]  # Start value
    t: Number  # Start time
    i: MDBezier  # In value for Bezier curve
    o: MDBezier  # Out value for Bezier curve


@dataclass
class Value:
    k: Number  # Value
    x: Optional[str] = None  # Expression
    ix: Optional[str] = None  # Property Index
    a: int = 0  # not animated


@dataclass
class ValueKeyframe:
    s: Number  # Start
    t: Number  # Time
    i: Bezier  # Bezier in


@dataclass
class ValueKeyframed:
    k: List[ValueKeyframe]  # Value Keyframes
    x: str  # Expression
    ix: str  # Property Index
    a: int = 1  # animated


@dataclass
class MultiDimensional:
    k: List[Any]  # Value
    x: Optional[str] = None  # Expression
    ix: Optional[str] = None  # Property Index
    a: int = 0  # not animated


@dataclass
class MultiDimensionalKeyframed:
    k: List[OffsetKeyframe]  # Value Keyframes
    x: str  # Expression
    ix: str  # Property Index
    ti: List[Number]  # In Tangent (for spatial properties)
    to: List[Number]  # Out Tangent (for spatial properties)
    a: int = 1  # animated


@dataclass
class ShapeProp:
    c: bool  # Closed
    i: List[Number]  # In point Bezier
    o: List[Number]  # Out point Bezier
    v: List[List[Number]]  # Bezier vertices


@dataclass
class ShapePropKeyframe:
    s: List[ShapeProp]  # Start value
    t: int  # Start time
    i: MDBezier  # In value Bezier
    o: MDBezier  # Out value Bezier


@dataclass
class Shape:
    k: ShapeProp  # Value
    x: str  # Expression
    ix: str  # Property Index
    a: int = 0  # not animated


@dataclass
class ShapeKeyframed:
    k: List[ShapePropKeyframe]  # Value Keyframes
    x: str  # Expression
    ix: str  # Property Index
    ti: List[Number]  # In Tangent (for spatial properties)
    to: List[Number]  # Out Tangent (for spatial properties)
    a: int = 1  # animated
