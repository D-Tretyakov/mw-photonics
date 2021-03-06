
class BaseElement:
    def __init__(self):
        self.transform = None
        self._input_node = None
        self._output_node = None
    
    def apply_transform(self):
        if self.input_node is None:
            raise RuntimeError('Not connected')

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
