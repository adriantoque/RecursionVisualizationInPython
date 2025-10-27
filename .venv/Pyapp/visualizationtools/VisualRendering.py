from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import math

class GraphicsView(QGraphicsView):
    def __init__(self, scene):
        super().__init__(scene)
        self.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.setDragMode(QGraphicsView.DragMode.ScrollHandDrag)  # pan with mouse drag
        self.setTransformationAnchor(QGraphicsView.ViewportAnchor.AnchorUnderMouse)
    def wheelEvent(self, event):
        # Zoom with mouse wheel
        zoom_in_factor = 1.25
        zoom_out_factor = 1 / zoom_in_factor
        if event.angleDelta().y() > 0:
            self.scale(zoom_in_factor, zoom_in_factor)
        else:
            self.scale(zoom_out_factor, zoom_out_factor)
            
def add_up_arrow(scene, start: QPointF, end: QPointF):
    # Draw the line (stop slightly before the tip so the arrowhead sits cleanly)
    line = QGraphicsLineItem(start.x(), start.y(), end.x(), end.y() )
    line.setPen(QPen(Qt.GlobalColor.black, 2))
    scene.addItem(line)

    arrow_size = 10

    # Arrowhead points (pointing UP)
    p1 = end + QPointF(-arrow_size / 2, arrow_size)   # bottom-left of tip
    p2 = end + QPointF( arrow_size / 2, arrow_size)   # bottom-right of tip

    arrow_head = QPolygonF([end, p1, p2])
    arrow_item = QGraphicsPolygonItem(arrow_head)
    arrow_item.setBrush(QBrush(Qt.GlobalColor.black))
    scene.addItem(arrow_item)

    return line, arrow_item
       
def add_down_arrow(scene, start: QPointF, end: QPointF):
    # Draw the line
    line = QGraphicsLineItem(start.x(), start.y(), end.x(), end.y()-11)
    line.setPen(QPen(Qt.GlobalColor.black, 2))
    scene.addItem(line)

    # calculate arrowhead points
    angle = math.atan2(-(end.y() - start.y()), end.x() - start.x())
    arrow_size = 10
    #  arrow (pointing down)
    p1 = end + QPointF(-arrow_size / 2, -arrow_size)   
    p2 = end + QPointF( arrow_size / 2, -arrow_size) 

    arrow_head = QPolygonF([end, p1, p2])
    arrow_item = QGraphicsPolygonItem(arrow_head)
    arrow_item.setBrush(QBrush(Qt.GlobalColor.black))
    scene.addItem(arrow_item)
    return line, arrow_item

def add_horizontal_arrow(scene, start: QPointF, end: QPointF):
    # Draw the line (straight left-to-right)
    line = QGraphicsLineItem(start.x(), start.y(), end.x() - 11, end.y())
    line.setPen(QPen(Qt.GlobalColor.black, 2))
    scene.addItem(line)

    # Arrowhead size
    arrow_size = 10

    # Arrowhead points (triangle pointing right)
    p1 = end + QPointF(-arrow_size, -arrow_size / 2)  # upper left
    p2 = end + QPointF(-arrow_size,  arrow_size / 2)  # lower left

    arrow_head = QPolygonF([end, p1, p2])
    arrow_item = QGraphicsPolygonItem(arrow_head)
    arrow_item.setBrush(QBrush(Qt.GlobalColor.black))
    scene.addItem(arrow_item)
     
