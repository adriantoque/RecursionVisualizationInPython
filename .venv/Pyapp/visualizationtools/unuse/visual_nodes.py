# from PyQt6.QtWidgets import QGraphicsObject, QGraphicsTextItem, QGraphicsLineItem
# from PyQt6.QtCore import QRectF, QPropertyAnimation, QEasingCurve, Qt, QPointF
# from PyQt6.QtGui import QBrush, QPen, QPainter

# class VisualRectNode(QGraphicsObject):
#     def __init__(self,text, size):
#         super().__init__()
#         self.size = size
#         self.setTransformOriginPoint(size/2, size/2)
        
#         self.setFlag(QGraphicsObject.GraphicsItemFlag.ItemIsSelectable, True)

#         #label
#         label = QGraphicsTextItem(text)
#         label.setDefaultTextColor(Qt.GlobalColor.black)
#         label.setParentItem(self)  # attach to rect
#         label.setPos(
#             (size - label.boundingRect().width()) / 2,
#             (size - label.boundingRect().height()) / 2
#         )
#         self.label = label
        
        
#         # Animate position
#         self.anim = QPropertyAnimation(self, b"scale")
#         self.anim.setDuration(5000)
#         self.anim.setStartValue(1.0)
#         self.anim.setKeyValueAt(0.7, 0.8)  # squeeze smaller
        
#         self.anim.setEndValue(1.0)
#         self.anim.setLoopCount(-1)
#         self.anim.start()

#     def boundingRect(self):
#         return QRectF(0, 0, self.size, self.size)

#     def paint(self, painter: QPainter, option, widget=None):
#         painter.setBrush(QBrush(Qt.GlobalColor.cyan))
#         painter.setPen(QPen(Qt.GlobalColor.black, 2))
#         painter.drawRect(self.boundingRect())
    
#     def move_to(self, pos: QPointF, duration=500):
#         anim = QPropertyAnimation(self, b"pos")
#         anim.setDuration(duration)
#         anim.setEndValue(pos)
#         anim.setEasingCurve(QEasingCurve.Type.OutCubic)
#         anim.start()
#         # Keep reference so it doesn't get garbage-collected
#         self.anim = anim
