# Finding My Closest Friends Using K-Nearest Neighbours (KNN)

## 📌 Project Overview

This project applies the **K-Nearest Neighbours (KNN)** algorithm to identify participants whose questionnaire responses are most similar to mine.

The similarity between participants was measured using **Euclidean distance**.

The project demonstrates how a machine learning technique can be applied to a simple real-world relationship-matching problem using questionnaire data.

---

## 🎯 Objective

The objective of this project was to:

- Identify participants with response patterns most similar to mine.
- Rank participants according to their Euclidean distance.
- Explore relationships between questionnaire responses.
- Visualize similarities and patterns within the dataset.
- Apply additional machine learning techniques to explore participant groupings.

---

## 📊 Dataset

The dataset was collected using **Google Forms**.

- **Participants:** 19
- **Questions:** 11
- **Response scale:** 1–3
- **Dataset:** `kNN Project.xlsx`

The questionnaire responses were used as the features for the analysis.

---

## 🛠️ Technologies & Libraries

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- NetworkX
- Excel

---

## 🔬 Methodology

The project followed these steps:

1. Collect questionnaire responses using Google Forms.
2. Import the dataset using Pandas.
3. Select the questionnaire features.
4. Build a KNN model using Euclidean distance.
5. Calculate the distance between my responses and other participants.
6. Rank participants based on similarity.
7. Visualize the results.
8. Apply PCA and K-Means clustering to explore additional patterns.

---

## 🤖 KNN Implementation

The KNN analysis used the `NearestNeighbors` algorithm from Scikit-learn with **Euclidean distance**.



## 📈 Visualizations and Interpretation

### 1. Euclidean Distance Bar Chart

The Euclidean distance bar chart ranks participants according to how similar their questionnaire responses are to mine.

**Interpretation:**

Shorter bars indicate smaller Euclidean distances and therefore greater similarity between my responses and those of the participant. Taller bars indicate greater distance and less similarity.

The visualization helped identify the participant with the closest response pattern to mine.

---

### 2. Friendship Network Graph

The friendship network graph visualizes the relationship between my responses and those of the other participants.

**Interpretation:**

The graph represents different levels of similarity between participants. The colours represent similarity levels, while the numbers displayed on the connecting lines represent the Euclidean distance between participants.

A smaller distance indicates a stronger similarity between response patterns.

---

### 3. Correlation Heatmap

The correlation heatmap shows the relationships between the 11 questionnaire questions.

**Interpretation:**

The heatmap helps identify how strongly the questionnaire questions relate to one another.

Stronger positive relationships indicate that two questions tend to have similar response patterns, while weaker or negative relationships indicate less similar patterns.

---

### 4. PCA Visualization

Principal Component Analysis (PCA) was used to reduce the 11 questionnaire responses into two dimensions.

**Interpretation:**

The PCA visualization provides a simplified view of the participants based on their response patterns.

Participants positioned closer together have more similar response patterns, while participants farther apart are less similar.

This visualization helped reveal natural spatial groupings within the dataset.

---

### 5. K-Means Clustering

K-Means clustering was used to group participants into three clusters based on their questionnaire responses.

**Interpretation:**

Participants belonging to the same cluster share similar characteristics based on their responses.

The visualization makes it easier to observe how participants naturally group together according to their questionnaire response patterns.

## 🔎 Key Findings

The KNN analysis and supporting visualizations produced the following key findings:

- **Obiwuru had the smallest Euclidean distance** and was identified as the closest match based on the questionnaire responses.
- Participants with **smaller Euclidean distances** had more similar response patterns to mine.
- **PCA revealed natural spatial groupings** among the participants based on their questionnaire responses.
- **K-Means clustering grouped the participants into three clusters**, showing that participants could be segmented according to similarities in their responses.
- The **friendship network graph visually represented participant similarity**, making the relationships between response patterns easier to understand.
- The **correlation heatmap** provided insight into the relationships between the different questionnaire questions.

### Overall Insight

The project demonstrated that KNN and Euclidean distance can be used to identify participants with similar response patterns, while PCA, K-Means clustering, correlation analysis and network visualization provided additional perspectives on the structure and relationships within the dataset.

👩🏿‍💻 Author
Oluwaseyi Obarayo
Data Analyst | Business Intelligence | Data & Machine Learning
