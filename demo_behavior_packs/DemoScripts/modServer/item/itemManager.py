# -*- coding: utf-8 -*-

import mod.server.extraServerApi as serverApi
from DemoScripts import logger
from DemoScripts.modServer.utils.taskQueue import TaskQueue
from DemoScripts.modCommon.config.const import Const

ServerSystem = serverApi.GetServerSystemCls()
serverFactory = serverApi.GetEngineCompFactory()
serverEnum = serverApi.GetMinecraftEnum()


class ItemManager(object):
    def __init__(self, server):
        self.server = server

        self.listen_event()

    def listen_event(self):
        self.server.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
                                   "OnScriptTickServer", self, self.tick)
        pass

    def tick(self):
        pass