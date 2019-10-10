import sklearn as sk
import pandas as pd
import csv
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

#this is garbage program

class Classifier:
    """Backend for django-scikit project"""

    def load_training_csv(self, dataset):
        """
        Load CSV into class and train a k-nearest algorithm based on it
        CSVs are assumed to have classification in the first column, and data in the remaining columns
        """
        #Loads iris datasets, replace load_iris() with a training set
        #For using iris:
        dataset=load_iris()
        #data is the data, target is the results, splits into 3-1 training to test (doesn't take input for target row or whatever)
        X_train, X_test, y_train, y_test=train_test_split(dataset['data'],dataset['target'], random_state=0)
        pass

    def load_unknown_csv(self, unknownDataset):
        """Run CSV through trained classifier"""
        #number of neighbors a datapoint is based on
        knn=KNeighborsClassifier(n_neighbors=3)

        pass

    def get_classification_list(self):
        """Return a list of predicted classifications based on unknown CSV"""
        for i in results:
            print(i)
        pass

    def get_classification_percent(self):
        """Return a dictionary of classification tags and their corresponding percent occurance in unknown CSV"""
        pass


dataset=load_iris()
print(dataset.keys())
print(dataset[''])