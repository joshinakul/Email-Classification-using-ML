from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import accuracy_score 
import joblib

def classifier_model(input_data,label_data):

    x_train, x_test, y_train, y_test = tts(input_data,label_data,test_size = 0.2)
    model = GaussianNB()
    model.fit(x_train,y_train)
    y_pred = model.predict(x_test)
    filename = 'saved_model.pkl'
    joblib.dump(model,filename)
    print(accuracy_score(y_test,y_pred))
    return filename