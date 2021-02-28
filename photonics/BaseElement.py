from sympy.plotting import plot


class BaseElement:
    """
    Base ("abstract") class for all elements.

    arguments:
    transform: a transform applied to the
               function got from input node and
               passed to output node
    """

    def __init__(self, transform):
        self._transform = transform
        self._input_node = None
        self._output_node = None
        self._plot = None
    
    def apply_transform(self):
        raise NotImplementedError

    @property
    def transform(self):
        return self._transform

    @property
    def input_node(self):
        return self._input_node

    @input_node.setter
    def input_node(self, node):
        if isinstance(node, BaseElement):
            self._input_node = node
        else:
            # TODO change error class
            raise RuntimeError(f'Invalid input node class: {type(node)}')

    @property
    def output_node(self):
        return self._output_node

    @output_node.setter
    def output_node(self, node):
        if isinstance(node, BaseElement):
            self._output_node = node
        else:
            # TODO change error class
            raise RuntimeError(f'Invalid output node class: {type(node)}')

    def plot_transform(self, show=True, save=False, element_name=None):
        self._plot = plot(self._transform, show=False)

        if save:
            name = element_name if element_name else type(self).__name__
            self._plot.save(f'{name}_transform_plot.png')

        if show:
            self._plot.show()