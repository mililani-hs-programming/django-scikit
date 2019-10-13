import sklearn as sk
import pandas as pd
import csv
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

# input: training csv, unknown csv, training a classifier on train csv, classifying unknown
# output: classification of unknown as list
#NEEDS: file names, names of everything in the first row

class Classifier:
    """Backend for django-scikit project"""

    def __init__(self):
        self.trainingSet ='dat.csv'
        self.unknownSet='newdat.csv'

    def load_training_csv(self):
        """
        Load CSV into class and train a k-nearest algorithm based on it
        CSVs are assumed to have classification in the first column, and data in the remaining columns
        """
        self.X_train=pd.read_csv(self.trainingSet, usecols=['B1', 'C1', 'D1','E1', 'F1'])
        self.y_train=pd.read_csv(self.trainingSet, usecols=['A1'])
        self.knn = KNeighborsClassifier(n_neighbors=3)
        self.knn.fit(self.X_train, self.y_train.values.ravel())

    def load_unknown_csv(self):
        """Run CSV through trained classifier"""
        self.test=pd.read_csv(self.unknownSet, usecols=['A1', 'B1', 'C1', 'D1','E1'])
        self.results=self.knn.predict(self.test)

    def get_classification_list(self):
        """Return a list of predicted classifications based on unknown CSV"""
        print("Predictions are\n",self.results)

    def get_classification_percent(self):
        """Return a dictionary of classification tags and their corresponding percent occurance in unknown CSV"""
        pass

x=Classifier()
x.load_training_csv()
x.load_unknown_csv()

'''
        self.training=csv.reader(self.trainingSet, delimiter=' ')
        self.trainingDict=csv.DictReader(self.trainingSet)
        for row in self.training:
            print(', '.join(row))
        for row in self.trainingDict:
            self.y_train+=row
'''