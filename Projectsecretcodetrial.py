import random
a = input("Choose mode (CODE/DECODE): ").upper()
k = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
      "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
i = 0
j = 0
if a == "CODE":
    print("You decided to code the secret word")
    b = input("Enter the text: ")
    d = list(b)
    f = len(b)
    if f > 3 :
        h = d[0]
        d.append(h)
        d.pop(0)
        random.shuffle(k)
        for j in range (3):
           print(k[j], end="")
           j = j+1
        for i in range (f):
           print(d[i], end="")
           i = i+1
        for j in range (3):
          print(k[j+3], end="")
          j = j+1
    else :
       d.reverse()
       for i in range (f):
        print(d[i], end="")
        i = i+1
elif a == "DECODE":
    print("You decided to decode the secret word")
    c = input("Enter the text: ")
    e = list(c)
    g = len(c)
    if g > 3 :
       e.pop(0)
       e.pop(0)
       e.pop(0)
       e.pop()
       e.pop()
       e.pop()
       m = len(e)
       n = e[m-1]
       e.pop()
       print(n, end="")
       for i in range (g):
        if i >= m - 1:
         break
        print(e[i], end="")
        i = i+1
    else :
       e.reverse()
       for i in range (g):
        print(e[i], end="")
        i = i+1
else:
    print("Wrong one")
