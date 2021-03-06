import os
import yaml

fp_config = os.getcwd() + "/package_upgrade/upgrade.yml"


def _import_config():
    with open(fp_config) as f:
        config = yaml.safe_load(f)
    return config


config = _import_config()
