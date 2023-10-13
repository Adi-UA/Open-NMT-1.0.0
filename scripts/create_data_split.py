import os

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_dir = os.path.join(project_dir, "dataset/data")
images_dir = os.path.join(data_dir, "formula_images_processed")

# Read the list of formulas
with open(os.path.join(data_dir, "im2latex_formulas.final.lst"), "r") as f:
    formulas = [formula.rstrip() for formula in f.readlines()]

splits = ["train", "validate", "test"]
for split in splits:
    print(f"Processing {split} split...")
    with open(os.path.join(data_dir, f"im2latex_{split}_filter.lst"), "r") as f:
        split_info = f.readlines()
        img_names, line_nos = [line.split()[0] for line in split_info], [
            int(line.split()[1]) for line in split_info
        ]

    split_formulas = [formulas[line_no] for line_no in line_nos]
    print(f"Number of formulas in {split} split: {len(split_formulas)}")

    with open(os.path.join(data_dir, f"tgt-{split}.txt"), "w") as f:
        f.write("\n".join(split_formulas))
        f.write("\n")

    with open(os.path.join(data_dir, f"src-{split}.txt"), "w") as f:
        f.write("\n".join(img_names))
        f.write("\n")

    print(f"Done with {split} split.")
