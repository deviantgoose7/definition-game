from bs4 import BeautifulSoup
import requests, io, random

file = ""

def getNewWord():
  text_file = open(file, "r")
  lines = text_file.readlines()
  return lines[int(random.randrange(len(lines)))]
  text_file.close()

def defineWordBS(word): #beautifulsoup version, web-scrapes in case of TypeError exception
  try:
    page = requests.get("https://www.merriam-webster.com/dictionary/" + str(word))
    soup = BeautifulSoup(page.content, 'html.parser')
    info = soup.find(class_="vg")
    text = str(info.find(class_='dtText').get_text())
    return text.replace(word, '____').replace('\n', ', ')
  except:
    return str(word) + ": We're not sure about this one... or at least Merriam Webster isn't..."

def play():
  print("Can you guess this one?")
  chosen_word = getNewWord().replace('\n', '')
  definition = defineWordBS(chosen_word)
  if definition.endswith("We're not sure about this one... or at least Merriam Webster isn't..."):
    play()
  else:
    won = 0
    while won != 1:
      print(definition)
      guess = input()
      # print("Guess: \"" + guess + "\"")
      # print("Answer: \"" + chosen_word + "\"")
      
      if guess.upper() == chosen_word.upper():
        print("Yes! The word was " + chosen_word + "\n")
        won = 1
        play()
      elif guess.upper() == "i give up".upper():
        print("You almost got it! The word was " + chosen_word + "\n")
        play()
      else:
        print("Nope! Try again!\n")

def setDifficulty():
  setting = input("What difficulty would you like to play?\n1 = Really Easy\n2 = Easy\n3 = Medium\n4 = Hard\n5 = Really Hard\n6 = Impossible\n")
  print("")
  if setting == "1":
    return "really-easy.txt"
  elif setting == "2":
    return "easy.txt"
  elif setting == "3":
    return "medium.txt"
  elif setting == "4":
    return "hard.txt"
  elif setting == "5":
    return "really-hard.txt"
  elif setting == "6":
    return "impossible.txt"
  else:
    print("\nInvalid number\n")
    return setDifficulty()

if __name__ == "__main__":
  print("\nWelcome to the Definition Guessing Game! I'll throw a definition at you and you have to type the word that fits that definition! Quite simple really but it's harder than it looks! You can always type \"I give up\" to get another word!\n")
  file = setDifficulty()
  play()