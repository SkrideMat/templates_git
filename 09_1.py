f = open('9.txt')
ans=0
for s in f:
     ans+=1
     m=[int(x) for x in s.split()]
     p=[x for x in m if m.count(x)==2]
     np=[x for x in m if m.count(x)==1]
     if len(p)==2 and len(np)==4 and p[0]>=sum(np)/len(np):
          print(ans)
          break