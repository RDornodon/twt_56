
for I in[input]*int(input()):D=[I().split()for Q in'.'*int(I())];E,F=zip(*D);G={}.fromkeys(F,0);[G.update([[k,G[k]+1-2*(v<'1')]])for v,k in D];print(str(not any(G.values())).lower())
