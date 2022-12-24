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
        qp.setFont(QFont("Arial", 10))

        we, he = w // 2.5, h // 2.5
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
            if self.deg not in (0, 90, 180, 270):
                if self.deg < 180 or self.deg > 330:
                    new_x = int((w // 2) + ((we + 15) * cos(deg)))
                    new_y = int((h // 2) + ((he + 15) * sin(deg)))
                else:
                    new_x = int((w // 2) + ((we + 35) * cos(deg)))
                    new_y = int((h // 2) + ((he + 35) * sin(deg)))
                qp.drawText(new_x, new_y, str(self.deg))

            qp.setPen(QPen(QColor(255, 0, 0), 4))
            qp.drawLine(w // 2, h // 2,
                        int((w // 2) + (we * cos(deg2))),
                        int((h // 2) + (he * sin(deg2))))
            d = self.deg + 180 if self.deg < 180 else self.deg - 180
            if d not in (0, 90, 180, 270):
                if d < 180 or d > 330:
                    new_x = int((w // 2) + ((we + 15) * cos(deg2)))
                    new_y = int((h // 2) + ((he + 15) * sin(deg2)))
                else:
                    new_x = int((w // 2) + ((we + 35) * cos(deg2)))
                    new_y = int((h // 2) + ((he + 35) * sin(deg2)))
                qp.drawText(new_x, new_y, str(d))

    def setDeg(self, deg: int):
        self.deg = deg
