#Made by YeeTEDWIN
import random
import sys
import os, time

print("This game was made by YEETEDWIN (Known as Y^^TED)")
time.sleep(4)
def clear():
  os.system("clear")
clear()
print("Special Limited Edition gamemodes are Coding Week, Christmas and Happy New Year")
time.sleep(3)
print("\n")
mode = input("What gamemode would you like? Easy, Normal, Negatives, Hardcore, Devil 666 or Impossible\n")

if mode == "Easy":
  clear()
  num2 = random.randint(1,10)
  guesses = 4
  print("Number Guessing Game (Easy mode)!")
  while True:
    num = int(input("Guess a number 1-10\n: "))

    if num > num2:
      print(f"Too high. You have {guesses-1} guesses left")
      guesses-=1
    if num < num2:
      print(f"Too low. You have {guesses-1} guesses left")
      guesses-=1
    if num == num2:
      print(f"You got it right! You finished with {guesses-1} guesses left")
      time.sleep(2)
      clear()
      print("Thank you for playing the Number Guessing Game")
      time.sleep(3)
      clear()
      sys.exit()
    if guesses == 0:
      print(f"You lost! The correct number was {num2}")
      time.sleep(2)
      clear()
      print("Thank you for playing the Number Guessing Game")
      time.sleep(3)
      clear()
      sys.exit()

elif mode == "Normal":
  clear()
  num2 = random.randint(1,100)
  guesses = 10
  print("Number Guessing Game (Normal mode)!")
  while True:
    num = int(input("Guess a number 1-100\n: "))

    if num > num2:
      print(f"Too high. You have {guesses-1} guesses left")
      guesses-=1
    if num < num2:
      print(f"Too low. You have {guesses-1} guesses left")
      guesses-=1
    if num == num2:
      print(f"You got it right! You finished with {guesses-1} guesses left")
      time.sleep(2)
      clear()
      print("Thank you for playing the Number Guessing Game")
      time.sleep(3)
      clear()
      sys.exit()
    if guesses == 0:
      print(f"You lost! The correct number was {num2}")
      time.sleep(2)
      clear()
      print("Thank you for playing the Number Guessing Game")
      time.sleep(3)
      clear()
      sys.exit()

elif mode == "Hardcore":
  clear()
  num2 = random.randint(1,1000)
  guesses = 10
  print("Number Guessing Game (Hardcore mode)!")
  while True:
    num = int(input("Guess a number 1-1000\n: "))

    if num > num2:
      print(f"Too high. You have {guesses-1} guesses left")
      guesses-=1
    if num < num2:
      print(f"Too low. You have {guesses-1} guesses left")
      guesses-=1
    if num == num2:
      print(f"You got it right! You finished with {guesses-1} guesses left")
      time.sleep(2)
      clear()
      print("Thank you for playing the Number Guessing Game")
      time.sleep(3)
      clear()
      sys.exit()
    if guesses == 0:
      print(f"You lost! The correct number was {num2}")
      time.sleep(2)
      clear()
      print("Thank you for playing the Number Guessing Game")
      time.sleep(3)
      clear()
      sys.exit()

elif mode == "Impossible":
  clear()
  num2 = random.randint(1,1000)
  guesses = 1
  print("Number Guessing Game (Impossible mode)!")
  while True:
    num = int(input("Guess a number 1-1\n: "))

    if num > num2:
      print(f"Too high. You have {guesses-1} guesses left")
      guesses-=1
    if num < num2:
      print(f"Too low. You have {guesses-1} guesses left")
      guesses-=1
    if num == num2:
      print(f"You got it right! You finished with {guesses-1} guesses left")
      time.sleep(2)
      clear()
      print("Thank you for playing the Number Guessing Game")
      time.sleep(3)
      clear()
      sys.exit()
    if guesses == 0:
      print(f"You lost! The correct number was {num2}")
      time.sleep(2)
      clear()
      print("Thank you for playing the Number Guessing Game")
      time.sleep(3)
      clear()
      sys.exit()

elif mode == "Devil 666":
  clear()
  num2 = random.randint(69,666)
  guesses = 5
  print('Number Guessing Game (Devil "666" mode)!')
  while True:
    num = int(input("Guess a number 69-666\n: "))

    if num > num2:
      print(f"Too high. You have {guesses-666} evil guesses left")
      guesses-=1
    if num < num2:
      print(f"Too low. You have {guesses-666} evil guesses left")
      guesses-=1
    if num == num2:
      print(f"You got it right! You finished with {guesses-666} evil guesses left")
      time.sleep(2)
      clear()
      print("Thank you for playing the Number Guessing Game")
      time.sleep(3)
      clear()
      sys.exit()
    if guesses == 0:
      print(f"You lost! The correct number was {num2}")
      time.sleep(2)
      clear()
      print("Thank you for playing the Number Guessing Game")
      time.sleep(3)
      clear()
      sys.exit()

elif mode == "Negatives":
  clear()
  num2 = random.randint(-400, 400)
  guesses = 10
  print('Number Guessing Game (With Negatives and Harder)!')
  while True:
    num = int(input("Guess a number -400-400\n: "))

    if num > num2:
      print(f"Too high. You have {guesses-1} guesses left")
      guesses-=1
    if num < num2:
      print(f"Too low. You have {guesses-1} guesses left")
      guesses-=1
    if num == num2:
      print(f"You got it right! You finished with {guesses-1} guesses left")
      time.sleep(2)
      clear()
      print("Thank you for playing the Number Guessing Game")
      time.sleep(3)
      clear()
      sys.exit()
    if guesses == 0:
      print(f"You lost! The correct number was {num2}")
      time.sleep(2)
      clear()
      print("Thank you for playing the Number Guessing Game")
      time.sleep(3)
      clear()
      sys.exit()

elif mode == "Christmas":
  clear()
  num2 = random.randint(1,31)
  guesses =  4
  print("Number Guessing Game (Christmas mode LIMITED TIME LEFT TO PLAY)!")
  while True:
    num = int(input("Guess a number  🎁 -🎁\n: "))

    if num > num2:
      print(f"Too Christmasy. You have 🎁 {guesses-1}🎁 guesses left")
      guesses-=1
    if num < num2:
      print(f"Too NOT Christmasy. You have 🎁 {guesses-1}🎁 guesses left")
      guesses-=1
    if num == num2:
      print(f"You got it on Christmas time! You finished with 🎁 {guesses-1}🎁 guesses left")
      time.sleep(2)
      clear()
      print("Merry Christmas! Thank you for playing the Number Guessing Game")
      time.sleep(3)
      clear()
      sys.exit()
    if guesses == 0:
      print(f"You are a Grinch! The correct number was 🎁 {num2}🎁")
      time.sleep(2)
      clear()
      print("Merry Christmas! Thank you for playing the Number Guessing Game")
      time.sleep(3)
      clear()
      sys.exit()

elif mode == "Happy New Year":
  clear()
  num2 = random.randint(1,365)
  guesses =  10
  print("Number Guessing Game (Happy New Year mode LIMITED TIME LEFT TO PLAY)!")
  while True:
    num = int(input("Guess a number  🎆 -🎆\n: "))

    if num > num2:
      print(f"We passed New Year's recently. You have 🎆 {guesses-1}🎆 guesses left")
      guesses-=1
    if num < num2:
      print(f"We have many days left till New Year's. You have 🎆 {guesses-1}🎆 guesses left")
      guesses-=1
    if num == num2:
      print(f"Its New Year! You finished with 🎆 {guesses-1}🎆 guesses left")
      time.sleep(2)
      clear()
      print("Happy New Year! Thank you for playing the Number Guessing Game")
      time.sleep(3)
      clear()
      sys.exit()
    if guesses == 0:
      print(f"You are time traveled Cheater! The correct number was 🎆 {num2}🎆")
      time.sleep(2)
      clear()
      print("Happy New Year! Thank you for playing the Number Guessing Game")
      time.sleep(3)
      clear()
      sys.exit()

