import json
import os

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_dir = os.path.join(project_dir, "dataset/data")

with open(os.path.join(data_dir, "tgt-test.txt"), "r") as f:
    train_formulae = [formula.rstrip() for formula in f.readlines()]

with open(os.path.join(data_dir, "src-test.txt"), "r") as f:
    train_img_names = [img_name.rstrip().rstrip(".png") for img_name in f.readlines()]

with open(os.path.join(project_dir, "pred.txt"), "r") as f:
    pred_formulae = [formula.rstrip() for formula in f.readlines()]


results = {}
for img_name, formula, pred_formula in zip(
    train_img_names, train_formulae, pred_formulae
):
    results[img_name] = {
        "prediction": pred_formula,
        "ground_truth": formula,
    }

# Create results directory if it doesn't exist
if not os.path.exists(os.path.join(project_dir, "results")):
    os.mkdir(os.path.join(project_dir, "results"))

results_dir = os.path.join(project_dir, "results")

# Save results
with open(os.path.join(results_dir, "im2latex100k_test_results.json"), "w") as f:
    json.dump(results, f, indent=4)
