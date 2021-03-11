import numpy as np

from .base_element import BaseElement
from .transform import Transform


class SimpleDispersion(Transform):
    def __init__(self, x, y, gamma, plot_xrange, plot_yrange, n_points):
        super().__init__(plot_xrange, plot_yrange, n_points)
        self.x = x / gamma
        self.y = y * gamma

class Fiber(BaseElement):
    def __init__(self): # TODO length, ... etc 
        super().__init__()

    def apply_transform(self):
        super().apply_transform()

        input_signal = self.input_node.apply_transform()

        self.transform = SimpleDispersion(
            input_signal.x,
            input_signal.y,
            0.5,
            input_signal.plot_xrange,
            input_signal.plot_yrange,
            input_signal.n_points
        )

        return self.transform