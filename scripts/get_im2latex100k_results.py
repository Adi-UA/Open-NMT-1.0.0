import os

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_dir = os.path.join(project_dir, "dataset/data")

with open(os.path.join(data_dir, "tgt-test.txt"), "r") as f:
    train_formulae = [formula.rstrip() for formula in f.readlines()]

with open(os.path.join(data_dir, "src-train.txt"), "r") as f:
    train_img_names = [img_name.rstrip().rstrip(".png") for img_name in f.readlines()]

with open(os.path.join(project_dir, "pred.txt"), "r") as f:
    pred_formulae = [formula.rstrip() for formula in f.readlines()]

print(len(train_formulae), len(train_img_names), len(pred_formulae))

results = {}
