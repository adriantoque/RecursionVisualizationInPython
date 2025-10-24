# from PyQt6.QtWidgets import QGraphicsRectItem, QGraphicsTextItem, QGraphicsScene, QGraphicsLineItem
# from PyQt6.QtGui import QBrush, QPen, QPainter
# from PyQt6.QtCore import Qt, QPointF
# from visualizationtools.visual_nodes import VisualRectNode

# class NodeRenderer():
#     def __init__(self, scene):
#         self.scene = scene
#         self.dataList = []
#         self.nodes = []
    
#     def createLine(self, direction):
#         if direction == 0:
            
#             prev = None
#             for n in self.nodes:
#                 if prev:
#                     line = QGraphicsLineItem(n.x() + 20, n.y() + (n.boundingRect().height() / 2), prev.x() + 20, prev.y() + (prev.boundingRect().height() / 2))
#                     line.setPen(QPen(Qt.GlobalColor.black, 2))
#                     line.setZValue(-1)
#                     self.scene.addItem(line)
#                 prev = n
#         else:
#             prev = None
#             for n in self.nodes:
#                 if prev:
#                     line = QGraphicsLineItem(n.x() + (n.boundingRect().width()/ 2), n.y() + 20, prev.x() + (prev.boundingRect().width() / 2), prev.y() + 20)
#                     line.setPen(QPen(Qt.GlobalColor.black, 2))
#                     line.setZValue(-1)
#                     self.scene.addItem(line)
#                 prev = n
                  
        
    
#     def setData(self, dl):
#         self.dataList = dl
        
#     def stack_render(self):
#         self.scene.clear()
#         cX = 0
#         cY = 0
#         self.nodes = []
#         for node in self.dataList:
#             self.nodes.append(VisualRectNode(str(node), 50))
            
#         self.nodes.reverse()
#         for n in self.nodes:
#             n.setPos(QPointF(cX, cY))
#             self.scene.addItem(n)
#             cY -= n.boundingRect().height() + 5
                
#     def linked_render(self):
#         self.scene.clear()
#         cX = 0
#         cY = 0
#         self.nodes = []
#         for node in self.dataList:
#             self.nodes.append(VisualNodes(str(node), 50))
        
#         prev_node = None
#         for n in self.nodes:
#             n.setPos(QPointF(cX, cY))
#             self.scene.addItem(n)
#             cX += n.boundingRect().width() + 20
#         self.createLine(0)
    
#     def stack_Linkedlist_render(self):
#         self.scene.clear()
#         cX = 0
#         cY = 0
#         for node in self.dataList:
#             self.nodes.append(VisualRectNode(str(node), 50))
        
#         for n in self.nodes:
#             n.setPos(QPointF(cX, cY))
#             self.scene.addItem(n)
#             cY -= n.boundingRect().height() + 5
            
#         self.createLine(1)
    

    
#     #not node ralated but needed

#     def recursive_traverse_renderer(self):
#         self.scene.clear()
#         rNode = []
#         height = len(self.dataList)
#         container = QGraphicsRectItem(0,-100,50 + (height * 50) , 50 )
#         # container.setBrush(QBrush(Qt.GlobalColor.yellow))
#         # container.setPen(QPen(Qt.GlobalColor.red, 3))
        
#         self.scene.addItem(container)
      