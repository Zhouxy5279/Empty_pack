# -*- coding: utf-8 -*-


class Const(object):
    # todo MOD名需要重写
    modName = "HolyDemo"

    modVersion = "0.0.1"
    minecraft = "Minecraft"

    # Server System
    serverSystemName = modName + "ServerSystem"
    serverSystemClsPath = "DemoScripts.modServer.serverSystem.Server"

    # Client System
    clientSystemName = modName + "ClientSystem"
    clientSystemClsPath = "DemoScripts.modClient.clientSystem.Client"

    # Custom Component
    componentList = []

    # todo 自定义事件，根据需要编写
    # Server Custom Event

    # Client Custom Event
    clientUIFinishedEvent = "ClientUIFinishedEvent"
    clientClickButtonEvent = "ClientClickButtonEvent"

    # todo 自定义UI  必须重写UI名和类名  不能存在相同命名空间的UI
    demoUIKey = "demoUI"
    demoUIClsPath = "DemoScripts.modClient.ui.demoUI.DemoUI"
    demoUINameSpace = "demoUI.main"
    # uiList不可删除，可置空
    uiList = [(demoUIKey, demoUIClsPath, demoUINameSpace)]








