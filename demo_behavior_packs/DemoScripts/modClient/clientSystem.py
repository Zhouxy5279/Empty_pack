# -*- coding: utf-8 -*-
import client.extraClientApi as clientApi
from DemoScripts import logger
from DemoScripts.modClient.utils.taskQueue import TaskQueue
from DemoScripts.modCommon.config.const import Const

ClientSystem = clientApi.GetClientSystemCls()
clientFactory = clientApi.GetEngineCompFactory()


class Client(ClientSystem):

    def __init__(self, namespace, system_name):
        ClientSystem.__init__(self, namespace, system_name)
        self.__playerId = clientApi.GetLocalPlayerId()
        self.__levelId = clientApi.GetLevelId()
        self.__current_ui = None

        self.__queue = TaskQueue()

        self.listen_event()

    def listen_event(self):
        # 监听系统事件
        self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(),
                            "UiInitFinished", self, self.ui_finished)
        self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(),
                            "OnScriptTickClient", self, self.tick)
        self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(),
                            "OnCarriedNewItemChangedClientEvent", self, self.on_carried_new_item)

        # todo 键盘按键事件，仅在开发中使用，发布后删除
        self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(),
                            "OnKeyPressInGame", self, self.on_key_press)

        logger.info("————>> 客户端开始监听事件 <<————")

    def on_key_press(self, data):
        key = data.get("key")
        is_down = data.get("isDown")
        if key == '90' and is_down == '1':  # 按下Z键
            # self.__current_ui.on_common_click({})
            pass

    def ui_finished(self, data):
        logger.info("————>> 注册UI <<————")
        for (key, clsPath, nameSpace) in Const.uiList:   # 批量注册UI
            clientApi.RegisterUI(Const.modName, key, clsPath, nameSpace)
            clientApi.CreateUI(Const.modName, key, {"isHud": 1})

        self.__current_ui = clientApi.GetUI(Const.modName, Const.demoUIKey)  # 获取UI实例
        if self.__current_ui:
            self.__current_ui.init(self)
            data = self.CreateEventData()
            data["player_id"] = self.__playerId
            self.NotifyToServer(Const.clientUIFinishedEvent, data)
        else:
            logger.error("————!! 创建UI失败 !!————")

    def tick(self):
        self.__queue.tick()
        if self.__current_ui:
            self.__current_ui.tick()

    def on_carried_new_item(self, data):
        pass
