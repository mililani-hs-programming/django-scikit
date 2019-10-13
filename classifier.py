import sklearn as sk
import pandas as pd
import csv
from sklearn.datasets import load_iris
#from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import numpy as np


# this is garbage program, rickroll?
# input: training csv, unknown csv, training a classifier on train csv, classifying unknown
# output: classification of unknown as list

class Classifier:
    """Backend for django-scikit project"""

    def __init__(self):
        self.trainingSet ='dat.csv'

    def load_training_csv(self):
        """
        Load CSV into class and train a k-nearest algorithm based on it
        CSVs are assumed to have classification in the first column, and data in the remaining columns
        """
        self.X_train=pd.read_csv(self.trainingSet, usecols=['B1', 'C1', 'D1','E1','F1'])
        self.y_train=pd.read_csv(self.trainingSet, usecols=['A1'])
        self.knn = KNeighborsClassifier(n_neighbors=3)
        self.knn.fit(self.X_train, self.y_train.values.ravel())
        X_new=np.array([[1, 4, 2, 4, 5]])
        prediction=self.knn.predict(X_new)
        print(prediction)
        pass

    def load_unknown_csv(self, unknownDataset):
        """Run CSV through trained classifier"""
        pass

    def get_classification_list(self):
        """Return a list of predicted classifications based on unknown CSV"""
        for i in results:
            print(i)
        pass

    def get_classification_percent(self):
        """Return a dictionary of classification tags and their corresponding percent occurance in unknown CSV"""
        for x in target:
            itemTotal = 0
            for y in results:
                if x == y:
                    itemTotal += 1
            print(x + itemTotal)
        pass

x=Classifier()
x.load_training_csv()

'''
        self.training=csv.reader(self.trainingSet, delimiter=' ')
        self.trainingDict=csv.DictReader(self.trainingSet)
        for row in self.training:
            print(', '.join(row))
        for row in self.trainingDict:
            self.y_train+=row
'''