import os
from collections import Counter
import codecs
def loading_data():
    root = "emails/"
    files = os.listdir(root)

    emails = [root + email for email in files]
    all_words_in_dataset = []
    number_of_emails = len(emails)
    for email in emails:
        f = codecs.open(email,mode='r',encoding = 'utf-8',errors = 'ignore')
        temp = f.read()
        all_words_in_dataset += temp.split(" ")
        print (number_of_emails)
        number_of_emails -= 1
    for i in range(len(all_words_in_dataset)):
        if not all_words_in_dataset[i].isalpha():
            all_words_in_dataset[i] = ""
    words_with_frequencies = Counter(all_words_in_dataset) 
    del words_with_frequencies[""]
    return words_with_frequencies.most_common(2500)

