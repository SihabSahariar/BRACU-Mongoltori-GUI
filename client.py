from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QShortcut, QLabel, QHBoxLayout
from PyQt5.Qt import Qt
from help import Ui_help
import socket


header=64
port=5050 #Common port
format="utf-8"
dc="!disconnect"
server=socket.gethostbyname(socket.gethostname()) #SET_IP
ADDR=(server,port)
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message=msg.encode()
    msg_length=len(msg)
    send_length=str(msg_length).encode(format)
    send_length+=b' '*(header-len(send_length))
    client.send(send_length)
    client.send(message)


class Ui_MainWindow(object):


    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_help()
        self.ui.setupUi(self.window)
        # MainWindow.hide()
        self.window.show()

    def disconnect(self):
        # function to disconnect
        print("Disconnecting")
        self.textEdit.setText("Disconnecting!!")
        send('9')

    def setupUi(self, MainWindow):
        # GUI Code
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1447, 810)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1451, 811))
        self.label.setStyleSheet("background-image: url(:/newPrefix/main.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(110, 240, 321, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalSlider = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider.setGeometry(QtCore.QRect(50, 479, 22, 121))
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.verticalSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_2.setGeometry(QtCore.QRect(120, 480, 22, 121))
        self.verticalSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_2.setObjectName("verticalSlider_2")
        self.verticalSlider_3 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_3.setGeometry(QtCore.QRect(200, 480, 22, 121))
        self.verticalSlider_3.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_3.setObjectName("verticalSlider_3")
        self.verticalSlider_4 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_4.setGeometry(QtCore.QRect(270, 480, 22, 121))
        self.verticalSlider_4.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_4.setObjectName("verticalSlider_4")
        self.verticalSlider_5 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_5.setGeometry(QtCore.QRect(340, 480, 22, 121))
        self.verticalSlider_5.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_5.setObjectName("verticalSlider_5")
        self.verticalSlider_6 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_6.setGeometry(QtCore.QRect(420, 480, 22, 121))
        self.verticalSlider_6.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_6.setObjectName("verticalSlider_6")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(510, 480, 131, 28))
        self.pushButton.setObjectName("pushButton")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(830, 480, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton.setObjectName("radioButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(510, 520, 431, 241))
        self.textEdit.setObjectName("textEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(650, 480, 131, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(500, 130, 121, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(650, 130, 121, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(800, 130, 121, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(500, 200, 121, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(650, 200, 121, 41))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(800, 200, 121, 41))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(500, 270, 121, 41))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(650, 270, 121, 41))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(800, 270, 121, 41))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(80, 700, 161, 51))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(260, 700, 161, 51))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(1130, 680, 151, 41))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(840, 40, 93, 28))
        self.pushButton_15.setObjectName("pushButton_15")

        self.pushButton_14.clicked.connect(self.openWindow)
        self.pushButton_14.clicked.connect(self.disconnect)
        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Binding Keys
        # Control Rover
        QShortcut(Qt.Key_W, MainWindow, self.forward)
        QShortcut(Qt.Key_Q, MainWindow, self.forward_left)
        QShortcut(Qt.Key_E, MainWindow, self.forward_right)
        QShortcut(Qt.Key_S, MainWindow, self.backward)
        QShortcut(Qt.Key_Z, MainWindow, self.backward_left)
        QShortcut(Qt.Key_C, MainWindow, self.backward_right)
        QShortcut(Qt.Key_A, MainWindow, self.left)
        QShortcut(Qt.Key_D, MainWindow, self.right)
        QShortcut(Qt.Key_X, MainWindow, self.stop)

        # Control Arms
        QShortcut(Qt.Key_R, MainWindow, self.Arm1Front)
        QShortcut(Qt.Key_F, MainWindow, self.Arm1Back)
        QShortcut(Qt.Key_T, MainWindow, self.Arm2Front)
        QShortcut(Qt.Key_G, MainWindow, self.Arm2Back)
        QShortcut(Qt.Key_Y, MainWindow, self.Arm3Front)
        QShortcut(Qt.Key_H, MainWindow, self.Arm3Back)
        QShortcut(Qt.Key_U, MainWindow, self.Arm4Front)
        QShortcut(Qt.Key_J, MainWindow, self.Arm4Back)
        QShortcut(Qt.Key_I, MainWindow, self.Arm5Front)
        QShortcut(Qt.Key_K, MainWindow, self.Arm5Back)
        QShortcut(Qt.Key_O, MainWindow, self.Arm6Front)
        QShortcut(Qt.Key_L, MainWindow, self.Arm6Back)

        # Cam Control
        QShortcut(Qt.Key_V, MainWindow, self.Cam1) 
        QShortcut(Qt.Key_B, MainWindow, self.Cam2)
        QShortcut(Qt.Key_9, MainWindow, self.disconnect)

    # Camera Control
    def Cam1(event):
        event.textEdit.setText("Ant/Box")
        print("From Base -> Ant/Box")
        send('v')

    def Cam2(event):
        event.textEdit.setText("Bot/Arm")
        print("From Base -> Bot/Arm")
        send('b')

    # Rover Control
    def forward(event):
        print("From Base -> Forward")
        event.textEdit.setText("Moving Forward")
        send('w')

    def forward_left(event):
        event.textEdit.setText("Moving Forward Left")
        print("From Base -> Forward Left")
        send('q')

    def forward_right(event):
        event.textEdit.setText("Moving Forward Right")
        print("From Base -> Forward Right")
        send('e')

    def left(event):
        event.textEdit.setText("Moving Left")
        print("From Base -> Left")
        send('a')

    def right(event):
        event.textEdit.setText("Moving Right")
        print("From Base -> Moving Right")
        send('d')

    def backward(event):
        event.textEdit.setText("Backward")
        print("From Base -> Moving Backward")
        send('s')

    def backward_right(event):
        print("From Base -> Moving Backward Right")
        event.textEdit.setText("Moving Backward Right")
        send('c')

    def backward_left(event):
        event.textEdit.setText("Backward Left")
        print("From Base -> Moving Backward Left")
        send('z')

    def Arm1Front(self):
        if self.verticalSlider.value() <= 97:
            self.verticalSlider.setValue(self.verticalSlider.value() + 2)
            self.textEdit.setText("Arm1 up")
            print("From Base -> Arm1 Up")
            send('r')

        else:
            print("From Base -> Can't go Up more")

    def Arm1Back(self):
        if self.verticalSlider.value() != 0:
            self.verticalSlider.setValue(self.verticalSlider.value() - 2)
            self.textEdit.setText("Arm1 down")
            print("From Base -> Arm1 Down")
            send('f')
        else:
            print("From Base -> Can't go down more")

    def Arm2Front(self):
        if self.verticalSlider_2.value() <= 97:
            self.verticalSlider_2.setValue(self.verticalSlider_2.value() + 2)
            print("From Base -> Arm2 Up")
            self.textEdit.setText("Arm2 up")
            send('t')
        else:
            print("From Base -> Can't go Up more")

    def Arm2Back(self):
        if self.verticalSlider_2.value() != 0:
            self.verticalSlider_2.setValue(self.verticalSlider_2.value() - 2)
            print("From Base -> Arm2 Down")
            self.textEdit.setText("Arm2 down")
            send('g')
        else:
            print("From Base -> Can't go down more")

    def Arm3Front(self):
        if self.verticalSlider_3.value() <= 97:
            self.verticalSlider_3.setValue(self.verticalSlider_3.value() + 2)
            self.textEdit.setText("Arm3 up")
            print("From Base -> Arm3 Up")
            send('y')
        else:
            print("From Base -> Can't go Up more")

    def Arm3Back(self):
        if self.verticalSlider_3.value() != 0:
            self.verticalSlider_3.setValue(self.verticalSlider_3.value() - 2)
            print("From Base -> Arm3 Down")
            self.textEdit.setText("Arm3 Down")
            send('h')
        else:
            print("From Base -> Can't go down more")

    def Arm4Front(self):
        if self.verticalSlider_4.value() <= 97:
            self.verticalSlider_4.setValue(self.verticalSlider_4.value() + 2)
            print("From Base -> Arm4 Up")
            self.textEdit.setText("Arm4 up")
            send('u')
        else:
            print("From Base -> Can't go Up more")

    def Arm4Back(self):
        if self.verticalSlider_4.value() != 0:
            self.verticalSlider_4.setValue(self.verticalSlider_4.value() - 2)
            print("From Base -> Arm4 Down")
            self.textEdit.setText("Arm4 Down")
            send('j')
        else:
            print("From Base -> Can't go down more")

    def Arm5Front(self):
        if self.verticalSlider_5.value() <= 97:
            self.verticalSlider_5.setValue(self.verticalSlider_5.value() + 2)
            print("From Base -> Arm5 Up")
            self.textEdit.setText("Arm5 up")
            send('i')
        else:
            print("From Base -> Can't go Up more")

    def Arm5Back(self):
        if self.verticalSlider_5.value() != 0:
            self.verticalSlider_5.setValue(self.verticalSlider_5.value() - 2)
            print("From Base -> Arm5 Down")
            self.textEdit.setText("Arm5 down")
            send('k')
        else:
            print("From Base -> Can't go down more")

    def Arm6Front(self):
        if self.verticalSlider_6.value() <= 97:
            self.verticalSlider_6.setValue(self.verticalSlider_6.value() + 2)
            print("From Base -> Arm6 Up")
            self.textEdit.setText("Arm6 up")
            send('o')
        else:
            print("From Base -> Can't go Up more")

    def Arm6Back(self):
        if self.verticalSlider_6.value() != 0:
            self.verticalSlider_6.setValue(self.verticalSlider_6.value() - 2)
            print("From Base -> Arm6 Down")
            self.textEdit.setText("Arm6 Down")
            send('l')
        else:
            print("From Base -> Can't go down more")

    def stop(self):
        self.textEdit.setText("From Base -> Stop")
        send('-')



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BRACU Mongoltori Control Panel - 2021"))
        self.pushButton.setText(_translate("MainWindow", "START"))
        self.radioButton.setText(_translate("MainWindow", "KEYBOARD"))
        self.pushButton_2.setText(_translate("MainWindow", "SAVE"))
        self.pushButton_3.setText(_translate("MainWindow", "Left Forward"))
        self.pushButton_4.setText(_translate("MainWindow", "Forward"))
        self.pushButton_5.setText(_translate("MainWindow", "Right Forward"))
        self.pushButton_6.setText(_translate("MainWindow", "Left"))
        self.pushButton_7.setText(_translate("MainWindow", "Stop"))
        self.pushButton_8.setText(_translate("MainWindow", "Right"))
        self.pushButton_9.setText(_translate("MainWindow", "Left Backward"))
        self.pushButton_10.setText(_translate("MainWindow", "Back"))
        self.pushButton_11.setText(_translate("MainWindow", "Right Backward"))
        self.pushButton_12.setText(_translate("MainWindow", "Ant/Box"))
        self.pushButton_13.setText(_translate("MainWindow", "Bot/Arm"))
        self.pushButton_14.setText(_translate("MainWindow", "HELP"))
        self.pushButton_15.setText(_translate("MainWindow", "DISCONNECT"))


import ui

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


