import Preprocess
import Model


def Main():
    url = 'higher-education-predictors-of-student-retention/dataset.csv'
    preprocessed_data = Preprocess(url)
    preprocessed_data.clean_data()

    model = Model()
    model.create(preprocessed_data)

    #######THIS IS THE LOGISTIC REGRESSION MODEL############
    regression_model = model.logreg
    #######USE THIS FILE TO CREATE AND PLOT IMAGES##########
