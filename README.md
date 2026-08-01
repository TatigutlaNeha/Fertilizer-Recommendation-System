# 🌱 Fertilizer Recommendation System

A Machine Learning web application that recommends the most suitable fertilizer based on soil nutrients and environmental conditions.

The model is trained using a Decision Tree Classifier and deployed as an interactive web application using Streamlit.

---

## 🚀 Live Demo

🔗 **Try the app:**
https://fertilizer-recommendation-system-tatigutla-neha.streamlit.app/

---

## 📌 Features

* Predicts the best fertilizer based on soil nutrients
* Interactive web interface built with Streamlit
* Uses Machine Learning for accurate recommendations
* Simple and user-friendly UI
* Real-time fertilizer prediction

---

## 🧠 Machine Learning Model

The model was trained using:

* **Algorithm:** Decision Tree Classifier
* **Libraries:** scikit-learn, pandas
* **Encoding:** LabelEncoder for categorical features

### Input Features

* Temperature
* Moisture
* Rainfall
* Soil pH
* Nitrogen
* Phosphorous
* Potassium
* Carbon
* Soil Type
* Crop Type

### Output

* Recommended Fertilizer

---

## 🛠 Tech Stack

* Python
* Streamlit
* Pandas
* Scikit-learn
* Pickle
* Git & GitHub

---

## 📂 Project Structure

```
Fertilizer_Recommendation_System
│
├── app.py
├── train_model.py
├── model.pkl
├── fertilizer_encoder.pkl
├── requirements.txt
├── README.md
```

---

## ⚙️ Installation & Running Locally

### Clone the repository

```
git clone https://github.com/TatigutlaNeha/Fertilizer-Recommendation-System
```

### Navigate to project folder

```
cd Fertilizer_Recommendation_System
```

### Install dependencies

```
pip install -r requirements.txt
```

### Run the Streamlit app

```
streamlit run app.py
```

---

## 📊 Model Training

To retrain the model:

```
python train_model.py
```

This will generate:

* `model.pkl`
* `fertilizer_encoder.pkl`

---

## 👩‍💻 Author

**Tatigutla Neha**

GitHub:
https://github.com/TatigutlaNeha

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
