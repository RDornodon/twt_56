for _ in[input]*int(input()):
 H,W=map(int, _().split())
 B,R=[],[]
 A=[_().split()for y in range(H)]
 while A:
  C=[]
  for s in range(4):
   if A: c=[*A.pop(0)];C+=c;R+=[len(c)];A=[*zip(*A)][::-1]
   else:break
  B+=[C]
 D=[]
 for x,b in enumerate(B):
  D+=[[([b[-1]]+b)[:-1],(b+[b[0]])[1:]][x%2]]
 E=[]
 for d in D:E.extend(d)
 E=E[::-1];S=[]
 for r in R[::-1]:L,E=E[:r],E[r:];S=[*zip(*(S+[L])[::-1])]
 S=[*zip(*S[::-1])]
 print(*[' '.join(s)for s in S],sep='\n')