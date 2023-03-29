from Preprocess import Preprocess
from Model import Model
from Model2 import Model2
from Model3 import Model3


def main():
    url = 'higher-education-predictors-of-student-retention/dataset.csv'
    preprocessed_data = Preprocess(url)
    preprocessed_data.clean_data()

    model = Model()
    model.create(preprocessed_data)

    #######THIS IS THE LOGISTIC REGRESSION MODEL############
    regression_model = model.logreg
    #######USE THIS FILE TO CREATE AND PLOT IMAGES##########

    model2 = Model2()
    model2.create(preprocessed_data)
    #######THIS IS THE RANDOM FOREST MODEL############
    randomforest_model = model2.rand_for
    # https://www.analyticsvidhya.com/blog/2021/06/understanding-random-forest/
    # https://www.datacamp.com/tutorial/random-forests-classifier-python
    # https://www.blopig.com/blog/2017/07/using-random-forests-in-python-with-scikit-learn/
    #######USE THIS FILE TO CREATE AND PLOT IMAGES##########

    model3 = Model3()
    model3.create(preprocessed_data)
    #######THIS IS THE KMEANS MODEL############
    kmeans_model = model3.kmeans
    #######USE THIS FILE TO CREATE AND PLOT IMAGES##########
