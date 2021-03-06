#!/usr/bin/env python3
''' template for ops435 assignment 1 script
    put your script level docstring here...
    you can have more than one line of docstring.
    Please personlize the following author declaration:
-----------------------------------------------------------------------
OPS435 Assignment 1 - Winter 2021
Program: a1_areyes15.py (replace [Seneca_name] with your Seneca User name)
Author: "Anthony Reyes"
The python code in this file (a1_areyes15.py) is original work written by
"Anthony Reyes". No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading.
I understand that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.
'''
'''
The purpose of this script is to be given a date of birth in three supported different formats.
For each supported format of date of birth the script will remove the unnecessary characters from
the input and return the date of birth in standard date format (EX. 2020-10-10 = Oct 10, 2020) The
script recoginzes leap years and will only allow inputs for years that are in range from 1900 - 9999.

'''
import os
import sys

def leap_year(obj):
    '''
    The leap_year() function will check for the amount of days in February to discover if it is a leap year.
    It will then return a false if it is not a leap year or a true if it is a leap year.
    '''
#Leap year calculations and conditional statements
    lyear = year % 4
    if (lyear == 0):

        lyear = year % 100
        if (lyear == 0):

            lyear = year % 400
            if (lyear == 0):
                status = True
            else:
               status = False
        else:
                status = False
    else:
           status = True

    return status

def sanitize(obj1,obj2):
    '''
    The sanitize() function removes unnecessary characters that are not within the allow-chars variable
    so that they don not interfere with the new format and are removed before output.
    '''
#Code for removing unwanted characters
    results = ''
    for char in obj1:
            if char in obj2:
                results += char
    return results

def size_check(obj, intobj):
    '''
    The size_check() function will check the size of the inputted format for the correct character length,
    if the size is not correct it will result status as false. If it is the correct length staatus will return
    as true.
    '''
#if condition for size check
    status = False
    if len(obj) == intobj:
        status = True
    else:
        status = False
    return status

def range_check(obj1, obj2):
 '''
  The range_check() function will check the user input to make sure the data is within the correct range.
  The user can only input a certain range of characters i.e 1900-9999 year and the correct month and date values.
  If the range is not correct it will return false to status, if the range is correct it will return true.
 '''
#range_check function is determining if the inputed data is within the parameters in the arguement.
 status = False

 if int(obj1) in range(obj2[0],obj2[1]+1):
    status = True
 else:
    status = False

#This return status will return true or false, if it returns false it'll display an error message to the screen.
 return status

def usage():
        '''
        The usage() function will inform the user on how to properly use the script and its syntax.
        '''
#Display message to the user informing of the scripts proper input format
#If the length of the command line arguments aren't the length of 2 this message will print to screen and exit the script
        help = """Usage: a1_areyes15.py YYYYMMDD|YYYY/MM/DD|YYYY-MM-DD|YYYY.MM.DD"""
        print (help)
        exit()

if __name__ == "__main__":
   # step 1
   if len(sys.argv) != 2:
      print(usage())
      sys.exit()
   # step 2
   month_name = ['Jan','Feb','Mar','Apr','May','Jun',
                 'Jul','Aug','Sep','Oct','Nov','Dec']
   days_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30,
                    7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
   user_raw_data = sys.argv[1]
   # step 3
   allow_chars = '0123456789'
   dob = sanitize(user_raw_data, allow_chars)
   # step 4
   result = size_check(dob,8)
   if result == False:
       print("Error 09: wrong date entered")
       sys.exit()
   # step 5
   year = int(dob[0:4])
    month = int(dob[4:6])
   day = int(dob[6:])
   # step 6
   result = range_check(year,(1900,9999))
   if result == False:
       print("Error 10: year out of range, must be 1900 or later")
       sys.exit()
   result = range_check(month,(1,12))
   if result == False:
       print("Error 02: wrong month entered")
       sys.exit()
   result = leap_year(year)
   if result == True:
       days_in_month[2] = 29
   result = range_check(day, (1, days_in_month[month]))
   if result == False:
       print("Error 03: wrong day entered")
       sys.exit()
   # step 7
   new_dob = str(month_name[month - 1])+' '+ str(day)+', '+str(year)
   # step 8
   print(new_dob)

