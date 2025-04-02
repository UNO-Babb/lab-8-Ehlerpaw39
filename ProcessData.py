#ProcessData.py
#Name:
#Date:
#Assignment:

import random

def makeID(first,last,num):
  if len(last) < 5:
    last = last + "x"


  last3 = num[-3:]
  

  

  id = first[0] + last + last3
  
  return id

def makeMajorYear(major, year):
  first3 = major[0:3]
  year = year.upper()
  yearAB = ""
  if year == "FRESHMAN":
    yearAB = "FR"
  elif year == "SOPHOMORE":
    yearAB = "SO"
  elif year == "JUNIOR":
    yearAB = "JR"
  elif year == "SENIOR":
    yearAB = "SR"
  
  MajorYear = first3 + "-" + yearAB
  return MajorYear

  

def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')

  #Process each line of the input file and output to the CSV file
  for student in inFile:
    #student = "Antwan Dougherty AntwanDougherty@yahoo.com 443-13-3556 03/28/1996 Freshman Philosophy"
    studentData = student.split()
    firstName = studentData[0]
    lastName = studentData[1]
    studentID = studentData[3]
    year = studentData[5]
    major = studentData[6]
    userID = firstName+lastName+studentID
    majorYear = makeMajorYear(major, year)

    studentOutput = lastName + "," + firstName + userID + majorYear + "\n"
    outFile.write(studentOutput)


  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()

if __name__ == '__main__':
  main()
