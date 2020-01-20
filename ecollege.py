f = open("census", "r")
l=[]
won=[]
for x in f:
  a=x.rstrip().split(" ")
  l.append((a[0],int(a[1])))
  won.append(False)
  if(len(a)>2):
      if(a[2]=="W"):
          won[-1]=True

priority=[]
nseats=[]

for i in range(len(l)):
    priority.append(l[i][1]/(2**0.5))
    nseats.append(1)

total=538
maxn=538-3*len(l)
for i in range(maxn):
    biggest_priority=-1
    biggest_priority_n=-1
    for j in range(len(l)):
        if(priority[j]>biggest_priority):
            biggest_priority=priority[j]
            biggest_priority_n=j
            
    nseats[biggest_priority_n]+=1
    n=nseats[biggest_priority_n]
    priority[biggest_priority_n]=l[biggest_priority_n][1]/((n*(n+1))**0.5)
    
    
total_vote=0

for i in range(len(l)):
    nseats[i]+=2
    if(won[i]):
        total_vote+=nseats[i]
        
print("final score:",total_vote,"-",total-total_vote,"which is a ",end="")
if total_vote>270:
    print("win!")
elif total_vote<270:
    print("loss!")
else:
    print("tie!")
