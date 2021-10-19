import sys

from PyQt5.QtWidgets import QApplication, QHBoxLayout, QMainWindow
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QTableWidget

__version__ = '0.1'
__author__ = "Trace Thompson"

#create a subclass of the main window to setup the GUI
class StockXscraperUI(QMainWindow):
    """StockXscraperUI View (GUI)"""
    def __init__(self):
        """View Initializer"""
        super().__init__()
        #set basic window properties
        self.setWindowTitle('StockXscraper')
        self.setFixedSize(500,500)
        #set the central widget
        self.__centralWidget = QWidget(self)
        self.setCentralWidget(self.__centralWidget)

#client code
def main():
    """Mian function"""
    #create an instance of QAPP
    StockXscraper = QApplication(sys.argv)
    #show the gui
    view = StockXscraperUI()
    view.show()
    #execute main loop
    sys.exit(StockXscraperUI.exec_())

if __name__ == '__main__':
    main()