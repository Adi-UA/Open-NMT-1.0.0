# OpenNMT-py: Open-Source Neural Machine Translation

[![GitHub License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/Python-3.8-brightgreen)](https://www.python.org/downloads/release/python-380/)
[![Conda Version](https://img.shields.io/badge/Miniconda-Latest-red)](https://docs.conda.io/en/latest/miniconda.html)

This is my "fork" of [OpenNMT-py v1.2.0](https://github.com/OpenNMT/OpenNMT-py/tree/v1.2.0) (aka the version that still had image input). The goal of this repository is to reproduce the training results of OpenNMT's im2markup model on the [normalized Im2latex-100k dataset](https://im2markup.yuntiandeng.com/data/) that has been put through [some additional preprocessing](https://github.com/Adi-UA/Open-NMT-1.2.0/blob/main/scripts/download_and_extract_data.py#L64-L90).

[The best model checkpoint can be found in google drive.](https://drive.google.com/drive/folders/12MvCNaQNJaqK0UfShOrQ-CC3yQlFQAxt?usp=sharing).

## How To Use

### Prerequisites

Miniconda: https://docs.conda.io/en/latest/miniconda.html

### Setup

Clone the repository to your computer and position your command line inside the repository folder:

```
git clone https://github.com/Adi-UA/Open-NMT-1.2.0.git
cd Open-NMT-1.2.0
```

Assuming you have Miniconda installed, run the following command to install the required packages:

```
./scripts/install
```

The install script will create and install the required packages in a virtual environment named `opennmt` that uses Python 3.8. This will automatically be reused by the training and testing scripts.

### Testing

1. Download and place the [best model checkpoint](https://drive.google.com/drive/folders/12MvCNaQNJaqK0UfShOrQ-CC3yQlFQAxt?usp=sharing) in the `model` directory.

2. Create the [test files in the format described here](./docs//source/im2text.md). Or if you ran training, the test files for our image2latex100k dataset should already exist in the `dataset/data` directory.

3. Run `./scripts/test` after modifying the paths to the input files or other options as needed.

### Training

Run:

```bash
./script/train
```

This will download the dataset, preprocess it, and train the model. The model checkpoints will be saved in the project directory. To change any of the configurations, inspect the `onmt/opts.py` file and update the `./scripts/train` script accordingly. The parameters passed in the training script are the ones I used to train the best model.

### Results

The results of our best model on the test set have been saved to the `results` directory. It was created with the following commands:

1. Activate the conda environment

   ```bash
   conda activate opennmt
   ```

2. Then, download and place the [best model checkpoint](https://drive.google.com/drive/folders/12MvCNaQNJaqK0UfShOrQ-CC3yQlFQAxt?usp=sharing) in the `model` directory.

3. Run the test script:

   ```bash
   ./scripts/test
   ```

4. Run the results script to collect the results in the JSON file from the `pred.txt` file:
   ```bash
   python3 scripts/get_im2latex100k_results.py
   ```
