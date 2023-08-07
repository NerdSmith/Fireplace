from PySide6.QtCore import QTimer, QPoint
from PySide6.QtGui import QPaintEvent, QPainter, QColor, QBrush
from PySide6.QtWidgets import QGraphicsView, QWidget


class PaintFrame(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupTimer()

    def setupTimer(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(1000)

    def paintEvent(self, event: QPaintEvent) -> None:
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.fillRect(event.rect(), QBrush(QColor(64, 32, 64)))
        painter.end()


    # def repaintFrame(self):
    #     self.update()
