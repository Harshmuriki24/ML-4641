import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression

url = 'higher-education-predictors-of-student-retention/dataset.csv'
df = pd.read_csv(url)
# print(df['Target'])
# print(df.loc[:, df.columns != 'Target'])

data = df.loc[:, df.columns != 'Target']
target = df['Target']

# 80-20 split
train_img, test_img, train_lbl, test_lbl = train_test_split(
    data, target, test_size=1/5.0, random_state=0)

#print(train_img)
scaler = StandardScaler()

# Fit on training set only.
scaler.fit(train_img)

# Apply transform to both the training set and the test set.
train_img = scaler.transform(train_img)
test_img = scaler.transform(test_img)

# Make an instance of the Model
pca = PCA(.90)
pca.fit(train_img)

# Create the test and the train data
train_img = pca.transform(train_img)
test_img = pca.transform(test_img)

#print(test_img)

########################################################################
#LINEAR REGRESSION SECTION. THIS SHOULD BE SPLIT INTO A SEPERATE FILE ##
########################################################################

logreg = LogisticRegression(solver="lbfgs")
logreg.fit(train_img, train_lbl)
#predicting for all observations
logreg.predict(test_img)

#Performance section
logreg.score(test_img, test_lbl)