elif mode == "Coding Week":
  clear()
  num2 = random.randint(10,25)
  guesses =  3
  print("Number Guessing Game (Coding Week mode LIMITED TIME LEFT TO PLAY)!")
  while True:
    num = int(input("Guess a number 💻 -💻\n: "))

    if num > num2:
      print(f"You are coding too much. You have 💻 {guesses-1}💻 guesses left")
      guesses-=1
    if num < num2:
      print(f"You are coding too less. You have 💻 {guesses-1}💻 guesses left")
      guesses-=1
    if num == num2:
      print(f"You won the Jam contest of the best coded game using repl.it! You finished with 💻 {guesses-1}💻 guesses left")
      time.sleep(2)
      clear()
      print("National Coding Week is on 14-20 September! Thank you for playing the Number Guessing Game")
      time.sleep(3)
      clear()
      sys.exit()
    if guesses == 0:
      print(f"You lost the Jam contest of the best coded game using repl.it, now everyone's making fun of you! The correct number was 💻 {num2}💻")
      time.sleep(2)
      clear()
      print("Thank you for playing the Number Guessing Game")
      time.sleep(3)
      clear()
      sys.exit()

elif mode == "347":
  clear()
  num2 = random.randint(347,34700)
  guesses = 347
  print("Number Guessing Game (Secret mode)!")
  while True:
    num = int(input("Guess a secret number 347-34700\n: "))

    if num > num2:
      print(f"Too high. You have {guesses-1} guesses left")
      guesses-=1
    if num < num2:
      print(f"Too low. You have {guesses-1} guesses left")
      guesses-=1
    if num == num2:
      print(f"You got it right! You finished with {guesses-1} guesses left")
      time.sleep(2)
      clear()
      print("Thank you for playing the Number Guessing Game")
      time.sleep(3)
      clear()
      sys.exit()
    if guesses == 0:
      print(f"You lost! The correct number was {num2}")
      time.sleep(2)
      clear()
      print("Thank you for playing the Number Guessing Game")
      time.sleep(3)
      clear()
      sys.exit()
  
elif mode == "Y^^TED":
  clear()
  num2 = random.randint(1,10000)
  guesses = 13
  print("Number Guessing Game (Creator mode)!")
  while True:
    num = int(input("Guess a number 1-10000\n: "))

    if num > num2:
      print(f"Too high. Hello, nice job at finding this gamemode. You have {guesses-1} guesses left")
      guesses-=1
    if num < num2:
      print(f"Too low. I am 12 years old and I love coding. You have {guesses-1} guesses left")
      guesses-=1
    if num == num2:
      print(f"You got it right! You are good at guessing (I guess...). You finished with {guesses-1} guesses left")
      time.sleep(2)
      clear()
      print("Thank you for playing the Number Guessing Game. Also the next secret hint I shall give you is in next mode write 347 as a gamemode")
      time.sleep(6)
      clear()
      sys.exit()
    if guesses == 0:
      print(f"You lost! HOW DID YOU LOSE, try again. If you win therThe correct number was {num2}")
      time.sleep(2)
      clear()
      print("Thank you for playing the Number Guessing Game")
      time.sleep(3)
      clear()
      sys.exit()

elif mode == "Opposite":
  clear()
  num2 = random.randint(-100,-1)
  guesses = 10
  print("Number Guessing Game (Opposite Normal mode))!")
  while True:
    num = int(input("Don't guess a number -100--1\n: "))

    if num > num2:
      print(f"Too low. You have {guesses+1} guesses left")
      guesses-=1
    if num < num2:
      print(f"Too high. You have {guesses+1} guesses left")
      guesses-=1
    if num == num2:
      print(f"You lost! The correct number was {num2}")
      time.sleep(2)
      clear()
      print("NOT Thank you for NOT playing the Number NOT Guessing Game")
      time.sleep(3)
      clear()
      sys.exit()
    if guesses == 0:
      print(f"You got it right! You finished with {guesses+1} guesses left")
      time.sleep(2)
      clear()
      print("NOT Thank you for NOT playing the Number NOT Guessing Game")
      time.sleep(3)
      clear()
      sys.exit()

