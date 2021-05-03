# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mixerNew.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import ImageView
import cv2
import numpy as np
# class Ui_MainWindow(object):
class Ui_MainWindow(QtGui.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        #MainWindow.resize(1131, 923)
        MainWindow.resize(1400, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.img1_combo = QtWidgets.QComboBox(self.centralwidget)
        self.img1_combo.setObjectName("comboBox")
        self.img1_combo.addItem("")
        self.img1_combo.addItem("")
        self.img1_combo.addItem("")
        self.img1_combo.addItem("")
        self.img1_combo.addItem("")
        self.gridLayout_2.addWidget(self.img1_combo, 0, 1, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.img2_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.img2_label.setFont(font)
        self.img2_label.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.img2_label, 0, 0, 1, 1)
        self.img2_combo = QtWidgets.QComboBox(self.centralwidget)
        self.img2_combo.setObjectName("comboBox_2")
        self.img2_combo.addItem("")
        self.img2_combo.addItem("")
        self.img2_combo.addItem("")
        self.img2_combo.addItem("")
        self.img2_combo.addItem("")
        self.gridLayout_3.addWidget(self.img2_combo, 0, 1, 1, 1)
        self.img2 = ImageView(self.centralwidget)
        self.img2.setObjectName("img2")
        self.gridLayout_3.addWidget(self.img2, 1, 0, 1, 1)
        self.img2_component = ImageView(self.centralwidget)
        self.img2_component.setObjectName("img2_component")
        self.gridLayout_3.addWidget(self.img2_component, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 2, 0, 1, 2)
        self.img1 = ImageView(self.centralwidget)
        # self.img1 = QtWidgets.QLabel(self.centralwidget)
        self.img1.setObjectName("img1")
        # self.img1.setScaledContents(True)
        # self.img1.setScaledContents(True)
        self.gridLayout_2.addWidget(self.img1, 1, 0, 1, 1)
        self.img1_component = ImageView(self.centralwidget)
        self.img1_component.setObjectName("img1_component")
        self.gridLayout_2.addWidget(self.img1_component, 1, 1, 1, 1)
        self.img1_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.img1_label.setFont(font)
        self.img1_label.setObjectName("label")
        self.gridLayout_2.addWidget(self.img1_label, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.output_channel = QtWidgets.QComboBox(self.centralwidget)
        self.output_channel.setObjectName("output_channel")
        self.output_channel.addItem("")
        self.output_channel.addItem("")
        self.output_channel.addItem("")
        self.gridLayout_5.addWidget(self.output_channel, 0, 1, 1, 2)
        self.Component1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Component1.setFont(font)
        self.Component1.setTextFormat(QtCore.Qt.AutoText)
        self.Component1.setAlignment(QtCore.Qt.AlignCenter)
        self.Component1.setObjectName("Component1")
        self.gridLayout_5.addWidget(self.Component1, 2, 0, 1, 1)
        self.component1_slider = QtWidgets.QSlider(self.centralwidget)
        self.component1_slider.setMaximum(100)
        self.component1_slider.setSingleStep(10)
        self.component1_slider.setOrientation(QtCore.Qt.Horizontal)
        self.component1_slider.setObjectName("component1_slider")
        self.component1_slider.setValue(100)
        self.gridLayout_5.addWidget(self.component1_slider, 3, 1, 1, 2)
        self.component1_img = QtWidgets.QComboBox(self.centralwidget)
        self.component1_img.setObjectName("component1_img")
        self.component1_img.addItem("")
        self.component1_img.addItem("")
        self.component1_img.addItem("")
        self.gridLayout_5.addWidget(self.component1_img, 2, 1, 1, 1)
        self.component2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.component2.setFont(font)
        self.component2.setTextFormat(QtCore.Qt.AutoText)
        self.component2.setAlignment(QtCore.Qt.AlignCenter)
        self.component2.setObjectName("component2")
        self.gridLayout_5.addWidget(self.component2, 5, 0, 1, 1)
        self.component2_img = QtWidgets.QComboBox(self.centralwidget)
        self.component2_img.setObjectName("component2_img")
        self.component2_img.addItem("")
        self.component2_img.addItem("")
        self.component2_img.addItem("")
        self.gridLayout_5.addWidget(self.component2_img, 5, 1, 1, 1)
        self.mixer_output = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.mixer_output.setFont(font)
        self.mixer_output.setTextFormat(QtCore.Qt.AutoText)
        self.mixer_output.setAlignment(QtCore.Qt.AlignCenter)
        self.mixer_output.setObjectName("mixer_output")
        self.gridLayout_5.addWidget(self.mixer_output, 0, 0, 1, 1)
        self.component1_type = QtWidgets.QComboBox(self.centralwidget)
        self.component1_type.setObjectName("component1_type")
        self.component1_type.addItem("")
        self.component1_type.addItem("")
        self.component1_type.addItem("")
        self.component1_type.addItem("")
        self.component1_type.addItem("")
        self.gridLayout_5.addWidget(self.component1_type, 2, 2, 1, 1)
        self.component2_type = QtWidgets.QComboBox(self.centralwidget)
        self.component2_type.setObjectName("component2_type")
        self.component2_type.addItem("")
        self.component2_type.addItem("")
        self.component2_type.addItem("")
        self.component2_type.addItem("")
        self.component2_type.addItem("")
        self.gridLayout_5.addWidget(self.component2_type, 5, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout_5.addItem(spacerItem, 4, 0, 1, 3)
        self.component2_slider = QtWidgets.QSlider(self.centralwidget)
        self.component2_slider.setMaximum(100)
        self.component2_slider.setSingleStep(10)
        self.component2_slider.setOrientation(QtCore.Qt.Horizontal)
        self.component2_slider.setObjectName("component2_slider")
        self.gridLayout_5.addWidget(self.component2_slider, 6, 1, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout_5.addItem(spacerItem1, 1, 0, 1, 3)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.output2 = ImageView(self.centralwidget)
        self.output2.setObjectName("output2")
        self.gridLayout_4.addWidget(self.output2, 2, 1, 1, 1)
        self.output1 = ImageView(self.centralwidget)
        self.output1.setObjectName("output1")
        self.gridLayout_4.addWidget(self.output1, 2, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.output1_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.output1_label.setFont(font)
        self.output1_label.setTextFormat(QtCore.Qt.AutoText)
        self.output1_label.setAlignment(QtCore.Qt.AlignCenter)
        self.output1_label.setObjectName("output1_label")
        self.horizontalLayout_8.addWidget(self.output1_label)
        self.output2_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.output2_label.setFont(font)
        self.output2_label.setTextFormat(QtCore.Qt.AutoText)
        self.output2_label.setAlignment(QtCore.Qt.AlignCenter)
        self.output2_label.setObjectName("output2_label")
        self.horizontalLayout_8.addWidget(self.output2_label)
        self.gridLayout_4.addLayout(self.horizontalLayout_8, 1, 0, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout_4.addItem(spacerItem2, 0, 0, 1, 2)
        self.gridLayout_5.addLayout(self.gridLayout_4, 7, 0, 1, 3)
        self.verticalLayout_2.addLayout(self.gridLayout_5)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1131, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.actionOpen1 = QtWidgets.QAction(MainWindow)
        self.actionOpen1.setObjectName("actionOpen1")
        self.actionOpen1.setText("Image 1")
        self.menuFile.addAction(self.actionOpen1)

        self.actionOpen2 = QtWidgets.QAction(MainWindow)
        self.actionOpen2.setObjectName("actionOpen2")
        self.actionOpen2.setText("Image 2")
        self.menuFile.addAction(self.actionOpen2)

        # self.pause = QtWidgets.QPushButton(self.centralwidget)
        # self.pause.setGeometry(QtCore.QRect(315, 1, 35, 35))
        # self.pause.setText("open")
        # self.pause.setObjectName("pause")
        # self.pause.setShortcut("Ctrl+o")
        # self.output2.close()
        # self.img1_component.close() 
        # self.output1.close()
        # self.img1.close()
        # self.img2_component.close()
        # self.img2.close()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # self.pause.clicked.connect(lambda:self.opensignal())
        #self.actionOpen.triggered.connect(lambda:self.Components())
        self.counter=-1
        self.images=[self.img1,self.img2,self.img1_component,self.img2_component,self.output1,self.output2]


    # def readsignal(self):
    #     #self.fname=QtGui.QFileDialog.getOpenFileName(self,"txt or CSV or xls","QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)")
    #     self.fname=QtGui.QFileDialog.getOpenFileName(self, 'Open file', "Image files (*.jpg *.gif)")
    #     self.path=self.fname[0]
    #     self.img= cv2.imread(self.path,0)
    #     print (self.img)
    # def opensignal(self):
    #     self.readsignal()
    #     self.counter+=1
    #     self.images[self.counter%2].setImage(self.img.T)
    #     # self.img1.setImage(self.img.T)

    # def Components(self):
    #     self.fft = np.fft.fft2(self.img)
    #     # print(self.fft)
    #     self.amplitude = abs(self.fft)
    #     self.magnitude = 20*np.log(np.abs(np.fft.fftshift(self.fft)))
    #     self.fshift = np.fft.fftshift(self.fft)
    #     self.ishift = np.fft.ifftshift(fshift)
    #     self.phase = np.angle(self.fft)
    #     self.real = np.real(self.fft)
    #     self.imaginary = np.imag(self.fft)
    #     self.imagnitude= np.fft.ifft2(self.magnitude)
    #     self.iamplitude= np.fft.ifft2(self.amplitude)
    #     print(self.phase)
    #     self.images[2+self.counter%2].setImage(self.imagnitude.T)





    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.img1_combo.setItemText(0, _translate("MainWindow", " "))
        self.img1_combo.setItemText(1, _translate("MainWindow", "Magnitude"))
        self.img1_combo.setItemText(2, _translate("MainWindow", "Phase"))
        self.img1_combo.setItemText(3, _translate("MainWindow", "Real"))
        self.img1_combo.setItemText(4, _translate("MainWindow", "Imaginary"))
        self.img2_label.setText(_translate("MainWindow", "Image 2"))
        self.img2_combo.setItemText(0, _translate("MainWindow", " "))
        self.img2_combo.setItemText(1, _translate("MainWindow", "Magnitude"))
        self.img2_combo.setItemText(2, _translate("MainWindow", "Phase"))
        self.img2_combo.setItemText(3, _translate("MainWindow", "Real"))
        self.img2_combo.setItemText(4, _translate("MainWindow", "Imaginary"))
        self.img1_label.setText(_translate("MainWindow", "Image 1"))
        self.output_channel.setItemText(0, _translate("MainWindow", " "))
        self.output_channel.setItemText(1, _translate("MainWindow", "Output 1"))
        self.output_channel.setItemText(2, _translate("MainWindow", "Output 2"))
        self.Component1.setText(_translate("MainWindow", "Component 1"))
        self.component1_img.setItemText(0, _translate("MainWindow", " "))
        self.component1_img.setItemText(1, _translate("MainWindow", "Image 1"))
        self.component1_img.setItemText(2, _translate("MainWindow", "Image 2"))
        self.component2.setText(_translate("MainWindow", "Component 2"))
        self.component2_img.setItemText(0, _translate("MainWindow", " "))
        self.component2_img.setItemText(1, _translate("MainWindow", "Image 1"))
        self.component2_img.setItemText(2, _translate("MainWindow", "Image 2"))
        self.mixer_output.setText(_translate("MainWindow", "Mixer Output"))
        self.component1_type.setItemText(0, _translate("MainWindow", " "))
        self.component1_type.setItemText(1, _translate("MainWindow", "Magnitude"))
        self.component1_type.setItemText(2, _translate("MainWindow", "Phase"))
        self.component1_type.setItemText(3, _translate("MainWindow", "Real"))
        self.component1_type.setItemText(4, _translate("MainWindow", "Imaginary"))
        self.component2_type.setItemText(0, _translate("MainWindow", " "))
        self.component2_type.setItemText(1, _translate("MainWindow", "Magnitude"))
        self.component2_type.setItemText(2, _translate("MainWindow", "Phase"))
        self.component2_type.setItemText(3, _translate("MainWindow", "Real"))
        self.component2_type.setItemText(4, _translate("MainWindow", "Imaginary"))
        self.output1_label.setText(_translate("MainWindow", "Outpu1 1"))
        self.output2_label.setText(_translate("MainWindow", "Output 2"))
        self.menuFile.setTitle(_translate("MainWindow", "Open"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
