# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frienditem.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FriendItem(object):
    def setupUi(self, FriendItem):
        FriendItem.setObjectName("FriendItem")
        FriendItem.resize(200, 60)
        FriendItem.setMinimumSize(QtCore.QSize(200, 0))
        FriendItem.setMaximumSize(QtCore.QSize(200, 16777215))
        self.horizontalLayout = QtWidgets.QHBoxLayout(FriendItem)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(FriendItem)
        self.label.setMinimumSize(QtCore.QSize(40, 40))
        self.label.setMaximumSize(QtCore.QSize(40, 40))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/head/resource/head/head.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.nameLabel = QtWidgets.QLabel(FriendItem)
        self.nameLabel.setMinimumSize(QtCore.QSize(0, 26))
        self.nameLabel.setMaximumSize(QtCore.QSize(16777215, 26))
        self.nameLabel.setStyleSheet("font: 11pt \"Arial\";")
        self.nameLabel.setObjectName("nameLabel")
        self.verticalLayout.addWidget(self.nameLabel)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(FriendItem)
        QtCore.QMetaObject.connectSlotsByName(FriendItem)

    def retranslateUi(self, FriendItem):
        _translate = QtCore.QCoreApplication.translate
        FriendItem.setWindowTitle(_translate("FriendItem", "Form"))
        self.nameLabel.setText(_translate("FriendItem", "这是好友名字"))
import res_rc
