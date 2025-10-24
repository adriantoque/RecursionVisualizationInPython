import sys
import random
from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout,
    QHBoxLayout, QLabel, QTextEdit, QLineEdit, QGraphicsScene
)
# from Pyapp.visualizationtools.VisualRendering import GraphicsView
from PyQt6.QtCore import Qt
from visualizationtools.VisualRendering import *

from linkedlist import LinkedList
from stack import Stack
from stacklinkedlist import StackLinkedlist

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Recursion + LinkedList + Stack")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("""
                           background-color: #201b4b;
                           color: white;
                           border-radius: 8px;
                        """)
        
        self.stateLayout = QHBoxLayout()
        self.stateButtons = [
            QPushButton("Linked List"),
            QPushButton("Stack"),
            QPushButton("Stack Built On LinkedList"),
            QPushButton("Recursion")
        ]
        self.scene = QGraphicsScene()
       
        self.stack = Stack() 
        self.linkedlist = LinkedList() 
        self.stack_on_linkedlist = StackLinkedlist()
        
       
        self.node_buttons = [
            QPushButton("Append"),
            QPushButton("Prepend"),
            QPushButton("Random nodes")]
        
        self.linkedlist_buttons = [
            QPushButton("Tail Recursive"),
            QPushButton("Iterative Traverse (Use Stack)"),
            QPushButton("Recursive Reverse"),
            QPushButton("Clear Linked List")]
        
        self.log_area = QTextEdit()
        self.log_area.setStyleSheet("""
                                    background-color: #3c30a3;
                                    color: white;
                                    border-radius: 8
                                    """)

       
       
        self.section_container_A = QWidget()
        self.section_container_A.hide()
        self.section_container_A.setStyleSheet("""
                                                QLabel {
                                                   color: white;
                                                }
                                                QLineEdit {
                                                    background-color: #5c4db3;
                                                    color: white;
                                                    border-radius: 8px;
                                                    padding: 4px;
                                                }
                                                QPushButton {
                                                    background-color: #5451f0;
                                                    color: white;
                                                    padding: 8px 16px;
                                                    border-radius: 8px;
                                                }
                                                """)
        self.linkedlist_layout = QVBoxLayout(self.section_container_A)
        
        self.section_container_B = QWidget()
        self.section_container_B.hide()
        self.section_container_B.setStyleSheet("""
                                                QLabel {
                                                   color: white;
                                                }
                                                QLineEdit {
                                                    background-color: #5c4db3;
                                                    color: white;
                                                    border-radius: 8px;
                                                    padding: 4px;
                                                }
                                                QPushButton {
                                                    background-color: #5451f0;
                                                    color: white;
                                                    padding: 8px 16px;
                                                    border-radius: 8px;
                                                }
                                                """)
        self.stackA_buttons = [
            QPushButton("Push(List)"),
            QPushButton("Pop(List)")
        ]
        self.stack_layout = QVBoxLayout(self.section_container_B)
        
        self.section_container_C = QWidget()
        self.section_container_C.hide()
        self.section_container_C.setStyleSheet("""
                                                QLabel {
                                                   color: white;
                                                }
                                                QLineEdit {
                                                    background-color: #5c4db3;
                                                    color: white;
                                                    border-radius: 8px;
                                                    padding: 4px;
                                                }
                                                QPushButton {
                                                    background-color: #5451f0;
                                                    color: white;
                                                    padding: 8px 16px;
                                                    border-radius: 8px;
                                                }
                                                """)
        self.sbl_buttons = [
            QPushButton("Push(List)"),
            QPushButton("Pop(List)")
        ]
        self.stacklinkedlist_layout = QVBoxLayout(self.section_container_C)
        
        self.section_container_D = QWidget()
        self.section_container_D.hide()
        self.section_container_D.setStyleSheet("""
                                                QLabel {
                                                   color: white;
                                                }
                                                QTextEdit {
                                                    background-color: #5c4db3;
                                                    color: white;
                                                    border-radius: 8px;
                                                    padding: 4px;
                                                }
                                                QPushButton {
                                                    background-color: #5451f0;
                                                    color: white;
                                                    padding: 8px 16px;
                                                    border-radius: 8px;
                                                }
                                                """)
        
        self.XD_layout = QVBoxLayout(self.section_container_D)
        #val tempdata
        self.tempdata = []
        self.recurcive_index = 0
        
        self.section_container_E = QWidget()
        self.section_container_E.hide()
        self.section_container_E.setStyleSheet("""
                                                QLabel {
                                                   color: white;
                                                }
                                                QTextEdit {
                                                    background-color: #5c4db3;
                                                    color: white;
                                                    border-radius: 8px;
                                                    padding: 4px;
                                                }
                                                QPushButton {
                                                    background-color: #5451f0;
                                                    color: white;
                                                    padding: 8px 16px;
                                                    border-radius: 8px;
                                                }
                                                """)
        self.VMax_layout = QVBoxLayout(self.section_container_E)
        self.iterstack = []
        self.iterresult = []
        
        self.uSection = QWidget()
        self.uSection.hide()
        self.uSection.setStyleSheet("""
                                        QLabel {
                                            color: white;
                                        }
                                        QTextEdit {
                                            background-color: #5c4db3;
                                            color: white;
                                            border-radius: 8px;
                                            padding: 4px;
                                        }
                                        QPushButton {
                                            background-color: #5451f0;
                                            color: white;
                                            padding: 8px 16px;
                                            border-radius: 8px;
                                        }
                                        """)
        self.uLayout = QVBoxLayout(self.uSection)
        self.recursion_buttons = [
            QPushButton("Tail && Head Recursion"),
            QPushButton("Tree Recursion"),
            QPushButton("Nested Recursion")
        ]
        self.uInputSection = QWidget()
        self.uInputSection.hide()
        self.uInputSection.setStyleSheet("""
                                            QLabel {
                                                color: white;
                                            }
                                            QTextEdit {
                                                background-color: #5c4db3;
                                                color: white;
                                                border-radius: 8px;
                                                padding: 4px;
                                            }
                                            QPushButton {
                                                background-color: #5451f0;
                                                color: white;
                                                padding: 8px 16px;
                                                border-radius: 8px;
                                            }
                                            """)
        self.uILayout = QVBoxLayout(self.uInputSection)
        self.tailButtons = [
            QPushButton("Run Tail Recursion"),
            QPushButton("Run Head Recursion"),
            QPushButton("Clear Visualization")
        ]
        self.uILayout.addWidget(QLabel("Tail Recursion Controls"), alignment=Qt.AlignmentFlag.AlignCenter)
        self.recursionCount = QLineEdit()
        self.recursionCount.setValidator(QIntValidator(0, 100, self))
        self.recursionCount.setStyleSheet("""
                                    background-color: #3c30a3;
                                    color: white;
                                    border-radius: 8
                                    """)
        self.uILayout.addWidget(self.recursionCount)
        for button in self.tailButtons:
            self.uILayout.addWidget(button)
            
        
        self.initUI()

    def initUI(self):
        # scene.setSceneRect(-400, -700, 1600, 1200)

        # Main operation layout
        operation_layout = QHBoxLayout()

        # ---------------- Node Operations ---------------- #
        node_label = QLabel("Node Value:")
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Node Value")

       

        node_button_layout = QHBoxLayout()
        for button in self.node_buttons:
            node_button_layout.addWidget(button)

        self.linkedlist_layout.addWidget(node_label)
        self.linkedlist_layout.addWidget(self.input_field)
        self.linkedlist_layout.addLayout(node_button_layout)

        # Node button actions
        def on_append():
            self.linkedlist.append(self.input_field.text())
            self._update_log_and_visual_for_linkedlist(self.scene)
            self.input_field.clear()

        def on_prepend():
            self.linkedlist.prepend(self.input_field.text())
            self._update_log_and_visual_for_linkedlist(self.scene)
            self.input_field.clear()

        def on_random():
            val = random.randint(1, 100)
            if random.choice([True, False]):
                self.linkedlist.append(val)
            else:
                self.linkedlist.prepend(val)
            self._update_log_and_visual_for_linkedlist(self.scene)

        

        # ---------------- LinkedList Operations ---------------- #
        linkedlist_label = QLabel("LinkedList Operation:")
        
        operation_layout.addWidget(linkedlist_label)
        for button in self.linkedlist_buttons:
            self.linkedlist_layout.addWidget(button)
            
        def on_clear_linked_list():
            self.linkedlist.clear()
            self._update_log_and_visual_for_linkedlist(self.scene)
            self.log_area.append("LinkedList cleared.")

        

        # ---------------- Stack Operations ---------------- #

        # Stack (separate list-based stack)
        stackA_label = QLabel("Stack (Separate):")
        self.stackA_input_field = QLineEdit()
        self.stackA_input_field.setPlaceholderText("Type something here...")

       
        clear_stackA_button = QPushButton("Clear Stack(List)")
        self.stack_layout.addWidget(stackA_label)
        self.stack_layout.addWidget(self.stackA_input_field)
        for button in self.stackA_buttons:
            self.stack_layout.addWidget(button)
            
        self.stack_layout.addWidget(clear_stackA_button)

        def on_push_stack():
            val = self.stackA_input_field.text()
            if val:
                self.stack.push(val)
                self.log_area.append(f"Stack Push: {val} | Current: {self.stack}")
                self._update_log_and_visual_for_stack(self.scene)
                self.stackA_input_field.clear()

        def on_pop_stack():
            if not self.stack.is_empty():
                val = self.stack.pop()
                self.log_area.append(f"Stack Pop: {val} | Current: {self.stack}")
                self._update_log_and_visual_for_stack(self.scene)
            else:
                self.log_area.append("Stack is empty.")

        def on_clear_stack():
            self.stack.clear()
            self.log_area.append("StackA cleared.")
            self._update_log_and_visual_for_stack(self.scene)

        

        # Stack Built in linkedlist (linked list-based stack)
        sbl_label = QLabel("Stack built on LinkedList (Push/Pop Head):")
        self.sbl_input_field = QLineEdit()
        self.sbl_input_field.setPlaceholderText("Type something here...")

        clear_sbl_button = QPushButton("Clear Stack(LL)")
        refresh_visual_button = QPushButton("Refresh Visualization")

        self.stacklinkedlist_layout.addWidget(sbl_label)
        self.stacklinkedlist_layout.addWidget(self.sbl_input_field)
        
        for button in self.sbl_buttons:
            self.stacklinkedlist_layout.addWidget(button)
      
        
        self.stacklinkedlist_layout.addWidget(clear_sbl_button)

      
        def on_push_sbl():
            val = self.sbl_input_field.text()
            if val:
                self.stack_on_linkedlist.push(val)  # push at head
                self._update_log_and_visual_for_stack_linkedlist(self.scene)
                self.log_area.append(f"Stack built in linkedlist Push: {val}")
                self.sbl_input_field.clear()

        def on_pop_sbl():
            if not self.stack_on_linkedlist.is_empty():
                val = self.stack_on_linkedlist.pop()
                self._update_log_and_visual_for_stack_linkedlist(self.scene)
                self.log_area.append(f"Stack built in linkedlist Pop: {val}")
            else:
                self.log_area.append("Stack built in linkedlist is empty.")

        def on_clear_sbl():
            self.stack_on_linkedlist.clear()
            self._update_log_and_visual_for_stack_linkedlist(self.scene)
            self.log_area.append("Stack built in linkedlist cleared.")

        def on_refresh_visualization():
            pass
            #refresh_node(self.scene)

        # Recursion Operations
        
        self.uLayout.addWidget(QLabel("Recursion Visualization Area"))
        for button in self.recursion_buttons:
            self.uLayout.addWidget(button)
        
        
        def show_Input_TailHeadRecursion():
            show_uInputSection()
            # clean the layout
            for i in reversed(range(self.uILayout.count())):
                widget_to_remove = self.uILayout.itemAt(i).widget()
                if widget_to_remove is not None:
                    self.uILayout.removeWidget(widget_to_remove)
                    widget_to_remove.setParent(None)
            
            self.uILayout.addWidget(QLabel("Tail & Head Recursion Controls"))
            self.uILayout.addWidget(self.recursionCount)
            for button in self.tailButtons:
                self.uILayout.addWidget(button) 
        
          # for uInputSection
        def show_uInputSection():
            self.uInputSection.setVisible(not self.uInputSection.isVisible())

                    
        def on_run_tail_recursion():
            accumulator = 0
            count = int(self.recursionCount.text()) - 1
            nodeRender = NodeRenderer(self.scene)
            nodeRender.tailRecursion_renderer(count, accumulator)
        def on_run_head_recursion():
            accumulator = 0
            count = int(self.recursionCount.text())
            nodeRender = NodeRenderer(self.scene)
            nodeRender.headRecursion_renderer(count, accumulator)
        def on_run_tree_recursion():
            depth = int(self.recursionCount.text())
            nodeRender = NodeRenderer(self.scene)
            nodeRender.treeRecursion_renderer(depth, 0, 0, 0, 100)
        def on_run_nested_recursion():
            nodeRenderer = NodeRenderer(self.scene)
            nodeRenderer.nestedRecursion_renderer(1)
        def on_nested_recursion():
            nodeRenderer = NodeRenderer(self.scene)
            nodeRenderer.nestedRecursion_renderer(4)
            
        # CONNECTING CLICK ON BUTTONS
        self.node_buttons[0].clicked.connect(on_append)
        self.node_buttons[1].clicked.connect(on_prepend)
        self.node_buttons[2].clicked.connect(on_random)
        self.linkedlist_buttons[3].clicked.connect(on_clear_linked_list)
        self.stackA_buttons[0].clicked.connect(on_push_stack)
        self.stackA_buttons[1].clicked.connect(on_pop_stack)
        clear_stackA_button.clicked.connect(on_clear_stack)
        self.sbl_buttons[0].clicked.connect(on_push_sbl)
        self.sbl_buttons[1].clicked.connect(on_pop_sbl)
        clear_sbl_button.clicked.connect(on_clear_sbl)
        refresh_visual_button.clicked.connect(on_refresh_visualization)
        
        
        self.recursion_buttons[0].clicked.connect(show_Input_TailHeadRecursion)
        self.tailButtons[0].clicked.connect(on_nested_recursion)
        self.tailButtons[1].clicked.connect(on_run_head_recursion)
        
      
        # ---------------- Visualization & Logs ---------------- #
        view_area_layout = QHBoxLayout()
       

        view = GraphicsView(self.scene)
        view.setStyleSheet("background-color: #3c30a3;")
        view_area_layout.addWidget(view, 2)
        view_area_layout.addWidget(self.uInputSection, 1)

        self.log_area.setReadOnly(True)
        self.log_area.setPlaceholderText("Log messages will appear here...")
        

        self.stateLayout = QHBoxLayout()
       
        # show and hide sections
        def toggle_linkedlist_ui():
            # show linkedlist ui
            show_section(self.section_container_A)
            print("linkedlist")
            
        def toggle_stack_ui():
            # show stack ui
            show_section(self.section_container_B)
            print("stack")    
            
        def toggle_stacklinkedlist_ui():
            # show stack built in linkedlist ui
            show_section(self.section_container_C)
            print("stack linkedlist")
        
        def toggle_Recursion_ui():
            show_section(self.uSection) 
        
        def show_section(section):
            # Hide all
            self.section_container_A.hide()
            self.section_container_B.hide()
            self.section_container_C.hide()

            # Show the one requested
            section.show()
        
        
         

        
        for b in self.stateButtons:
            b.setStyleSheet("""
                            QPushButton {
                                background-color: #5451f0;
                                color: white;
                                padding: 8px 16px;
                                border-radius: 8px;
                            }
                            """)
            self.stateLayout.addWidget(b)
        
        
       
            
        self.stateButtons[0].clicked.connect(toggle_linkedlist_ui)
        self.stateButtons[1].clicked.connect(toggle_stack_ui)
        self.stateButtons[2].clicked.connect(toggle_stacklinkedlist_ui)
        self.stateButtons[3].clicked.connect(toggle_Recursion_ui)
        
       
        
    
        
        main_layout = QVBoxLayout()
        main_layout.addLayout(self.stateLayout)
        main_layout.addWidget(QLabel("Main Content Area"))
        main_layout.addLayout(view_area_layout, 3)  
        
        io_layout = QHBoxLayout()
        io_layout.addWidget(self.log_area, 3)
        io_layout.addWidget(self.section_container_A, 1)
        io_layout.addWidget(self.section_container_B, 1)
        io_layout.addWidget(self.section_container_C, 1)
        io_layout.addWidget(self.uSection, 1)
        main_layout.addLayout(io_layout)
         
        self.setLayout(main_layout)
        
        
#======================= function ==================
    #Helper to update log and visualization after list changes.
    def _update_log_and_visual_for_linkedlist(self, scene):
       
        self.log_area.append(f"LinkedList: [{self.linkedlist.getList()}]")
        node_data = self.linkedlist.getval()
        nodeRender = NodeRenderer(scene)
        nodeRender.setData(node_data)
        nodeRender.linked_render()
        
    def _update_log_and_visual_for_stack(self, scene):
        self.log_area.append(f"Stack: [ {self.stack} ]")
        node_data = self.stack.getVal()
        nodeRender = NodeRenderer(scene)
        nodeRender.setData(node_data)
        nodeRender.stack_render()
    
    def _update_log_and_visual_for_stack_linkedlist(self, scene):
        self.log_area.append(f"Stack built on LinkedList: [ {self.stack_on_linkedlist} ]")
        node_data = self.stack_on_linkedlist.getVal()# change
        nodeRender = NodeRenderer(scene)
        nodeRender.setData(node_data)
        nodeRender.stack_Linkedlist_render()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())