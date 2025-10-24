# from PyQt6.QtWidgets import QGraphicsRectItem, QGraphicsTextItem, QGraphicsScene
# from PyQt6.QtGui import QBrush, QPen
# from PyQt6.QtCore import Qt


# def createNodeShape(text: str) -> QGraphicsRectItem:
#     if not text:
#         text = "empty"
#     rect = QGraphicsRectItem(0, 0, 50, 50)
#     rect.setBrush(QBrush(Qt.GlobalColor.blue))
#     rect.setPen(QPen(Qt.GlobalColor.black, 2))
#     rect.setFlag(QGraphicsRectItem.GraphicsItemFlag.ItemIsMovable)
  
#     label = QGraphicsTextItem(text, rect)
#     label.setDefaultTextColor(Qt.GlobalColor.white)
#     label.setPos(
#         (rect.rect().width() - label.boundingRect().width()) / 2,
#         (rect.rect().height() - label.boundingRect().height()) / 2
#     )
#     return rect


# def renderNode(scene: QGraphicsScene, ns: QGraphicsRectItem,
#     x_offset: int, y_offset: int, spacing: int = -5):
#     # Position the node
#     ns.setPos(x_offset, y_offset)

#     # Store the original position in custom data (for refresh)
#     ns.setData(0, ns.pos())

#     # Add only if not already in the scene
#     if ns.scene() is None:
#         scene.addItem(ns)

#     # Return updated offset
#     return x_offset, y_offset - ns.rect().height() + spacing


# def updateVisualization(scene: QGraphicsScene, values: list):
#     scene.clear()
#     x, y = 0, 0
#     for val in values:
#         node = createNodeShape(str(val))
#         x, y = renderNode(scene, node, x, y)


# def refresh_node(scene: QGraphicsScene):
#     for item in scene.items():
#         if isinstance(item, QGraphicsRectItem):
#             original_pos = item.data(0)
#             if original_pos is not None:
#                 item.setPos(original_pos)