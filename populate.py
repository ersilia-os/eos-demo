import sys
import os
import shutil
import json

root_dir = os.path.dirname(os.path.abspath(__file__))
model_dir = os.path.abspath(sys.argv[1])
print("Completing for demo purposes: {0}".format(model_dir))

shutil.rmtree(os.path.join(model_dir, "model"))
shutil.copytree(os.path.join(root_dir, "model"), os.path.join(model_dir, "model"))
shutil.copy(os.path.join(root_dir, "Dockerfile"), os.path.join(model_dir, "Dockerfile"))

metadata_json = os.path.join(os.path.join(model_dir, "metadata.json"))

with open(metadata_json, "r") as f:
    metadata = json.load(f)

metadata["Mode"] = "Retrained"
metadata["Task"] = ["Classification"]
metadata["Input"] = ["Compound"]
metadata["Input Shape"] = "Single"
metadata["Output"] = ["Score"]
metadata["Output Type"] = ["Float"]
metadata["Output Shape"] = "Single"
metadata["Interpretation"] = "Classification score"

with open(metadata_json, "w") as f:
    json.dump(metadata, f, indent=4)
