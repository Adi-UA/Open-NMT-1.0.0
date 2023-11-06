import argparse
import os
import json
from tqdm import tqdm

def save_results(dataset: str, results: dict):
    if not os.path.exists(os.path.join(project_dir, "results")):
        os.mkdir(os.path.join(project_dir, "results"))

    results_dir = os.path.join(project_dir, "results")

    # Save results
    with open(os.path.join(results_dir, f"{dataset}_test_results.json"), "w") as f:
        json.dump(results, f, indent=4)

    print(f"Saved results to {results_dir}.")

def generate_img_paths_file(dataset_dir):
    print("Generating src-test.txt...")
    images = os.listdir(os.path.join(dataset_dir, "images_processed"))
    images.sort(key = lambda x : int(x.split(".")[0]))

    with open(os.path.join(dataset_dir, "src-test.txt"), "w") as f:
        f.write("\n".join(images))

    print("Generated src-test.txt")


def run_predictions(dataset_dir):
    print("Running predictions...")
    os.system(
        f"python3 translate.py -data_type img \
               -model model/model.pt \
               -src_dir {dataset_dir}/images_processed \
               -src {dataset_dir}/src-test.txt \
               -output {dataset_dir}/pred.txt\
               -image_channel_size 1 \
               -max_length 150 \
               -beam_size 5 \
               -batch_size 16 \
               -gpu 0 \
               -verbose"
    )
    print("Finished running predictions")


def consolidate_predictions(dataset_dir):
    print("Consolidating predictions...")
    with open(os.path.join(dataset_dir, "pred.txt")) as f:
        predictions = [line.strip() for line in f.readlines()]

    with open(os.path.join(dataset_dir, "latex.norm.lst")) as f:
        ground_truth = [line.strip() for line in f.readlines()]

    results = {}
    for i, (pred, gt) in tqdm(enumerate(zip(predictions, ground_truth)), total=len(predictions)):
        results[i] = {"prediction": pred, "ground_truth": gt}

    print("Consolidated predictions")

    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--dataset",
        type=str,
        default="physics-10k",
        help="Dataset to use. Defaults to physics-10k.",
    )

    args = parser.parse_args()

    project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dataset_dir = os.path.join(project_dir, args.dataset)
    
    generate_img_paths_file(dataset_dir)

    run_predictions(dataset_dir)

    results = consolidate_predictions(dataset_dir)

    save_results(args.dataset, results)

