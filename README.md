# Network Security Threat Detection ML Pipeline

A production-grade **Machine Learning pipeline** designed to detect phishing and malicious network activity using structured cybersecurity data. The project follows a **modular MLOps architecture** with automated data ingestion, validation, transformation, and model training.

---

# Overview

This project implements an **end-to-end machine learning workflow** for detecting malicious network traffic and phishing activities.

The pipeline is designed with **artifact-driven architecture**, where every stage generates reusable outputs that are passed to the next stage. This makes the system **reproducible, scalable, and suitable for deployment in production environments**.

---

# Key Features

- Automated **data ingestion from MongoDB**
- **Schema validation** using YAML configuration
- **Data drift detection** using Kolmogorov–Smirnov statistical test
- Modular **feature engineering pipeline**
- Training multiple machine learning models
- Artifact-based **MLOps workflow**
- Reproducible preprocessing and model artifacts
- Web interface support through **Flask application**

---

# Project Architecture

```
MongoDB Database
        │
        ▼
Data Ingestion
        │
        ▼
Data Validation
        │
        ▼
Data Transformation
        │
        ▼
Model Training
        │
        ▼
Model Evaluation
        │
        ▼
Model Artifact + Preprocessing Object
        │
        ▼
Flask API / Web App
```

---

# Project Structure

```
network-security-ml-pipeline/
│
├── artifacts/                     # Generated pipeline artifacts
│
├── config/
│   └── schema.yaml                # Dataset schema definition
│
├── src/
│   └── networksecurity/
│
│       ├── components/            # Core pipeline components
│       │   ├── data_ingestion.py
│       │   ├── data_validation.py
│       │   ├── data_transformation.py
│       │   └── model_trainer.py
│
│       ├── pipeline/
│       │   └── training_pipeline.py
│
│       ├── entity/                # Entity classes
│       │   ├── config_entity.py
│       │   └── artifact_entity.py
│
│       ├── exception/             # Custom exception handling
│
│       ├── logger/                # Logging module
│
│       └── utils/                 # Utility functions
│
├── notebooks/                     # Experiment notebooks
│
├── main.py                        # Training pipeline entry point
│
├── app.py                         # Flask application for inference
│
├── requirements.txt               # Project dependencies
│
├── setup.py                       # Package configuration
│
└── README.md
```

---

# Technologies Used

- Python
- Scikit-learn
- Pandas
- NumPy
- MongoDB
- MLflow
- YAML
- Flask
- MLOps Pipeline Architecture

---

# Machine Learning Models

The following models are trained and evaluated in the pipeline:

- Random Forest
- Gradient Boosting
- Logistic Regression
- AdaBoost
- Decision Tree

The best model is selected automatically based on performance metrics.

---

# Data Processing Pipeline

The transformation pipeline performs:

- Data cleaning
- Missing value handling
- Feature scaling
- Feature encoding
- Data preparation for model training

The preprocessing pipeline is **serialized and saved** to ensure consistent predictions during deployment.

---

# Data Drift Detection

To ensure model reliability, **statistical data drift detection** is implemented using the **Kolmogorov–Smirnov (KS) Test**.

This compares distributions between training and incoming datasets to detect:

- Changes in feature distributions
- Data inconsistencies
- Potential model degradation

---

# Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/network-security-ml-pipeline.git
```

Navigate into the project directory:

```bash
cd network-security-ml-pipeline
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

Mac / Linux

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Running the Training Pipeline

Run the training pipeline:

```bash
python main.py
```

This will execute:

1. Data Ingestion
2. Data Validation
3. Data Transformation
4. Model Training

Artifacts will be generated inside the `artifacts/` directory.

---

# Running the Web Application

To start the Flask application:

```bash
python app.py
```

The application will load the trained model and preprocessing pipeline for inference.

---

# Model Artifacts

The pipeline generates:

- Training dataset
- Testing dataset
- Transformed datasets
- Preprocessing pipeline object
- Trained model
- Evaluation metrics

These artifacts ensure **reproducibility and easy deployment**.

---

# Future Improvements

- Real-time network traffic monitoring
- Streaming data ingestion
- Continuous model retraining
- Docker-based deployment
- Kubernetes scaling

---

# Author

**Madhav Manoj**  
VIT-AP University
