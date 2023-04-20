import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class NeuralNet:
    def __init__(self, input, neurons):
        self.weights = [0]
        self.biases = [0]
        self.df = pd.read_csv(self.url)

    def forward(self, input):
        #self.output = np.dot(inputs, self.weights) + self.biases
        return np.dot(input, self.weights) + self.biases

    def main():
        # input = [0.5, 0.7, 0.25, 0.33, 0.1, 0.8, 0.11, 0.28]
        # neurons = 8
        # net = NeuralNet(input=input, neurons=neurons)

        # layer1 = NeuralNet(4,4)
        # output = layer1.forward()
        # layer2 = NeuralNet(output, 4)
        # layer2.forward()


        url = 'higher-education-predictors-of-student-retention/dataset.csv'
        sns.set_theme()
        unfiltered = pd.read_csv(url)
        marital_status = unfiltered['Marital status']
        marital_status0_3 = marital_status[:4]
        print(marital_status0_3)
        # sns.relplot(data=unfiltered).set(title='Unfiltered Data')
        # plt.show()


        # xlabels = []#["Train Image Before", "Test Image Before", "Train Image After", "Test Image After"]
        # ylabels = []#[train_before, test_before, train_after, test_after]
        # dataf = pd.DataFrame({" ":xlabels, "Columns":ylabels})
        # sns.barplot(x = " ", y = "Columns", data=dataf).set(title='title')
        # plt.show()

    if __name__ == "__main__":
        main()

class ReLU:
    def relu(self, input):
        return np.maximum(o, input)
    
class Softmax:
    def softmax(self, input):
        return np.exp(input - np.max(input))