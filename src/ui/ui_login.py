# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:/git/AxisChat/ui/login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginWidget(object):
    def setupUi(self, LoginWidget):
        LoginWidget.setObjectName("LoginWidget")
        LoginWidget.resize(450, 300)
        LoginWidget.setMinimumSize(QtCore.QSize(450, 300))
        LoginWidget.setMaximumSize(QtCore.QSize(450, 300))
        self.verticalLayout = QtWidgets.QVBoxLayout(LoginWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(LoginWidget)
        self.widget.setMinimumSize(QtCore.QSize(0, 150))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 150))
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/background/resource/background/timg.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.verticalLayout.addWidget(self.widget)
        self.loginWidget = QtWidgets.QWidget(LoginWidget)
        self.loginWidget.setMinimumSize(QtCore.QSize(0, 150))
        self.loginWidget.setMaximumSize(QtCore.QSize(16777215, 150))
        self.loginWidget.setStyleSheet("")
        self.loginWidget.setObjectName("loginWidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.loginWidget)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(30, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.widget_3 = QtWidgets.QWidget(self.loginWidget)
        self.widget_3.setMinimumSize(QtCore.QSize(98, 98))
        self.widget_3.setMaximumSize(QtCore.QSize(98, 98))
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.headLabel = QtWidgets.QLabel(self.widget_3)
        self.headLabel.setText("")
        self.headLabel.setPixmap(QtGui.QPixmap(":/head/resource/head/head.png"))
        self.headLabel.setScaledContents(True)
        self.headLabel.setObjectName("headLabel")
        self.verticalLayout_2.addWidget(self.headLabel)
        self.horizontalLayout_3.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.loginWidget)
        self.widget_4.setMinimumSize(QtCore.QSize(250, 98))
        self.widget_4.setMaximumSize(QtCore.QSize(250, 98))
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.userLineEdit = QtWidgets.QLineEdit(self.widget_4)
        self.userLineEdit.setObjectName("userLineEdit")
        self.verticalLayout_4.addWidget(self.userLineEdit)
        self.passwordLineEdit = QtWidgets.QLineEdit(self.widget_4)
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.verticalLayout_4.addWidget(self.passwordLineEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rememberCheckBox = QtWidgets.QCheckBox(self.widget_4)
        self.rememberCheckBox.setObjectName("rememberCheckBox")
        self.horizontalLayout.addWidget(self.rememberCheckBox)
        self.autoLoginCheckBox = QtWidgets.QCheckBox(self.widget_4)
        self.autoLoginCheckBox.setObjectName("autoLoginCheckBox")
        self.horizontalLayout.addWidget(self.autoLoginCheckBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.loginButton = QtWidgets.QPushButton(self.widget_4)
        self.loginButton.setMinimumSize(QtCore.QSize(0, 60))
        self.loginButton.setMaximumSize(QtCore.QSize(16777215, 60))
        self.loginButton.setObjectName("loginButton")
        self.verticalLayout_5.addWidget(self.loginButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem1)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.horizontalLayout_3.addWidget(self.widget_4)
        spacerItem2 = QtWidgets.QSpacerItem(30, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.line = QtWidgets.QFrame(self.loginWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_6.addWidget(self.line)
        self.widget_2 = QtWidgets.QWidget(self.loginWidget)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 18))
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 18))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.settingsButton = QtWidgets.QToolButton(self.widget_2)
        self.settingsButton.setAutoRaise(True)
        self.settingsButton.setObjectName("settingsButton")
        self.horizontalLayout_4.addWidget(self.settingsButton)
        spacerItem3 = QtWidgets.QSpacerItem(361, 15, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.registerButton = QtWidgets.QToolButton(self.widget_2)
        self.registerButton.setAutoRaise(True)
        self.registerButton.setObjectName("registerButton")
        self.horizontalLayout_4.addWidget(self.registerButton)
        self.verticalLayout_6.addWidget(self.widget_2)
        self.verticalLayout.addWidget(self.loginWidget)

        self.retranslateUi(LoginWidget)
        QtCore.QMetaObject.connectSlotsByName(LoginWidget)

    def retranslateUi(self, LoginWidget):
        _translate = QtCore.QCoreApplication.translate
        LoginWidget.setWindowTitle(_translate("LoginWidget", "Form"))
        self.userLineEdit.setPlaceholderText(_translate("LoginWidget", "账号"))
        self.passwordLineEdit.setPlaceholderText(_translate("LoginWidget", "密码"))
        self.rememberCheckBox.setText(_translate("LoginWidget", "记住密码"))
        self.autoLoginCheckBox.setText(_translate("LoginWidget", "自动登陆"))
        self.loginButton.setText(_translate("LoginWidget", "登陆"))
        self.settingsButton.setText(_translate("LoginWidget", "设置"))
        self.registerButton.setText(_translate("LoginWidget", "注册"))
import res_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWidget = QtWidgets.QWidget()
    ui = Ui_LoginWidget()
    ui.setupUi(LoginWidget)
    LoginWidget.show()
    sys.exit(app.exec_())
