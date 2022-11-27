from math import cos, sin, radians, pi, degrees

from PySide6.QtCore import QPoint
from PySide6.QtGui import QPainter, QPaintEvent, QBrush, QColor, QPen, QFont
from PySide6.QtWidgets import QLabel


class ArrowLabel(QLabel):
    def __init__(self):
        super().__init__()
        self.deg = None

    def paintEvent(self, arg__1: QPaintEvent) -> None:
        super(ArrowLabel, self).paintEvent(arg__1)

        self.setMinimumSize(self.height(), self.height())
        self.setMaximumSize(self.height(), self.height())
        w, h = self.width(), self.height()

        qp = QPainter(self)
        qp.setPen(QPen(QColor(0, 0, 0), 4))
        qp.setFont(QFont("Arial", 16))

        we, he = w // 2.4, h // 2.4
        qp.drawEllipse(QPoint(w // 2, h // 2), we, he)

        qp.drawText(QPoint(w // 2 - 10, (h // 2 - he) - 10), '0')  # type: ignore
        qp.drawText(QPoint(w // 2 - 20, (h // 2 + he) + 25), '180')  # type: ignore
        qp.drawText(QPoint((w // 2 - we) - 38, (h // 2 + 10)), '270')  # type: ignore
        qp.drawText(QPoint((w // 2 + we) + 10, (h // 2 + 10)), '90')  # type: ignore

        if self.deg is not None:
            deg = radians(self.deg - 90)
            deg2 = radians(self.deg + 90)
            qp.drawLine(w // 2, h // 2,
                        int((w // 2) + (we * cos(deg))),
                        int((h // 2) + (he * sin(deg))))
            qp.setPen(QPen(QColor(255, 0, 0), 4))
            qp.drawLine(w // 2, h // 2,
                        int((w // 2) + (we * cos(deg2))),
                        int((h // 2) + (he * sin(deg2))))

    def setDeg(self, deg: int):
        self.deg = deg
