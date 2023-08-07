from PySide6.QtCore import Qt, QObject, QEvent
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import QWidget, QBoxLayout, QGridLayout, QVBoxLayout

from Definitions import WND_HEIGHT, WND_WIDTH
from PaintFrame import PaintFrame


class MainWindow(QWidget):
    def __init__(self):
        super().__init__(parent=None)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.resize(WND_HEIGHT, WND_WIDTH)

        # events block
        self.installEventFilter(self)
        self.startPos = None
        # events block end

        # widgets block
        paintFrame = PaintFrame(self)

        layout = QVBoxLayout(self)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(paintFrame)

        self.setLayout(layout)
        # widgets block end

        self.installEventFilter(self)
        self.installEventFilter(paintFrame)


    def eventFilter(
        self, watched: QObject, event: QEvent
    ) -> bool:
        e: QMouseEvent = event
        if event.type() == QEvent.MouseButtonDblClick:
            self.startPos = e.globalPos()
            return True
        if event.type() == QEvent.MouseButtonRelease and self.startPos is not None:
            currPos = self.pos()
            diff = e.globalPos() - self.startPos
            self.move(currPos + diff)
            self.startPos = None
            return True
        return super().eventFilter(watched, event)
