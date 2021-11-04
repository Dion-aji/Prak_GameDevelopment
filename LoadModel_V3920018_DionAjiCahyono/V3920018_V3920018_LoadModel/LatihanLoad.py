from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3


class Myapp(ShowBase):
    def __init__(self):
        super().__init__()
    #     # Load the environment model.
    #     self.scene = self.loader.loadModel("models/environment")
    #     # Reparent the model to render.
    #     self.scene.reparentTo(self.render)
    #    # Apply scale and position transforms on the model.
    #     self.scene.setScale(0.25, 0.25, 0.25)
    #     self.scene.setPos(-8, 42, 0)

        self.pohon = self.loader.load_model("E 45 Aircraft_obj.obj")
        self.pohon.reparentTo(self.render)
        self.pohon.setScale(2, 2, 2)
        self.pohon.setPos(-8, 42, 0)

app = Myapp()
app.run()