elif mode == "Glitchy":
  clear()
  num2 = random.randint(-1000000,1000000)
  guesses = 11
  print("Number Guessing Game (Ģ̽̈́͜l̠͚̪̓̎̀i̪͐tc͕̦̔͡h̬̰̝́́͛͊͜ẏ̨͉̥̇͡ ̰̂M͇̠̂͛o̭͕̣̍́͂d̩̀e̼̳̭̅͊̿)!")
  while True:
    num = int(input("Guess a number 1̡̧̡̢̡̡̡̢̛̰̠̺̠̻̣͇̗͖̙̖̣̺̬͈̟͈͍̹͖̤̝͚̼̮̳̩͙̺̣̲̠͕̹̞̪̟̙̺̺͉͇̬̳̙̖̣͚͚̘̰͉̝̞̩̪͕̻͖̰̗͍̺̼͉̤͉̻̳̩̰̰͙̰͙̦̰͙̭̜̥̤̤͇̯͖̈́̈́̽͛͑̏́̍̈͑̍̓̓̐̓̽̒͗́͆̒̿̈́̎̎̍̃̏͊̏̉͑̓̒̇̑̓́́̈͋̐̉̄̔͒̅̒́͋̀͌̍̏̑̿̇̃́̋̇̅̀͛̓̐̉̍͆̑̑̿͛͒̎̚̚̚̕͘͜͢͡͠͡͞͞͝͞͡͡͞͡͡͡͡͡͞ͅͅ-̡̨̨̨̧̢̡̢̨̢̡̢̨̢̨̡̢̢̢̧̡̨̨̢̨̧̢̧̡̛̛̛̛̛̛̛̛̛͍͇̙̪̭̼͓̰̹̟͔̲͈̜͓͍̟̳̲̳̲̟̦̪̣̙̳̜̫̙͓̝͙͙͎͇͎̜͍̩̠̘̩̮̥͉̪̠̰̖̳͎͕̘̥̣͚̰̱̼̲͚͚͈͙̗̰͙̤̮̭̤̖̭̟̳̞̮̼̥̗͍̠̬͔̤̳̳͉̖̦̱̟̩̣͇͚̥̻̳̙͓̪̠͉̮͉̯͍͈͙̻̬̪̠̬̼̣̲̫̰̮̘͉̦̦͖͎̪̬̬̮̝̯̫̤̠͖̱͎͇̭̫͙̱͍̣͓̘͇̝̮̙̟̺͓̣̹̩̘͍̻̠̖̼̬͓̱͚̯͈̘͚̭͇̼̦̮̩͚̰͓̥̮͙͙͍̙̮̗͖͖̥̦̞̺̝̲̹̮̝̳͚̱̱͍̟͕̟͔̱̪̺̣̹̮̗̺̝̗̥̝̯͕̼̲̠̠̠͕̠̬̺̫͓̺̦͍̖̼̬̲̞̝̦͓͇̺̹̲̜͔̣͖̭̟͈̫͚͓̹̲͚̗͂͐͋͛͌̉̈́́̑̈̀̌̃̔̅͊͊̏̓̋̓͐̈́͛́̿́͑̇̎̃̌̀̎̊̾́̈͑͐͛̐̃͒̈́̈́́̾́͛͂͂̅̇̂̊̎́̿̈́̀̿̐̓͐̀̒͒̊̏̾̈̂̀̑̊̀̆̈́̋̅̿̽̄̑̑̑̃̈̆͛̌̂̎͊̓̆͋͐̑̽̀́̾̋͒̒̈́͋̔͋̓͑̊̑̃̒̎͌̆͗̀̃̃͂̽̀͗̒̍͋͆̓̒͊̐̄̀̽̿̊̒̈̇͋̽͒́̿̔́̃̈́̊͆̑́̈́̇͆̆͊͌̾̑͌̄̌͌̿̍̽̓̑̊̇̑̾̓̒̉̉͂̐̐͆̾͂̐̏̅̅̓͐͐̓͑̔̎̈͌̊͑͐̏̆́̈́̂͊̓̎͌͊̉͆͊̔̑͌̌̂͗̾͒̐̂͒͌̈́̽͌̋̐̽͛̉͆̉͛̔̋̒͊́́̂̄͑̌͂̋̓͛̽̋̔̓͊̓̓̈́́͋̆̈́̉̍̊̿͒̒͂͆́̒͘̕̚͘̕̚̕̚͘̚̚͘̚͘͘̚̚̚͢͟͜͢͢͟͜͟͢͜͢͟͜͟͜͢͟͢͢͢͜͢͜͟͟͠͞͡͞͠͡͠͝͞͠͝͝͞͠͡͠͡͡͞͡͡ͅͅͅͅͅͅͅͅ1̨̢̨̧̧̨̡̡̡̡̢̢̡̡̨̨̧̡̧̨̡̨̢̡̢̡̨̧̨̡̨̨̡̡̢̛̛̛̛̛͙̜̤̺͇͈̗͙̻̩̪͚̜̙͖͉̟͍̺̫̘͚̼̬̥̦̺̳̹͔͉̝̖̩̟̫͙͇̟̱̻͎̫̬̣̯̠̬̪̤̰̰̮͍̭̫̝͓͓̥̦͙͈͔̺̼̥̮̬̥̝͖͍͇̠͓̺̲͍̬̲͇̙̬͕̪̪͙̺̻̝̻̞̟̮͍͍͉̟̝̻͖̦̭̹̫͖̙͔̳͕͖͎̣͎̜̰̺̩̫̻͕̜͈̟͎̯̭̳͔̣͕̞̱̠̹̱͖̟̣͚̟̼̬̯͕͉͍̲̺̘̯͚̤̟̱̙̤͓̱̮̬͚̰̗̬̼̥̯̰̹̮͇̥̩̝̝̺͓̘͙͍͎̗͍̱̩͉̥̜͕̟͙͔̫͕̺̮̪̹̜̟̺͉̠̝̹̲͕̯͖̩̰̪̫͈̼͈̦̥̜̰̰̭͓̼̤̖̰̰͎̬͎͚̰̖̗͉̦̳͖̪͔̺̘̭̥͚͓̞͍̙̲̣͙̼̭̹̳͖̺̤̲̙̲̞̲͕̣̟̣̰̝̯̺̱͖͎̩̤̠̖̜͍̯͍̳͖͓̤̞͎͉̹̜͇̞͉̭̤̩̳͔̱̜̝̹̭͖̖̹̖̯̪̦̮̗͈͔̲͕̝̟̭̬͎͓͙̞̖͍̱͇̟̝̯̠̺̠̲͖̳̻̜̩̜̼̳̫̘͇͓̜̻̘̖̤̭̣̠̬̇̎̀̌̌͊͋̀̀̌̄̀̍͊̒́̂͋̊͌̀̈́̏́̀̿̒́̊̄̀̓̌̑͒̔̍̅̓̍̿͌̎̍̔́̀͊͑́̒͗̎̓̓͋́̉̓̏̄͗̎̓̈́͂̄̉͋͗̒̈̍̀̈͆̒̉̓̈́̋́̌̅͌͊̿̐̍̃̃͋̍̉́̎̇͑͌̒̆̋͛̾͌͌̂̋͋̽͊̏͊̆̽́̿̇̋̊̊́̋͗̊̍̆́̔͋́̽̀͒̅̑͛͂̉̄̃͋̌͒̌̿̒͆̇̈́̂̆͐̅̽͒̓͋̍̅̎̇͂̅͊̾̽̓͛͑̂̀͌̀̉̔̅́̆̓̿̇̊̂̊͊̔͑͊̓͒̐̔̋̑͌̊̒͒͒̎̏͂̈͋̅̃̅̏̍͗͛̿̅̊͂̃̏̽̄̉̓͂̄̃̌͐̑͛̋̆̀̀̍̀̇́̔̐̉̈̄͋̀͛̅̀͐̿̀̊̋̊̇̓̅̌̈́̃́͑̎͐̋̀̂̌͆́́͗̀̀͌̐̾͛̾̔̿͆́̓́̍̅̀̔́̇͐͂́́̈́́̓͊̽̃̽͌̔̃̓̋͑́̀̾̈͆̌̽̀̌̈͗͛̓͛́͑́̓̂̄̾̓̏̈̀̀̑̌̀̀̀̿̎͗̾̉̂̽̈̃̿̀̿̌̿̋́̇͑̄́̕̕̕̚͘̚̚̚̕̕̚̚̕͘̕̚̕̚̚̕̕̕̕͘̚̚̕͘͘̕̕͘͟͟͟͜͜͟͟͢͢͜͢͟͜͜͢͢͟͢͟͜͟͜͜͢͜͟͢͟͠͡͡͝͠͝͝͝͞͝͝͡͠͠͝͡͡͝͠͠͠͝͞͝͞͝͝͞͝͝͡͞͞ͅͅͅͅͅ0̡̧̢̧̢̧̡̢̡̨̧̧̢̧̨̧̡̡̧̨̧̡̧̨̛̛̛̛̛͎͚͚̺̪̱̰̗̹͇̘̰̜̩̞͈͉̼̩̰̻̲̮̘̥̗̳̳͍̳͖̪̯̱͇̥͍͇̺̻̗͓̲̦̳̰̗͓̱͈̼̼̮̝̥̼̖̫̲̭͓̟̟̻̫͙̱̱̤͓̱̬͉̠͔̞̪͈̤̼͔̩̥͈̜̜̦̥̠̻̭̩͚͎̙̹͖̦̲̭̝̙̻̩̠͓̼̯͇̺̲̟͍͉̺̙̣̳̤̤̦͔̥̼̪̥̻̥̜̭̭̻̺̲̜͎̫̤̱̳̙͉͖͕̭͕̲͎̮̦̪͚̹̠̠̠̩̯͓̞͕̬͚̜̩̟̝̩̣̼̹̣̪͎̙̖̼͚̹̗̼̼͕̘̖̩͖̩̳͓̣̼̭̯̜̤̗̰͍̠̲̗̝̰̭̺̯͇̪̞͇̻̗͇̲̾͌̐̑̑͌̃̔̐̆̏̈̄̾̽̀̐͆͑͂̄͌̾͒̾̈́̔̋͆̃̋̾̐́͌̌̽̅͋̽́̊̏̃̾͋͗̏̋͛̄̿̎̍̂̿͗̐̈̓̋̂͑̌̌͂̀̔̏̋͂͒͌̓͒̓̇͐͌̅̓͌͒̌̌̅͗̀͆̀̀̅̾͊̓̎̈́̍̎̓͑̆̉͛͑̽̑̀̐̎̊̈̉̌̏̔̉̄̐̀͒̏̓͐͑͛̏̉̉͛̀̀̅̆͂͊̏͋͋͊͊̊̊̽̾̉́̿̀͌̏̀̓̒̄͆̌̑̒͌̎͛̀͋̈́͋͒̏͒̉̐̀̑̊̈̒͒̃͊̿̌͋̍̒̾͌̄̽͒̄̇̃̓́̋̃͑̆́͑̄̈́̈́̾̾̂̀̈́̎͘͘͘͘̚̕̕̚͘͘͘̚̕̕̕͜͢͜͟͜͟͜͢͟͜͢͢͜͜͜͠͡͝͞͝͡͡͝͞͡͡͡͝͡͡͠͠͡͡͡͝͞͝͞͡ͅ0̢̧̡̨̧̛̛̙̳̯͉̥̝̙̺̣̝̤͉̘̘̙̦̻͙̬̯̜̝͓̱̖̥̭̪̦̰̳̯̤͕͙͇̣̖̻̤̖͎̹́̀̓̊̏̊̓̊͒͐͊̉̂́̓̈͗̋͑̿̓̍̒̋̍̒͂̾̈̈͋̀͂̌̋́̑̽̉̉͘͘̚͢͠͡͞͝\n: "))

    if num > num2:
      print(f"Too high. You have 0̡̢̧̨̧̧͇̟̣̯͉̝̠̦̘̠̭͙͕̬̟̱̲̥̩͕̯̱̳̘̘̜̰̜͇̯̗̝͕̘̲̦̰͇͕͚͔̲̦̞̗̯͊͒̑͋͐́̏̐͆̊̉͐̄͛̓̏̍͊̏̎͌̀̉̈́͛̂́͑͆̌̿̉̇̒͋̇̒̾͆̔̇̾͗̋͆͂͐͒̅̑͊̍̀̚̕̕͘͢͟͟͢͟͢͝͝͝͡ͅͅͅ0̡̡̢̨̢̨̧̛̛̛̥̲̙͖̲̪̙͓̹̮͉̼͎̣̖̯̦̟͕͉̻͉̤͙̹͍̞̫͍̻̞̫͎̞̯̥̦̭̦͍̪̻̱̙̰̖̝̝̭̘͚̪͎̼̘̳͎̝̥̺͓̗̦͇͇̰̰̘̙͇̱̥͓͚͕͚̦̘̖̻̻̗̻̲͚̻̪̭̤̠̯̳̼̯̣̝͖̙͉̯̥̣̇͊̃̈͑̀̍̓̂̋͊͆̓̒͒͆̀̊̎̅̌̍́̓̑͐͆͌̈́̔̌̇̐̿̓̊̅̏̽̇͂̾̃̆̓͊̌̆͂͐̇̆̌̈́͒͛͋̐́̈́͐̂̓̿̏͆̃̔̄͌͆̓͆̍͛́̆͑̂͒̄͂̎͐̀͋̓͆̏̾̏̍͐̾̑̍̃͘͘͘̚͘̚͘͘̚͘̚͜͟͜͟͟͟͟͢͡͝͡͞͝͠͠͠͠͝͝ͅͅͅͅͅ0̧̡̧̡̡̨̢̧̨̧̡̡̨̧̢̢̢̧̢̧̛̛̲͔͚̪͕̩̯̟̜̹̻̼̤̘͚͙̪̪̝̭̦̰̰̼̦͖̝̗̰̺̼͖̼̹̠̗̜͇͔̣̖̪̞͕̻̪̣̜̠͙̻̣̥̼̳̫̪͓͈̹̞̯̤̞̠̪̫̟̦͚͇̮̰̦͕͈̭̹̖̼̜̰̗̬͍̯͇͚̙̳̥̬͙̗̼̳̳̼̣̲͙̗͖͕̗̞̟̰̖͚̫͕͍̭͚͚̱͉͈̱̰͇͐͋͛̄̎̀̈́̔̿̄̊̀̇͆̀͗͐̔̍̎͌̌̊͐͂̀͂̀̋̽̓̎̅̃̔͑̈̅̇̇̐̊̃͗̆̇̾̾̄͋̑̈́̿́̾̌̈́̀̆̓͆̈́͋̎͂̎̃̔́̄̎̋̂̎̓̐̒͛̏̄̐͌̈́̏͑̓̃͑̊͛̓͆̅̈̿̽̀́̌̔̈̀͛͌̿͌͐̀͌͐̔͌́͒̏͗͒̓̽̅͑̽̚͘̚̕̕͘̚̕͘͘̚͘͘̕͟͢͢͜͟͠͠͠͝͠͠͞͞͠͠͝͞͞͠͞ͅͅͅͅͅͅ0̧̨̢̧̨̧̡̡̨̧̨̨̡̨̨̢̡̨̨̧̨̛̛̛̛̛̛̛͉̫͖̭͕̦͖̳͙̩͕̱̳̥̥̦͕̦̼͕̠̮̫̠̮̻͍͕̘̖̬̞̲̯̞̦͉͚̘̞̜̻͍̩̦̼̺̦̤̠͔̤̥̯̝̟̻̟͈͉̗̥̖̪̱̦̟̼̪̖̰͈̰͖̱̯̭̗͈̮͈̺̭͕͖͇͇͓̖̱͚̱͈͇̲̘͕̘̟͈̼̱̬̪͙̳͈̰̹̠̩̩̯̖̤̠̩̭̻̱͇̞͈̝̹̦̱̠̭͔͕̪̬̤̥̙͖̪̯̯̜̠̙̭͈̖͇̘̮͚̻͕̏̀̐̋̂̀̌̑̄̄̿̏͒̊̊͊̓̽̄͗̾̈́̿͋́̏͐̊̓͒͌̓͗͋́͑͑͒̂͋̂̾̑̈͆̉͗́̎͑͊͗̉͌̃͗͌̋̀̏̑̎̽̓̏̈͋́͑̓͒̓̒͒͒̆͗̏̈̅̈̂̆̆̃́̉͌̎͒̔͑͆̅̔͗͗̓͐͒͆̌̌̽͊͋̽̌͗̂̑̇̎̂̒̔̂́͛́͂̋̃͗͛̈̆̅͐̽͗̌̔́̑̀̈́̔͂̀͋̽̆̄̑́̑̂́͆́́̈́̔̐̑͋̎̔̊̄̎͊̐̕͘̚̕̚͘̚̕̚̕̚̚̚͢͢͢͟͜͢͜͟͢͢͜͟͞͡͝͡͡͡͝͠͞ͅͅͅͅͅͅͅͅ guesses left")
      guesses-=1
    if num < num2:
      print(f"Too low. You have 0̡̢̧̨̧̧͇̟̣̯͉̝̠̦̘̠̭͙͕̬̟̱̲̥̩͕̯̱̳̘̘̜̰̜͇̯̗̝͕̘̲̦̰͇͕͚͔̲̦̞̗̯͊͒̑͋͐́̏̐͆̊̉͐̄͛̓̏̍͊̏̎͌̀̉̈́͛̂́͑͆̌̿̉̇̒͋̇̒̾͆̔̇̾͗̋͆͂͐͒̅̑͊̍̀̚̕̕͘͢͟͟͢͟͢͝͝͝͡ͅͅͅ0̡̡̢̨̢̨̧̛̛̛̥̲̙͖̲̪̙͓̹̮͉̼͎̣̖̯̦̟͕͉̻͉̤͙̹͍̞̫͍̻̞̫͎̞̯̥̦̭̦͍̪̻̱̙̰̖̝̝̭̘͚̪͎̼̘̳͎̝̥̺͓̗̦͇͇̰̰̘̙͇̱̥͓͚͕͚̦̘̖̻̻̗̻̲͚̻̪̭̤̠̯̳̼̯̣̝͖̙͉̯̥̣̇͊̃̈͑̀̍̓̂̋͊͆̓̒͒͆̀̊̎̅̌̍́̓̑͐͆͌̈́̔̌̇̐̿̓̊̅̏̽̇͂̾̃̆̓͊̌̆͂͐̇̆̌̈́͒͛͋̐́̈́͐̂̓̿̏͆̃̔̄͌͆̓͆̍͛́̆͑̂͒̄͂̎͐̀͋̓͆̏̾̏̍͐̾̑̍̃͘͘͘̚͘̚͘͘̚͘̚͜͟͜͟͟͟͟͢͡͝͡͞͝͠͠͠͠͝͝ͅͅͅͅͅ0̧̡̧̡̡̨̢̧̨̧̡̡̨̧̢̢̢̧̢̧̛̛̲͔͚̪͕̩̯̟̜̹̻̼̤̘͚͙̪̪̝̭̦̰̰̼̦͖̝̗̰̺̼͖̼̹̠̗̜͇͔̣̖̪̞͕̻̪̣̜̠͙̻̣̥̼̳̫̪͓͈̹̞̯̤̞̠̪̫̟̦͚͇̮̰̦͕͈̭̹̖̼̜̰̗̬͍̯͇͚̙̳̥̬͙̗̼̳̳̼̣̲͙̗͖͕̗̞̟̰̖͚̫͕͍̭͚͚̱͉͈̱̰͇͐͋͛̄̎̀̈́̔̿̄̊̀̇͆̀͗͐̔̍̎͌̌̊͐͂̀͂̀̋̽̓̎̅̃̔͑̈̅̇̇̐̊̃͗̆̇̾̾̄͋̑̈́̿́̾̌̈́̀̆̓͆̈́͋̎͂̎̃̔́̄̎̋̂̎̓̐̒͛̏̄̐͌̈́̏͑̓̃͑̊͛̓͆̅̈̿̽̀́̌̔̈̀͛͌̿͌͐̀͌͐̔͌́͒̏͗͒̓̽̅͑̽̚͘̚̕̕͘̚̕͘͘̚͘͘̕͟͢͢͜͟͠͠͠͝͠͠͞͞͠͠͝͞͞͠͞ͅͅͅͅͅͅ0̧̨̢̧̨̧̡̡̨̧̨̨̡̨̨̢̡̨̨̧̨̛̛̛̛̛̛̛͉̫͖̭͕̦͖̳͙̩͕̱̳̥̥̦͕̦̼͕̠̮̫̠̮̻͍͕̘̖̬̞̲̯̞̦͉͚̘̞̜̻͍̩̦̼̺̦̤̠͔̤̥̯̝̟̻̟͈͉̗̥̖̪̱̦̟̼̪̖̰͈̰͖̱̯̭̗͈̮͈̺̭͕͖͇͇͓̖̱͚̱͈͇̲̘͕̘̟͈̼̱̬̪͙̳͈̰̹̠̩̩̯̖̤̠̩̭̻̱͇̞͈̝̹̦̱̠̭͔͕̪̬̤̥̙͖̪̯̯̜̠̙̭͈̖͇̘̮͚̻͕̏̀̐̋̂̀̌̑̄̄̿̏͒̊̊͊̓̽̄͗̾̈́̿͋́̏͐̊̓͒͌̓͗͋́͑͑͒̂͋̂̾̑̈͆̉͗́̎͑͊͗̉͌̃͗͌̋̀̏̑̎̽̓̏̈͋́͑̓͒̓̒͒͒̆͗̏̈̅̈̂̆̆̃́̉͌̎͒̔͑͆̅̔͗͗̓͐͒͆̌̌̽͊͋̽̌͗̂̑̇̎̂̒̔̂́͛́͂̋̃͗͛̈̆̅͐̽͗̌̔́̑̀̈́̔͂̀͋̽̆̄̑́̑̂́͆́́̈́̔̐̑͋̎̔̊̄̎͊̐̕͘̚̕̚͘̚̕̚̕̚̚̚͢͢͢͟͜͢͜͟͢͢͜͟͞͡͝͡͡͡͝͠͞ͅͅͅͅͅͅͅͅ guesses left")
      guesses-=1
    if num == num2:
      print(f"You got it right! You finished with 0̡̢̧̨̧̧͇̟̣̯͉̝̠̦̘̠̭͙͕̬̟̱̲̥̩͕̯̱̳̘̘̜̰̜͇̯̗̝͕̘̲̦̰͇͕͚͔̲̦̞̗̯͊͒̑͋͐́̏̐͆̊̉͐̄͛̓̏̍͊̏̎͌̀̉̈́͛̂́͑͆̌̿̉̇̒͋̇̒̾͆̔̇̾͗̋͆͂͐͒̅̑͊̍̀̚̕̕͘͢͟͟͢͟͢͝͝͝͡ͅͅͅ0̡̡̢̨̢̨̧̛̛̛̥̲̙͖̲̪̙͓̹̮͉̼͎̣̖̯̦̟͕͉̻͉̤͙̹͍̞̫͍̻̞̫͎̞̯̥̦̭̦͍̪̻̱̙̰̖̝̝̭̘͚̪͎̼̘̳͎̝̥̺͓̗̦͇͇̰̰̘̙͇̱̥͓͚͕͚̦̘̖̻̻̗̻̲͚̻̪̭̤̠̯̳̼̯̣̝͖̙͉̯̥̣̇͊̃̈͑̀̍̓̂̋͊͆̓̒͒͆̀̊̎̅̌̍́̓̑͐͆͌̈́̔̌̇̐̿̓̊̅̏̽̇͂̾̃̆̓͊̌̆͂͐̇̆̌̈́͒͛͋̐́̈́͐̂̓̿̏͆̃̔̄͌͆̓͆̍͛́̆͑̂͒̄͂̎͐̀͋̓͆̏̾̏̍͐̾̑̍̃͘͘͘̚͘̚͘͘̚͘̚͜͟͜͟͟͟͟͢͡͝͡͞͝͠͠͠͠͝͝ͅͅͅͅͅ0̧̡̧̡̡̨̢̧̨̧̡̡̨̧̢̢̢̧̢̧̛̛̲͔͚̪͕̩̯̟̜̹̻̼̤̘͚͙̪̪̝̭̦̰̰̼̦͖̝̗̰̺̼͖̼̹̠̗̜͇͔̣̖̪̞͕̻̪̣̜̠͙̻̣̥̼̳̫̪͓͈̹̞̯̤̞̠̪̫̟̦͚͇̮̰̦͕͈̭̹̖̼̜̰̗̬͍̯͇͚̙̳̥̬͙̗̼̳̳̼̣̲͙̗͖͕̗̞̟̰̖͚̫͕͍̭͚͚̱͉͈̱̰͇͐͋͛̄̎̀̈́̔̿̄̊̀̇͆̀͗͐̔̍̎͌̌̊͐͂̀͂̀̋̽̓̎̅̃̔͑̈̅̇̇̐̊̃͗̆̇̾̾̄͋̑̈́̿́̾̌̈́̀̆̓͆̈́͋̎͂̎̃̔́̄̎̋̂̎̓̐̒͛̏̄̐͌̈́̏͑̓̃͑̊͛̓͆̅̈̿̽̀́̌̔̈̀͛͌̿͌͐̀͌͐̔͌́͒̏͗͒̓̽̅͑̽̚͘̚̕̕͘̚̕͘͘̚͘͘̕͟͢͢͜͟͠͠͠͝͠͠͞͞͠͠͝͞͞͠͞ͅͅͅͅͅͅ0̧̨̢̧̨̧̡̡̨̧̨̨̡̨̨̢̡̨̨̧̨̛̛̛̛̛̛̛͉̫͖̭͕̦͖̳͙̩͕̱̳̥̥̦͕̦̼͕̠̮̫̠̮̻͍͕̘̖̬̞̲̯̞̦͉͚̘̞̜̻͍̩̦̼̺̦̤̠͔̤̥̯̝̟̻̟͈͉̗̥̖̪̱̦̟̼̪̖̰͈̰͖̱̯̭̗͈̮͈̺̭͕͖͇͇͓̖̱͚̱͈͇̲̘͕̘̟͈̼̱̬̪͙̳͈̰̹̠̩̩̯̖̤̠̩̭̻̱͇̞͈̝̹̦̱̠̭͔͕̪̬̤̥̙͖̪̯̯̜̠̙̭͈̖͇̘̮͚̻͕̏̀̐̋̂̀̌̑̄̄̿̏͒̊̊͊̓̽̄͗̾̈́̿͋́̏͐̊̓͒͌̓͗͋́͑͑͒̂͋̂̾̑̈͆̉͗́̎͑͊͗̉͌̃͗͌̋̀̏̑̎̽̓̏̈͋́͑̓͒̓̒͒͒̆͗̏̈̅̈̂̆̆̃́̉͌̎͒̔͑͆̅̔͗͗̓͐͒͆̌̌̽͊͋̽̌͗̂̑̇̎̂̒̔̂́͛́͂̋̃͗͛̈̆̅͐̽͗̌̔́̑̀̈́̔͂̀͋̽̆̄̑́̑̂́͆́́̈́̔̐̑͋̎̔̊̄̎͊̐̕͘̚̕̚͘̚̕̚̕̚̚̚͢͢͢͟͜͢͜͟͢͢͜͟͞͡͝͡͡͡͝͠͞ͅͅͅͅͅͅͅͅ guesses left")
      time.sleep(2)
      clear()
      print("Thank you for playing the Number Guessing Game")
      time.sleep(3)
      clear()
      sys.exit()
    if guesses == 0:
      print(f"You lost! The correct number was 0̡̢̧̨̧̧͇̟̣̯͉̝̠̦̘̠̭͙͕̬̟̱̲̥̩͕̯̱̳̘̘̜̰̜͇̯̗̝͕̘̲̦̰͇͕͚͔̲̦̞̗̯͊͒̑͋͐́̏̐͆̊̉͐̄͛̓̏̍͊̏̎͌̀̉̈́͛̂́͑͆̌̿̉̇̒͋̇̒̾͆̔̇̾͗̋͆͂͐͒̅̑͊̍̀̚̕̕͘͢͟͟͢͟͢͝͝͝͡ͅͅͅ0̡̡̢̨̢̨̧̛̛̛̥̲̙͖̲̪̙͓̹̮͉̼͎̣̖̯̦̟͕͉̻͉̤͙̹͍̞̫͍̻̞̫͎̞̯̥̦̭̦͍̪̻̱̙̰̖̝̝̭̘͚̪͎̼̘̳͎̝̥̺͓̗̦͇͇̰̰̘̙͇̱̥͓͚͕͚̦̘̖̻̻̗̻̲͚̻̪̭̤̠̯̳̼̯̣̝͖̙͉̯̥̣̇͊̃̈͑̀̍̓̂̋͊͆̓̒͒͆̀̊̎̅̌̍́̓̑͐͆͌̈́̔̌̇̐̿̓̊̅̏̽̇͂̾̃̆̓͊̌̆͂͐̇̆̌̈́͒͛͋̐́̈́͐̂̓̿̏͆̃̔̄͌͆̓͆̍͛́̆͑̂͒̄͂̎͐̀͋̓͆̏̾̏̍͐̾̑̍̃͘͘͘̚͘̚͘͘̚͘̚͜͟͜͟͟͟͟͢͡͝͡͞͝͠͠͠͠͝͝ͅͅͅͅͅ0̧̡̧̡̡̨̢̧̨̧̡̡̨̧̢̢̢̧̢̧̛̛̲͔͚̪͕̩̯̟̜̹̻̼̤̘͚͙̪̪̝̭̦̰̰̼̦͖̝̗̰̺̼͖̼̹̠̗̜͇͔̣̖̪̞͕̻̪̣̜̠͙̻̣̥̼̳̫̪͓͈̹̞̯̤̞̠̪̫̟̦͚͇̮̰̦͕͈̭̹̖̼̜̰̗̬͍̯͇͚̙̳̥̬͙̗̼̳̳̼̣̲͙̗͖͕̗̞̟̰̖͚̫͕͍̭͚͚̱͉͈̱̰͇͐͋͛̄̎̀̈́̔̿̄̊̀̇͆̀͗͐̔̍̎͌̌̊͐͂̀͂̀̋̽̓̎̅̃̔͑̈̅̇̇̐̊̃͗̆̇̾̾̄͋̑̈́̿́̾̌̈́̀̆̓͆̈́͋̎͂̎̃̔́̄̎̋̂̎̓̐̒͛̏̄̐͌̈́̏͑̓̃͑̊͛̓͆̅̈̿̽̀́̌̔̈̀͛͌̿͌͐̀͌͐̔͌́͒̏͗͒̓̽̅͑̽̚͘̚̕̕͘̚̕͘͘̚͘͘̕͟͢͢͜͟͠͠͠͝͠͠͞͞͠͠͝͞͞͠͞ͅͅͅͅͅͅ0̧̨̢̧̨̧̡̡̨̧̨̨̡̨̨̢̡̨̨̧̨̛̛̛̛̛̛̛͉̫͖̭͕̦͖̳͙̩͕̱̳̥̥̦͕̦̼͕̠̮̫̠̮̻͍͕̘̖̬̞̲̯̞̦͉͚̘̞̜̻͍̩̦̼̺̦̤̠͔̤̥̯̝̟̻̟͈͉̗̥̖̪̱̦̟̼̪̖̰͈̰͖̱̯̭̗͈̮͈̺̭͕͖͇͇͓̖̱͚̱͈͇̲̘͕̘̟͈̼̱̬̪͙̳͈̰̹̠̩̩̯̖̤̠̩̭̻̱͇̞͈̝̹̦̱̠̭͔͕̪̬̤̥̙͖̪̯̯̜̠̙̭͈̖͇̘̮͚̻͕̏̀̐̋̂̀̌̑̄̄̿̏͒̊̊͊̓̽̄͗̾̈́̿͋́̏͐̊̓͒͌̓͗͋́͑͑͒̂͋̂̾̑̈͆̉͗́̎͑͊͗̉͌̃͗͌̋̀̏̑̎̽̓̏̈͋́͑̓͒̓̒͒͒̆͗̏̈̅̈̂̆̆̃́̉͌̎͒̔͑͆̅̔͗͗̓͐͒͆̌̌̽͊͋̽̌͗̂̑̇̎̂̒̔̂́͛́͂̋̃͗͛̈̆̅͐̽͗̌̔́̑̀̈́̔͂̀͋̽̆̄̑́̑̂́͆́́̈́̔̐̑͋̎̔̊̄̎͊̐̕͘̚̕̚͘̚̕̚̕̚̚̚͢͢͢͟͜͢͜͟͢͢͜͟͞͡͝͡͡͡͝͠͞ͅͅͅͅͅͅͅͅ{num2}0̡̢̧̨̧̧͇̟̣̯͉̝̠̦̘̠̭͙͕̬̟̱̲̥̩͕̯̱̳̘̘̜̰̜͇̯̗̝͕̘̲̦̰͇͕͚͔̲̦̞̗̯͊͒̑͋͐́̏̐͆̊̉͐̄͛̓̏̍͊̏̎͌̀̉̈́͛̂́͑͆̌̿̉̇̒͋̇̒̾͆̔̇̾͗̋͆͂͐͒̅̑͊̍̀̚̕̕͘͢͟͟͢͟͢͝͝͝͡ͅͅͅ0̡̡̢̨̢̨̧̛̛̛̥̲̙͖̲̪̙͓̹̮͉̼͎̣̖̯̦̟͕͉̻͉̤͙̹͍̞̫͍̻̞̫͎̞̯̥̦̭̦͍̪̻̱̙̰̖̝̝̭̘͚̪͎̼̘̳͎̝̥̺͓̗̦͇͇̰̰̘̙͇̱̥͓͚͕͚̦̘̖̻̻̗̻̲͚̻̪̭̤̠̯̳̼̯̣̝͖̙͉̯̥̣̇͊̃̈͑̀̍̓̂̋͊͆̓̒͒͆̀̊̎̅̌̍́̓̑͐͆͌̈́̔̌̇̐̿̓̊̅̏̽̇͂̾̃̆̓͊̌̆͂͐̇̆̌̈́͒͛͋̐́̈́͐̂̓̿̏͆̃̔̄͌͆̓͆̍͛́̆͑̂͒̄͂̎͐̀͋̓͆̏̾̏̍͐̾̑̍̃͘͘͘̚͘̚͘͘̚͘̚͜͟͜͟͟͟͟͢͡͝͡͞͝͠͠͠͠͝͝ͅͅͅͅͅ0̧̡̧̡̡̨̢̧̨̧̡̡̨̧̢̢̢̧̢̧̛̛̲͔͚̪͕̩̯̟̜̹̻̼̤̘͚͙̪̪̝̭̦̰̰̼̦͖̝̗̰̺̼͖̼̹̠̗̜͇͔̣̖̪̞͕̻̪̣̜̠͙̻̣̥̼̳̫̪͓͈̹̞̯̤̞̠̪̫̟̦͚͇̮̰̦͕͈̭̹̖̼̜̰̗̬͍̯͇͚̙̳̥̬͙̗̼̳̳̼̣̲͙̗͖͕̗̞̟̰̖͚̫͕͍̭͚͚̱͉͈̱̰͇͐͋͛̄̎̀̈́̔̿̄̊̀̇͆̀͗͐̔̍̎͌̌̊͐͂̀͂̀̋̽̓̎̅̃̔͑̈̅̇̇̐̊̃͗̆̇̾̾̄͋̑̈́̿́̾̌̈́̀̆̓͆̈́͋̎͂̎̃̔́̄̎̋̂̎̓̐̒͛̏̄̐͌̈́̏͑̓̃͑̊͛̓͆̅̈̿̽̀́̌̔̈̀͛͌̿͌͐̀͌͐̔͌́͒̏͗͒̓̽̅͑̽̚͘̚̕̕͘̚̕͘͘̚͘͘̕͟͢͢͜͟͠͠͠͝͠͠͞͞͠͠͝͞͞͠͞ͅͅͅͅͅͅ0̧̨̢̧̨̧̡̡̨̧̨̨̡̨̨̢̡̨̨̧̨̛̛̛̛̛̛̛͉̫͖̭͕̦͖̳͙̩͕̱̳̥̥̦͕̦̼͕̠̮̫̠̮̻͍͕̘̖̬̞̲̯̞̦͉͚̘̞̜̻͍̩̦̼̺̦̤̠͔̤̥̯̝̟̻̟͈͉̗̥̖̪̱̦̟̼̪̖̰͈̰͖̱̯̭̗͈̮͈̺̭͕͖͇͇͓̖̱͚̱͈͇̲̘͕̘̟͈̼̱̬̪͙̳͈̰̹̠̩̩̯̖̤̠̩̭̻̱͇̞͈̝̹̦̱̠̭͔͕̪̬̤̥̙͖̪̯̯̜̠̙̭͈̖͇̘̮͚̻͕̏̀̐̋̂̀̌̑̄̄̿̏͒̊̊͊̓̽̄͗̾̈́̿͋́̏͐̊̓͒͌̓͗͋́͑͑͒̂͋̂̾̑̈͆̉͗́̎͑͊͗̉͌̃͗͌̋̀̏̑̎̽̓̏̈͋́͑̓͒̓̒͒͒̆͗̏̈̅̈̂̆̆̃́̉͌̎͒̔͑͆̅̔͗͗̓͐͒͆̌̌̽͊͋̽̌͗̂̑̇̎̂̒̔̂́͛́͂̋̃͗͛̈̆̅͐̽͗̌̔́̑̀̈́̔͂̀͋̽̆̄̑́̑̂́͆́́̈́̔̐̑͋̎̔̊̄̎͊̐̕͘̚̕̚͘̚̕̚̕̚̚̚͢͢͢͟͜͢͜͟͢͢͜͟͞͡͝͡͡͡͝͠͞ͅͅͅͅͅͅͅͅ")
      time.sleep(2)
      clear()
      print("Ţ̧̨̨̙͉̱͖̗͎͚̭̗͍̖̠̲̤͉͇̫̤̮̭̺͍͖̪͍͚̭̣̻̥̖̰͒̂̈̊͂̀̔̓̽̉̎͛̑̅̎͐̒̉͛̄̾̈́̒͆̈̂̑͑̀̑̇̑̀͘͘̚͢͟͞͞͠͝ͅͅḫ̡͙̱͈̫͈̹̭̝̩̫̻̝͎̾̾̊̀͌̊́̐͂͂̊́͑̑̋̅̏̀͜͟͝ͅͅą̧̧̨̨̞͕͔̲͎̲̲̻̟̮͍͙͓̗̠̣̜̙̹͖̟̣̤̦̗̫̟̺͚̞̳̹̘͎͖͐͒̓̔̀͐́̏̐̈́̽̿̍̇̋̂͗̋̑̏͋͑͊̊̏̃̄́̌̓̇̈́͊̄͘̕̚͡͠͠͝ͅń̛̫̝̮̞̮̩͕̥͑̉̑͛̂͌̚͢͠ͅk̡̧̢̢̲̘̥͇̼̮̻͉̦̜͉̲̞̫̻͍̩͉͍̠̫̟̋̓͛̎̋͂̽̽́͆̓͌͋̀̈́̈́̂̍̒̃̑̏͆̇̚̕͟͞͝ͅ ̢̨̧̡̨̛̞͓͎̲̙̝̦̥̳̪̤͍̮̥̦̤̬̱̭̪̬̩͕̻̺̼̘͓͎̩̗̗͕̘̱͍͒͑̂̂̅͐̽̆͋̉̽̒́̄̏̆̅́̋̌̇͑̂̆̎̐̍͆̊̆͛̃̃̑͛̊̐̃͋̌͂̀̕͜͟͢͝ͅy̨̧̯͍̫̪̲̤̲̼͕͓͉̯̪͎̳̽̇͆̍͂́̌́̃̅͊͂̽̽͂̈̑͂̏͜ͅo̭̹̥̲̣͎̝̖̜̪̭̗̹͖͍͚͉̦̱̪̺͍̦͓̝̠̩̟̭͇̎̀͐͑̓̂̑̏͂̆͂̓͌̏̓̽͐̋̎̄͒̂̅̈́̓̏̒̌̎̆̋̚͟͜͝͞ͅͅų̛̛̘̤̳͉̞̘̫̒̓̃̄͛̏ ͕̞̃̋f̢͓̭͈͓̤̲̩̙̯̜̰̱̺͎̲̘͇̩̘͈̩͈̩̱̫̰̄͑̂̂̈́̉̌̔̊̿͒͆̿̊͑̀̊̓͌̓̓͐̕͘̕͠͞ờ̧̡̨̨̡̢̢̛͇̺̦̺͕̝͍̠̠̤̬͎̫͈͉͕̯̙̩̬̲̠̱̝̹̭͚͊̍̓̾̈̋̒̍̈̀̒͒̓͆̊̊̔̊̒͆̋̔͊͛̓͗̇̀͘̕͜͝͞͝ͅŗ̨̧̨̨̡͔͓̞̘̤̹̰͖̳̜̼̝͕͖͇̠̬̩̥̖̻͈̥̮̬̗͍͖͇̤͍̭̘̬̹̬͇̣͛̆̓́̂̒̇͛́͛͗͋͌̄͊̆͊̓̔̃́͂̾̄̈́̋̾̂̇́̏̑̋͒̐͊͊͆̓̅̽̊͆͘͢͜͠͡͝ͅ ̨̨̨̡̛̛̩̟̣̝̟̩̗͚̱̣̳͕͙̞̦̺͉̣͔̟̣̱͇̣́́̉̀̈̌̏͑̈̑͋͌͌̔́̔͛̔̀́̚̚͘͢͠͝͠͞p̧̢̢̨̡̧̟̘͉̙̲̗͔͓͇̥͓̥͈̯̳̠̙̦͕͎̮͍͖̖̪̲̗̫̑̌̉̓͋̊͒͐̌̋̓̾̅͆͆̄̈̄͐͆͐̏͒̈́̅̍̈́͛̀̐͂͘͜͜͞͡͝͝l̢̡̛̺̳͍̪͖̳̲̘͙͗̋̑͂́̈́͗̀̓͐͜͢͠͡ả̱̦̻̂̀̒̀͜ͅy̡̡̡̧̮̺͖̱̣͍̭̬͇̲͙̝̬̳̝̼̬̦̠̼͉̲̰͓̲̰͎̳̆̉̊̈́͂͋̀̿̐̅̉̀̈̇̈̆́̄̿̓̐̇̾͛͂͒͐̆̕͜͢͞͡͠͡͝ͅi̯͚̜̼͔̹̪͙̤̋͒̇͛̽͆̀̀͞ṉ̨̨̢̡̩͓̤͖͎̠̪̼̻͍͕̹̤̠̮͔̜̭̮͇͓̜̻̣̪̩͕̬̙̥͕̞͈̞͖͖̈̉̊̎̈͋̊͋̌̋̌́͐̌̑͑͌̓̒̓̈́̇̃̀̑̍̓̂͊̋͂̕͘̕̕͢͟͠͠͞͠͝͠͡͡g̨̛̘̰̗̯͙̖̩̔͆̓̉͒̂̾ ̢̢̡̛͚͚̟͔̪̝̺̼̰̠̦͙̣̖͍̻̖͓̙̱́̂̎̃͊̈́͑̔̓͆̈̅̓͋̔̿́̃̀̀̚͜͞͞t̢̢̛͎̬͙͍̭͖̗̺̥͇̱͇̝̙̠̞̦͙̮̯̙̍̐́̽̾̐͋̏̔͒͛̆̄̋͐͂̏̓̊̽́̽͘ͅḩ̧̧̼̲͙͖̜̣͓͍̤̠̰̗̳͉̫̹̥̝̩͈͈̝͙͖̭͖̱͍͔̟͓̭̟͗̀̈̾̑͂̀͆͌̋̾̉́̾̍͗̿̈̑̑̉̽̑̃͊̂͛̍͒̂́̽̎̔͊͛͐͢͜͞ȩ̘͖͉̲͓̙͎͕̼̪͉̲̹̲̣͍͍̹̱̼̭͕͓͔̭̗͔̯͙̤̘̜̱̲̟͊̃̏͛̋̀͛́̏̒̌̐̊̆͑͋̉͌̽̈̓́̓͐̌̌̾̆͆́̋̓͢͝͞͡͞͞ ̡̢̦̠̖̪̯̥̣͖̠̯̰͔͚̜̔̌̊̄́͑̀̅̏̋́͛̊̉̔͒͢͡N̨̨̡̛̛̛͕͇̯͙̩̤̻̤̳̝̤̘͕̟̮͎̰͍̜̣͓̻̱̪̮̠̭̱̻̳͇̱̥̩͙̲̺̻̟̳̹͓̥̯̳̽͑̏͌̅̏̍͆̈́͑͒̐̾́͐͊͌̍́͛͛̎̈́͌́̈́̽̀͌̂̑̑͐̔̔̌͘͘̕͘͝͝͡͡͡͡ͅư̡̢̮͖̠̬͖̗̰̲͓̬̠̳͕͇̩̠̪̲̭͍̠̘͎͚̤͍̱͈̙̤̤̘̲̫͎͈̻͎̲͉͚̺̞̂͐̓̍̔̐͋̑̔̎̆̒͌͊͒̈̍̀͌̅́̈́͛̈̓͐̉̄̂̾͊̍̅͌̾̓̇͗̍̂̎̅͘͢͟͠͡͠ṁ͓̼̫̉͋͜͞b̧̝̘̘̰̮͚͖̜̙̭͎͇͂͗͆̾̅̈́̀̓̄̑̀́͘͜͝e̢̧̨̡̧̛̛̞̳̘̻̭̻̞͙͚̰͚̲͎̜̗̬̫̰̻̝͍̙̼̲̗̳͉͎̥̠̯̥͎̮͕̳̪͉̓̃̄͂́̿́͋͛̂̿̎͂́̋̇̍̂̓̓̔̾̈̓̒̾͋̉͋͑̐̾̓͗͋́̾̚̚̕͘̕͟͟͢͝͠͡ͅr̨̧̨̨̢̝̺̲̲̝̲̹̻̞͍̯̳͓͇͓̼̬̤͓̫̞̤͋̿̄͗̈́͐̀̈͆͛͋͛̍̐͐̿̉̑̊̅͂͆̌̓̐͋͢͢͡͡͡ ̨̢̡̛̼̱͇͔̥̬̤̰͖̰͕̱̣͚͈͍͔̲̯͈̻̻̮̓͂͐̓́͋̆̒̇̆̒̋̈́̈́͆͂́̌̀̔͒̂̈̒̕̚͢͟͢͟͢͠͡͠͠͞ͅG̢̛̹͎͔͇͍̳̞̺̭̰̤̝̦̖̝̯͙͚̤̣̜͖̫̮̘̘͎̮̮̬̬̫͚͆͐̇̀̾͊͊̇͐̑̊̌͗͊̍̎̉͒́̔̈́̏̀̀͆̌͂̈́͂͛͐͛̚̚̕͟͢͜͢͟͝͞͡u̧̡̨̜͈̮̖͉̰̠̖̣̟̯̝͔̪̰̮͈͖̦̗͍͓̼̣̼̳̬̟̙̮̩̥̬͙̒̉̔̈́̄͂̌̊̌̒̔̋̿̇̈̑̋̾̅̇͂̍̃̉̉͂̆͐̎́̌̿̍̀͘̕̚͢͜͢͡͞͝͞ͅȩ̢̧̢̢̬̣͉̜͖͔̱̤̖̥͔͓̬̦̠͎̞̣̰͇̞̫͓̯͉͓̯̙̭̬̲̙̥̭̩͉͖͇̪͛̾̃̽̂͊̿̌́̓͛̈́͒͐͂͂͊́̄̅̈́̍͂̍͐̓̐̏͗͛͋̓̈̓͗̽͑̓́̕͘͘͘͘͢͟͜͝͡͠͞ͅş̨̧̨̢̧̨̛̳̼͍̺̜̺̤̹̩̭̳̰̺̤͚̻͚̟̯͓̥̰̟͉̪͕̻̮̖͓̞̯͉̔͊͌̀̔̃̃̎͛͗̆̀́̀̓̿͌̌̈́̀̓̐̏̐̑̉̾͆̉̓͌̈́̍̐͟͢͟͠͡͡͡͝͝͡͡s̡̧̡̞̘͔͈̲̻̱̺̖̠͔͎̲͈̗͇̠͈̥̫̗̝̼̯̿̆̔̔̏͋̀̊́̃̊͛̒́́̂͊͂̋͆̊̈́̓̚͡͝͠͝ͅį̡̛͔̭̫̰͕͍̜͓́̉̅̍̽́̍͆̌n̨͔͙̭̘͓̱͎͕̦̜͑̅̓̇͆̃̄̔̀̚͝g̨̧̨̡̛̞̳̦̝̩͔̟͖̮͎͖̞̜̭̮̜̗̝̱̙͖̱͖̩͖̪̦͈̭̭̪̺͖̯̣͉̜̔̂̀̓̇͗̑́̊͛̍͆̿̃̊̉͊̃̽͒͛̌̅̅̓́͑̌̓́̒̍̍̚̕̚̕͟͡͡͠͝͡͞ͅͅ ̗̥͔͓̯̞̺͎̬̲͙̭̭̹̰̌̉͂̈͊͋͛̏̽̄͂͂̉̿͆͑̚͟͢͠ͅǦ̡̧̢̧̢̛̭̙̝̖̠̺̤̣̗͔̭̣͙̥̤͓͈͔͉̯͖͍͖͙͉̬̦͕͍̹̥̱͕͓̿́͂̓̈́͊̑̊̍̋͒̏̾̉͋͌̓̓̀͋̔͒͗̽͗͌͊̅̇́̔̐̓̔͘̚̕̕͘͜͢͜͜͟͝͞͞a̡̧̧̨̢̛͈̠͇͇͍̤̞̬̩̘̮͓̗̼͇̠̮͖͔̖͕͎̟͓͚͎͇͎̖̥̤̻̪̳̲̪̲͙͕͙̯̳̱̒̀̄̏͒́́̌͐́̾́̈́͌́̽͋͑͗͑́̿̄͗̄̈́̀̿́̿̏́̀̈́̓̄́̒̕̕̕͘͘͜͞͞͡͝͝͠ͅm̡̨̨̛̖͔̳͈̲̯̘̹̼̦͔̮̩̯͓̖̟̱̖͍̠̘͕͇͙̭͇̳͇̫̗̫̌̓̑͗̆̓̉̇̈̌͊̾͋̓̄̆̎̂̿̏̐̌͗̒̓́̈̊̈́̓͗̎́͟͟͡͠͝é̢̢̧̟͔̖͕͍̙̯̞̱̠͈̠̭͚̺̜̲̤͎̺̞͇̟̐̀̅̆͒͗̏̈́̇͛͋͗̌̓͌͂̒͊͆̽̂͊͑̑̐͑̚̚͘͢͢ͅͅ")
      time.sleep(3)
      clear()
      sys.exit()
      
