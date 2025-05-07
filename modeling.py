from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, mean_squared_error, silhouette_score
from sklearn.cluster import KMeans

def train_classification_model(X_train, y_train):
    model = RandomForestClassifier(class_weight='balanced')
    model.fit(X_train, y_train)
    return model

def train_regression_model(X_train, y_train):
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

def train_clustering_model(X):
    kmeans = KMeans(n_clusters=3, random_state=42)
    clusters = kmeans.fit_predict(X)
    return kmeans, clusters

def evaluate_classification(model, X_test, y_test):
    preds = model.predict(X_test)
    print(classification_report(y_test, preds))

def evaluate_regression(model, X_test, y_test):
    preds = model.predict(X_test)
    mse = mean_squared_error(y_test, preds)
    print(f"RMSE: {mse ** 0.5}")

def evaluate_clustering(X, labels):
    score = silhouette_score(X, labels)
    print(f"Silhouette Score: {score}")
