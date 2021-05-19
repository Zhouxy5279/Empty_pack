# -*- coding: utf-8 -*-

import client.extraClientApi as clientApi
from DemoScripts import logger
from DemoScripts.modCommon.config.const import Const
from DemoScripts.modClient.ui.BaseScreenNode import BaseScreenNode
ViewBinder = clientApi.GetViewBinderCls()
ViewRequest = clientApi.GetViewViewRequestCls()
ScreenNode = clientApi.GetScreenNodeCls()


class DemoUI(BaseScreenNode):
    def __init__(self, namespace, name, param):
        BaseScreenNode.__init__(self, namespace, name, param)
        self.__playerId = clientApi.GetLocalPlayerId()
        self.__btnPanel = "/buttonPanel"
        self.__btnCommon = self.__btnPanel + "/button_common"
        self.__client = None

    # 引擎调用函数, UI创建成功时调用
    def Create(self):
        pass

    def init(self, client):
        self.__client = client

    def set_common_btn_visible(self, val):
        self.set_visible(self.__btnCommon, val)

    def tick(self):
        pass

    # 旧版绑定按钮方法
    @ViewBinder.binding(ViewBinder.BF_ButtonClickUp)
    def on_common_click(self, args):
        data = self.__client.CreateEventData()
        data["player"] = self.__playerId
        logger.info("通知服务端点击按钮")
        self.__client.NotifyToServer(Const.clientClickButtonEvent, data)
        return ViewRequest.Refresh

