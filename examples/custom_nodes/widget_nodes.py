from pathlib import Path

from nodegraph import BaseNode


class DropdownMenuNode(BaseNode):
    """
    An example node with a embedded added QCombobox menu.
    """

    # unique node identifier.
    __identifier__ = 'nodes.widget'

    # initial default node name.
    NODE_NAME = 'menu'

    def __init__(self):
        super(DropdownMenuNode, self).__init__()

        # create input & output ports
        self.add_input('in 1')
        self.add_output('out 1')
        self.add_output('out 2')

        # create the QComboBox menu.
        items = ['item 1', 'item 2', 'item 3']
        self.add_combo_menu(
            'my_menu',
            'Menu Test',
            items=items,
            # tooltip='example custom tooltip'
        )


class ImageNode(BaseNode):
    """
    A node class with 1 inputs and 4 outputs.
    Also has an image presented in a QLabel/QPixmap
    """

    # unique node identifier.
    __identifier__ = "nodes.widget"

    # initial default node name.
    NODE_NAME = "image"

    def __init__(self):
        super(ImageNode, self).__init__()

        # create node inputs.
        self.add_input("input")

        # create node outputs.
        self.add_output("North")
        self.add_output("South")
        self.add_output("East")
        self.add_output("West")

        # create the QLabel/QPixmap widget
        img = Path(Path(__file__).parent.parent, 'star.png')
        self.add_image_label(
            'my_image',
            'star.png',
            file_path=str(img)
        )


class TextInputNode(BaseNode):
    """
    An example of a node with a embedded QLineEdit.
    """

    # unique node identifier.
    __identifier__ = 'nodes.widget'

    # initial default node name.
    NODE_NAME = 'text'

    def __init__(self):
        super(TextInputNode, self).__init__()

        # create input & output ports
        self.add_input('in')
        self.add_output('out')

        # create QLineEdit text input widget.
        self.add_text_input('my_input', 'Text Input', tab='widgets')


class CheckboxNode(BaseNode):
    """
    An example of a node with 2 embedded QCheckBox widgets.
    """

    # set a unique node identifier.
    __identifier__ = 'nodes.widget'

    # set the initial default node name.
    NODE_NAME = 'checkbox'

    def __init__(self):
        super(CheckboxNode, self).__init__()

        # create the checkboxes.
        self.add_checkbox('cb_1', '', 'Checkbox 1', True)
        self.add_checkbox('cb_2', '', 'Checkbox 2', False)

        # create input and output port.
        self.add_input('in', color=(200, 100, 0))
        self.add_output('out', color=(0, 100, 200))
