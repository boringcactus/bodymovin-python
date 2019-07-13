import json.encoder
import dataclasses
import enum

from .animation import Animation

from . import effects, helpers, layers, properties, shapes, sources


class JSONEncoder(json.encoder.JSONEncoder):

    def default(self, o):
        if dataclasses.is_dataclass(o):
            return o.__dict__
        else:
            return o.value
