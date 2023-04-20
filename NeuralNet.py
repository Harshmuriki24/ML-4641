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
        # print("prediction", predictions)

        # Plot the predictions along with the actual values
        plt.plot(Y, label='Actual')
        plt.plot(predictions, label='Predicted')
        plt.legend()
        plt.show()

        # print()
        # x = np.array(np.arange(4424))

        # plt.plot(x, Y, label='Dataset 1')
        # plt.plot(x, predictions, label='Dataset 2')
        # plt.legend()
        # plt.title('Two Datasets on the Same Line Plot')
        # plt.xlabel('X-axis')
        # plt.ylabel('Y-axis')
        # plt.show()

        # sns.relplot(data=data).set(title='data Data')
        # plt.show()

        # xlabels = []#["Train Image Before", "Test Image Before", "Train Image After", "Test Image After"]
        # ylabels = []#[train_before, test_before, train_after, test_after]
        # dataf = pd.DataFrame({" ":xlabels, "Columns":ylabels})
        # #sns.barplot(x = " ", y = "Columns", data=dataf).set(title='title')
        # #plt.show()

    if __name__ == '__main__':
        main()
