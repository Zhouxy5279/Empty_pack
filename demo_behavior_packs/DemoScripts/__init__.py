import logging
import shutil
import sys
import os
import time

from DemoScripts import regi


def make_logger():
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter('[%(asctime)s] [%(levelname)s][TEST]{}: %(message)s{}'.
                                           format('\033[32m[AdvLOG]', '\033[0m')))
    log = logging.getLogger('Development')
    log.addHandler(handler)
    log.propagate = False
    log.setLevel(logging.INFO)
    return log


logger = make_logger()

if __name__ == "__main__":
    mods = regi.get_mods()
    for mod_name in mods:
        beh_path = mods[mod_name][1]
        b_target = os.path.join(regi.WorldPath, "behavior_packs", mod_name)
        if os.path.exists(b_target):
            shutil.rmtree(b_target)
        shutil.copytree(beh_path, b_target)

        res_path = mods[mod_name][2]
        r_target = os.path.join(regi.WorldPath, "resource_packs", mod_name)
        if os.path.exists(r_target):
            shutil.rmtree(r_target)
        shutil.copytree(res_path, r_target)
    os.system(regi.LauncherPath)
