import sys
from PySide6.QtWidgets import QApplication
from widget import Widget

app=QApplication(sys.argv)

Window=Widget()
Window.show()

app.exec()
#----------------------------------------------------------------------------------------------