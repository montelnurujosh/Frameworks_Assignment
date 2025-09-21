# 🦠 CORD-19 Research Data Explorer

This project provides a **basic analysis** of the CORD-19 metadata dataset and a **Streamlit web app** to visualize insights about COVID-19 research papers.  
It was created as part of the **Frameworks Assignment**.

---

## 📌 Assignment Overview

The project demonstrates:

- ✅ Loading and exploring a real dataset  
- ✅ Data cleaning and preparation  
- ✅ Generating visualizations  
- ✅ Building an interactive Streamlit app  
- ✅ Presenting insights effectively  

---

## 📂 Dataset Information

The dataset used is **`metadata.csv`** from the [CORD-19 Research Challenge](https://www.kaggle.com/datasets/allen-institute-for-ai/cord-19-research-challenge).  

It contains details about COVID-19 research papers, including:
- Paper titles & abstracts  
- Publication dates  
- Authors and journals  
- Source information  

⚠️ Since the full dataset is very large (18GB+), a **sample (`metadata_sample.csv`)** is used in this project for easier analysis and deployment.

---

## 🛠️ Tools & Libraries

- Python 3.7+  
- pandas  
- matplotlib  
- seaborn  
- wordcloud  
- streamlit  

---

## 📖 Project Structure

Frameworks_Assignment/
│── app.py # Streamlit application
│── create_sample.py # Script to generate a smaller dataset
│── metadata_clean.csv # Cleaned dataset
│── metadata_sample.csv # Sample dataset (for sharing/deployment)
│── part1_exploration.py # Data exploration
│── part2_cleaning.py # Data cleaning
│── requirements.txt # Dependencies
│── README.md # Documentation


📊 Features

📈 Publications over time – bar chart of paper counts by year

🏛 Top journals – ranking of publishing journals

☁️ Word cloud – most frequent terms in paper titles

🎛 Interactive filtering – filter papers by year range

📂 Data preview – sample of the dataset

🚀 Live Demo

👉 Click here to view the deployed Streamlit app

(Replace with your actual Streamlit Cloud link after deployment)

📝 Evaluation Criteria

Complete implementation (40%) – all tasks completed

Code quality (30%) – clear, commented, structured code

Visualizations (20%) – meaningful, easy to interpret

Streamlit app (10%) – functional, interactive application

✨ Author

Student: Joshua Nuru

Course: Frameworks Assignment
