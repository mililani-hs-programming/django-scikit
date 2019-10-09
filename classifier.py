import sklearn as sk


class Classifier:
    """Backend for django-scikit project"""

    def load_training_csv(self):
        """
        Load CSV into class and train a k-nearest algorithm based on it
        CSVs are assumed to have classification in the first column, and data in the remaining columns
        """
        pass

    def load_unknown_csv(self):
        """Run CSV through trained classifier"""
        pass

    def get_classification_list(self):
        """Return a list of predicted classifications based on unknown CSV"""
        pass

    def get_classification_percent(self):
        """Return a dictionary of classification tags and their corresponding percent occurance in unknown CSV"""
        pass
