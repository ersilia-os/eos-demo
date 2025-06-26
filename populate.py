import sys
import os
import shutil
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

metadata["Deployment"] = ["Local"]
metadata["Source"] = "Local"
metadata["Source Type"] = "Replicated"
metadata["Task"] = "Annotation"
metadata["Subtask"] = "Activity prediction"
metadata["Input"] = ["Compound"]
metadata["Input Dimension"] = 1
metadata["Output"] = ["Score"]
metadata["Output Dimension"] = 1
metadata["Output Consistency"] = "Fixed"
metadata["Interpretation"] = "Classification score, higher values indicate higher inhibition potential"
metadata["Biomedical Area"] = ["Malaria"]
metadata["Target Organism"] = ["Plasmodium falciparum"]
metadata["Publication Type"] = "Peer reviewed"
metadata["Publication Year"] = 2025

with open(metadata_yaml, "w") as f:
    yaml.dump(metadata, f, default_flow_style=False, sort_keys=False)
