# Imports : Random Forest Model
import numpy as np
from Preprocess import Preprocess
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, ConfusionMatrixDisplay
from sklearn.model_selection import RandomizedSearchCV, train_test_split
from scipy.stats import randint


class Model2(object):
    def __init__(self):
        self.data = None
        self.rand_for = None
        self.acc_score = None
        self.conf_matrix = None

    def create(self, preprocessed_data):
        self.rand_for = RandomForestClassifier()

        self.rand_for.fit(preprocessed_data.train_img, preprocessed_data.train_lbl)
        # predicting for all observations
        self.rand_for.predict(preprocessed_data.test_img)

        # Performance section
        self.acc_score = self.rand_for.score(preprocessed_data.test_img, preprocessed_data.test_lbl)
        # print(self.acc_score)


        #accuracy_score(preprocessed_data.test_img, preprocessed_data.test_lbl)

