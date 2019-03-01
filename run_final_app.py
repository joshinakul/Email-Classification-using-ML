import joblib
import loading_data_in_dictionary_fashion as l

if __name__ == "__main__":
    print('model loading!')
    model = joblib.load('saved_model.pkl')
    print('model loaded!')

    data = l.loading_data()

    while True:
        output = []    
        text = input('Enter your message!') 
        if text == 'exit':
            break
        for word in data:
            output.append(text.count(word[0]))
        result = model.predict([output])
        if result == 0:
            print('geunine msg')
        else:
            print('fake msg')