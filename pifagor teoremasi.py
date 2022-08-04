def pifagor(a,b,c):
     if (c*c)==(a*a) + (b*b):
          return 1
     else :
          return 0



a,b,c = map(int,input().split())
x=pifagor(a,b,c) 
if x ==1:
     print ('yes')
else :
     print ('no')