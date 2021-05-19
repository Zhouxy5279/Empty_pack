# -*- coding: utf-8 -*-

import json
import uuid
import shutil
import os

WorldPath = r'C:/Users/Administrator/AppData/Roaming/MinecraftPE_Netease/minecraftWorlds/demo'
LauncherPath = r'C:/Users/Administrator/Desktop/Minecraft/1.22.0.123134/Minecraft.Windows.exe'
projectName = "demo"

header = 'demo_'
version = [0, 0, 1]


if __name__ == "__main__":
    # 重置uuid 版本同步
    with open("../pack_manifest.json", "r") as f:
        b_packs = json.load(f)
    b_header = b_packs.get("header")
    b_header["uuid"] = str(uuid.uuid4())
    b_header["version"] = version
    b_modules = b_packs.get("modules")[0]
    b_modules["uuid"] = str(uuid.uuid4())
    b_modules["version"] = version
    with open("../pack_manifest.json", "w") as f:
        json.dump(b_packs, f)

    with open("../../" + header + 'resource_packs' + "/pack_manifest.json", "r") as f:
        r_packs = json.load(f)
    r_header = r_packs.get("header")
    r_header["uuid"] = str(uuid.uuid4())
    r_header["version"] = version
    r_modules = r_packs.get("modules")[0]
    r_modules["uuid"] = str(uuid.uuid4())
    r_modules["version"] = version
    with open("../../" + header + 'resource_packs' + "/pack_manifest.json", "w") as f:
        json.dump(r_packs, f)

    netease_b_path = os.path.join(WorldPath, "netease_world_behavior_packs.json")
    with open(netease_b_path, 'r') as f:
        netease_b_packs = json.load(f)
    netease_b_packs[0]["pack_id"] = b_header["uuid"]
    netease_b_packs[0]["version"] = b_header["version"]
    with open(netease_b_path, 'w') as f:
        json.dump(netease_b_packs, f)

    netease_r_path = os.path.join(WorldPath, "netease_world_resource_packs.json")
    with open(netease_r_path, 'r') as f:
        netease_r_packs = json.load(f)
    netease_r_packs[0]["pack_id"] = r_header["uuid"]
    netease_r_packs[0]["version"] = r_header["version"]
    with open(netease_r_path, 'w') as f:
        json.dump(netease_r_packs, f)


