import os
import codecs
def text_to_numbers(dict_converted_dataset):
    root = 'emails/'
    files = os.listdir(root)
    emails = [root + email for email in files]

    input_data = []
    label_data = []
    number_of_emails = len(emails)

    for email in emails:
        temp = []
        f = codecs.open(email,mode='r',encoding='utf-8',errors='ignore')
        words = f.read().split(' ')
        for word in dict_converted_dataset:
            temp.append(words.count(word[0]))
        input_data.append(temp)
        if 'spam' in email:
            label_data.append(1)
        if 'ham' in email:
            label_data.append(0)
    print(number_of_emails)
    number_of_emails -= 1
    print(len(input_data),len(label_data))

    return input_data,label_data

        