import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt


class UI(QWidget):
    def __init__(self):
        super().__init__()
        self.button = QPushButton("КуРуГ", self)
        self.button.setGeometry(290, 40, 62, 19)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = UI()
        self.setCentralWidget(self.ui)
        self.setFixedSize(600, 500)  # Устанавливаем фиксированный размер окна

        self.ui.button.clicked.connect(self.paint)
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def paintEvent(self, event):
        if self.do_paint:
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing)

            x = random.randint(0, 600)
            y = random.randint(0, 500)
            diameter = random.randint(20, 100)
            color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            pen = QPen(color, 7)  # Используем ширину 7 для окружности

            painter.setPen(pen)
            painter.setBrush(Qt.NoBrush)  # Устанавливаем необходимость только рисования контура

            painter.drawEllipse(x, y, diameter, diameter)

            self.do_paint = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
