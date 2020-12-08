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
            avgrats.update({dictor(data, search_string1) : (float(avgrats[dictor(data, search_string1)] + dictor(data, search_string2)/2))})
 #           print(avgrats[dictor(data, search_string1)])
        else:
            avgrats.update({dictor(data, search_string1) : float(dictor(data, search_string2))})
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
ax.set_xticklabels(avgrats.keys(), rotation = 90)
plt.gcf().subplots_adjust(bottom=.2)
ax.bar(avgrats.keys(), avgrats.values())
plt.savefig('overall_rating_dept_bar')

search_string = 'Douglas Aaron.reviews.0.reviewTags'
#print(dictor(data, search_string))


#Create dictionary with department and average quality:
dept = ['']
score = []
avgrats = {}
count = 0
for k, v in data.items():
    count +=1
    search_string1 = k + '.department'
    search_string2 = k + '.reviews.0.quality' #TODO: currently only getting first of each review, fix so we get all of them?
    if count != 53 and count != 95 and count != 115 and count != 243 and count != 410 and count != 660 and count != 717 and count != 804 and count != 942 and count != 966:
        if dictor(data, '.department') in avgrats.keys():
            avgrats.update({dictor(data, search_string1) : float(avgrats[dictor(data, search_string1)] + dictor(data, search_string2)/2)})
        else:
            avgrats.update({dictor(data, search_string1) : float(dictor(data, search_string2))})
    if count > 1094:
        break

#Graph:
fig, ax = plt.subplots(figsize = (20, 15))
plt.tight_layout()
x = avgrats.keys()
y = avgrats.values()
x_len = np.arange(len(x))
g1 = ax.bar(x, y, .5, label='Average Overall Quality Rating')
ax.set_xticks(x_len)
ax.set_xticklabels(x, rotation = 90)
ax.tick_params(axis = 'both', which = 'major', labelsize=12)

plt.gcf().subplots_adjust(bottom=.2)

plt.xticks(rotation = 90)
ax.set_title('Average Overall Quality Rating per Department')
plt.savefig('quality rating per dept.png')

#Average difficulty per dept:
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
            avgrats.update({dictor(data, search_string1) : float((avgrats[dictor(data, search_string1)] + dictor(data, search_string2)/2))})
 #           print(avgrats[dictor(data, search_string1)])
        else:
            avgrats.update({dictor(data, search_string1) : float(dictor(data, search_string2))})
#            print(avgrats[dictor(data, search_string1)])
    if count > 1094:
        break
#Graph:
fig, ax = plt.subplots(figsize = (20, 15))
plt.tight_layout()
x = avgrats.keys()
y = avgrats.values()
x_len = np.arange(len(x))
g1 = ax.bar(x, y, .35, label='Average Overall Difficulty Rating')
ax.set_xticks(x_len)
ax.set_xticklabels(x, rotation = 90)
ax.tick_params(axis = 'both', which = 'major', labelsize=12)

plt.gcf().subplots_adjust(bottom=.2)

plt.xticks(rotation = 90)
ax.set_title('Average Overall Difficulty Rating per Department')
plt.savefig('difficulty rating per dept.png')



#Find lowest rated prof (difficulty) per dept:
low_prof = {} #key is dept, value is prof (get rating from data.json)
high_prof = {}#same format as other
count = 0
for k, v in data.items():
    search_string0 = k + '.department'
    search_string = k + '.reviews.0.difficulty'
    
    if count != 52 and count != 94 and count != 114 and count != 242 and count != 409 and count != 659 and count != 716 and count != 803 and count != 941 and count != 965:
        if dictor(data, search_string0) in low_prof.keys():
            search_stringbase = str(low_prof[dictor(data, search_string0)]) + '.reviews.0.difficulty'
#            print('department: ', dictor(data, search_string0))
#            print('new: ', dictor(data, search_string))
#            print('current:',dictor(data, search_stringbase))
            if dictor(data, search_string) < dictor(data, search_stringbase):
                low_prof.update({dictor(data,search_string0) : k})
        else:
            low_prof.update({dictor(data, search_string0) : k})
    count +=1
    
    if count > 1094:
        break


