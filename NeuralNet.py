# Import required libraries
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.model_selection import train_test_split


class NeuralNet:
    def main():
        # Define input data
        url = 'higher-education-predictors-of-student-retention/dataset.csv'
        sns.set_theme()
        data = pd.read_csv(url)

        X = data.iloc[:, :-1].values
        Y = data.iloc[:, -1].values

        Y = np.where(Y == 'Dropout', 0, 1)

        X_train, X_test, y_train, y_test = train_test_split(
            X, Y, test_size=0.3, random_state=42)

        # print()

        # Define the model architecture
        model = Sequential()
        model.add(Dense(4, input_dim=34, activation='relu'))
        model.add(Dense(1, activation='sigmoid'))

        # Compile the model
        model.compile(loss='binary_crossentropy',
                      optimizer='adam', metrics=['accuracy'])

        # Train the model
        model.fit(X_train, y_train, epochs=10, batch_size=4)

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


        predictions = model.predict(X_test)
        actual = Y
        accuracy = actual/(predictions + actual)

        five_epoch_accuracy = None
        ten_epoch_accuracy = accuracy
        twenty_epoch_accuracy = None
        fifty_epoch_accuracy = None

        five_feature_accuracy = None
        ten_feature_accuracy = accuracy
        twenty_feature_accuracy = None
        thirtyfour_feature_accuracy = None


        # Accuracy vs Epochs plot
        xlabels = ["5 Epochs", "10 Epochs", "20 Epochs", "50 Epochs"]
        ylabels = [five_epoch_accuracy, ten_epoch_accuracy, twenty_epoch_accuracy, fifty_epoch_accuracy]
        dataf = pd.DataFrame({" ":xlabels, "Accuracy":ylabels})
        sns.barplot(x = " ", y = "Accuracy", data=dataf).set(title='Accuracy versus Number of Epochs')
        plt.show()

        # Accuracy vs Number of Features plot

        xlabels = ["5 Features", "10 Features", "20 Features", "34 Features"]
        ylabels = [five_feature_accuracy, ten_feature_accuracy, twenty_feature_accuracy, thirtyfour_feature_accuracy]
        dataf = pd.DataFrame({" ":xlabels, "Accuracy":ylabels})
        sns.barplot(x = " ", y = "Accuracy", data=dataf).set(title='Accuracy versus Number of Features')
        plt.show()

    if __name__ == '__main__':
        main()
