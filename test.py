import os

path="notebooks/research.ipynb"

dir,filename = os.path.split(path)

os.makedirs(dir,exist_ok=True)

with open(path,"w") as f:
    pass

