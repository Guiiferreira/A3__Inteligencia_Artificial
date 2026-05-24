# utils/modelos.py
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


class Perceptron:

    def __init__(self, lr=0.01, epocas=100):
        self.lr = lr
        self.epocas = epocas

    def fit(self, X, y):
        self.w = np.zeros(X.shape[1])
        self.b = 0

        for _ in range(self.epocas):
            for i in range(len(X)):
                linear = np.dot(X[i], self.w) + self.b
                y_pred = 1 if linear >= 0 else 0
                erro = y.iloc[i] - y_pred
                self.w += self.lr * erro * X[i]
                self.b += self.lr * erro

    def predict(self, X):
        return np.array([
            1 if np.dot(x, self.w) + self.b >= 0 else 0
            for x in X
        ])


def treinar_modelos(X_train, X_test, y_train, y_test):

    # KNN
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train, y_train)
    y_pred_knn = knn.predict(X_test)
    acc_knn = accuracy_score(y_test, y_pred_knn)

    # Perceptron
    p = Perceptron()
    p.fit(X_train, y_train)
    y_pred_p = p.predict(X_test)
    acc_p = accuracy_score(y_test, y_pred_p)

    return knn, p, y_pred_knn, y_pred_p, acc_knn, acc_p