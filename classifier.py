import sklearn as sk


class Classifier:
    """Backend for django-scikit project"""

    def load_training_csv(self):
        """
        Load CSV into class and train a k-nearest algorithm based on it
        CSVs are assumed to have classification in the first column, and data in the remaining columns
        """
        import csv
        import pandas as pd


        from locale import Iris_Dataset.csv1173

        filepath = "Iris_Dataset.csv"


        Iris_Dataset = pd.read.csv(filepath)
        Iris_Dataset
        print(Iris_Dataset.head)

"""     Iris_Dataset.csv = load_iris()
        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(Iris_Dataset['data'],Iris_Dataset['target'],random_state=0)
        from sklearn.neighbors import KNeighborsClassifier
        knn = KNeighborsClassifier(n_neighbors=3)
        knn.fit(X_train,y_train)"""


    def load_unknown_csv(self):
        """Run CSV through trained classifier"""
        pass

    def get_classification_list(self):
        """Return a list of predicted classifications based on unknown CSV"""
        pass

    def get_classification_percent(self):
        """Return a dictionary of classification tags and their corresponding percent occurance in unknown CSV"""
        pass

