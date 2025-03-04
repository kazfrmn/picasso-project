# Basic paint app using PyQt5 and Pillow
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen, QColor
from PyQt5.QtCore import Qt, QPoint

class PaintApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.image = QImage(800, 600, QImage.Format_ARGB32)
        self.image.fill(Qt.white)
        self.label = QLabel()
        self.setCentralWidget(self.label)
        self.last_point = QPoint()

    def mousePressEvent(self, event):
        self.last_point = event.pos()

    def mouseMoveEvent(self, event):
        painter = QPainter(self.image)
        painter.setPen(QPen(Qt.blue, 5))
        painter.drawLine(self.last_point, event.pos())
        self.last_point = event.pos()
        self.update()

    def paintEvent(self, event):
        self.label.setPixmap(QPixmap.fromImage(self.image))

app = QApplication([])
window = PaintApp()
window.show()
app.exec_()