import re
import getpass

name=input("Enter your Name: \t")
surname=input("Enter your Surname:\t")
DOB=input("Enter your Date of Birth:\t").replace("-"," ")
print(DOB)
date = DOB.split(" ")

len1=len(name)
len1=(len1/2)

len2=len(surname)
len2=(len2/2)

password=getpass.getpass("Enter Password: \t")
flag = 0
print(password)
while True:
  if len(password)<8:
    flag = -1
    print("POOR PASSWORD")
    break
  elif name[:int(len1)] in password:
    flag = -1
    print("WEAK PASSWORD")
    break
  elif name[int(len1):] in password:
    flag = -1
    print("WEAK PASSWORD")
    break
  elif date[0] in password:
    flag = -1
    print("WEAK PASSWORD")
    break
  elif date[1] in password:
    flag = -1
    print("WEAK PASSWORD")
    break
  elif date[2] in password:
    flag = -1
    print("WEAK PASSWORD")
    break
  elif surname[:int(len2)] in password:
    flag = -1
    print("WEAK PASSWORD")
    break
  elif surname[int(len2):] in password:
    flag = -1
    print("WEAK PASSWORD")
    break
  elif not re.search("[a-z]", password):
    flag = -1
    break
  elif not re.search("[A-Z]", password):
    flag = -1
    break
  elif not re.search("[0-9]", password):
    flag = -1
    print("OKAISH PASSWORD")
    break
  elif not re.search("[!-~]", password):
    flag = -1
    break
  elif re.search("\s", password):  
    flag = -1
    break
  else:
    flag = 0
    print("Strong Password")
    break
