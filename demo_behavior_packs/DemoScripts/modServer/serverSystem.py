# -*- coding: utf-8 -*-
import mod.server.extraServerApi as serverApi
from DemoScripts import logger
from DemoScripts.modServer.utils.taskQueue import TaskQueue
from DemoScripts.modServer.item.itemManager import ItemManager
from DemoScripts.modCommon.config.const import Const

ServerSystem = serverApi.GetServerSystemCls()
serverFactory = serverApi.GetEngineCompFactory()
serverEnum = serverApi.GetMinecraftEnum()


class Server(ServerSystem):
    def __init__(self, namespace, system_name):
        ServerSystem.__init__(self, namespace, system_name)

        self.__playerIdList = []
        self.__levelId = serverApi.GetLevelId()
        self.__queue = TaskQueue()

        self.item_manager = ItemManager(self)  # 一个用于管理物品功能的实例

        self.listen_event()

    # 监听事件
    def listen_event(self):
        # todo 注册自定义事件，根据需要重写或删除
        # 监听系统事件
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
                            "AddServerPlayerEvent", self, self.add_player)
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
                            "OnScriptTickServer", self, self.tick)
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
                            "LoadServerAddonScriptsAfter", self, self.init)

        # 监听自定义事件
        self.ListenForEvent(Const.modName, Const.clientSystemName, Const.clientClickButtonEvent,
                            self, self.on_click)
        self.ListenForEvent(Const.modName, Const.clientSystemName, Const.clientUIFinishedEvent,
                            self, self.ui_finished)

        logger.info("————>> 服务端开始监听事件 <<————")

    def init(self, data):
        pass

    def tick(self):
        self.__queue.tick()

    def add_player(self, data):
        player_id = data.get("id", "-1")
        if player_id == "-1":
            return
        self.__playerIdList.append(player_id)

    def ui_finished(self, data):
        pass

    def on_click(self, data):
        player = data.get("player".encode)
        comp = self.CreateComponent(player, Const.minecraft, 'item')
        player_pos = self.CreateComponent(player, Const.minecraft, 'pos')
        pos = player_pos.pos
        player_rot = self.CreateComponent(player, Const.minecraft, 'rot')
        rot = player_rot.rot
        if comp.carriedItem:
            pass




