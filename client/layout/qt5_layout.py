# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        self.stackedWidget = QtWidgets.QStackedWidget(MainWindow)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 601, 601))
        self.stackedWidget.setObjectName("stackedWidget")
        self.link = QtWidgets.QWidget()
        self.link.setObjectName("link")
        self.label = QtWidgets.QLabel(self.link)
        self.label.setGeometry(QtCore.QRect(130, 80, 331, 71))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.link)
        self.groupBox.setGeometry(QtCore.QRect(40, 190, 511, 211))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(160, 140, 181, 31))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(80, 70, 341, 24))
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(216, 100, 79, 24))
        self.comboBox.setObjectName("comboBox")
        self.label_2 = QtWidgets.QLabel(self.link)
        self.label_2.setGeometry(QtCore.QRect(100, 20, 391, 61))
        font = QtGui.QFont()
        font.setPointSize(31)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_18 = QtWidgets.QLabel(self.link)
        self.label_18.setGeometry(QtCore.QRect(130, 420, 331, 71))
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setWordWrap(True)
        self.label_18.setObjectName("label_18")
        self.stackedWidget.addWidget(self.link)
        self.home = QtWidgets.QWidget()
        self.home.setObjectName("home")
        self.groupBox_6 = QtWidgets.QGroupBox(self.home)
        self.groupBox_6.setGeometry(QtCore.QRect(0, 0, 211, 601))
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox_6)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 0, 211, 121))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 61, 61))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 90, 81, 16))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(130, 20, 71, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(100, 20, 21, 21))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_6)
        self.groupBox_3.setGeometry(QtCore.QRect(0, 121, 211, 41))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_2.setGeometry(QtCore.QRect(-1, 3, 211, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_6)
        self.groupBox_5.setGeometry(QtCore.QRect(0, 161, 211, 41))
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 0, 211, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_6)
        self.groupBox_4.setGeometry(QtCore.QRect(0, 560, 211, 41))
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_5.setGeometry(QtCore.QRect(0, 0, 211, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.groupBox_8 = QtWidgets.QGroupBox(self.groupBox_6)
        self.groupBox_8.setGeometry(QtCore.QRect(0, 520, 211, 41))
        self.groupBox_8.setTitle("")
        self.groupBox_8.setObjectName("groupBox_8")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_8)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 0, 211, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.home)
        self.stackedWidget_2.setGeometry(QtCore.QRect(210, 0, 391, 601))
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.groupBox_7 = QtWidgets.QGroupBox(self.page)
        self.groupBox_7.setGeometry(QtCore.QRect(20, 150, 351, 121))
        self.groupBox_7.setTitle("")
        self.groupBox_7.setObjectName("groupBox_7")
        self.label_7 = QtWidgets.QLabel(self.groupBox_7)
        self.label_7.setGeometry(QtCore.QRect(120, 15, 221, 31))
        self.label_7.setText("")
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox_7)
        self.label_8.setGeometry(QtCore.QRect(15, 15, 91, 91))
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(self.groupBox_7)
        self.label_10.setGeometry(QtCore.QRect(120, 60, 221, 41))
        self.label_10.setText("")
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName("label_10")
        self.label_9 = QtWidgets.QLabel(self.page)
        self.label_9.setGeometry(QtCore.QRect(110, 120, 171, 21))
        self.label_9.setObjectName("label_9")
        self.label_11 = QtWidgets.QLabel(self.page)
        self.label_11.setGeometry(QtCore.QRect(30, 10, 91, 91))
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_13 = QtWidgets.QLabel(self.page)
        self.label_13.setGeometry(QtCore.QRect(140, 10, 211, 31))
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.page)
        self.label_14.setGeometry(QtCore.QRect(140, 60, 231, 41))
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.pushButton_7 = QtWidgets.QPushButton(self.page)
        self.pushButton_7.setGeometry(QtCore.QRect(80, 550, 111, 41))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.page)
        self.pushButton_8.setGeometry(QtCore.QRect(200, 550, 111, 41))
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_20 = QtWidgets.QLabel(self.page)
        self.label_20.setEnabled(True)
        self.label_20.setGeometry(QtCore.QRect(30, 280, 341, 80))
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setWordWrap(True)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.page)
        self.label_21.setEnabled(True)
        self.label_21.setGeometry(QtCore.QRect(100, 360, 201, 20))
        self.label_21.setText("")
        self.label_21.setTextFormat(QtCore.Qt.RichText)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setOpenExternalLinks(True)
        self.label_21.setObjectName("label_21")
        self.stackedWidget_2.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.scrollArea = QtWidgets.QScrollArea(self.page_2)
        self.scrollArea.setGeometry(QtCore.QRect(-10, 0, 401, 601))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 385, 599))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.stackedWidget_2.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_12 = QtWidgets.QLabel(self.page_3)
        self.label_12.setGeometry(QtCore.QRect(10, 10, 101, 21))
        self.label_12.setObjectName("label_12")
        self.pushButton_6 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_6.setGeometry(QtCore.QRect(140, 550, 111, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_15 = QtWidgets.QLabel(self.page_3)
        self.label_15.setGeometry(QtCore.QRect(10, 50, 101, 21))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.page_3)
        self.label_16.setGeometry(QtCore.QRect(10, 90, 101, 21))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.page_3)
        self.label_17.setGeometry(QtCore.QRect(10, 130, 101, 21))
        self.label_17.setObjectName("label_17")
        self.label_19 = QtWidgets.QLabel(self.page_3)
        self.label_19.setGeometry(QtCore.QRect(10, 170, 101, 21))
        self.label_19.setObjectName("label_19")
        self.stackedWidget_2.addWidget(self.page_3)
        self.stackedWidget.addWidget(self.home)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Nintendo Switch Online Rich Presence"))
        self.label.setText(_translate("MainWindow", " Right click \"Select this account\" and copy the link to proceed with linking the account selected to Nintendo Switch Online Rich Presence."))
        self.pushButton.setText(_translate("MainWindow", "Log In"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Paste the URL here!"))
        self.label_2.setText(_translate("MainWindow", "Link an account"))
        self.label_18.setText(_translate("MainWindow", "\n"
"If you\'d like to use this app for Discord Rich Presence purposes, please link an account that is friended with the target account."))
        self.label_5.setText(_translate("MainWindow", "NSO-RPC"))
        self.pushButton_2.setText(_translate("MainWindow", "Profile"))
        self.pushButton_3.setText(_translate("MainWindow", "Friend List"))
        self.pushButton_5.setText(_translate("MainWindow", "Quit"))
        self.pushButton_4.setText(_translate("MainWindow", "Settings"))
        self.label_9.setText(_translate("MainWindow", "Currently Playing"))
        self.pushButton_7.setText(_translate("MainWindow", "Select Profile"))
        self.pushButton_8.setText(_translate("MainWindow", "Revert"))
        self.label_20.setText(_translate("MainWindow", "Notice: You currently don\'t have an account selected.\n"
"Please note that NSO-RPC requires two different Nintendo accounts."))
        self.label_12.setText(_translate("MainWindow", "Discord:"))
        self.pushButton_6.setText(_translate("MainWindow", "Logout"))
        self.label_15.setText(_translate("MainWindow", "Update Status:"))
        self.label_16.setText(_translate("MainWindow", "Dark Mode:"))
        self.label_17.setText(_translate("MainWindow", "Start Minimized:"))
        self.label_19.setText(_translate("MainWindow", "Start on Launch:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
