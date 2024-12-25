import sys
from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import (QTableWidgetItem,QMessageBox,QGraphicsScene,QWidget)
from PySide6.QtCore import Slot
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from PySide6.QtGui import QPixmap,QImage
import matplotlib.pyplot as plt
from uiaccess import Ui_Form
#-------------------------------------------------------------------------------------------------------------
class Widget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Expense Tracker")
# --------Dummy data---------------------------------------------------------------------------------------------------
        self.data = [
            ("Insurance",7500),
            ("Food",1000),
            ("Room Rent",15000),
            ("Transportation",1000),
            ("Ramen",1400)
            
        ]
        for description, price in self.data:
            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)
            self.tableWidget.setItem(row_position, 0, QTableWidgetItem(description))
            self.tableWidget.setItem(row_position, 1, QTableWidgetItem(str(price)))

        self.tableWidget.setColumnWidth(0,100)
        self.tableWidget.setColumnWidth(1,180)
 #------------------------------Connecting with Buttons----------------------------------------------------------------       
        # Configure buttons
        self.pushButton.clicked.connect(self.add_data)
        self.pushButton_2.clicked.connect(self.plot_data)
        self.pushButton_4.clicked.connect(self.clear_data)
        self.pushButton_3.clicked.connect(self.close)
      #------------Adding----------------------------------  
    @Slot()
    def add_data(self):
        description = self.desLineEdit.text()
        price = self.priceLineEdit.text()

        if description and price.isdigit():
            # Addding data to table
            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)
            self.tableWidget.setItem(row_position, 0, QTableWidgetItem(description))
            self.tableWidget.setItem(row_position, 1, QTableWidgetItem(price))

            # Addding data to internal storage
            self.data.append((description, int(price)))
            self.desLineEdit.clear()
            self.priceLineEdit.clear()
            print("After clearing:", self.desLineEdit.text(), self.priceLineEdit.text())
  
        else:
            # Display error message for invalid input
            QMessageBox.warning(self, "Invalid Input", "Expense must be a valid number.")
#--------Ploting data ----------------------------------------------------------------
    @Slot()
    def plot_data(self):
        if not self.data:
            QMessageBox.information(self, "No Data", "No data available to plot.")
            return
    # Extracting data
        descriptions, expenses = zip(*self.data)
    # Creating the Matplotlib figure and plot with a smaller size
        figure = Figure(figsize=(3, 3))  # Adjust size (smaller chart)
        ax = figure.add_subplot(111)
        ax.pie(
            expenses,
            labels=descriptions,
            autopct='%1.1f%%',
            startangle=120,
            colors=plt.cm.Paired.colors
        )
        ax.set_title("Expense Distribution")
        canvas = FigureCanvas(figure)
        canvas.draw()
        width, height = canvas.get_width_height()
        image = QPixmap.fromImage(
            QImage(canvas.buffer_rgba(), width, height, QImage.Format_RGBA8888)
        )

        # Display 
        scene = QGraphicsScene()
        scene.addPixmap(image)
        self.graphicsView.setScene(scene)
        # self.graphicsView.setAlignment(Qt.AlignCenter)
        scene.setSceneRect(-50, -20, scene.width(), scene.height())

    @Slot()
    def clear_data(self):
        self.tableWidget.setRowCount(0)
        self.data.clear()
        self.graphicsView.scene().clear()

#---closing----------------
    @Slot()
    def close(self):
        sys.exit()