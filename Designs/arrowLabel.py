from math import cos, sin, radians

from PySide6.QtCore import QPoint
from PySide6.QtGui import QPainter, QPaintEvent, QColor, QPen, QFont
from PySide6.QtWidgets import QLabel


class ArrowLabel(QLabel):
    def __init__(self, width, height):
        super().__init__()
        self.setMinimumSize(width, height)
        self.setMaximumSize(width, height)
        self.deg = None

    def paintEvent(self, arg__1: QPaintEvent) -> None:
        super(ArrowLabel, self).paintEvent(arg__1)
        w, h = self.width(), self.height()

        qp = QPainter(self)
        qp.setPen(QPen(QColor(0, 0, 0), 2))
        qp.setFont(QFont("Arial", 6))

        r = w // 3
        qp.drawEllipse(QPoint(w // 2, h // 2), r, r)

        qp.drawText(QPoint(w // 2 - 1, h // 2 - r - 5), '0')
        qp.drawText(QPoint(w // 2 + r + 2, h // 2 + 3), '90')
        qp.drawText(QPoint(w // 2 - 8, h // 2 + r + 10), '180')
        qp.drawText(QPoint((w // 2 - r) - 15, (h // 2 + 5)), '270')

        if self.deg is None:
            return

        deg = radians(self.deg - 90)
        self.draw_arrow(qp, deg, w, h, r)
        if self.deg not in (0, 90, 180, 270):
            self.draw_deg(qp, self.deg, w, r)

        qp.setPen(QPen(QColor(255, 0, 0), 2))

        deg = radians(self.deg + 90)
        self.draw_arrow(qp, deg, w, h, r)
        if self.deg not in (0, 90, 180, 270):
            deg = self.deg + 180
            if deg >= 360:
                deg -= 360
            self.draw_deg(qp, deg, w, r)

    @staticmethod
    def draw_arrow(qp, deg, w, h, r):
        line_x, line_y = int((w // 2) + (r * cos(deg))), int((h // 2) + (r * sin(deg)))
        qp.drawLine(w // 2, h // 2, line_x, line_y)
        qp.drawLine(line_x, line_y,
                    int((w // 2) + (r * cos(deg + .1) * .8)),
                    int((h // 2) + (r * sin(deg + .1) * .8)))
        qp.drawLine(line_x, line_y,
                    int((w // 2) + (r * cos(deg - .1) * .8)),
                    int((h // 2) + (r * sin(deg - .1) * .8)))

    @staticmethod
    def draw_deg(qp, deg, w, r):
        length = len(str(deg))
        rad = radians(-deg + 90)
        c = w // 2
        new_x = c + r * cos(rad) * (1 + length * .1)
        new_y = c - r * sin(rad) * (1 + length * .1)
        qp.drawText(new_x, new_y, str(deg))

    def setDeg(self, deg: int):
        self.deg = deg

    def resetDeg(self):
        self.deg = None
