from Preprocess import Preprocess
from Model import Model
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def main():
    url = 'higher-education-predictors-of-student-retention/dataset.csv'
    preprocessed_data = Preprocess(url)
    preprocessed_data.clean_data()

    model = Model()
    model.create(preprocessed_data)

    #######THIS IS THE LOGISTIC REGRESSION MODEL############
    regression_model = model.logreg
    #######USE THIS FILE TO CREATE AND PLOT IMAGES##########

    sns.set_theme()
    dataset = pd.read_csv(url) # read the unfiltered data

    unfiltered = sns.relplot(
        data=dataset
    ).set(title='Unfiltered Data')

    plt.show() # show the plot


if __name__ == "__main__":
    main()
