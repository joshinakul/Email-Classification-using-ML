import os
from collections import Counter

direc = "emails/"
files = os.listdir(direc)

emails = [direc + email for email in files]

words = []
c = len(emails)

for email in emails:
    f = open(email)
    blob = f.read()
    words += blob.split(" ")
    print (c)
    c -= 1
    
print (words)
    
    