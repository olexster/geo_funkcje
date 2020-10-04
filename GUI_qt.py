from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def window():
	app = QApplication(sys.argv) #to obowiązkowa linia, którą trzeba dodać, coś w rodzaju inicjalizatora
	win = QMainWindow() #funkcja faktycznie utworzy okno, w którym będziemy wyświetlać nasze różne widżety, jednak nie będzie go (jeszcze) wyświetlać.
	win.setGeometry(400,400,300,300) #setGeometry( X-coordinate, Y-coordinate, width, height)
	win.setWindowTitle("CodersLegacy")

	win.show()
	sys.exit(app.exec_())

window()