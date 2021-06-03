for _ in[input]*int(input()):
  H,W = map(int,_().split())
  Y,X = H-1,W-1
  A,B = [],[]
  for y in range(H):
    A+=[_().split()]
    B+=[[0]*W]
  for y in range(H):
    for x in range(W):
      a,b=y,x
      # shift up
      if   (~x%2 and y >= x and x < X/2 and Y-y >  x) or ( (X-x)%2 and y >= X-x and x > X/2 and Y-y >  X-x): a+=1
      # shift down
      elif ( x%2 and y >  x and x < X/2 and Y-y >= x) or (~(X-x)%2 and y >  X-x and x > X/2 and Y-y >= X-x): a-=1
      # shift right
      elif (~y%2 and x >  y and y < Y/2 and X-x >= y) or ( (Y-y)%2 and x >  Y-y and y > Y/2 and X-x >= Y-y): b-=1
      # shift left
      elif ( y%2 and x >= y and y < Y/2 and X-x >  y) or (~(Y-y)%2 and x >= Y-y and y > Y/2 and X-x >  Y-y): b+=1
      # cases for odd dimension matrix
      else:
        if   (x==y==X/2==Y/2): pass
        # vertical single line shifts
        elif (x==X/2 and x < y < Y - x): a += [-1,1][x%2]
        elif (x==X/2==y): a += [Y-X,1][x%2]
        elif (x==X/2 and y == Y - x): a -= [1,Y-X][x%2]
        # horizontal single line shifts
        elif (y==Y/2 and y < x < X - y): b += [-1,1][y%2]
        elif (y==Y/2==x): b += [X-Y,1][y%2]
        elif (y==Y/2 and x == X - y): b -= [1,X-Y][y%2]
        else: raise Exception("This sucks!")
      B[y][x]=A[a][b]
  print(*[' '.join(map(str, l)) for l in B], sep='\n')


# ( 1, 0) - CE & R >= C & C < MC//2 & MR-R >  C | CO & R >= MC-C & C > MC//2 & MR-R >  MC-C
# (-1, 0) - CO & R >  C & C < MC//2 & MR-R >= C | CE & C >  MR-R & C > MC//2 & MR-R >= MC-C
#
# ( 0,-1) - RE & C >  R & R < MR//2 & MC-C >= R | RO & C >  MR-R & R > MR//2 & MC-C >  MR-R
# ( 0, 1) - RO & C >= R & R < MR//2 & MC-C >  R | RE & C >= MR-R & R > MR//2 & MC-C >= MR-R
#
