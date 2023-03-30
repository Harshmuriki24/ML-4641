import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


class Preprocess(object):
    def __init__(self, url):
        self.url = url
        self.data = None
        self.train_img = None
        self.test_img = None
        self.train_lbl = None
        self.test_lbl = None

    def clean_data(self):

        #plot filtered data

        df = pd.read_csv(self.url)
        # print(df['Target'])
        # print(df.loc[:, df.columns != 'Target'])

        self.data = df.loc[:, df.columns != 'Target']
        target = df['Target']

        # 80-20 split
        self.train_img, self.test_img, self.train_lbl, self.test_lbl = train_test_split(
            self.data, target, test_size=1 / 5.0, random_state=0)

        # print(train_img)

        print("train_img size before: " + str(self.train_img.size))
        print("test_img size before: " + str(self.test_img.size))

        scaler = StandardScaler()

        # Fit on training set only.
        scaler.fit(self.train_img)

        # Apply transform to both the training set and the test set.
        self.train_img = scaler.transform(self.train_img)
        self.test_img = scaler.transform(self.test_img)

        # Make an instance of the Model
        pca = PCA(.90)
        pca.fit(self.train_img)

        # Create the test and the train data
        self.train_img = pca.transform(self.train_img)
        self.test_img = pca.transform(self.test_img)

        print("train_img size after: " + str(self.train_img.size))
        print("test_img size after: " + str(self.test_img.size))


pca = Preprocess("C:/Users/alexb/Documents/GitHub/ML-4641/higher-education-predictors-of-student-retention/dataset.csv")
pca.clean_data()

