f = open("census", "r")
l=[]
for x in f:
  a=x.rstrip().split(" ")
  l.append(tuple((a[0],int(a[1]))))
  
print(l)
