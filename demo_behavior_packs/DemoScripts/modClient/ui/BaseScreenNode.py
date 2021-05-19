# -*- coding: utf-8 -*-

import mod.client.extraClientApi as clientApi
from DemoScripts import logger
from DemoScripts.modCommon.config.const import Const
ViewBinder = clientApi.GetViewBinderCls()
ViewRequest = clientApi.GetViewViewRequestCls()
ScreenNode = clientApi.GetScreenNodeCls()


class BaseScreenNode(ScreenNode):
    def __init__(self, namespace, name, param):
        ScreenNode.__init__(self, namespace, name, param)

    # 引擎调用函数 UI创建成功时调用
    def Create(self):
        logger.info('{}创建成功'.format(type(self).__name__))

    # 按钮绑定旧方法
    @ViewBinder.binding(ViewBinder.BF_ButtonClickUp)
    def on_click(self, args):
        """
        :param args: 'ButtonPath' 'TouchPosX' 'TouchPosY' 'ButtonState'
        :type args:dict
        :return:
        """
        return ViewRequest.Refresh

    # UI 销毁时调用
    def Destroy(self):
        logger.info('{}UI被销毁'.format(type(self).__name__))

    # ———————————— RE:built-in BaseUIControl method ————————————

    # ———— get ————

    def get_position(self, path):
        ui_ctrl = self.GetBaseUIControl(path)
        return ui_ctrl.GetPosition()

    def get_text(self, path):
        label_ctrl = self.GetBaseUIControl(path).asLabel()
        return label_ctrl.GetText()

    def get_size(self, path):
        ui_ctrl = self.GetBaseUIControl(path)
        return ui_ctrl.GetSize()

    # ———— set ————

    def set_touch_enable(self, path, val):
        ui_ctrl = self.GetBaseUIControl(path)
        ui_ctrl.SetTouchEnable(val)

    def set_visible(self, path, val):
        ui_ctrl = self.GetBaseUIControl(path)
        ui_ctrl.SetVisible(val)

    def set_position(self, path, pos):
        ui_ctrl = self.GetBaseUIControl(path)
        ui_ctrl.SetPosition(pos)

    def set_size(self, path, size):
        ui_ctrl = self.GetBaseUIControl(path)
        ui_ctrl.SetSize(size)

    def set_text(self, path, txt):
        label_ctrl = self.GetBaseUIControl(path).asLabel()
        label_ctrl.SetText(txt)

    def set_alpha(self, path, alpha):
        ui_ctrl = self.GetBaseUIControl(path)
        ui_ctrl.SetAlpha(alpha)

    def set_text_color(self, path, rgba):
        label_ctrl = self.GetBaseUIControl(path).asLabel()
        label_ctrl.SetTextColor(rgba)

    def set_sprite(self, path, img):
        button_ctrl = self.GetBaseUIControl(path).asImage()
        button_ctrl.SetSprite(img)

    def set_clip_ratio(self, path, ratio):
        img_ctrl = self.GetBaseUIControl(path).asImage()
        img_ctrl.SetSpriteClipRatio(1.0 - ratio)

