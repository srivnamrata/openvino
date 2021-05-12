#!/usr/bin/env python3
import subprocess
import sys
from pathlib import Path
import os

pythonpath = sys.executable
curdir = Path(__file__).parent.resolve()
parentdir = curdir.parent

# If openvino_env is already activated, launch jupyter lab
# This will also start if openvino_env_2 is activated instead of openvino_env
# The assumption is that that is usually intended
if "openvino_env" in pythonpath:
    subprocess.run([pythonpath, "-m", "jupyterlab", "notebooks"])
else:
    if sys.platform == "win32":
        scripts_dir = "Scripts"
    else:
        scripts_dir = "bin"

    # If openvino_env is not activated, search for the openvino_env folder in the
    # current and parent directory and launch the notebooks
    try:
        pythonpath = os.path.normpath(os.path.join(curdir, f"openvino_env/{scripts_dir}/python"))
        subprocess.run([pythonpath, "-m", "jupyterlab", "notebooks"])
    except:
        try:
            pythonpath = os.path.normpath(os.path.join(parentdir, f"openvino_env/{scripts_dir}/python"))
            subprocess.run([pythonpath, "-m", "jupyterlab", "notebooks"])
        except:
            pythonpath = str(Path(f"../openvino_env/{scripts_dir}/python"))
            print(pythonpath)
            print(
                "openvino_env could not be found. Please activate the openvino_env virtual "
                "environment manually and try again."
            )

