def checkStatus(a,b):
  if(a>=0 or b>=0):
    flag=False
    return flag
  elif(a<0 and b<0):
    flag=True
    return flag
  else:
    flag=False
    return flag

x=int(input("enter first num") )
y=int(input("enter second num") )
flag=0
checkStatus(x,y)
