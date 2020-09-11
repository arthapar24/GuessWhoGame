import random 

print ("Welcome to Guess Who! \n")

dictionary = {
  "mike" : ['Male', '15', "6'1", 'Blonde'],
  "liv" : ['Female', '25', "5'11", 'Blonde'],
  "lisa" : ['Female', '15', "5'10", 'Red'],
  "linda" : ['Female', '25', "5'7", 'Brown'],
  "bill" : ['Male', '20', "5'5", 'Brown']
}

playing = True 

random_character = random.choice(list(dictionary))

def list():
  for i in dictionary:
    print (str(i) + ": \n" + str(dictionary[i]))

def gender():
  list_of_traits = dictionary[random_character]
  i = list_of_traits[0]
  print(i)
 
def age():
  list_of_traits = dictionary[random_character]
  i = list_of_traits[1]
  print(i)

def height():
  list_of_traits = dictionary[random_character]
  i = list_of_traits[2]
  print(i)

def hair():
  list_of_traits = dictionary[random_character]
  i = list_of_traits[3]
  print(i)

def guess():
  global playing
  if action == "guess " + str(random_character):
    print("You win! \nEND")
    playing = False
  else:
    print("You lost... \nEND")
    playing = False

def help():
  print(
    "list: list out all the character’s names\ngender/age/height/hair: asks for a piece of information\nguess name: guess a character\nquit: exits the game"
    )
    
def quit():
  global playing
  playing = False

counter = 0
while playing:
  action = input("What would you like to do? ")
  
  if action == "list":
    list()
  if action == "guess mike" or action == "guess liv" or action == "guess lisa" or action == "guess linda" or action == "guess bill":
    guess()
  if counter < 2:
    if action == "gender":
      gender()
      counter += 1
    if action == "age":
      age()
      counter += 1
    if action == "height":
      height()
      counter += 1
    if action == "hair":
      hair()
      counter += 1
  if counter == 2:
    print("\nYou can't guess any more traits now!\n")
    counter += 1
  if action == "help":
    help()
  if action == "quit":
    quit()
  
  
  
    