class BaseVisualNode(QGraphicsObject):
    def __init__(self, text, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.color = QColor("cyan")
        self.setAcceptHoverEvents(True)
        self.setTransformOriginPoint(width/2, height/2)
        self.setFlag(QGraphicsObject.GraphicsItemFlag.ItemIsSelectable, True)

        # --- main label ---
        label = QGraphicsTextItem(text)
        label.setDefaultTextColor(Qt.GlobalColor.black)
        label.setParentItem(self)
        label.setPos(
            (self.width - label.boundingRect().width()) / 2,
            (self.height - label.boundingRect().height()) / 2
        )
        self.label = label

        # marker
        self.side_label = QGraphicsTextItem("")
        self.side_label.setDefaultTextColor(Qt.GlobalColor.red)
        self.side_label.setParentItem(self)
        self.side_label.setPos(self.width + 10, (self.height - 15) / 2)  # right side

        # --- animation (pulse) ---
        self.anim = QPropertyAnimation(self, b"scale")
        self.anim.setDuration(5000)
        self.anim.setStartValue(1.0)
        self.anim.setKeyValueAt(0.7, 0.8)
        self.anim.setEndValue(1.0)
        self.anim.setLoopCount(-1)
        self.anim.start()

        self.next = None
        self.children = []

    def hoverEnterEvent(self, event):
        self.color = QColor("yellow")
        self.update()

    def hoverLeaveEvent(self, event):
        self.color = QColor("cyan")
        self.update()

    
    def set_marker(self, text: str):
       # marker setuff
        self.side_label.setPlainText(text)

    # required methods
    def boundingRect(self):
        return QRectF(0, 0, self.width, self.height)

    def paint(self, painter: QPainter, option, widget=None):
        painter.setBrush(QBrush(self.color))
        painter.setPen(QPen(Qt.GlobalColor.black, 2))
        painter.drawEllipse(self.boundingRect())
            
class VisualRectNode(QGraphicsObject):
    def __init__(self,text, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.setTransformOriginPoint(width/2, height/2)
        self.setFlag(QGraphicsObject.GraphicsItemFlag.ItemIsSelectable, True)
        #label
        label = QGraphicsTextItem(text)
        label.setDefaultTextColor(Qt.GlobalColor.black)
        label.setParentItem(self)  # attach to rect
        label.setPos(
            (self.width - label.boundingRect().width()) / 2,
            (self.height - label.boundingRect().height()) / 2
        )
        self.label = label
        # Animate position
        self.anim = QPropertyAnimation(self, b"scale")
        self.anim.setDuration(5000)
        self.anim.setStartValue(1.0)
        self.anim.setKeyValueAt(0.7, 0.8)  # squeeze smaller
        self.anim.setEndValue(1.0)
        self.anim.setLoopCount(-1)
        self.anim.start()

    def boundingRect(self):
        return QRectF(0, 0, self.width, self.height)

    def paint(self, painter: QPainter, option, widget=None):
        painter.setBrush(QBrush(Qt.GlobalColor.cyan))
        painter.setPen(QPen(Qt.GlobalColor.black, 2))
        painter.drawRect(self.boundingRect())
    
    def move_to(self, pos: QPointF, duration=500):
        anim = QPropertyAnimation(self, b"pos")
        anim.setDuration(duration)
        anim.setEndValue(pos)
        anim.setEasingCurve(QEasingCurve.Type.OutCubic)
        anim.start()
        # Keep reference so it doesn't get garbage-collected
        self.anim = anim
        
class VisualNodes(QGraphicsObject):
    def __init__(self,text, size):
        super().__init__()
        self.size = size
        self.setTransformOriginPoint(size/2, size/2)
        
        self.setFlag(QGraphicsObject.GraphicsItemFlag.ItemIsSelectable, True)

        #label
        label = QGraphicsTextItem(text)
        label.setDefaultTextColor(Qt.GlobalColor.black)
        label.setParentItem(self)  # attach to rect
        label.setPos(
            (size - label.boundingRect().width()) / 2,
            (size - label.boundingRect().height()) / 2
        )
        self.label = label
        
        # Animate position
        self.anim = QPropertyAnimation(self, b"scale")
        self.anim.setDuration(5000)
        self.anim.setStartValue(1.0)
        self.anim.setKeyValueAt(0.7, 0.8)  # squeeze smaller
        
        self.anim.setEndValue(1.0)
        self.anim.setLoopCount(-1)
        self.anim.start()

    def boundingRect(self):
        return QRectF(0, 0, self.size, self.size)

    def paint(self, painter: QPainter, option, widget=None):
        painter.setBrush(QBrush(Qt.GlobalColor.cyan))
        painter.setPen(QPen(Qt.GlobalColor.black, 2))
        painter.drawEllipse(self.boundingRect())
    
    def move_to(self, pos: QPointF, duration=500):
        anim = QPropertyAnimation(self, b"pos")
        anim.setDuration(duration)
        anim.setEndValue(pos)
        anim.setEasingCurve(QEasingCurve.Type.OutCubic)
        anim.start()
        # Keep reference so it doesn't get garbage-collected
        self.anim = anim
            
class NodeRenderer():
    def __init__(self, scene):
        self.scene = scene
        self.dataList = []
        self.nodes = []
    
    def createLine(self, direction):
        if direction == 0:
            
            prev = None
            for n in self.nodes:
                if prev:
                    line = QGraphicsLineItem(n.x() + 20, n.y() + (n.boundingRect().height() / 2), prev.x() + 20, prev.y() + (prev.boundingRect().height() / 2))
                    line.setPen(QPen(Qt.GlobalColor.black, 2))
                    line.setZValue(-1)
                    self.scene.addItem(line)
                prev = n
        else:
            prev = None
            for n in self.nodes:
                if prev:
                    line = QGraphicsLineItem(n.x() + (n.boundingRect().width()/ 2), n.y() + 20, prev.x() + (prev.boundingRect().width() / 2), prev.y() + 20)
                    line.setPen(QPen(Qt.GlobalColor.black, 2))
                    line.setZValue(-1)
                    self.scene.addItem(line)
                prev = n          
        
    def setData(self, dl):
        self.dataList = dl
        
    def stack_render(self):
        self.scene.clear()
        cX = 0
        cY = 0
        self.nodes = []
        for node in self.dataList:
            self.nodes.append(VisualRectNode(str(node), 100, 20))
            
        for n in self.nodes:
            n.setPos(QPointF(cX, cY))
            self.scene.addItem(n)
            cY -= n.boundingRect().height() + 5
    def linked_render(self):
        self.scene.clear()
        cX = 0
        cY = 0
        self.nodes = []

        # Build nodes
        for node in self.dataList:
            self.nodes.append(BaseVisualNode(str(node), 50, 50))

        prev_node = None
        for n in self.nodes:
            # Place node
            n.setPos(QPointF(cX, cY))
            self.scene.addItem(n)

            # If there is a previous node, draw an arrow from it to this one
            if prev_node is not None:
                start = prev_node.pos() + QPointF(prev_node.boundingRect().width(), prev_node.boundingRect().height() / 2)
                end   = n.pos() + QPointF(0, n.boundingRect().height() / 2)
                add_horizontal_arrow(self.scene, start, end)

            # Advance X for next node
            cX += n.boundingRect().width() + 20
            prev_node = n
    
    def stack_Linkedlist_render(self):
        self.scene.clear()
        self.nodes.clear()

        cX = 0
        cY = 0
        spacing = 20  # vertical spacing between nodes

        # Build visual nodes from data
        for value in self.dataList:
            self.nodes.append(VisualRectNode(str(value), 100, 20))

        # Top of stack should be the last rendered (higher up visually)
        self.nodes.reverse()

        prev = None
        for n in self.nodes:
            # Place current node
            n.setPos(QPointF(cX, cY))
            self.scene.addItem(n)

            # If there is a previous node, draw an arrow up from it to this one
            if prev is not None:
                start = prev.pos() + QPointF(prev.boundingRect().width() / 2, 0)  # top center of previous
                end   = n.pos()   + QPointF(n.boundingRect().width() / 2, n.boundingRect().height())  # bottom center of current
                add_up_arrow(self.scene, start, end)

            # Move Y upward for next node
            cY -= n.boundingRect().height() + spacing
            prev = n
    # direct recursion
        
    def tailRecursion_renderer(self, n, accumulator=0):
        # clear the scene once at the start
        if accumulator == 0:
            self.scene.clear()
            self.nodes = []

        node = BaseVisualNode(str(accumulator), 50, 50)
        node.setPos(QPointF(0, + (len(self.nodes) * 70)))
        self.scene.addItem(node)
        if self.nodes:
            prev = self.nodes[-1]
            start = prev.pos() + QPointF(prev.width / 2, prev.height)
            end   = node.pos() + QPointF(node.width /2, 0)
            add_down_arrow(self.scene, start, end)

        self.nodes.append(node)

        if n == 0: 
            if self.nodes:
                self.nodes[0].set_marker("START")
                self.nodes[-1].set_marker("END")

            return self.nodes  # return the list of created nodes

        # last action is the recursive call
        return self.tailRecursion_renderer(n - 1, accumulator + 1)
    
    def headRecursion_renderer(self, n, accumulator=0):
        if n == 0:  
            self.scene.clear()
            self.nodes = []
            return

        # recursive call first
        self.headRecursion_renderer(n - 1, accumulator + 1)

        # work happens after recursion 
        node = BaseVisualNode(str(accumulator), 50, 50)
        node.setPos(QPointF(0, len(self.nodes) * 70))
        self.scene.addItem(node)
        if self.nodes:
            prev = self.nodes[-1]
            start = prev.pos() + QPointF(prev.width / 2, prev.height)
            end   = node.pos() + QPointF(node.width /2, 0)
            add_down_arrow(self.scene, start, end)
        self.nodes.append(node)

        # mark head and tail after all nodes are added
        if accumulator == 0 and self.nodes:
            self.nodes[0].set_marker("START")
            self.nodes[-1].set_marker("END")
        
    def treeRecursion_renderer(self, n, depth=0, x=0, y=0, offset=100):
        
        if n <= 0: return None
        # --- create the node ---
        node = BaseVisualNode(str(depth), 50, 50)
        node.setPos(QPointF(x, y))
        self.scene.addItem(node)

        # --- base case ---
        if n == 1: return node

        # --- recursive calls for children ---
        # left child
        left = self.treeRecursion_renderer(
            n - 1,
            depth + 1,
            x - offset,
            y + 80,
            offset // 2 if offset > 20 else 20
        )
        # right child
        right = self.treeRecursion_renderer(
            n - 1,
            depth + 1,
            x + offset,
            y + 80,
            offset // 2 if offset > 20 else 20
        )
        # --- draw arrows to children ---
        if left:
            add_down_arrow(self.scene, node.pos() + QPointF(node.width / 2, node.height), left.pos() + QPointF(left.width / 2, 0))
        if right:
            add_down_arrow(self.scene, node.pos() + QPointF(node.width / 2, node.height), right.pos() + QPointF(right.width / 2, 0))

        return node
    
    def nestedRecursion_renderer(self, n, x=0, y=0, depth=0):
 
        # --- create a node for this call ---
        node = BaseVisualNode(f"{n}", 50, 50)
        node.setPos(QPointF(x, y))
        self.scene.addItem(node)

        # --- base case ---
        if n <= 0:
            return node

        # --- nested recursion: call inside call ---
        # First compute nested_example(n-1) visually
        inner = self.nestedRecursion_renderer(n - 1, x - 80, y + 80, depth + 1)

        if inner:
            # use your global add_arrow function
            add_down_arrow(self.scene, node.pos() + QPointF(node.width/2, node.height),
                                inner.pos() + QPointF(inner.width/2, 0))

            # simulate "nested_example(inner_value - 1)"
            inner_val = int(inner.label.toPlainText())
            next_val = inner_val - 1
            outer = self.nestedRecursion_renderer(next_val, x + 80, y + 80, depth + 1)

            if outer:
                add_down_arrow(self.scene, node.pos() + QPointF(node.width/2, node.height),
                                    outer.pos() + QPointF(outer.width/2, 0))

        return node

def indirectRecursion_renderer_A(n, renderer, x=0, y=0):
    if n <= 0:
        return None
    # create node for A
    node = BaseVisualNode(f"A:{n}", 50, 50)
    node.setPos(QPointF(x, y))
    renderer.scene.addItem(node)
    # call B
    b_node = indirectRecursion_renderer_B(n - 1, renderer, x - 100, y + 80)
    if b_node:
        add_down_arrow(renderer.scene, node.pos() + QPointF(node.width/2, node.height),
                                b_node.pos() + QPointF(b_node.width/2, 0))
    return node
def indirectRecursion_renderer_B(n, renderer, x=0, y=0):
    if n <= 0:
        return None
    # create node for B
    node = BaseVisualNode(f"B:{n}", 50, 50)
    node.setPos(QPointF(x, y))
    renderer.scene.addItem(node)
    # call A
    a_node = indirectRecursion_renderer_A(n - 1, renderer, x + 100, y + 80)
    if a_node:
        add_down_arrow(renderer.scene, node.pos() + QPointF(node.width/2, node.height),
                                a_node.pos() + QPointF(a_node.width/2, 0))
    return node
def indirectRecursion_renderer(n, renderer):
    renderer.scene.clear()
    indirectRecursion_renderer_A(n, renderer, 0, 0)
    