import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
pchoice=input  ("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")

if pchoice=='0' :
  print(rock)
elif(pchoice=='1'):
  print(paper)
else:
  print(scissors) 



cchoice=str(random.randint(0,3-1))
print("Computer choose",cchoice)

if cchoice=='0' :
  print(rock)
elif(cchoice=='1'):
  print(paper)
else:
  print(scissors) 


if(pchoice == cchoice):
  print("DRAW DO REPLAY")
else: 
    if(pchoice=='0'and cchoice=='2'):
        print("U WIN")
    elif(pchoice=='2' and cchoice=='1'):
        print("U WIN")
    elif(pchoice =='1'and cchoice=='0'):
        print("U WIN")
    else:
        print("U LOST")
    
print("CODE EXITED")
