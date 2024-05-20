# nodeGraph
Node Graph Framework

This a port of the [NodeGraphQt](https://github.com/jchanvfx/NodeGraphQt) framework to run using [PySide6](https://doc.qt.io/qtforpython/).

#### What's Changed In This Fork?
- May 18, 2024 (Travis L. Seymour, PhD)
  - Forked from fivedbrothers/nodegraph 
  - Fixed various incompatibilities with PySide6 v6.7
  - Verified working with Python 3.11
- May 19, 2024 (Travis L. Seymour, PhD)
  - Added `add_image_label` to `nodes.base_node.BaseNode` which gives the ability create custom nodes that feature a static image widget (QPixmap) displayed in the center. See `basic_example.py` for example on how to use it.

## References
[NodeGraphQt](https://github.com/jchanvfx/NodeGraphQt) by Johnny Chan

[PyQtNodeEditor](https://gitlab.com/pavel.krupala/pyqt-node-editor) by Pavel Křupala

[Qt for Python](https://doc.qt.io/qtforpython/) by Qt Company

