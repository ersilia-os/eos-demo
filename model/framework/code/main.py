import csv
import sys
import os
import numpy as np
import joblib

from rdkit import Chem
from rdkit.Chem import rdFingerprintGenerator


ROOT = os.path.dirname(os.path.abspath(__file__))

infile = sys.argv[1]
outfile = sys.argv[2]

with open(infile, "r") as f:
    reader = csv.reader(f)
    next(reader)
    smiles = []
    for r in reader:
        smiles += [r[0]]

# calculate morgan fingerprintsss
RADIUS = 3
NBITS = 2048
mfpgen = rdFingerprintGenerator.GetMorganGenerator(radius=RADIUS,fpSize=NBITS)

def clip_sparse(vect, nbits):
    l = [0] * nbits
    for i, v in vect.GetNonzeroElements().items():
        l[i] = v if v < 255 else 255
    return l
    
def morganfp(mol):
    v = mfpgen.GetCountFingerprint(mol)
    return clip_sparse(v, NBITS)

X = np.zeros((len(smiles), NBITS), dtype=np.int8)
for i, smi in enumerate(smiles):
    mol = Chem.MolFromSmiles(smi)
    if mol is None:
        continue
    fp = np.array(morganfp(mol), dtype=np.int8)
    X[i] = fp

# run maip predictions
model = joblib.load(os.path.join(ROOT, "..", "..", "checkpoints", "random_forest.joblib"))

preds = model.predict(X)

# write output
with open(outfile, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["score"])
    for p in preds:
        writer.writerow([p])
