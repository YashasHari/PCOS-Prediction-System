# 🧬 PCOS Prediction System

This project is a comprehensive machine learning–based application developed for the prediction of Polycystic Ovary Syndrome (PCOS). It includes both a web-based interface (using Flask) and a desktop-based GUI (using Tkinter) for flexible user interaction.

---

## 📌 Project Overview

The system enables healthcare researchers or users to input clinical and physiological data and receive predictions for PCOS. It integrates several machine learning models, supports multiple datasets, and provides both visualization and comparative analysis of model performance.

---

## 🧠 Core Capabilities

* Prediction of PCOS from medical data
* Integration of multiple machine learning models:

  * Logistic Regression
  * Random Forest
  * Decision Tree
  * AdaBoost
  * Gradient Boosting
  * LightGBM
  * Multi-layer Perceptron (MLP)
  * K-Nearest Neighbors (KNN)
  * Voting Classifier (Ensemble)
* Model evaluation with metrics:

  * Accuracy, Precision, Recall
  * Confusion Matrix
  * Mean Absolute Error, RMSE, R² Score
* Web and desktop interfaces
* Real-time visual analytics
* Preprocessing and data cleaning

---

## 🧱 System Architecture

```
                    +---------------------------+
                    |   PCOS Dataset (.csv, .xlsx) |
                    +------------+--------------+
                                 |
                                 v
+----------------+     +----------------+     +------------------+
|  Preprocessing  | --> | Feature Selection | --> | Train/Test Split |
+----------------+     +----------------+     +------------------+
                                 |
                                 v
               +----------------------------------------+
               |     Multiple ML Model Implementations   |
               |  (RF, LR, KNN, GB, LGBM, AdaBoost, etc.)|
               +----------------+------------------------+
                                |
                                v
             +-------------------------------------------+
             |   Comparative Evaluation & Voting Classifier |
             +----------------+----------------------------+
                                |
                 +-------------+-------------+
                 |                           |
     +-----------v--------+      +-----------v----------+
     |   Web Interface     |      |   GUI (Tkinter App)  |
     |   (Flask + HTML)    |      |   (Main.py)          |
     +---------------------+      +----------------------+
```

---

## 📂 Folder Structure Overview

```
PCOS/
├── Webapplication/           # Web app (Flask)
│   ├── static/               # CSS, JS, images
│   └── templates/            # HTML templates
│   └── app.py                # Flask app entry
├── results/                  # Output results
├── Main.py                   # Tkinter GUI app
├── preprocess.py             # Data cleaning/preprocessing
├── Logisticregression.py     # Logistic Regression model
├── RF.py                     # Random Forest model
├── DT.py                     # Decision Tree model
├── adaboost.py               # AdaBoost model
├── GB.py                     # Gradient Boosting model
├── LGBM.py                   # LightGBM model
├── MLP.py                    # MLP model
├── KNN.py                    # KNN model
├── votingclassifier.py       # Voting/ensemble logic
├── comparision.py            # Model performance comparison
├── *.csv / *.xlsx            # Input datasets
```

---

## 💻 Technologies Used

### Machine Learning & Analysis

* `scikit-learn`
* `lightgbm`
* `pandas`, `numpy`
* `matplotlib`

### Frontend/UI

* `Flask` + `Jinja2` for web interface
* `Tkinter` for desktop GUI
* `Pillow` for image support

### Backend/Logic

* Modular Python scripts for each model
* Flask-SocketIO (real-time communication)
* SQLite3 (optional for user/session handling)

---

## 📊 Data Formats Supported

* `.csv` (e.g., `PCOS_infertility.csv`)
* `.xlsx` (e.g., `PCOS_data_without_infertility.xlsx`)

---

## 🖼️ Web Application UI

![Home Page](https://github.com/user-attachments/assets/4750adad-32a3-49f9-bf88-9f58b34082e2)

## 📌 Notes

* This system is intended for research, experimentation, and education.
* Easily extensible to include additional models or evaluation metrics.
* Built with modularity in mind: each model and component is in a separate file.
