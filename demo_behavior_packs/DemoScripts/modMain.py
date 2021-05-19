# -*- coding: utf-8 -*-

from common.mod import Mod
import client.extraClientApi as clientApi
import server.extraServerApi as serverApi
from DemoScripts import logger
from DemoScripts.modCommon.config.const import Const


# todo 类名需要重写
@Mod.Binding(name=Const.modName, version=Const.modVersion)
class DemoMod(object):

    def __init__(self):
        logger.info("MOD初始化")

    @Mod.InitServer()
    def serverInit(self):
        serverApi.RegisterSystem(Const.modName, Const.serverSystemName, Const.serverSystemClsPath)

    @Mod.DestroyServer()
    def serverDestroy(self):
        logger.info("===== destroy test server =====")
    
    @Mod.InitClient()
    def clientInit(self):
        clientApi.RegisterSystem(Const.modName, Const.clientSystemName, Const.clientSystemClsPath)
        # 注册Component
        for (name, clsPath) in Const.componentList:
            clientApi.RegisterComponent(Const.modName, name, clsPath)

    @Mod.DestroyClient()
    def clientDestroy(self):
        logger.info("===== destroy test client =====")
