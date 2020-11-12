#!/usr/bin/env python3

import requests
import json
import math
from bs4 import BeautifulSoup
import argparse

#TODO: make everything lowercase, add sleep, get individual ratings instead of just overall, write scraped data to json file for storage, write function to load json data from stored file

class Review():
    def __init__( self, reviewBody, reviewTags, quality, difficulty ):
        self.reviewBody = reviwBody
        self.reviewTags = reviewTags
        self.quality = quality
        self.difficulty = difficulty

class Professor():
    def __init__( self, numReviews, department, firstName, middleName, lastName, overallRating ):
        self.numReviews = numReviews
        self.department = department
        self.firstName = firstName
        self.middleName = middleName
        self.lastName = lastName
        self.fullName = firstName + " " + lastName
        self.overallRating = overallRating
        self.reviews = []

    def addReview( self, review ):
        self.reviews.append( review )

    def print( self ):
        print( "Name: " + self.fullName + ":" )
        print( "Department: " + self.department )
        print( str( self.numReviews ) + " reviews" )
        print( "Length of reviews list: " + str( len( self.reviews ) ) )
        print( "Overall rating: " + str( self.overallRating ) )
        print()
   
def scrape():
    #This the UT's school ID on RateMyProfessors.
    UTid = 1385

    #Get the list of professors for UT.
    webpage = requests.get( "https://www.ratemyprofessors.com/filter/professor/?&page=1&filter=teacherlastname_sort_s+asc&query=*%3A*&queryoption=TEACHER&queryBy=schoolId&sid=" + str( UTid ) )

    #Get the number of professors for UT.
    jsonpage = json.loads( webpage.content )
    num_professors = jsonpage["remaining"] + 20

    print( "Got " + str( num_professors ) + " professors" )

    # what to get??
    listOfProfs = []
    pageCount = math.ceil(num_professors / 20)

    professors = {}
    professorsWithoutReviews = {}
    numProfsWithReviews = 0
    numProfsWithoutReviews = 0

    # cycile through profs
    for i in range (pageCount):
        # get profs on each page
        profsOnCurrentPage = requests.get("http://www.ratemyprofessors.com/filter/professor/?&page=" + str(i) + "&filter=teacherlastname_sort_s+asc&query=*%3A*&queryoption=TEACHER&queryBy=schoolId&sid=" + str(UTid))
        jsonPage = json.loads(profsOnCurrentPage.content)
        currentPageList = jsonPage['professors']
        
        listOfProfs.extend(currentPageList)
  
        for j in range (len(currentPageList)):
           #print( currentPageList[j] )

           if currentPageList[j]['overall_rating'] != "N/A":
               professorP = Professor( int( currentPageList[j]['tNumRatings'] ), currentPageList[j]['tDept'], currentPageList[j]['tFname'], currentPageList[j]['tMiddlename'], currentPageList[j]['tLname'], float( currentPageList[j]['overall_rating'] ) )
               numProfsWithReviews += 1
           else:
               professorP = Professor( int( currentPageList[j]['tNumRatings'] ), currentPageList[j]['tDept'], currentPageList[j]['tFname'], currentPageList[j]['tMiddlename'], currentPageList[j]['tLname'], 0.0 )
               numProfsWithoutReviews += 1
               continue

           continue

           #if str(currentPageList[j]['tLname']) != "Plank" or str(currentPageList[j]['tFname']) != "James": #<<used for testing
            #   continue
           # print out teacher full name
           #print(str(currentPageList[j]['tFname']) + " " + str(currentPageList[j]['tLname']))
           profURL = "https://www.ratemyprofessors.com/ShowRatings.jsp?tid=" + str(currentPageList[j]['tid'])
           profPage = requests.get(profURL)
           profInfo = BeautifulSoup(profPage.text, "html.parser")
           # print(profInfo)
           #classes: Tag-bs9vf4-0, jqEvsD
           profTags = profInfo.findAll("span", {"class": "Tag-bs9vf4-0 jqEvsD" })
           for tag in profTags:
               #print(tag.get_text())
               continue

           #body of review:
           profBody = profInfo.findAll("div", {"class": "Comments__StyledComments-dzzyvm-0 dvnRbr" })
           for tag in profBody:
              #print(tag.get_text())
              continue
           #print()

    # merge same prof (variance?) 
    #print(str(listOfProfs[0]))

    print( "There are " + str( numProfsWithReviews ) + " professors with reviews." )
    print( "There are " + str( numProfsWithoutReviews ) + " professors without reviews." )

    """
    for i in range (len(listOfProfs)):
        print(str(listOfProfs[i]))
    """

def loadJson( fileName ):
    #TODO
    print( "TODO " + fileName )

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument( "-s", dest = "scrape", required = True )
    parser.add_argument( "-f", dest = "file", required = False )

    args = parser.parse_args()

    if args.scrape.lower() == "true" or args.scrape.lower() == "t":
        print( "Scrape is set to true. Calling scrape function." )
        scrape()
    else:
        print( "Scrape is set to false. Calling load function." )
        if args.file is not None:
            loadJson( args.file )
        else:
            print( "File for loading JSON is not specified. Use -f option with file name." )
            exit()
