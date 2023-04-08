from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_help(object):
    def setupUi(self, help):
        help.setObjectName("help")
        help.resize(867, 553)
        self.centralwidget = QtWidgets.QWidget(help)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 901, 571))
        self.label.setStyleSheet("background-color: rgb(0, 0, 68);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(260, 530, 391, 16))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(300, 80, 271, 311))
        self.frame_2.setStyleSheet("background-color: rgb(255, 253, 221);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(70, 50, 181, 251))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(70, 0, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 80, 271, 311))
        self.frame.setStyleSheet("background-color: rgb(255, 253, 221);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(50, 60, 181, 201))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(50, 0, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 831, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(580, 80, 271, 311))
        self.frame_3.setStyleSheet("background-color: rgb(255, 253, 221);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_8 = QtWidgets.QLabel(self.frame_3)
        self.label_8.setGeometry(QtCore.QRect(80, 70, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame_3)
        self.label_9.setGeometry(QtCore.QRect(50, 0, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(20, 410, 831, 101))
        self.frame_4.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_10 = QtWidgets.QLabel(self.frame_4)
        self.label_10.setGeometry(QtCore.QRect(0, 0, 831, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.frame_4)
        self.label_11.setGeometry(QtCore.QRect(0, 40, 831, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        help.setCentralWidget(self.centralwidget)

        self.retranslateUi(help)
        QtCore.QMetaObject.connectSlotsByName(help)

    def retranslateUi(self, help):
        _translate = QtCore.QCoreApplication.translate
        help.setWindowTitle(_translate("help", "Help"))
        self.label_2.setText(_translate("help", "Copyright© 2021, Sihab Sahariar"))
        self.label_5.setText(_translate("help", "R->Arm1Up\n"
"F->Arm1Down\n"
"T->Arm2Up\n"
"G->Arm2Down\n"
"Y->Arm3Up\n"
"H->Arm3Down\n"
"U->Arm4Up\n"
"J->Arm4Down\n"
"I->Arm5Up\n"
"K->Arm5Down\n"
"O->Arm6Up\n"
"L->Arm6Down"))
        self.label_6.setText(_translate("help", "ARM CONTROL"))
        self.label_4.setText(_translate("help", "W-> forward\n"
"Q-> forward_left\n"
"E-> forward_right\n"
"S-> backward\n"
"Z-> backward_left\n"
"C-> backward_right\n"
"A-> left\n"
"D-> right"))
        self.label_3.setText(_translate("help", "ROVER CONTROL"))
        self.label_7.setText(_translate("help", "HELP"))
        self.label_8.setText(_translate("help", "V-> Ant/Box\n"
"B-> Bot/Arm"))
        self.label_9.setText(_translate("help", "CAMERA CONTROL"))
        self.label_10.setText(_translate("help", "ABOUT"))
        self.label_11.setText(_translate("help", "Developed By : Sihab Sahariar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    help = QtWidgets.QMainWindow()
    ui = Ui_help()
    ui.setupUi(help)
    help.show()
    sys.exit(app.exec_())