#Find highest rated prof (difficulty) per dept:
count = 0
for k, v in data.items():
    search_string0 = k + '.department'
    search_string = k + '.reviews.0.difficulty'
    if count != 52 and count != 94 and count != 114 and count != 242 and count != 409 and count != 659 and count != 716 and count != 803 and count != 941 and count != 965:
        if dictor(data, search_string0) in high_prof.keys():
            search_stringbase = str(low_prof[dictor(data, search_string0)]) + '.reviews.0.difficulty'
            if dictor(data, search_string) > dictor(data, search_stringbase):
                high_prof.update({dictor(data,search_string0) : k})
        else:
            high_prof.update({dictor(data, search_string0) : k})
    
    count +=1
    if count > 1094:
        break


#Bar graph with highest and lowest rated professor (difficulty) per dept:
barWidth = .25;
bars1 = {}
count = 0
#print('lowest: ', low_prof)
#print('')
#print('highest:', high_prof)
for v in low_prof:
    x_string = low_prof[v] + '.department'
    search_string = str(low_prof[v]) + '.reviews.0.difficulty'
    if count != 52 and count != 94 and count != 114 and count != 242 and count != 409 and count != 659 and count != 716 and count != 803 and count != 941 and count != 965:
        bars1.update({dictor(data, x_string): float(dictor(data, search_string))})
    count+=1

bars2 = {}
count = 0
for v in high_prof:
    x_string = high_prof[v] + '.department'
    search_string = high_prof[v] + '.reviews.0.difficulty'
    if count != 52 and count != 94 and count != 114 and count != 242 and count != 409 and count != 659 and count != 716 and count != 803 and count != 941 and count != 965:
        bars2.update({dictor(data, x_string): float(dictor(data, search_string))})
    count +=1

fig, ax = plt.subplots(figsize = (20, 15))
plt.tight_layout()
x1 = bars1.keys()
y1 = bars1.values()
x2 = bars2.keys()
y2 = bars2.values()
x = np.arange(len(x1))
g1 = ax.bar(x - barWidth/2, y1, barWidth, label='worst')
g2 = ax.bar(x + barWidth/2, y2, barWidth, label='best')
ax.set_xticks(x)
ax.set_xticklabels(x1, rotation = 90)
ax.tick_params(axis = 'both', which = 'major', labelsize=8)

plt.gcf().subplots_adjust(bottom=.2)
plt.legend()

plt.xticks(rotation = 90)
ax.set_title('Best and Worst Professors by Difficulty Rating per Department')
plt.savefig('difficulty ratings for best and worst.png', bbox_inches='tight')




#Find lowest rated prof (quality) per dept:
low_prof = {} #key is dept, value is prof (get rating from data.json)
high_prof = {}#same format as other
count = 0
for k, v in data.items():
    search_string0 = k + '.department'
    search_string = k + '.reviews.0.quality'
    
    if count != 52 and count != 94 and count != 114 and count != 242 and count != 409 and count != 659 and count != 716 and count != 803 and count != 941 and count != 965:
        if dictor(data, search_string0) in low_prof.keys():
            search_stringbase = str(low_prof[dictor(data, search_string0)]) + '.reviews.0.quality'
#            print('department: ', dictor(data, search_string0))
#            print('new: ', dictor(data, search_string))
#            print('current:',dictor(data, search_stringbase))
            if dictor(data, search_string) < dictor(data, search_stringbase):
                low_prof.update({dictor(data,search_string0) : k})
        else:
            low_prof.update({dictor(data, search_string0) : k})
    count +=1
    
    if count > 1094:
        break


#Find highest rated prof (quality) per dept:
count = 0
for k, v in data.items():
    search_string0 = k + '.department'
    search_string = k + '.reviews.0.quality'
    if count != 52 and count != 94 and count != 114 and count != 242 and count != 409 and count != 659 and count != 716 and count != 803 and count != 941 and count != 965:
        if dictor(data, search_string0) in high_prof.keys():
            search_stringbase = str(low_prof[dictor(data, search_string0)]) + '.reviews.0.quality'
            if dictor(data, search_string) > dictor(data, search_stringbase):
                high_prof.update({dictor(data,search_string0) : k})
        else:
            high_prof.update({dictor(data, search_string0) : k})
    
    count +=1
    if count > 1094:
        break


