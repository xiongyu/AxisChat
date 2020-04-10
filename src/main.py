from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QListWidgetItem
from PyQt5.QtNetwork import QTcpSocket
from PyQt5.QtCore import QTimer
from PyQt5 import QtCore

from ui.ui_login import Ui_LoginWidget
from ui.ui_chat import Ui_ChatWidget
from ui.ui_frienditem import Ui_FriendItem

import sys
sys.path.append('../common')

from protocol import GetRecvPackage
import entry
import logger
import protocol.p_login
import timer
import time

TYPE_ACCOUNTPWD_ERROR = 1
TYPE_NETWORK_ERR = 2
TYPE_LOGIN_SUCC = 3

class CFriendItem(QWidget, Ui_FriendItem):

    def __init__(self):
        super().__init__()
        self.setupUi(self)   #执行类中的setupUi函数

class CChatView(QWidget, Ui_ChatWidget):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)   #执行类中的setupUi函数

class CLoginView(QWidget, Ui_LoginWidget):

    def __init__(self):
        super().__init__()
        self.setupUi(self)   #执行类中的setupUi函数
        self.setWindowTitle("AxisChat")

    def DisableUI(self, enable1):
        enable = not enable1
        self.userLineEdit.setEnabled(enable)
        self.passwordLineEdit.setEnabled(enable)
        self.loginButton.setEnabled(enable)
        self.rememberCheckBox.setEnabled(enable)
        self.autoLoginCheckBox.setEnabled(enable)

class CApplicationController:
    
    def __init__(self):
        self.m_Socket = QTcpSocket()
        self.m_Socket.connected.connect(self.Connected)
        self.m_Socket.readyRead.connect(self.ReadyRead)
        self.m_Socket.disconnected.connect(self.Disconnected)
        self.m_Socket.error.connect(self.Error)
        self.m_Timer = QTimer()
        self.m_HeartbeatTimes = 0

        self.m_Data = bytes()
        self.m_User = ""
        self.m_Password = ""

        self.m_Timer.timeout.connect(self.Heartbeat)
        
    def Heartbeat(self):
        print('HB')
        self.m_Timer.start(1000)
        self.m_HeartbeatTimes += 1
        if self.m_HeartbeatTimes >= 8:
            self.m_HeartbeatTimes = 0
            p = protocol.p_login.P_RequestSyncTime()
            p.m_ClientTime = timer.GetSecond()
            self.SendProtocol(p)

        self.UpdateDate(timer.GetSecond())

    def UpdateDate(self, second):
        timeArray = time.localtime(second)#秒数
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        print(otherStyleTime)

    def CheckUserPassword(self, sUser, sPassword):
        if len(sUser) < 6:
            return 1
        if len(sPassword) < 8:
            return 2
        return 0

    def Login(self, sUser, sPassword):
        print(sUser, sPassword)
        ret = self.CheckUserPassword(sUser, sPassword)
        if ret:
            return ret
        self.m_User = sUser
        self.m_Password = sPassword
        self.m_Socket.connectToHost("47.115.41.13", 12349)

    def LoginResult(self, iType):
        if iType == TYPE_NETWORK_ERR:
            sReason = "网络错误"
        else:
            self.m_Timer.start(5000)
            sReason = "登陆成功"
        self.OnLoginResult(iType, sReason)
        
    def OnLoginResult(self, iType, sReason = ""):
        pass

    def Error(self, err):
        print("Error", err)
        self.LoginResult(TYPE_NETWORK_ERR)

    def Connected(self):
        print("Connected")

    def ReadyRead(self):
        print("ReadyRead")
        self.m_Data += self.m_Socket.readAll()
        data, pkglist = GetRecvPackage(self.m_Data)
        if not pkglist:
            return
        self.m_Data = data
        for pkgdata in pkglist:
            entry.OnEntry(self, pkgdata)

    def Disconnected(self):
        print("Disconnected")

    def SendProtocol(self, oProtocol):
        data = oProtocol.PacketData()
        self.m_Socket.write(data)

class CApplicationView(CApplicationController):

    def __init__(self):
        super().__init__()
        self.m_LoginUI = CLoginView()
        self.m_ChatUI = CChatView()

        self.m_LoginUI.loginButton.clicked.connect(self.ClickLogin)

    def ClickLogin(self):
        self.m_LoginUI.DisableUI(True)

        sUser = self.m_LoginUI.userLineEdit.text()
        sPassword = self.m_LoginUI.passwordLineEdit.text()
        ret = self.Login(sUser, sPassword)
        if not ret:
            return

        self.OnLoginResult(1, "账号或密码错误%s"%(ret))
        
    def OnLoginResult(self, iType, sReason = ""):
        self.m_LoginUI.DisableUI(False)
        if iType in (TYPE_ACCOUNTPWD_ERROR, TYPE_NETWORK_ERR):
            QMessageBox.information(self.m_LoginUI, "提示", sReason)
            return
        elif TYPE_LOGIN_SUCC == iType:
            #QMessageBox.information(self.m_LoginUI, "提示", sReason)
            self.m_ChatUI.show()
            self.m_LoginUI.hide()
            return
    
    def UpdateDate(self, second):
        timeArray = time.localtime(second)#秒数
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        self.m_ChatUI.dateLabel.setText(otherStyleTime)

    def Show(self):
        self.m_LoginUI.show()
        # self.m_ChatUI.show()

if __name__=='__main__':
    logger.Init()
    app=QApplication(sys.argv)
    w=CApplicationView()
    w.Show()

    item = QListWidgetItem()
    item.setSizeHint(QtCore.QSize(200, 60))
    w.m_ChatUI.friendWIdget.addItem(item)

    item2 = QListWidgetItem()
    item2.setSizeHint(QtCore.QSize(200, 60))
    w.m_ChatUI.friendWIdget.addItem(item2)

    w.m_ChatUI.friendWIdget.setItemWidget(item, CFriendItem())
    w.m_ChatUI.friendWIdget.setItemWidget(item2, CFriendItem())

    sys.exit(app.exec_())