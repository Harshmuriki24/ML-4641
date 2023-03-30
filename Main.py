from Preprocess import Preprocess
from Model import Model
from Model2 import Model2
from Model3 import Model3
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def main():
    url = 'higher-education-predictors-of-student-retention/dataset.csv'
    preprocessed_data = Preprocess(url)

    train_before = preprocessed_data.train_img.shape[0]
    test_before = preprocessed_data.test_img.shape[0]

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


    sns.set_theme()
    unfiltered = pd.read_csv(url)
    sns.relplot(data=unfiltered).set(title='Unfiltered Data')
    plt.show()

    train_after = preprocessed_data.train_img.shape[0]
    test_after = preprocessed_data.test_img.shape[0]

    xlabels = ["Train Image Before", "Test Image Before", "Train Image After", "Test Image After"]
    ylabels = [train_before, test_before, train_after, test_after]
    dataf = pd.DataFrame({" ":xlabels, "Size":ylabels})
    sns.barplot(x = " ", y = "Size", data=dataf).set(title='Size of Image before and after PCA')
    plt.show()

if __name__ == '__main__':
    main()