#Bar graph with highest and lowest rated professor (quality) per dept:
barWidth = .25;
bars1 = {}
count = 0
#print('lowest: ', low_prof)
#print('')
#print('highest:', high_prof)
for v in low_prof:
    x_string = low_prof[v] + '.department'
    search_string = str(low_prof[v]) + '.reviews.0.quality'
    if count != 52 and count != 94 and count != 114 and count != 242 and count != 409 and count != 659 and count != 716 and count != 803 and count != 941 and count != 965:
        bars1.update({dictor(data, x_string): float(dictor(data, search_string))})
    count+=1

bars2 = {}
count = 0
for v in high_prof:
    x_string = high_prof[v] + '.department'
    search_string = high_prof[v] + '.reviews.0.quality'
    if count != 52 and count != 94 and count != 114 and count != 242 and count != 409 and count != 659 and count != 716 and count != 803 and count != 941 and count != 965:
        bars2.update({dictor(data, x_string): float(dictor(data, search_string))})
    count +=1

fig, ax = plt.subplots(figsize = (20, 15))
plt.tight_layout()
x1 = bars1.keys()
y1 = bars1.values()
x2 = bars2.keys()
y2 = bars2.values()
x = np.arange(len(x1))
g1 = ax.bar(x - barWidth/2, y1, barWidth, label='worst')
g2 = ax.bar(x + barWidth/2, y2, barWidth, label='best')
ax.set_xticks(x)
ax.set_xticklabels(x1, rotation = 90)
ax.tick_params(axis = 'both', which = 'major', labelsize=8)

plt.gcf().subplots_adjust(bottom=.2)
plt.legend()

plt.xticks(rotation = 90)
ax.set_title('Best and Worst Professors by Quality Rating per Department')

plt.savefig('quality ratings for best and worst.png', bbox_inches='tight')



#Create word cloud with professor's tags for given department:

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
cloud = wordcloud.to_file('wordcloud_overall.png')

#Word cloud specifically for engineering:
tags = ''
for k,v in data.items():
    search_string = k + '.reviews.0.reviewTags'
    ssd = k + '.department'
    if dictor(data, ssd) == 'Engineering':
        reviewTag = dictor(data, str(search_string), default='None')

    for i in reviewTag:
        if(str(i) == 'None'):
            break
        tags = tags + ' ' + str(i) + ' '

wordcloud = WordCloud().generate(tags)
cloud = wordcloud.to_file('wordcloud_engineering.png')

#Find highest rated prof:
best = dictor(data, 'Douglas Aaron')
bss = 'Douglas Aaron.overallRating'
for v in high_prof:
    search_string = high_prof[v] + '.overallRating'
    if dictor(data, bss) < dictor(data, search_string):
        bss = search_string
        best = high_prof[v]

#Word cloud for highest rated prof:
tags = ''
search_string = best + '.reviews.0.reviewTags'
reviewTag = dictor(data, str(search_string), default='None')
for i in reviewTag:
    if(str(i) == 'None'):
        break
    tags = tags + ' ' + str(i) + ' '
wordcloud = WordCloud().generate(tags)
cloud = wordcloud.to_file('wordcloud_best.png')
#print(best)

#Find lowest rated prof:
worst = dictor(data, 'Douglas Aaron')
bss = 'Douglas Aaron.overallRating'
for v in high_prof:
    search_string = high_prof[v] + '.overallRating'
    if dictor(data, bss) > dictor(data, search_string):
        bss = search_string
        worst = high_prof[v]
#print(worst)

tags = ''
#Word cloud for lowest rated prof:
search_string = worst + '.reviews.0.reviewTags'
#print(dictor(data, str(search_string)))
reviewTag = dictor(data, str(search_string), default='None')
for i in reviewTag:
    if(str(i) == 'None'):
        break
    tags = tags + ' ' + str(i) + ' '
wordcloud = WordCloud().generate(tags)
cloud = wordcloud.to_file('wordcloud_worst.png')
