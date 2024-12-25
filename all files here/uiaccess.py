from PySide6.QtCore import (QCoreApplication,QMetaObject, QRect,QSize)
from PySide6.QtWidgets import (QLabel, QLineEdit,QPushButton, QTableWidget, QTableWidgetItem)
from PySide6.QtCharts import QChartView
from PySide6.QtGui import QFont

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(600, 430)
        Form.setMinimumSize(QSize(600, 430))
        Form.setMaximumSize(QSize(600, 430))
        Form.setStyleSheet(u"background-color: rgb(0, 233, 233);")
        self.description = QLabel(Form)
        self.description.setObjectName(u"description")
        self.description.setGeometry(QRect(310, 0, 121, 31))
        self.description.setStyleSheet(u"color: rgb(0, 0, 0);\n",)
        font = QFont()
        font.setFamilies([u"Bookman Old Style"])
        font.setPointSize(14)
        self.description.setFont(font)
        self.desLineEdit = QLineEdit(Form)
        self.desLineEdit.setObjectName(u"desLineEdit")
        self.desLineEdit.setGeometry(QRect(310, 30, 281, 21))
        font1 = QFont()
        font1.setPointSize(12)
        self.desLineEdit.setFont(font1)
        self.desLineEdit.setStyleSheet(u"*{\n"
"	background-color: rgb(255,255,255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius:9px;\n"
"border:0.5px solid black;\n"
"}")
        self.priceLineEdit = QLineEdit(Form)
        self.priceLineEdit.setObjectName(u"priceLineEdit")
        self.priceLineEdit.setGeometry(QRect(310, 73, 281, 21))
        self.priceLineEdit.setFont(font1)
        self.priceLineEdit.setStyleSheet(u"*{\n"
"	background-color: rgb(255,255,255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius:9px;\n"
"border:0.5px solid black;\n"
"}")
        self.price = QLabel(Form)
        self.price.setObjectName(u"price")
        self.price.setGeometry(QRect(312, 48, 121, 31))
        self.price.setFont(font)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(310, 100, 131, 31))
        self.pushButton.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"\n"
"background-color: rgb(170, 85, 255);\n"
"font: 12pt \"Snap ITC\";\n"
"\n"
"border-radius:8px;\n"
"border:0.5px solid black;")
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(460, 100, 131, 31))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(255, 255, 127);\n"
"color: rgb(0, 0, 0);\n"
"\n"
"font: 12pt \"Snap ITC\";\n"
"\n"
"border-radius:8px;\n"
"border:0.5px solid black;")
        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(460, 390, 131, 31))
        self.pushButton_3.setStyleSheet(u"background-color: rgb(255, 85, 0);\n"
"color: rgb(0, 0, 0);\n"
"\n"
"font: 12pt \"Snap ITC\";\n"
"\n"
"border-radius:8px;\n"
"border:0.5px solid black;")
        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(310, 390, 131, 31))
        self.pushButton_4.setStyleSheet(u"background-color: rgb(85, 255, 127);\n"
"color: rgb(0, 0, 0);\n"
"font: 12pt \"Snap ITC\";\n"
"\n"
"border-radius:8px;\n"
"border:0.5px solid black;")
        self.graphicsView = QChartView(Form)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(310, 136, 281, 251))
        self.graphicsView.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.tableWidget = QTableWidget(Form)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        font2 = QFont()
        font2.setFamilies([u"Bahnschrift SemiBold"])
        font2.setPointSize(12)
        font2.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font2);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font2);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 10, 291, 381))
        self.tableWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"Bahnschrift SemiLight\";\n"
"color: rgb(0, 0, 0);")
        self.description.raise_()
        self.price.raise_()
        self.desLineEdit.raise_()
        self.priceLineEdit.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.graphicsView.raise_()
        self.tableWidget.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.description.setText(QCoreApplication.translate("Form", u"Description", None))
        self.price.setText(QCoreApplication.translate("Form", u"Expenses", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Add", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Plot", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"Quit", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"Clear", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Description", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Expenses", None));
    # retranslateUi

