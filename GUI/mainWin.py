# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWin.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(701, 620)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(701, 620))
        MainWindow.setStyleSheet("")
        self.mainWidget = QtWidgets.QWidget(MainWindow)
        self.mainWidget.setStyleSheet("QWidget#mainWidget{\n"
"background-image: url(:/bg/bg.jpg);\n"
"background-size:  cover;               \n"
"background-repeat:   no-repeat;\n"
"background-position: center center;        \n"
"\n"
"}")
        self.mainWidget.setObjectName("mainWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.mainWidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.TitleLabel_withURL = QtWidgets.QLabel(self.mainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TitleLabel_withURL.sizePolicy().hasHeightForWidth())
        self.TitleLabel_withURL.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        self.TitleLabel_withURL.setFont(font)
        self.TitleLabel_withURL.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.TitleLabel_withURL.setAlignment(QtCore.Qt.AlignCenter)
        self.TitleLabel_withURL.setOpenExternalLinks(True)
        self.TitleLabel_withURL.setObjectName("TitleLabel_withURL")
        self.verticalLayout_5.addWidget(self.TitleLabel_withURL)
        self.widgetWithRadius = QtWidgets.QWidget(self.mainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetWithRadius.sizePolicy().hasHeightForWidth())
        self.widgetWithRadius.setSizePolicy(sizePolicy)
        self.widgetWithRadius.setMaximumSize(QtCore.QSize(16777212, 16777215))
        self.widgetWithRadius.setStyleSheet("QWidget#widgetWithRadius{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(124, 57, 191, 120), stop:1 rgba(42, 44, 89, 220));\n"
"border-radius: 80px;\n"
"}")
        self.widgetWithRadius.setObjectName("widgetWithRadius")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widgetWithRadius)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.Status = QtWidgets.QLabel(self.widgetWithRadius)
        self.Status.setAlignment(QtCore.Qt.AlignCenter)
        self.Status.setObjectName("Status")
        self.verticalLayout_6.addWidget(self.Status)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.radioButton_3 = QtWidgets.QRadioButton(self.widgetWithRadius)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridLayout.addWidget(self.radioButton_3, 10, 2, 1, 1)
        self.Port_Label = QtWidgets.QLabel(self.widgetWithRadius)
        self.Port_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Port_Label.setObjectName("Port_Label")
        self.gridLayout.addWidget(self.Port_Label, 3, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 5, 2, 1, 1)
        self.GameIcon = QtWidgets.QRadioButton(self.widgetWithRadius)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.GameIcon.setFont(font)
        self.GameIcon.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.GameIcon.setStyleSheet("color: rgb(255, 255, 255);")
        self.GameIcon.setChecked(True)
        self.GameIcon.setObjectName("GameIcon")
        self.gridLayout.addWidget(self.GameIcon, 8, 2, 1, 1)
        self.Port_input = QtWidgets.QLineEdit(self.widgetWithRadius)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Port_input.sizePolicy().hasHeightForWidth())
        self.Port_input.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(True)
        self.Port_input.setFont(font)
        self.Port_input.setStyleSheet("border-radius: 10px;")
        self.Port_input.setInputMask("")
        self.Port_input.setMaxLength(6)
        self.Port_input.setAlignment(QtCore.Qt.AlignCenter)
        self.Port_input.setObjectName("Port_input")
        self.gridLayout.addWidget(self.Port_input, 3, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 3, 1, 1)
        self.SysIcon_Note = QtWidgets.QLabel(self.widgetWithRadius)
        self.SysIcon_Note.setObjectName("SysIcon_Note")
        self.gridLayout.addWidget(self.SysIcon_Note, 11, 2, 1, 1)
        self.IP_input = QtWidgets.QLineEdit(self.widgetWithRadius)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IP_input.sizePolicy().hasHeightForWidth())
        self.IP_input.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(True)
        self.IP_input.setFont(font)
        self.IP_input.setStyleSheet("border-radius: 10px;")
        self.IP_input.setText("")
        self.IP_input.setMaxLength(16)
        self.IP_input.setAlignment(QtCore.Qt.AlignCenter)
        self.IP_input.setClearButtonEnabled(True)
        self.IP_input.setObjectName("IP_input")
        self.gridLayout.addWidget(self.IP_input, 2, 2, 1, 1)
        self.Change_label = QtWidgets.QLabel(self.widgetWithRadius)
        self.Change_label.setObjectName("Change_label")
        self.gridLayout.addWidget(self.Change_label, 10, 1, 1, 1)
        self.IP_Label = QtWidgets.QLabel(self.widgetWithRadius)
        self.IP_Label.setObjectName("IP_Label")
        self.gridLayout.addWidget(self.IP_Label, 2, 1, 1, 1)
        self.ChangeAvatar = QtWidgets.QRadioButton(self.widgetWithRadius)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        self.ChangeAvatar.setFont(font)
        self.ChangeAvatar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ChangeAvatar.setStyleSheet("color: rgb(255, 255, 255);")
        self.ChangeAvatar.setObjectName("ChangeAvatar")
        self.gridLayout.addWidget(self.ChangeAvatar, 12, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 1, 2, 1, 1)
        self.GameIcon_Note = QtWidgets.QLabel(self.widgetWithRadius)
        self.GameIcon_Note.setAlignment(QtCore.Qt.AlignCenter)
        self.GameIcon_Note.setObjectName("GameIcon_Note")
        self.gridLayout.addWidget(self.GameIcon_Note, 9, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(500, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 6, 2, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(-1, 15, -1, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.CacheBar = QtWidgets.QProgressBar(self.widgetWithRadius)
        self.CacheBar.setStyleSheet("QProgressBar {\n"
"border-radius: 12px;\n"
"color:rgb(255, 255, 255)\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"background: QLinearGradient( x1:0.358, y1:0.602182, x2:0.960318, y2:0.648, stop:0 rgb(124, 57, 191), stop:0.903409 rgb(242, 80, 231));\n"
"border-radius: 12px;\n"
"};\n"
"")
        self.CacheBar.setProperty("value", 99)
        self.CacheBar.setAlignment(QtCore.Qt.AlignCenter)
        self.CacheBar.setTextVisible(True)
        self.CacheBar.setObjectName("CacheBar")
        self.gridLayout_2.addWidget(self.CacheBar, 4, 2, 1, 1)
        self.Cache_label = QtWidgets.QLabel(self.widgetWithRadius)
        self.Cache_label.setObjectName("Cache_label")
        self.gridLayout_2.addWidget(self.Cache_label, 4, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.widgetWithRadius)
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 7, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem5, 0, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem6, 2, 1, 2, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem7, 2, 0, 1, 1)
        self.Credits = QtWidgets.QLabel(self.widgetWithRadius)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Credits.sizePolicy().hasHeightForWidth())
        self.Credits.setSizePolicy(sizePolicy)
        self.Credits.setAlignment(QtCore.Qt.AlignCenter)
        self.Credits.setOpenExternalLinks(True)
        self.Credits.setObjectName("Credits")
        self.gridLayout_2.addWidget(self.Credits, 6, 2, 1, 1)
        self.Connect_btn = QtWidgets.QPushButton(self.widgetWithRadius)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Connect_btn.sizePolicy().hasHeightForWidth())
        self.Connect_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.Connect_btn.setFont(font)
        self.Connect_btn.setStyleSheet("color: rgb(42, 44, 89);")
        self.Connect_btn.setCheckable(False)
        self.Connect_btn.setFlat(False)
        self.Connect_btn.setObjectName("Connect_btn")
        self.gridLayout_2.addWidget(self.Connect_btn, 2, 2, 2, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem8, 5, 2, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem9, 1, 2, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem10, 2, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widgetWithRadius)
        self.label_2.setOpenExternalLinks(True)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 8, 2, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_6)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem11)
        self.verticalLayout_5.addWidget(self.widgetWithRadius)
        MainWindow.setCentralWidget(self.mainWidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 701, 22))
        self.menubar.setObjectName("menubar")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.Options = QtWidgets.QAction(MainWindow)
        self.Options.setObjectName("Options")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.About = QtWidgets.QAction(MainWindow)
        self.About.setObjectName("About")
        self.Special_thanks = QtWidgets.QAction(MainWindow)
        self.Special_thanks.setObjectName("Special_thanks")
        self.menuSettings.addAction(self.Options)
        self.menuSettings.addSeparator()
        self.menuSettings.addAction(self.About)
        self.menuSettings.addAction(self.Special_thanks)
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        self.GameIcon.toggled['bool'].connect(self.GameIcon_Note.setVisible)
        self.radioButton_3.toggled['bool'].connect(self.SysIcon_Note.setVisible)
        self.ChangeAvatar.toggled['bool'].connect(self.SysIcon_Note.hide)
        self.ChangeAvatar.toggled['bool'].connect(self.GameIcon_Note.hide)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.TitleLabel_withURL.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><a href=\"https://github.com/OfficialAhmed/Iconit-PS4/releases\"><span style=\" text-decoration: underline; color:#f250e7;\">Iconit v4.72</span></a></p></body></html>"))
        self.Status.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700; color:#f2ae30;\">Waiting Connection ..</span></p></body></html>"))
        self.radioButton_3.setText(_translate("MainWindow", "System Icons"))
        self.Port_Label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700; color:#f2ae30;\">PS4 Port</span></p></body></html>"))
        self.GameIcon.setText(_translate("MainWindow", "Game Icon/Pic"))
        self.Port_input.setText(_translate("MainWindow", "21"))
        self.SysIcon_Note.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:8pt; font-weight:700; color:#f2ae30;\">Note: Full R/W permissions required ( PS4 Xplorer FTP &amp; make sure to enable danger mode)</span></p></body></html>"))
        self.IP_input.setPlaceholderText(_translate("MainWindow", "192.168.XXX.XXX"))
        self.Change_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700; color:#f2ae30;\">Mode</span></p></body></html>"))
        self.IP_Label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700; color:#f2ae30;\">PS4 IP</span></p></body></html>"))
        self.ChangeAvatar.setText(_translate("MainWindow", "Profile Avatar"))
        self.GameIcon_Note.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:8pt; font-weight:700; color:#f2ae30;\">Note: You can enable Homebrew icons in the settings before connecting to the PS4</span></p></body></html>"))
        self.Cache_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#f2ae30;\">Caching</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><a href=\"https://www.paypal.com/paypalme/Officialahmed0\"><span style=\" font-weight:700; font-style:italic; text-decoration: underline; color:#f250e7;\">Donate (PayPal)</span></a></p></body></html>"))
        self.Credits.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><a href=\"https://all-exhost.github.io/icon%20downloader.html\"><span style=\" font-size:8pt; font-weight:700; font-style:italic; text-decoration: underline; color:#f250e7;\">Download Free Icons</span></a></p></body></html>"))
        self.Connect_btn.setText(_translate("MainWindow", "Connect PS4"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><a href=\"https://twitter.com/OfficialAhmed0\"><span style=\" font-weight:700; font-style:italic; text-decoration: underline; color:#f250e7;\">Created by @OfficialAhmed0</span></a></p></body></html>"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.Options.setText(_translate("MainWindow", "Options..."))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.About.setText(_translate("MainWindow", "About"))
        self.Special_thanks.setText(_translate("MainWindow", "Special thanks"))
import iconit_rc
