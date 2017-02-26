def baszontify(word):
 zonges=["gy","zs","z","b","d","dz","dzs","g","v"]
 zongetlen=["ty","s","sz","p","t","c","cs","k","f"]
 i=0;
 while(i!=len(zonges)):
  word=word.replace(zonges[i],zongetlen[i])
  i+=1
 return word
text=input()
words=text.split()
newtext=""
for word in words:
 newtext+=" "+baszontify(word)
print(newtext)


