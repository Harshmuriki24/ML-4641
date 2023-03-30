import numpy as np
from Preprocess import Preprocess
from sklearn.linear_model import LogisticRegression


class Model(object):
    def __init__(self):
        self.data = None
        self.logreg = None
        self.score = None

    def create(self, preprocessed_data):
        self.logreg = LogisticRegression(solver="lbfgs")
        self.logreg.fit(preprocessed_data.train_img, preprocessed_data.train_lbl)
        # predicting for all observations
        self.logreg.predict(preprocessed_data.test_img)

        #plot prediction?

        # Performance section
        self.score = self.logreg.score(preprocessed_data.test_img, preprocessed_data.test_lbl)
