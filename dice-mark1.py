import random
times=[]
def filllists(number):
   number=str(number)
   for x in number:
         times.append(x)
def diceroller(rolls,number):
   while len(times)>0:
      n=0
      #number=str(number)
      checkpoint=int(times[n])
      amount=0
      while rolls >0:
         dice = random.randint(1,6)
         if dice >= checkpoint:
            amount+=1
         rolls-=1
         #print(rolls)
         #print(amount)
      print(amount)
      times.pop(0)
      rolls=amount
      amount=0
diceroller(40,filllists(343))
