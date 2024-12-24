a=input("enter the letter: ")
b=a.split(" ")
coding=input("enter 1 for encoding and 2 for decoding:" )
coding=True if (coding=="1") else False
if(coding):
  nword=[]
  for word in b:
    if(len(word)>=3):
     word1="efm"
     word2="erj"
     word3=word1+word[1:]+word[0]+word2
     nword.append(word3)
    else:
      nword.append(word[::-1])
  print(" ".join(nword))

else:
  nword=[]
  for word in b:
    if(len(word)>=3):
      word1=word[3:-3]
      word1=word1[-1]+word1[:-1]
      nword.append(word1)
    else:
      nword.append(word[::-1])
  print(" ".join(nword))
