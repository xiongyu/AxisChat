# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:/git/AxisChat/ui/registerdlg.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(299, 180)
        Dialog.setMinimumSize(QtCore.QSize(0, 180))
        Dialog.setMaximumSize(QtCore.QSize(16777215, 180))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.userLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.userLineEdit.setObjectName("userLineEdit")
        self.horizontalLayout.addWidget(self.userLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.passwordLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.horizontalLayout_2.addWidget(self.passwordLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.comfirmLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.comfirmLineEdit.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.comfirmLineEdit.setObjectName("comfirmLineEdit")
        self.horizontalLayout_4.addWidget(self.comfirmLineEdit)
        self.righticon = QtWidgets.QLabel(self.groupBox)
        self.righticon.setMinimumSize(QtCore.QSize(16, 16))
        self.righticon.setMaximumSize(QtCore.QSize(16, 16))
        self.righticon.setStyleSheet("")
        self.righticon.setText("")
        self.righticon.setPixmap(QtGui.QPixmap(":/resource/icon/right.png"))
        self.righticon.setScaledContents(True)
        self.righticon.setObjectName("righticon")
        self.horizontalLayout_4.addWidget(self.righticon)
        self.erroricon = QtWidgets.QLabel(self.groupBox)
        self.erroricon.setMinimumSize(QtCore.QSize(16, 16))
        self.erroricon.setMaximumSize(QtCore.QSize(16, 16))
        self.erroricon.setText("")
        self.erroricon.setPixmap(QtGui.QPixmap(":/resource/icon/error.png"))
        self.erroricon.setScaledContents(True)
        self.erroricon.setObjectName("erroricon")
        self.horizontalLayout_4.addWidget(self.erroricon)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addWidget(self.groupBox)
        spacerItem = QtWidgets.QSpacerItem(20, 12, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cancelButton = QtWidgets.QPushButton(Dialog)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout_3.addWidget(self.cancelButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.registerButton = QtWidgets.QPushButton(Dialog)
        self.registerButton.setObjectName("registerButton")
        self.horizontalLayout_3.addWidget(self.registerButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Register"))
        self.groupBox.setTitle(_translate("Dialog", "注册信息"))
        self.label.setText(_translate("Dialog", "新用户名："))
        self.userLineEdit.setPlaceholderText(_translate("Dialog", "新用户名"))
        self.label_2.setText(_translate("Dialog", "新的密码："))
        self.passwordLineEdit.setPlaceholderText(_translate("Dialog", "新的密码"))
        self.label_3.setText(_translate("Dialog", "确认密码："))
        self.comfirmLineEdit.setPlaceholderText(_translate("Dialog", "新的密码"))
        self.cancelButton.setText(_translate("Dialog", "取消"))
        self.registerButton.setText(_translate("Dialog", "注册"))
import res_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
