import logging
import shutil
import sys
import os
import time

from DemoScripts.regi import projectName, WorldPath, LauncherPath, header


def make_logger():
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter('[%(asctime)s] [%(levelname)s]{}: %(message)s{}'.
                                           format('\033[34m', '\033[0m')))
    log = logging.getLogger('Development')
    log.addHandler(handler)
    log.propagate = False
    log.setLevel(logging.INFO)
    return log


logger = make_logger()

if __name__ == "__main__":
    b_source = "../../" + header + "behavior_packs"
    b_target = os.path.join(WorldPath, "behavior_packs", projectName)
    if os.path.exists(b_target):
        shutil.rmtree(b_target)
    shutil.copytree(b_source, b_target)

    r_source = "../../" + header + "resource_packs"
    r_target = os.path.join(WorldPath, "resource_packs", projectName)
    if os.path.exists(r_target):
        shutil.rmtree(r_target)
    shutil.copytree(r_source, r_target)

    os.system(LauncherPath)