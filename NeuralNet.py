# Import required libraries
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.model_selection import train_test_split
import sklearn
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression

class NeuralNet:
    def main():
        # Define input data
        url = 'higher-education-predictors-of-student-retention/dataset.csv'
        sns.set_theme()
        data = pd.read_csv(url)

        # My intuition is that it might be hard to print 34 features so we might need to eliminate some.
        # If we do need to I'm not sure how we will do that. The bar graph also doesn't name the feature at least
        # on the website example so we should probably add labels to the graph

        # X, y = make_regression(n_samples=1000, n_features=10, n_informative=5, random_state=1) example
        X, y = make_regression(n_samples=4424, n_features=34, n_informative=5, random_state=1)
        model = LinearRegression()
        model.fit(X, y)
        importance = model.coef_
        scores = []
        
        for i,v in enumerate(importance):
            print('Feature: %0d, Score: %.5f' % (i,v))
            scores.append(i)


        features = data.iloc[1, :].values #get all of the names

        # xlabels = features
        # ylabels = scores
        # dataf = pd.DataFrame({" ": xlabels, "Importance": ylabels})
        # sns.barplot(x=" ", y="Importance", data=dataf).set(
        #     title='Feature Importance')
        # plt.show()
        
        # plt.bar([x for x in range(len(importance))], importance)
        # plt.show()










        

        # X = data.iloc[:, :-1].values
        # Y = data.iloc[:, -1].values

        # Y = np.where(Y == 'Dropout', 0, 1)

        # X_train, X_test, y_train, y_test = train_test_split(
        #     X, Y, test_size=0.3, random_state=42)

        # Define the model architecture

        # dim = [5, 10, 20, 34]
        """
        num_epocs = [1, 5, 10, 15]
        accuracy_arr = []

        for i in range(len(num_epocs)):

            X = data.iloc[:, :-1].values
            Y = data.iloc[:, -1].values

            Y_mono = np.where(Y == 'Dropout', 0, 1)

            X_train, X_test, y_train, y_test = train_test_split(
                X, Y_mono, test_size=0.3, random_state=42)

            model = Sequential()
            model.add(Dense(4, input_dim=34, activation='relu'))
            model.add(Dense(1, activation='sigmoid'))

            # Compile the model
            model.compile(loss='binary_crossentropy',
                          optimizer='adam', metrics=['accuracy'])

            # Train the model
            model.fit(X_train, y_train, epochs=num_epocs[i], batch_size=4)

            # Get the accuracy
            _, accuracy = model.evaluate(X_test, y_test)

            accuracy_arr.append(accuracy)
        """
        # Test the model
        # course = data['Course']
        # gender = data['Gender']
        # age_enrollement = data['Age at enrollment']
        # nationality = data['Nacionality']
        # father_occupation = data['Father`s occupation']
        # Scholarship = data['Scholarship holder']

        # test_data = np.array([course, gender, age_enrollement,
        #                      nationality, Scholarship])

        # test_data = np.random.choice(4424, size = (30,4424))

        # print("shape:", test_data.shape)

        # predictions = model.predict(X_test)

        # actual = Y
        # accuracy = actual/(predictions + actual)

        # five_epoch_accuracy = None
        # ten_epoch_accuracy = accuracy
        # twenty_epoch_accuracy = None
        # fifty_epoch_accuracy = None
        """print("Accuracy:", accuracy_arr)
        five_feature_accuracy, ten_feature_accuracy, twenty_feature_accuracy, thirtyfour_feature_accuracy = accuracy_arr"""

        # Accuracy vs Epochs plot
        # xlabels = ["5 Epochs", "10 Epochs", "20 Epochs", "50 Epochs"]
        # ylabels = [five_epoch_accuracy, ten_epoch_accuracy, twenty_epoch_accuracy, fifty_epoch_accuracy]
        # dataf = pd.DataFrame({" ":xlabels, "Accuracy":ylabels})
        # sns.barplot(x = " ", y = "Accuracy", data=dataf).set(title='Accuracy versus Number of Epochs')
        # plt.show()

        # Accuracy vs Number of Features plot

        """xlabels = ["1 epoch", "5 epochs", "10 epochs", "15 epochs"]
        ylabels = [five_feature_accuracy, ten_feature_accuracy,
                   twenty_feature_accuracy, thirtyfour_feature_accuracy]
        dataf = pd.DataFrame({" ": xlabels, "Accuracy": ylabels})
        sns.barplot(x=" ", y="Accuracy", data=dataf).set(
            title='Accuracy versus Number of Epochs')
        plt.show()"""

    if __name__ == '__main__':
        main()
