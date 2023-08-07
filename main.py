import sys

from PySide6.QtWidgets import QApplication

from MainWindow import MainWindow


def main():
    app = QApplication(sys.argv)
    wnd = MainWindow()
    wnd.show()
    app.exec()


if __name__ == '__main__':
    main()
