import joblib
import loading_data_in_dictionary_fashion as l
import preprocessing_loaded_data as p
import training_the_model as t

def loading_data():
    dict_data = l.loading_data()
    return dict_data

def preprocessing(dict_data):
    input_data,label_data = p.text_to_numbers(dict_data)
    return input_data,label_data

def create_model(input_data,label_data):
    saved_model_name = t.classifier_model(input_data,label_data)
    return saved_model_name
def load_model(model_name):
    model = joblib.load(model_name)
    return model

if __name__ == "__main__":

    load_data = loading_data()
    input_data,label_data = preprocessing(load_data)
    model_name = create_model(input_data,label_data)

