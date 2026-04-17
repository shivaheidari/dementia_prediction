# Dementia Prediction

A machine learning project designed to predict the likelihood of dementia based on clinical and demographic data.

## Prerequisites

Ensure you have the following installed on your system:
- Python 3.8 or higher
- `pip` or `conda` for package management

## Setup and Installation

1. Clone this repository and navigate to the project folder:
   ```bash
   git clone <your-repo-url>
   cd dementia_prediction
   ```

2. Create a virtual environment (highly recommended to avoid dependency conflicts):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## How to Run

### 1. Training the Model
To train the predictive model from scratch using the provided dataset, run:
```bash
python src/train.py
```

### 2. Making Predictions (Inference)
To evaluate the model or run inference on new patient data, execute:
```bash
python src/predict.py --input data/test_data.csv
```

### 3. Exploratory Data Analysis (EDA)
To view the initial data exploration, feature engineering, and model experiments, launch Jupyter:
```bash
jupyter notebook
```
Then, open the notebooks located in the `notebooks/` directory.
