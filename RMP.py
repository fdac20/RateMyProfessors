#!/usr/bin/env python3

import requests
import json
import math
from bs4 import BeautifulSoup

#TODO: make everything lowercase, add sleep, make professor class (then put the things in it and make a dictionary of professors), get individual ratings instead of just overall 

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
    
    listOfProfs.extend(currentPageList)
  
    for j in range (len(currentPageList)):
       #if str(currentPageList[j]['tLname']) != "Plank" or str(currentPageList[j]['tFname']) != "James": #<<used for testing
        #   continue
       # print out teacher full name
       print(str(currentPageList[j]['tFname']) + " " + str(currentPageList[j]['tLname']))
       profURL = "https://www.ratemyprofessors.com/ShowRatings.jsp?tid=" + str(currentPageList[j]['tid'])
       profPage = requests.get(profURL)
       profInfo = BeautifulSoup(profPage.text, "html.parser")
       # print(profInfo)
       # TODO: figure out what they're labeling tags as
       #classes: Tag-bs9vf4-0, jqEvsD
       profTags = profInfo.findAll("span", {"class": "Tag-bs9vf4-0 jqEvsD" })
       for tag in profTags:
           print(tag.get_text())

       #body of review:
       profBody = profInfo.findAll("div", {"class": "Comments__StyledComments-dzzyvm-0 dvnRbr" })
       for tag in profBody:
          print(tag.get_text())
       #print()



# merge same prof (variance?) 
print(str(listOfProfs[0]))

# which college has hottest profs??? (chili pepper)



"""
for i in range (len(listOfProfs)):
    print(str(listOfProfs[i]))
"""
