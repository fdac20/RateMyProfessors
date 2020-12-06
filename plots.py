import json
import csv
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

"""
def func1(data):
    for key,value in data.items():
        if str(key) == 'reviewTags':
            print (str(key)+'->'+str(value))
            continue
        else: 
            break
        if type(value) == type(dict()):
            func1(value)
        elif type(value) == type(list()):
            for val in value:
                if type(val) == type(str()):
                    pass
                elif type(val) == type(list()):
                    pass
                else:
                    func1(val)
"""
def Convert(a):
    #b = dict([i.split(': ') for i in a])
    #final = dict((k, v) for k, v in b.items())
    #final = {k:v for k,v in (x.split(':') for x in a) }
    return a

def myprint(d):
    for k, v in d.items():
        print("HEYYYYYYYYYYYYYYYYYYYYY!!!")
        print(k)
        if (k == "reviews"):
            #print("REVIEWS TYPE COMING!!!!!!!!!")
            #print(type(v))
            # convert list to dick
            # converting list v 
            v = Convert(v)
            #myprint(v)
        # when dick conversion is working, change to elif????
        if isinstance(v, dict):
            print(str(v) + " is a dict")
            myprint(v)
        else:
            print("{0} : {1}".format(k, v))

def print_dict(dictionary):
    dictionary_array = [dictionary]
    for sub_dictionary in dictionary_array:
        if type(sub_dictionary) is dict:
            for key, value in sub_dictionary.items():
                print("key=", key)
                print("value", value)
                if type(value) is dict:
                    dictionary_array.append(value)

# TEST CODE
lst = ['a', 1, 'b', 2, 'c', 3]
print(Convert(lst))

#Get data:
with open('data.json', "r") as f:
  data = json.load(f)


#Create bar graph with department and score
dept = ['']
score = ['']
for element in data:
    for value in data[element]:
        dept.append(data[element]['department'])
        score.append(str(data[element]['overallRating']))

fig, axs = plt.subplots(1,3, figsize=(9,3), sharey=True)
axs[0].bar(dept, score)
axs[1].scatter(dept, score)
axs[2].plot(dept,score)
fig.suptitle('Overall rating')
plt.show()

myprint(data)
#print_dict(data)

#Create word cloud with professor's tags:
#func1(data)
text= ['']
for element in data:
    for names in data[element]:
        for reviews in names['reviews']:
            print(reviews.get('reviewTags'))

#    for value in element:
#        var1 = data[element][value]['reviewTags']
#        for n3 in value:
 #           var = data[element][value]['reviewTags'][n3]
#text.append(data['Douglas Aaron']['reviewTags2'])
#text.append(data['Douglas Aaron']['reviewTags3'])
#iwordcloud = WordCloud().generate(text)

#Word cloud for highest rated prof:

#Word cloud for lowest rated prof:


