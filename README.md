# OpenNMT-py: Open-Source Neural Machine Translation

This is my "fork" of v1.0.0 of the OpenNMT-py project made to reproduce the training results of the model on the [normalized Im2latex-100k dataset](https://im2markup.yuntiandeng.com/data/) that has been put through [some additional preprocessing](https://github.com/Adi-UA/Open-NMT-1.0.0/blob/main/scripts/download_and_extract_data.py#L64-L97).

[The best model can be found at the this google drive link.](https://drive.google.com/drive/folders/12MvCNaQNJaqK0UfShOrQ-CC3yQlFQAxt?usp=sharing)

## Training

Run the following command to train the model:

```bash
./scripts/train
```

The script will create a conda environment, install the required packages, download the data, preprocess it, and train the model.
