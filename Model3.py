import numpy as np
from Preprocess import Preprocess
import pandas as pd
import itertools
from sklearn.cluster import KMeans
from sklearn.metrics import davies_bouldin_score, silhouette_score
from scipy.spatial.distance import cdist
import seaborn as sns
import matplotlib.pyplot as plt

class Model3(object):
    def __init__(self):
        self.data = None
        self.kmeans = None
        self.score = None

    def create(self, preprocessed_data):

        # Use Elbow Method to determine optimal number of clusters
        self.kmeans = KMeans(n_clusters=5)
        self.data = preprocessed_data.data
        # Elbow Method

        def elbow(data, cluster):
            wcss = []
            for clus in range(1, cluster + 1):
                kmeans = KMeans(n_clusters=clus, init='k-means++', random_state=0)
                temp = np.nan_to_num(np.array(data).reshape(-1,1), copy=True, nan=0.0, posinf=None, neginf=None)
                kmeans.fit(data)
                wcss.append(kmeans.inertia_)
            plt.xlabel('Number of Clusters')
            plt.ylabel('Distortion')
            sns.lineplot(x=list(range(1, cluster + 1)), y=wcss).set(title='Elbow Method')
        elbow(self.data, 15)
        #self.kmeans.predict(preprocessed_data)
        # predicting for all observations
        #train_lbl_prediction = self.rand_for.predict(preprocessed_data.test_img)
        self.kmeans.fit(preprocessed_data.train_img, preprocessed_data.train_lbl)
        self.kmeans.predict(preprocessed_data.test_img)
        # Performance section
        self.score = self.kmeans.score(preprocessed_data.test_img, preprocessed_data.test_lbl)