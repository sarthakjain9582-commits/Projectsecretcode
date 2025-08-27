
import random

alphabets = "qwertyuiopasdfghjklzxcvbnm"

a = input("Encode(E) or Decode (D)")
encode = True if(a == "E") else False

inputText = input("Enter your string: ")
wordList = list(inputText)

if(encode):

 if(wordList. len ()>=3):
  print("Larger than 3")
  wordList.append(wordList.pop(0))

  for i in range(3):
   wordList.insert(0,random.choice(alphabets))
   wordList.insert(-1,random.choice(alphabets))

 else:
  wordList.reverse()

else:
 if(wordList.__len__() >=3):
   firstLetter = wordList.pop(-1)

 for i in range(3):
  wordList.pop(0)
  wordList.pop(-1)
  wordList.insert(0, firstLetter)
 else:
wordList.reverse()

print(str(wordList))
