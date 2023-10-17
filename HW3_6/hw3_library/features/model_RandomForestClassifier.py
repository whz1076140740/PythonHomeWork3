from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, roc_auc_score


def model(train, test, features, target):
    X_train = train[features] 
    Y_train = train[target]
    X_test = test[features] 
    Y_test = test[target]
    model = RandomForestClassifier(n_estimators=100, random_state=42) 
    model.fit(X_train, Y_train)
    train_predictions = model.predict_proba(X_train)[:, 1] 
    test_predictions = model.predict_proba(X_test)[:, 1]
    y_train_pred = model.predict(X_train) 
    y_test_pred = model.predict(X_test)
    train['train_predictions'] = train_predictions 
    test['test_predictions'] = test_predictions
    train_accuracy = accuracy_score(Y_train, y_train_pred) 
    test_accuracy = accuracy_score(Y_test, y_test_pred)
    print("Train Accuracy:", train_accuracy)
    print("Test Accuracy:", test_accuracy)
    train_roc_auc = roc_auc_score(Y_train, train_predictions) 
    test_roc_auc = roc_auc_score(Y_test, test_predictions)
    print("Train ROC AUC:", train_roc_auc)
    print("Test ROC AUC:", test_roc_auc)
    return train, test