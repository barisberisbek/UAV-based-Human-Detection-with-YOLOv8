# YOLOv8-Powered Aerial Human Detection for UAV Search & Rescue

An implementation of a YOLOv8 object detection model, fine-tuned for robust human detection in high-altitude aerial imagery captured by UAVs. This model was trained on a large, custom-aggregated dataset to optimize performance for real-world search and rescue (SAR) operations.

This project was developed by Team Sirius for the **TEKNOFEST** competition.

## About The Project

The primary goal of this project is to provide a fast and reliable system for detecting humans in aerial footage, which can be deployed on a UAV platform to assist in search and rescue missions. By leveraging the speed and accuracy of the YOLOv8 architecture, this model can process video streams to identify potential individuals in challenging environments.

## Getting Started

Follow these steps to set up the project and run the model on your own machine.

### Prerequisites

Make sure you have the following installed on your system:
* Python 3.8+
* Git
* Git LFS (Large File Storage)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/](https://github.com/)<your-username>/<your-repo-name>.git
    cd <your-repo-name>
    ```

2.  **Download the model file:**
    This project uses Git LFS to handle the large model weight file. Pull the file from LFS:
    ```bash
    git lfs pull
    ```

3.  **Install dependencies:**
    Install all the required Python libraries using the `requirements.txt` file.
    ```bash
    pip install -r requirements.txt
    ```

## Usage

You can run inference on a video file using the `predict.py` script from your terminal.

```bash
python predict.py --model best.pt --source sample.mp4
```

* `--model`: Path to the trained `.pt` model file.
* `--source`: Path to the source video file you want to test.

The resulting video, with detections drawn on it, will be saved in a `results/` directory that will be created automatically.

## Model Performance

This model was trained on a custom-aggregated dataset of over 10,000 aerial images. The final performance metrics on our validation set are as follows:

| Metric | Value |
| :--- | :--- |
| Precision | 0.909 |
| Recall | 0.906 |
| mAP50 | 0.949 |
| mAP50-95 | 0.542 |

These strong and balanced metrics indicate high reliability (few false positives) and high sensitivity (few missed detections), making the model suitable for critical SAR applications.
