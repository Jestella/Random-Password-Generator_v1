import random

#A function do shuffle all the characters of a String
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

#Main program starts here
#Generate a random Upperase letter (based on ASCII code)
uppercaseLetter1=chr(random.randint(65,90)) 
uppercaseLetter2=chr(random.randint(65,90))
uppercaseLetter3=chr(random.randint(65,90))  
lowercaseLetter1=chr(random.randint(97,122))
lowercaseLetter2=chr(random.randint(97,122))
lowercaseLetter3=chr(random.randint(97,122))
digit1=chr(random.randint(48,57))
digit2=chr(random.randint(48,57))


#Comebine the characters
password = uppercaseLetter1 + uppercaseLetter2 + uppercaseLetter3 + lowercaseLetter1 + lowercaseLetter2 + lowercaseLetter3 + digit1 + digit2

pasword = shuffle(password)

#Output
print(password)
