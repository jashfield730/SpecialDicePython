import random, sys
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
      #print(amount)
      times.pop(0)
      rolls=amount
      amount=0
   print(rolls)
def collectinput():
   global dicerolls, comparisons
   dicerolls=input('Enter in your required Dice Rolls: ')
   if dicerolls == 'q':
      times=[]
      sys.exit()
   dicerolls=int(dicerolls)
   comparisons=input('Enter in your comparisons in the follow order\nfirst comparistion ,second etc. \ne.g.123 compare 1 first 2 second 3 third: ')
print('Welcome to John\'s dice calculator')

def main():
   try:
      collectinput()
      diceroller(dicerolls,filllists(comparisons))
      main()
   except NameError:
      print('Put in values next time')

print('Thanks for using John\'s Dice to QUIT type \'q\' in the dice rolls')

if __name__ == "__main__":
   main()
