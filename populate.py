import sys
import os
import shutil
import json
import yaml

root_dir = os.path.dirname(os.path.abspath(__file__))
model_dir = os.path.abspath(sys.argv[1])
print("Completing for demo purposes: {0}".format(model_dir))

shutil.rmtree(os.path.join(model_dir, "model"))
shutil.copytree(os.path.join(root_dir, "model"), os.path.join(model_dir, "model"))
shutil.copy(os.path.join(root_dir, "install.yml"), os.path.join(model_dir, "install.yml"))

metadata_yaml = os.path.join(os.path.join(model_dir, "metadata.yml"))

with open(metadata_yaml, "r") as f:
    metadata = yaml.safe_load(f)

metadata["Mode"] = "Retrained"
metadata["Task"] = ["Classification"]
metadata["Input"] = ["Compound"]
metadata["Input Shape"] = "Single"
metadata["Output"] = ["Score"]
metadata["Output Type"] = ["Float"]
metadata["Output Shape"] = "Single"
metadata["Interpretation"] = "Classification score"

with open(metadata_yaml, "w") as f:
    yaml.dump(metadata, f, default_flow_style=False, sort_keys=False)
