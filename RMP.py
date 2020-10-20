#!/usr/bin/env python3

import requests
import json
import math

UTid = 1385

webpage = requests.get( "https://www.ratemyprofessors.com/filter/professor/?&page=1&filter=teacherlastname_sort_s+asc&query=*%3A*&queryoption=TEACHER&queryBy=schoolId&sid=" + str( UTid ) )

jsonpage = json.loads( webpage.content )
num_professors = jsonpage["remaining"] + 20

print( "Got " + str( num_professors ) + " professors" )
