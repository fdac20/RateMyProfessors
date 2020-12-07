import json
import csv
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from dictor import dictor

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
#print(Convert(lst))

#Get data:
with open('data.json', "r") as f:
  data = json.load(f)

for k,v in data.items():
    search_string = k + '.department'
#    print("search string is " + str(search_string))
    department = dictor(data, str(search_string))
"""
#Try to print review tags:
dept = ['']
tags = ''
for k,v in data.items():
    search_string = k + '.reviews.0.reviewTags'
#    print("search string is " + str(search_string))
    reviewTag = dictor(data, str(search_string), default='None')
    #Change reviewTag to a string with each list element concatenated on:

    for i in reviewTag:
        if(str(i) == 'None'):
            break
        tags = tags + ' ' + str(i) + ' '
#    tags.append(reviewTag)
wordcloud = WordCloud().generate(tags)
cloud = wordcloud.to_file('wordcloud1.png')
"""
#Create dictionary with department and average overall score:
dept = ['']
score = []
avgrats = {}
count = 0
for k, v in data.items():
    count +=1
    search_string1 = k + '.department'
    search_string2 = k + '.overallRating'
    if count != 53 and count != 95 and count != 115 and count != 243 and count != 410 and count != 660 and count != 717 and count != 804 and count != 942 and count != 966:
        if dictor(data, '.department') in avgrats.keys():
            avgrats.update({dictor(data, search_string1) : (avgrats[dictor(data, search_string1)] + dictor(data, search_string2)/2)})
 #           print(avgrats[dictor(data, search_string1)])
        else:
            avgrats.update({dictor(data, search_string1) : dictor(data, search_string2)})
#            print(avgrats[dictor(data, search_string1)])
    if count > 1094:
        break


#Create bar graph for average overall score per department:
#*************TODO: make x-axis labels readable

font = {'family':'DejaVu Sans','weight':'bold','size':40}
plt.rc('font', **font)
fig, ax = plt.subplots(figsize=(64, 48))
#ax = figure.add_axes([0,0,1,1])
ax.set_title('Average Overall Rating of Professor per department')
ax.set_xlabel('Department')
ax.set_ylabel('Rating')
ax.bar(avgrats.keys(), avgrats.values())
plt.savefig('overall_rating_dept_bar')

search_string = 'Douglas Aaron.reviews.0.reviewTags'
print(dictor(data, search_string))


#Create dictionary with department and average quality:
dept = ['']
score = []
avgrats = {}
count = 0
for k, v in data.items():
    count +=1
    search_string1 = k + '.department'
    search_string2 = k + '.reviews.0.quality' #TODO: currently only getting first of each review, fix so we get all of them?
    print(dictor(data, search_string1))
    print(dictor(data, search_string2))
    if count != 53 and count != 95 and count != 115 and count != 243 and count != 410 and count != 660 and count != 717 and count != 804 and count != 942 and count != 966:
        if dictor(data, '.department') in avgrats.keys():
            avgrats.update({dictor(data, search_string1) : (avgrats[dictor(data, search_string1)] + dictor(data, search_string2)/2)})
            print(avgrats[dictor(data, search_string1)])
        else:
            avgrats.update({dictor(data, search_string1) : dictor(data, search_string2)})
            print(avgrats[dictor(data, search_string1)])
    if count > 1094:
        break
    print(count)
    print(avgrats)

#Create bar graph for average quality score per dept:
fig, ax = plt.subplots(figsize=(64, 48))
#ax = figure.add_axes([0,0,1,1])
ax.set_title('Average Quality Rating of Professor per department')
ax.set_xlabel('Department')#TODO: order y-axis from 1 - 5 like a normal human
ax.set_ylabel('Rating')
ax.bar(avgrats.keys(), avgrats.values())
plt.savefig('quality_rating_dept_bar')

#Dict, avg difficulty per dept:
dept = ['']
score = []
avgrats = {}
count = 0
for k, v in data.items():
    count +=1
    search_string1 = k + '.department'
    search_string2 = k + '.reviews.0.difficulty'
    if count != 53 and count != 95 and count != 115 and count != 243 and count != 410 and count != 660 and count != 717 and count != 804 and count != 942 and count != 966:
        if dictor(data, '.department') in avgrats.keys():
            avgrats.update({dictor(data, search_string1) : (avgrats[dictor(data, search_string1)] + dictor(data, search_string2)/2)})
 #           print(avgrats[dictor(data, search_string1)])
        else:
            avgrats.update({dictor(data, search_string1) : dictor(data, search_string2)})
#            print(avgrats[dictor(data, search_string1)])
    if count > 1094:
        break
#bar graph, avg difficulty per dept:
fig, ax = plt.subplots(figsize=(64, 48))
#ax = figure.add_axes([0,0,1,1])
ax.set_title('Average Difficulty Rating of Professor per department')
ax.set_xlabel('Department')
ax.set_ylabel('Rating')
ax.bar(avgrats.keys(), avgrats.values())
plt.savefig('difficulty_rating_dept_bar')

"""
fig, axs = plt.subplots(1,3, figsize=(9,3), sharey=True)
axs[0].bar(dept, score)
axs[1].scatter(dept, score)
axs[2].plot(dept,score)
fig.suptitle('Overall rating')
plt.show()
plt.savefig('bar.png')

"""
#Create word cloud with professor's tags:
#func1(data)
#text= ['']
#"for element in data:
#    for names in data[element]:
#        for reviews in names['reviews']:
#            print(reviews.get('reviewTags'))
#"
#    for value in element:
#        var1 = data[element][value]['reviewTags']
#        for n3 in value:
 #           var = data[element][value]['reviewTags'][n3]
#text.append(data['Douglas Aaron']['reviewTags2'])
#text.append(data['Douglas Aaron']['reviewTags3'])
#iwordcloud = WordCloud().generate(text)

#Word cloud for highest rated prof:

#Word cloud for lowest rated prof:
