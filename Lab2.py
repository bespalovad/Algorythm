import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt

class Window(QWidget):
	def __init__(self):
		super().__init__()
		self.setGeometry(100, 100, 960, 540)
		self.setWindowTitle('Lab2')
		self.show()
		
	def paintEvent(self, event):
		qp = QPainter()
		qp.begin(self)
		self.draw(qp)
		qp.end()

	def draw(self, qp):
		f = open("DS2.txt", "r")
		qp.setPen(Qt.black)
		size = self.size()
		for line in f:
			line = line.replace("\n", "")
			coord_list = line.split(" ")
			qp.drawPoint(int(coord_list[1]), int(coord_list[0]))


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Window()
	sys.exit(app.exec_())
