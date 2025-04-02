#ProcessData.py
#Name:
#Date:
#Assignment:

import random

def makeID(first,last,num):
  while len(last) < 5:
    last += "x"     # Append 'x' until the last name has at least 5 character


  last3 = num[-3:]  #Extract last 3 digits of student ID 
  return first[0] + last + last3  # Creat user ID
  
  

def makeMajorYear(major, year):
  first3 = major[:3].upper()    # Standard major abbreviation
  year = year.upper()   # Ensure year is uppercase
  
  yearAB = {
      "FRESHMAN": "FR",
      "SOPHOMORE":  "SO",
      "JUNIOR": "JR",
      "SENIOR": "SR"
  }.get(year, "UNK")  # Dictionary lookup for abbreviation
  
  return first3 + "-" + yearAB

  

def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r') # Open input file
  outFile = open("StudentList.csv", 'w')  # Open output file

  #Process each line of the input file and output to the CSV file
  for student in inFile:
    studentData = student.strip().split()

    #might need to delete this
    # if len(studentData) < 8:  # Ensure line has enough elements
    #     continue # Skip malformed lines

    firstName = studentData[0]
    lastName = studentData[1]
    studentID = studentData[3]  # Exracting ID  (now corrected index)
    year = studentData[5]  # Year should be the seond last item
    major = studentData[6] # Major should be the last item


    userID = makeID(firstName,lastName,studentID) # Generate user ID
    majorYear = makeMajorYear(major, year)  # Format  major-year

    

    studentOutput = f"{lastName},{firstName},{userID},{majorYear}\n"  # Correct CSV format
    outFile.write(studentOutput)


  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()

if __name__ == '__main__':
  main()
