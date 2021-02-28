import sympy
from .BaseElement import BaseElement


class Laser(BaseElement):
    """
    Class to represent Laser source
    
    arguments:
    transform_type: Gauss or step function
    wavelength:     wavelength at max intensity
    delta:          delta of wavelength
    max_intensity:  max intensity value
    """

    def __init__(self, transform_type, wavelength, delta, max_intensity):
        self._transform_type = transform_type
        self._wavelength = wavelength
        self._delta = delta
        self._max_intensity = max_intensity

        t = sympy.symbols('t')
        if self._transform_type == 'gauss':
            transform = sympy.exp(-t**2)
        elif self._transform_type == 'step':
            transform = sympy.Piecewise(
                (0, t < -1), 
                (1, ((-1 < t) & (t < 1))), 
                (0, t > 1)
            )
        else:
            raise RecursionError('Transform type can be only "gauss" or "step"')

        super().__init__(transform)

    def apply_transform(self):
        return self.transform