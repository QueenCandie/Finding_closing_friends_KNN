# ============================================================
# FINDING MY CLOSEST FRIENDS USING K-NEAREST NEIGHBOURS (KNN)
# Machine Learning Project
# ============================================================

# ============================================================
# 1. IMPORT LIBRARIES
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

from sklearn.neighbors import NearestNeighbors
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans


# ============================================================
# 2. LOAD DATASET
# ============================================================

df = pd.read_excel("kNN Project.xlsx")

print("Dataset loaded successfully!")
print("Dataset shape:", df.shape)

print("\nFirst five rows:")
print(df.head())


# ============================================================
# 3. PREPARE QUESTIONNAIRE FEATURES
# ============================================================

# The first two columns contain participant information.
# The questionnaire responses begin from the third column.

X = df.iloc[:, 2:].copy()

print("\nQuestionnaire features:")
print(X.head())


# ============================================================
# 4. BUILD KNN MODEL
# ============================================================

# Euclidean distance is used to measure similarity.

knn = NearestNeighbors(
    n_neighbors=len(df),
    metric="euclidean"
)

knn.fit(X)


# ============================================================
# 5. CALCULATE EUCLIDEAN DISTANCES
# ============================================================

# The first participant represents my responses.

distances, indices = knn.kneighbors(
    X.iloc[[0]]
)


# ============================================================
# 6. CREATE SIMILARITY RANKING
# ============================================================

results = []

for rank, (index, distance) in enumerate(
    zip(indices[0], distances[0]),
    start=1
):

    results.append({
        "Rank": rank,
        "Name": df.iloc[index]["Name"],
        "Euclidean Distance": round(distance, 2)
    })


results_df = pd.DataFrame(results)

print("\nKNN Similarity Ranking:")
print(results_df)


# ============================================================
# 7. IDENTIFY CLOSEST MATCH
# ============================================================

# The first result is the participant being compared with
# themselves, so the second result is the closest other
# participant.

closest_match = results_df.iloc[1]

print("\nClosest Match:")
print(
    f"{closest_match['Name']} "
    f"(Euclidean Distance: "
    f"{closest_match['Euclidean Distance']})"
)


# ============================================================
# 8. EUCLIDEAN DISTANCE BAR CHART
# ============================================================

plt.figure(figsize=(10, 6))

plt.bar(
    results_df["Name"],
    results_df["Euclidean Distance"]
)

plt.xlabel("Participant")
plt.ylabel("Euclidean Distance")
plt.title(
    "Euclidean Distance Between My Responses "
    "and Participants"
)

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()


# ============================================================
# 9. CORRELATION HEATMAP
# ============================================================

questions = df.iloc[:, 2:]

corr = questions.corr()

plt.figure(figsize=(10, 8))

plt.matshow(
    corr,
    cmap="coolwarm",
    fignum=1
)

plt.colorbar()

plt.title(
    "Correlation Heatmap of Questionnaire Responses",
    pad=20
)

plt.show()


# ============================================================
# 10. PRINCIPAL COMPONENT ANALYSIS (PCA)
# ============================================================

pca = PCA(n_components=2)

X_pca = pca.fit_transform(X)

plt.figure(figsize=(8, 6))

plt.scatter(
    X_pca[:, 0],
    X_pca[:, 1]
)

plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("PCA Visualization of Participants")

plt.show()


# ============================================================
# 11. K-MEANS CLUSTERING
# ============================================================

kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

clusters = kmeans.fit_predict(X)

print("\nK-Means Cluster Assignments:")
print(clusters)


# ============================================================
# 12. K-MEANS VISUALIZATION
# ============================================================

plt.figure(figsize=(8, 6))

plt.scatter(
    X_pca[:, 0],
    X_pca[:, 1],
    c=clusters
)

plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("K-Means Clustering of Participants")

plt.show()


# ============================================================
# 13. FRIENDSHIP NETWORK GRAPH
# ============================================================

G = nx.Graph()

# Add all participants as nodes.

for name in df["Name"]:
    G.add_node(name)


# Connect my responses to every other participant.
# The edge weight represents Euclidean distance.

my_name = df.iloc[0]["Name"]

for i in range(1, len(indices[0])):

    participant_index = indices[0][i]

    participant_name = df.iloc[
        participant_index
    ]["Name"]

    distance = distances[0][i]

    G.add_edge(
        my_name,
        participant_name,
        weight=round(distance, 2)
    )


# ============================================================
# 14. DRAW NETWORK GRAPH
# ============================================================

plt.figure(figsize=(10, 8))

pos = nx.spring_layout(
    G,
    seed=42
)

nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=2000,
    font_size=9
)

edge_labels = nx.get_edge_attributes(
    G,
    "weight"
)

nx.draw_networkx_edge_labels(
    G,
    pos,
    edge_labels=edge_labels
)

plt.title(
    "Friendship Network Based on Euclidean Distance"
)

plt.show()


# ============================================================
# 15. SAVE KNN RESULTS
# ============================================================

results_df.to_csv(
    "knn_similarity_results.csv",
    index=False
)

print("\nKNN similarity results saved successfully!")

print("\nProject completed successfully!")
