# mw-photonics
Наброски кода для симуляции схем радиофотоники.

Каждый элемент схемы описывается 2мя классами:
1. Наследуется от `BaseElement`. 
Представляет собой сам элемент, в нем описываются входные/выходные узлы и какие преобразования со входным сигналом происходят внутри этого элемента (см. 2).
2. Наследуется от `Transform`.
Представляет собой преобразования сигнала внутри элемента.

См. `laser.py`, `fiber.py` для примера.

В `example` лежит пример скрипта, в котором соединяются лазер и волновод и картинки сигнала в разные этапы прохождения схемы.
```
from photonics.laser import Laser
from photonics.optical_fiber import Fiber

laser = Laser('gauss', 550, 5, 9) # Создаем объект лазера

fiber = Fiber() # Создаем объект волновода
fiber.input_node = laser # На вход волновода идет сигнал от лазера

# Сохраняем график сигнала на выходе из лазера в .png файл
laser.transform.plot(save=True, name='laser_plot.png') 
```
![laser_plot.png](https://github.com/D-Tretyakov/mw-photonics/blob/main/example/laser_plot.png?raw=true)
```
# Сохраняем график сигнала на выходе из волновода
fiber.apply_transform().plot(save=True, name='fiber_plot.png')
```
![fiber_plot.png](https://github.com/D-Tretyakov/mw-photonics/blob/main/example/fiber_plot.png?raw=true)
