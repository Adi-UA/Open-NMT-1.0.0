# OpenNMT-py: Open-Source Neural Machine Translation

This is my "fork" of [OpenNMT-py v1.2.0](https://github.com/OpenNMT/OpenNMT-py/tree/v1.2.0) (aka the version that still had image input). The goal of this repository is to reproduce the training results of OpenNMT's im2markup model on the [normalized Im2latex-100k dataset](https://im2markup.yuntiandeng.com/data/) that has been put through [some additional preprocessing](https://github.com/Adi-UA/Open-NMT-1.2.0/blob/main/scripts/download_and_extract_data.py#L64-L90).

[The best model checkpoint can be found in google drive.](https://drive.google.com/drive/folders/12MvCNaQNJaqK0UfShOrQ-CC3yQlFQAxt?usp=sharing).

## Testing

1. Create a virtual environment or a conda environment and install th required packages (or the training script would have done it for you):

   ```bash
   python3 -m venv venv && \
   pip3 install  -r requirements.txt && \
   source ./venv/bin/activate # or .\venv\Scripts\activate on Windows
   ```

2. Then, download and place the [best model checkpoint](https://drive.google.com/drive/folders/12MvCNaQNJaqK0UfShOrQ-CC3yQlFQAxt?usp=sharing) in the `model` directory.

3. Create the [test files as required based on the original repo's documentation](https://github.com/OpenNMT/OpenNMT-py/blob/v1.2.0/docs/source/im2text.md). Or if you ran training, the test files for our image2latex100k dataset should already exist in the `dataset/data` directory.

4. Run `./scripts/test` after modifying the paths to the input files or other options as needed.

## Training

Run:

```bash
./script/train
```

This will download the dataset, preprocess it, and train the model. The model checkpoints will be saved in the project directory. To change any of the configurations, inspect the `onmt/opts.py` file and update the `./scripts/train` script accordingly. The parameters passed in the training script are the ones I used to train the best model.

## Results

The results of our best model on the test set have been saved to the `results` directory. It was created with the following commands:

1. Create a virtual environment or a conda environment and install th required packages (or the training script would have done it for you):

   ```bash
   python3 -m venv venv && \
   pip3 install  -r requirements.txt && \
   source ./venv/bin/activate # or .\venv\Scripts\activate on Windows
   ```

2. Then, download and place the [best model checkpoint](https://drive.google.com/drive/folders/12MvCNaQNJaqK0UfShOrQ-CC3yQlFQAxt?usp=sharing) in the `model` directory.

3. Run the test script:
   ```bash
   ./scripts/test
   ```

This will create `pred.txt` with the predictions on each newline in the order they were input. You can stop here if you don't need these in JSON format.

4. Run the results script to collect the results in the JSON file.
   ```bash
   python3 scripts/get_im2latex100k_results.py
   ```

Everything else is the same as in the original repo.
