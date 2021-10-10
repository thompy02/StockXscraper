import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import Qlabel
from PyQt5.QtWidgets import Qwidget

app = QApplication(sys.argv)

window = Qwidget()
window.setWindowTitle('PyQt5 App')
window.SetGeometry(100,100,280,80)
window.move(60,15)
helloMsg = Qlabel('<h1>Hello World!</h1>')