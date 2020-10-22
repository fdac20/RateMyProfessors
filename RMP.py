#!/usr/bin/env python3

import requests
import json
import math

UTid = 1385

webpage = requests.get( "https://www.ratemyprofessors.com/filter/professor/?&page=1&filter=teacherlastname_sort_s+asc&query=*%3A*&queryoption=TEACHER&queryBy=schoolId&sid=" + str( UTid ) )

jsonpage = json.loads( webpage.content )
num_professors = jsonpage["remaining"] + 20

print( "Got " + str( num_professors ) + " professors" )

# what to get??
listOfProfs = []
pageCount = math.ceil(num_professors / 20)

# cycle through profs
for i in range (pageCount):
    # get profs on each page
    profsOnCurrentPage = requests.get("http://www.ratemyprofessors.com/filter/professor/?&page=" + str(i) + "&filter=teacherlastname_sort_s+asc&query=*%3A*&queryoption=TEACHER&queryBy=schoolId&sid=" + str(UTid))
    jsonPage = json.loads(profsOnCurrentPage.content)
    currentPageList = jsonPage['professors']
    
    for j in range (len(currentPageList)):
       # print out teacher full name
       print(str(currentPageList[j]['tFname']) + " " + str(currentPageList[j]['tLname']))
    listOfProfs.extend(currentPageList)

print(str(listOfProfs[0]))
"""
for i in range (len(listOfProfs)):
    print(str(listOfProfs[i]))
"""
