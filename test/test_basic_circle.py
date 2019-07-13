import json
import gzip

import bodymovin
from bodymovin.properties import Value, MultiDimensional


def test_circle():
    circle = bodymovin.shapes.Ellipse(
        d=0, nm='circle', mn='', p=MultiDimensional([0, 0]), s=MultiDimensional([512, 512])
    )
    fill = bodymovin.shapes.Fill(
        c=MultiDimensional([0.8, 0.2, 0.8, 1]), o=Value(100), nm='Fill', mn=''
    )
    group = bodymovin.shapes.Group(
        mn='', nm='cir', np=0, it=[circle, fill]
    )
    transform = bodymovin.helpers.Transform(
        o=Value(100), r=Value(0), a=MultiDimensional([256, 256, 0]),
        p=MultiDimensional([256, 256, 0]), s=MultiDimensional([100, 100, 100])
    )
    layer = bodymovin.layers.Shape(
        ks=transform, ao=0, ind=1, ip=0, op=180,
        st=0, nm='circle', shapes=[group]
    )
    anim = bodymovin.Animation(
        v="5.5.2",
        ip=0, op=180, w=512, h=512, fr=60,
        nm='circle', ddd=0,
        layers=[layer]
    )
    anim.tgs = 1
    with gzip.open('circle.tgs', mode='wt', encoding='utf-8') as f:
        json.dump(anim, f, cls=bodymovin.JSONEncoder)
    assert True
