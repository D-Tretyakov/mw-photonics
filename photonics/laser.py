import numpy as np

from .base_element import BaseElement
from .transform import Transform

class GaussFunction(Transform):
    def __init__(self, a, b, plot_xrange=[-5, 5], plot_yrange=[0, 10], n_points=101):
        super().__init__(plot_xrange, plot_yrange, n_points)
        self.x = np.linspace(*plot_xrange, n_points)
        self.y = a*np.exp(-(self.x**2)/b)

class StepFunction(Transform):
    def __init__(self, a, b, plot_xrange=[-5, 5], plot_yrange=[0, 10], n_points=101):
        super().__init__(plot_xrange, plot_yrange, n_points)
        self.x = np.linspace(*plot_xrange, n_points)
        self.y = np.heaviside(self.x+b/2, 0) - np.heaviside(self.x-b/2, 0)


class Laser(BaseElement):
    """
    Class to represent Laser source
    
    arguments:
    transform_type: Gauss or step function
    wavelength:     wavelength at max intensity
    delta:          delta of wavelength
    max_intensity:  max intensity value
    """

    def __init__(self, transform_type, wavelength, width, max_intensity):
        super().__init__()
        
        self._transform_type = transform_type
        self._wavelength = wavelength
        self._width = width
        self._max_intensity = max_intensity

        if self._transform_type == 'gauss':
            self.transform = GaussFunction(max_intensity, width)
        elif self._transform_type == 'step':
            self.transform = StepFunction(max_intensity, width)
        else:
            raise RuntimeError('Transform type can be only "gauss" or "step"')

    def apply_transform(self):
        return self.transform