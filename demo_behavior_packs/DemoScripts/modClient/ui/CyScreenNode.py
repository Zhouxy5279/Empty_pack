#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : classmate_chen
# @Email   : c_l-m@qq.com
# @Time    : 2020/10/16 15:57

import mod.client.extraClientApi as clientApi
from mod.client.system.clientSystem import ClientSystem
from DemoScripts.modClient.ui.BaseScreenNode import BaseScreenNode

ScreenNode = clientApi.GetScreenNodeCls()
MiniMapScreenNode = clientApi.GetMiniMapScreenNodeCls()

CY_UI_CLIENT_NAMESPACE = 'cy_ui_client_namespace'
CY_UI_CLIENT_SYSTEM_NAME = 'cy_ui_client_system_name'
UI_STATE_CHANGE_EVENT_NAME = 'CyUiStateChangeEvent'


class CyScreenNode(BaseScreenNode):
    def __init__(self, namespace, name, param, base_path=''):
        BaseScreenNode.__init__(self, namespace, name, param)
        self.__Base_Path = base_path
        self.GetVisible = self.get_visible
        self.ui_name = type(self).__name__

        self.cy_ui_client = ClientSystem(
            CY_UI_CLIENT_NAMESPACE, CY_UI_CLIENT_SYSTEM_NAME)
        if self.__Base_Path:
            self.cy_ui_client.ListenForEvent(
                CY_UI_CLIENT_NAMESPACE,
                CY_UI_CLIENT_SYSTEM_NAME,
                UI_STATE_CHANGE_EVENT_NAME,
                self,
                self.cy_ui_state_change_event_callback
            )

        self.base_state = True
        self.can_show = True

    def get_visible(self, component_path):
        """
        获取控件是否显示

        :param component_path: 控件路径
        :type component_path: str
        :return: True:已显示 False:未显示
        :rtype: bool
        """
        size = self.GetSize(component_path)
        if size == (0, 0) or not size:
            return False
        return True

    def cy_ui_open(self):
        """
        该UI文件中的二级UI显示时调用该函数
        """
        send_dict = dict()
        send_dict['ui_name'] = self.ui_name
        send_dict['state'] = True
        self.cy_ui_client.BroadcastEvent(UI_STATE_CHANGE_EVENT_NAME, send_dict)

    def cy_ui_close(self):
        """
        该UI文件中的二级UI隐藏时调用该函数
        """
        send_dict = dict()
        send_dict['ui_name'] = self.ui_name
        send_dict['state'] = False
        self.cy_ui_client.BroadcastEvent(UI_STATE_CHANGE_EVENT_NAME, send_dict)

    def cy_ui_state_change_event_callback(self, args):
        """
        创艺UI状态改变事件
        args:
            ui_name: ui的名字
            state: ui改变后的状态 True为开启 False为关闭
        """
        if args['state'] and self.ui_name != args['ui_name']:
            self.base_state = self.GetVisible(self.__Base_Path)
            self.SetVisible(self.__Base_Path, False)
            self.can_show = False
        elif not args['state'] and self.ui_name != args['ui_name']:
            if self.base_state:
                self.SetVisible(self.__Base_Path, True)
            self.can_show = True

