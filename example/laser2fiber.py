from photonics.laser import Laser
from photonics.optical_fiber import Fiber

laser = Laser('gauss', 550, 5, 9)

fiber = Fiber()
fiber.input_node = laser

laser.transform.plot(save=True, name='laser_plot.png')
fiber.apply_transform().plot(save=True, name='fiber_plot.png')