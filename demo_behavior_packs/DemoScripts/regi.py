# -*- coding: utf-8 -*-
import json
import sys
import uuid
import shutil
import os

WorldPath = r'C:\Users\Administrator\AppData\Roaming\MinecraftPE_Netease\minecraftWorlds\AkumaFruit'
LauncherPath = r'C:\Users\Administrator\Desktop\MC_developer_pack\1.23.0.127310\Minecraft.Windows.exe'

root_path = "../../"
pack_path_list = os.listdir(root_path)

mods = {}


def get_pack_type(path):
    """ 获取一个文件夹下包的类型

    @param path:
    @return 0: 没什么用， 1:行为包，   2: 资源包
    """
    if os.path.isdir(path):
        files = os.listdir(path)
        if "entities" in files:
            return 1
        elif "textures" in files:
            return 2
        else:
            print path, "目录下不存在entities 或 textures 请确保文件的规范性"
            return 0
    return 0


def get_config_json(path):
    """
    获取一个包下的配置文件路径
    @param path:
    @return:
    """
    json_file = path + "/pack_manifest.json"
    if not os.path.isfile(json_file):
        json_file = path + "/manifest.json"
    if not os.path.isfile(json_file):
        print "未在文件夹下", path, "找到配置文件, 请检查"
        return None
    return json_file


def get_mod_name(path):
    """ 获取一个包所属的ModName

    @param path:
    """
    json_file = get_config_json(path)
    if not json_file:
        return None

    with open(json_file, "r") as f:
        config_json = json.load(f)
        mod_name = config_json["header"]["name"]
        return mod_name


def get_mods():
    print(pack_path_list)
    for path in pack_path_list:
        pack_path = root_path + path
        p_type = get_pack_type(pack_path)
        if p_type:
            mod_name = get_mod_name(pack_path)
            if mod_name not in mods:
                mods[mod_name] = {}
            mods[mod_name][p_type] = pack_path
    return mods


# 仅仅在第一次将项目注册进游戏地图时调用
if __name__ == "__main__":
    # 设置行为包中资源的UUID值
    mods = get_mods()
    print(mods)
    # 检测网易配置文件
    netease_b_path = os.path.join(WorldPath, "netease_world_behavior_packs.json")
    print "初始化世界行为包配置json"
    with open(netease_b_path, 'w') as f:
        json.dump([{"pack_id": "", "version": []}] * mods.keys().__len__(), f)

    netease_r_path = os.path.join(WorldPath, "netease_world_resource_packs.json")
    print "初始化世界资源包配置json"
    with open(netease_r_path, 'w') as f:
        json.dump([{"pack_id": "", "version": []}] * mods.keys().__len__(), f)

    i = -1
    for mod_name in mods:
        i += 1
        print "开始修改", mod_name, "的行为包uuid"
        beh_path = mods[mod_name][1]
        beh_json_path = get_config_json(beh_path)
        with open(beh_json_path, "r") as f:
            b_packs = json.load(f)
        b_header = b_packs.get("header")
        b_header["uuid"] = str(uuid.uuid4())
        b_modules = b_packs.get("modules")[0]
        b_modules["uuid"] = str(uuid.uuid4())
        with open(beh_json_path, "w") as f:
            json.dump(b_packs, f, indent=4)

        print "开始修改", mod_name, "的资源包uuid"
        res_path = mods[mod_name][2]
        res_json_path = get_config_json(res_path)
        with open(res_json_path, "r") as f:
            b_packs = json.load(f)
        r_header = b_packs.get("header")
        r_header["uuid"] = str(uuid.uuid4())
        r_modules = b_packs.get("modules")[0]
        r_modules["uuid"] = str(uuid.uuid4())
        with open(res_json_path, "w") as f:
            json.dump(b_packs, f, indent=4)

        print "开始复制", mod_name, "行为包"
        b_target = os.path.join(WorldPath, "behavior_packs", mod_name)
        if os.path.exists(b_target):
            shutil.rmtree(b_target)
        shutil.copytree(beh_path, b_target)

        print "开始复制", mod_name, "资源包"
        r_target = os.path.join(WorldPath, "resource_packs", mod_name)
        if os.path.exists(r_target):
            shutil.rmtree(r_target)
        shutil.copytree(res_path, r_target)

        # 在网易配置文件中启用该行为包
        netease_b_path = os.path.join(WorldPath, "netease_world_behavior_packs.json")
        with open(netease_b_path, 'r') as f:
            netease_b_packs = json.load(f)
        netease_b_packs[i]["pack_id"] = b_header["uuid"]
        netease_b_packs[i]["version"] = b_header["version"]
        with open(netease_b_path, 'w') as f:
            json.dump(netease_b_packs, f)

        # 在网易配置文件中启用该资源包
        netease_r_path = os.path.join(WorldPath, "netease_world_resource_packs.json")
        with open(netease_r_path, 'r') as f:
            netease_r_packs = json.load(f)
        netease_r_packs[i]["pack_id"] = r_header["uuid"]
        netease_r_packs[i]["version"] = r_header["version"]
        with open(netease_r_path, 'w') as f:
            json.dump(netease_r_packs, f)
