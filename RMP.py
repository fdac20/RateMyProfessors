#!/usr/bin/env python3

'''
RateMyProfessors Project:
Gather review information for all UT professors,
perform frequency and sentiment analysis.
Calculate overall review of UT professors
and different departments.

Rachel Harris
Shivam Patel
Madeline Phillips
'''

import requests
import json
import math
from bs4 import BeautifulSoup
import argparse

#TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO
'''
TODO
@scrape:
add sleep
get individual (quality and difficulty) ratings for reviews instead of just overall
write scraped data to json file for storage

@analysis:
make everything lowercase
????: merge same professors (variance?)

@load json:
write function to load json data from stored file
'''
#TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO

class Review():
    def __init__( self, reviewBody, reviewTags, quality, difficulty ):
        self.reviewBody = reviwBody
        self.reviewTags = reviewTags
        self.quality = quality
        self.difficulty = difficulty

    def print( self ):
        print( "Quality: " + str( self.quality ) )
        print( "Difficulty: " + str( self.difficulty ) )
        print()
        print( "Tags:" )
        for tag in self.reviewTags:
            print( tag )
        print()
        print( "Review:" )
        print( self.reviewBody )
        print()

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
   
def scrape( fileName ):
    print( "Printing scraped information to " + fileName + "." )

    #This the UT's school ID on RateMyProfessors.
    UTid = 1385

    #Get the list of professors for UT.
    webpage = requests.get( "https://www.ratemyprofessors.com/filter/professor/?&page=1&filter=teacherlastname_sort_s+asc&query=*%3A*&queryoption=TEACHER&queryBy=schoolId&sid=" + str( UTid ) )

    #Get the number of professors for UT.
    jsonpage = json.loads( webpage.content )
    num_professors = jsonpage["remaining"] + 20

    print( "Got " + str( num_professors ) + " professors" )

    iteration = 0
    listOfProfs = []
    pageCount = math.ceil( num_professors / 20 )

    professors = {}
    professorsWithoutReviews = {}
    numProfsWithReviews = 0
    numProfsWithoutReviews = 0
    totalReviews = 0

    #Iterate through pages.
    for i in range( pageCount ):
        #Get professors on each page.
        profsOnCurrentPage = requests.get( "http://www.ratemyprofessors.com/filter/professor/?&page=" + str( i ) + "&filter=teacherlastname_sort_s+asc&query=*%3A*&queryoption=TEACHER&queryBy=schoolId&sid=" + str( UTid ) )
        jsonPage = json.loads( profsOnCurrentPage.content )
        currentPageList = jsonPage['professors']
        
        #Add professors to list to professors.
        listOfProfs.extend( currentPageList )
  
        #Iterate through each professor.
        for j in range( len( currentPageList ) ):
            #Get overall information about professor.
            if currentPageList[j]['overall_rating'] != "N/A":
                professorP = Professor( int( currentPageList[j]['tNumRatings'] ), currentPageList[j]['tDept'], currentPageList[j]['tFname'], currentPageList[j]['tMiddlename'], currentPageList[j]['tLname'], float( currentPageList[j]['overall_rating'] ) )
                numProfsWithReviews += 1
            else:
                professorP = Professor( int( currentPageList[j]['tNumRatings'] ), currentPageList[j]['tDept'], currentPageList[j]['tFname'], currentPageList[j]['tMiddlename'], currentPageList[j]['tLname'], 0.0 )
                numProfsWithoutReviews += 1
                continue

            #Get professor's page.
            profURL = "https://www.ratemyprofessors.com/ShowRatings.jsp?tid=" + str(currentPageList[j]['tid'])
            profPage = requests.get( profURL )
            profInfo = BeautifulSoup( profPage.text, "html.parser" )
            #Get tags. classes: Tag-bs9vf4-0, jqEvsD
            profTags = profInfo.findAll( "span", { "class": "Tag-bs9vf4-0 jqEvsD" } )

            #Get review bodies. classes: Comments__StyledComments-dzzyvm-0 dvnRbr
            profBody = profInfo.findAll( "div", { "class": "Comments__StyledComments-dzzyvm-0 dvnRbr" } )

        iteration += 1
        if iteration % 100 == 0:
            print( "Finished " + str( iteration ) + " professors." )

    print( "There are " + str( numProfsWithReviews ) + " professors with reviews." )
    print( "There are " + str( numProfsWithoutReviews ) + " professors without reviews." )

def loadJson( fileName ):
    #TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO
    print( "TODO " + fileName )

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument( "-s", dest = "scrape", required = True )
    parser.add_argument( "-i", dest = "input", required = False )
    parser.add_argument( "-o", dest = "output", required = False )

    args = parser.parse_args()

    if args.scrape.lower() == "true" or args.scrape.lower() == "t":
        print( "Scrape is set to true. Calling scrape function." )
        if args.output is not None:
            scrape( args.output )
        else:
            print( "File for writing scraped data is not specified. Use -o option with output file name." )
            exit()
    else:
        print( "Scrape is set to false. Calling load function." )
        if args.input is not None:
            loadJson( args.input )
        else:
            print( "File for loading JSON is not specified. Use -i option with input file name." )
            exit()
