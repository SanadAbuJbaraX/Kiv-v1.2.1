import os
path = input("path for KIV_MODULES (leave empty for default): ")
if path == "":
    path = __file__.removesuffix("setup.py") + "modules\\"
    os.environ["KIV_MODULES"] = path
    print(os.getenv("KIV_MODULES"))