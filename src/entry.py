#encoding: utf-8

from bindfunc import CFunction
import customprotocol.p_player
import protocol
import struct
import logger
import timer
import time

def OnHello(oCtrl, oProtocol):
    print("Hello", oProtocol.m_Seed)
    a = protocol.p_login.P_AnswerHello()
    a.m_Answer = oProtocol.m_Seed
    oCtrl.SendProtocol(a)

    # 账密
    l = protocol.p_login.P_Login()
    l.m_User = oCtrl.m_User
    l.m_Password = oCtrl.m_Password
    oCtrl.SendProtocol(l)

def OnPlayerInfo(oCtrl, oInfo):
    print(oInfo.m_Uid)
    print(oInfo.m_Name)

    p = protocol.p_login.P_RequestSyncTime()
    p.m_ClientTime = timer.GetSecond()

    oCtrl.SendProtocol(p)
    oCtrl.LoginResult(3)

def OnSyncTime(oCtrl, oSyncTime):
    iClientMS = int(time.time() * 1000)
    iServerMS = oSyncTime.m_ServerTimeS * 1000 + oSyncTime.m_ServerTimeMS
    iTimeDiff = iServerMS - iClientMS
    timer.SetTimeDifference(iTimeDiff)

g_Func = {
    protocol.P_Hello_Idx : OnHello,
    protocol.P_BaseInfo_Idx: OnPlayerInfo,
    protocol.P_SyncTime_Idx: OnSyncTime,
}

def OnEntry(oCtrl, data):
    iProtocolNumber = struct.unpack("H", data[2:4])[0]
    cls = protocol.GetProtocol(iProtocolNumber)
    if not cls:
        logger.Warning("没找到合适的解析协议 %s"%(iProtocolNumber))
        return
    oProtocol = cls()
    oProtocol.UnpackData(data)
    oFunc = g_Func.get(oProtocol.m_ProtocolNumber, None)
    if oFunc:
        oFunc(oCtrl, oProtocol)