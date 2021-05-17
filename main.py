import random
import turtle as t
import re
import os
import logging
from itertools import cycle

#all turtle config
font_setup = ("Arial", 20, "normal")

#visual output function
output = t.Screen()
output.setup(height=1.0, width=1.0)

#rolling turtle
rolling_turtle = t.Turtle()
rolling_turtle.pensize(1)
rolling_turtle.speed(1)

#character turtle
#writes down the character you got next to the rarity meter
character_turtle = t.Turtle()

#character count turtle
#writes down total number of characters gotten in the session
character_count_turtle = t.Turtle()
character_count_turtle.speed(0)
character_count_turtle.pensize(1)

'''def side_leaderboard(characters):

  character_count_turtle.clear()

  #get the number of different total characters you can get
  #sort out the numbers so only the names remain
  with open("characters.txt") as f:
    characters = f.read().splitlines()

  people = []
  
  for character in characters:
    people.append(character)
  
  print(people)
  
  #count up collected characters
  with open("character_data.txt") as f:
    collected_characters = f.read().split()
  
  collected_people = []

  for name in collected_characters:
    collected_people.append(name)
  
  depth = 150
  x = 0

  while x < len(people):
    character_count_turtle.penup()
    character_count_turtle.goto(-272, depth)
    character_count_turtle.pendown()
    character_count_turtle.write(people[x])
    depth = depth - 10
    x = x + 1'''

#rarity bar turtle
rarity_bar = t.Turtle()
rarity_bar.penup()
rarity_bar.speed(0)
rarity_bar.pensize(1)
rarity_bar_width = 50
rarity_size_shrinker = 60

def rarity_bar_draw():
  #common values
  rarity_bar.color("grey")
  rarity_bar.fillcolor("gray")
  rarity_bar.goto(0, int(5001/rarity_size_shrinker))
  rarity_bar.pendown()
  rarity_bar.begin_fill()
  rarity_bar.goto(rarity_bar_width, int(5001/rarity_size_shrinker))
  rarity_bar.goto(rarity_bar_width, int(10000/rarity_size_shrinker))
  rarity_bar.goto(0, int(10000/rarity_size_shrinker))
  rarity_bar.goto(0, int(5001/rarity_size_shrinker))
  rarity_bar.end_fill()
  rarity_bar.penup()
  
  #normal-lucky value
  rarity_bar.color("lime")
  rarity_bar.fillcolor("lime")
  rarity_bar.goto(0, int(5000/rarity_size_shrinker))
  rarity_bar.pendown()
  rarity_bar.begin_fill()
  rarity_bar.goto(rarity_bar_width, int(5000/rarity_size_shrinker))
  rarity_bar.goto(rarity_bar_width, int(2001/rarity_size_shrinker))
  rarity_bar.goto(0, int(2001/rarity_size_shrinker))
  rarity_bar.goto(0, int(5000/rarity_size_shrinker))
  rarity_bar.end_fill()
  rarity_bar.penup()

  #rare-exceptional value
  rarity_bar.color("blue")
  rarity_bar.fillcolor("blue")
  rarity_bar.goto(0, int(2000/rarity_size_shrinker))
  rarity_bar.pendown()
  rarity_bar.begin_fill()
  rarity_bar.goto(rarity_bar_width, int(2000/rarity_size_shrinker))
  rarity_bar.goto(rarity_bar_width, int(301/rarity_size_shrinker))
  rarity_bar.goto(0, int(301/rarity_size_shrinker))
  rarity_bar.goto(0, int(2000/rarity_size_shrinker))
  rarity_bar.end_fill()
  rarity_bar.penup()

  #epic value
  rarity_bar.color("purple")
  rarity_bar.fillcolor("purple")
  rarity_bar.goto(0, int(300/rarity_size_shrinker))
  rarity_bar.pendown()
  rarity_bar.begin_fill()
  rarity_bar.goto(rarity_bar_width, int(300/rarity_size_shrinker))
  rarity_bar.goto(rarity_bar_width, int(151/rarity_size_shrinker))
  rarity_bar.goto(0, int(151/rarity_size_shrinker))
  rarity_bar.goto(0, int(300/rarity_size_shrinker))
  rarity_bar.end_fill()
  rarity_bar.penup()

  #legendary value
  rarity_bar.color("pink")
  rarity_bar.fillcolor("pink")
  rarity_bar.goto(0, int(150/rarity_size_shrinker))
  rarity_bar.pendown()
  rarity_bar.begin_fill()
  rarity_bar.goto(rarity_bar_width, int(150/rarity_size_shrinker))
  rarity_bar.goto(rarity_bar_width, int(51/rarity_size_shrinker))
  rarity_bar.goto(0, int(51/rarity_size_shrinker))
  rarity_bar.goto(0, int(150/rarity_size_shrinker))
  rarity_bar.end_fill()
  rarity_bar.penup()

  #supreme value
  rarity_bar.color("red")
  rarity_bar.fillcolor("red")
  rarity_bar.goto(0, int(50/rarity_size_shrinker))
  rarity_bar.pendown()
  rarity_bar.begin_fill()
  rarity_bar.goto(rarity_bar_width, int(50/rarity_size_shrinker))
  rarity_bar.goto(rarity_bar_width, int(11/rarity_size_shrinker))
  rarity_bar.goto(0, int(11/rarity_size_shrinker))
  rarity_bar.goto(0, int(50/rarity_size_shrinker))
  rarity_bar.end_fill()
  rarity_bar.penup()

  #godly value
  rarity_bar.color("gold")
  rarity_bar.fillcolor("gold")
  rarity_bar.goto(0, int(10/rarity_size_shrinker))
  rarity_bar.pendown()
  rarity_bar.begin_fill()
  rarity_bar.goto(rarity_bar_width, int(10/rarity_size_shrinker))
  rarity_bar.goto(rarity_bar_width, int(4/rarity_size_shrinker))
  rarity_bar.goto(0, int(4/rarity_size_shrinker))
  rarity_bar.goto(0, int(10/rarity_size_shrinker))
  rarity_bar.end_fill()
  rarity_bar.penup()

  #devine value
  rarity_bar.color("black")
  rarity_bar.fillcolor("white")
  rarity_bar.goto(0, int(3/rarity_size_shrinker))
  rarity_bar.pendown()
  rarity_bar.begin_fill()
  rarity_bar.goto(rarity_bar_width, int(3/rarity_size_shrinker))
  rarity_bar.goto(rarity_bar_width, int(0/rarity_size_shrinker))
  rarity_bar.goto(0, int(0/rarity_size_shrinker))
  rarity_bar.goto(0, int(3/rarity_size_shrinker))
  rarity_bar.end_fill()
  rarity_bar.penup()



with open("characters.txt") as f:
  characters = f.read().splitlines()

list_end = len(characters) - 1

while True:

  #menu
  menu = input("\n\n\n\n\n\n\n\n1, play\n2, shop\n3, options\n4, exit\n")
  t.clear()
  GC = open("GC.txt", "a+")

  with open("GC.txt") as f:
    GC_read = f.read().splitlines()

  gacha_credits = re.search("\d+", GC_read[len(GC_read)- 1])

  if menu == "1":


    #pulling amount
    pull = input("\n\n\n\n\n\n\n\nyou have %s credits\n\nhow many do you want to pull?\n\n" % (gacha_credits.group()))


    #money function
    def spend(pull_amount, credits):
      if int(credits) >= int(pull_amount):
        ending_credits = int(credits) - int(pull_amount)
      else:
        ending_credits = int(credits)
        print("not enough points")
      return(ending_credits)
    
    credits_spent = spend(pull, gacha_credits.group())
    GC.write("\n%s" % (credits_spent))
    GC.close()

    if int(GC_read[len(GC_read)- 1]) < int(pull):
      print("not enough gacha points")
      if_num = int(pull)
    else:
      if_num = 0

    print("debug: GC_Read", int(GC_read[len(GC_read)- 1]), "pull", int(pull), "credits left", credits_spent)

    def rarity_color(x, y):
      global color_for_turtle
      divine_colors = ["red", "green", "orange", "blue", "purple"]
      color_for_turtle = cycle(divine_colors)
      if 9000 <= int(x):
        color_for_turtle = "grey"
        return("\033[1;31;40mSuper dooper common %s\033[1;37;40m\n" % (y))
      elif 8000 <= int(x):
        color_for_turtle = "grey"
        return("\033[1;31;40mVery common %s\033[1;37;40m\n" % (y))
      elif 7000 <= int(x):
        color_for_turtle = "grey"
        return("\033[1;31;40mPretty common %s\033[1;37;40m\n" % (y))
      elif 6000 <= int(x):
        color_for_turtle = "grey"
        return("\033[1;32;40mCommon %s\033[1;37;40m\n" % (y))
      elif 5000 <= int(x):
        color_for_turtle = "lime"
        return("\033[1;32;40mNormal %s\033[1;37;40m\n" % (y))
      elif 4000 <= int(x):
        color_for_turtle = "lime"
        return("\033[1;33;40mUncommon %s\033[1;37;40m\n" % (y))
      elif 3000 <= int(x):
        color_for_turtle = "lime"
        return("\033[1;33;40mLucky %s\033[1;37;40m\n" % (y))
      elif 2000 <= int(x):
        color_for_turtle = "blue"
        return("\033[1;34;40mRare %s\033[1;37;40m\n" % (y))
      elif 1000 <= int(x):
        color_for_turtle = "blue"
        return("\033[1;34;40mOutstanding %s\033[1;37;40m\n" % (y))
      elif 500 <= int(x):
        color_for_turtle = "blue"
        return("\033[1;36;40mExceptional %s\033[1;37;40m\n" % (y))
      elif 300 <= int(x):
        color_for_turtle = "purple"
        return("\033[1;35;40mepic %s\033[1;37;40m\n" % (y))
      elif 150 <= int(x):
        color_for_turtle = "pink"
        return("\033[1;35;40mLegendary %s\033[1;37;40m\n" % (y))
      elif 50 <= int(x):
        color_for_turtle = "red"
        return("\033[1;31;47mSupreme %s\033[1;37;40m\n" % (y))
      elif 10 <= int(x):
        color_for_turtle = "gold"
        return("\033[1;30;43mGodly %s\033[1;37;40m\n" % (y))
      elif 3 <= int(x):
        color_for_turtle = cycle(divine_colors)
        return("\033[1;31;40mD\033[1;32;40mi\033[1;33;40mv\033[1;34;40mi\033[1;35;40mn\033[1;36;40m\033[1;37;40me %s" % (y))

    #character pulling sequence
    rarity_bar_draw()
    x = if_num
    while x < int(pull):
      #random character data
      char_picker = random.randint(0, int(list_end))
      chance = random.randint(0, 10000)


      #character and rarity grabber
      character_name = re.search("\D+", characters[int(char_picker)])
      character_rarity = re.search("\d+", characters[int(char_picker)])
      if chance <= int(character_rarity.group()):

        #gacha results
        print("you pulled a(n) %swhich has a %s out of 10000 chance!" % (rarity_color(character_rarity.group(), character_name.group()), character_rarity.group()))

        rolling_turtle.penup()

        rolling_turtle.goto(0, int(int(character_rarity.group())/rarity_size_shrinker))

        rolling_turtle.pendown()

        rolling_turtle.goto(rarity_bar_width + 10, int(int(character_rarity.group())/rarity_size_shrinker))

        character_turtle.goto(rarity_bar_width, int(int(character_rarity.group())/rarity_size_shrinker))

        character_turtle.color(color_for_turtle)

        character_turtle.write(character_name.group(), font=("Calibri", 8, "bold"), move=True)
        
        rolling_turtle.penup()

        rolling_turtle.goto(0, 0)

        rolling_turtle.clear()

        x = x + 1
        char_picker = random.randint(0, int(list_end))
        chance = random.randint(0, 10000)
          
        #saving caracter data
        character_data = open("character_data.txt", "a+")
        character_data.write("%s\n" % (character_name.group()))


        #sorting the data
        def sorting(character_data):
          infile = open(character_data)
          words = []
          for line in infile:
            temp = line.split()
            for i in temp:
              words.append(i)
          infile.close()
          words.sort()
          outfile = open("character_data.txt", "w")
          for i in words:
            outfile.writelines(i)
            outfile.writelines(" ")
          outfile.close()
        sorting("character_data.txt")

        #output
        print("you pulled %s characters!\nyou have %s points left!" % (int(if_num), credits_spent))

        
      else:
        char_picker = random.randint(0, int(list_end))
        chance = random.randint(0, 10000)

  elif menu == "2":
    #money function
    shop = input("\n\n\n\n\n\n\n\n1, buy gacha credits\n2, see how many points you have\n")
    if shop == "1":
      def buy(credits):
        buy_money = input("\n\n\n\n\n\n\n\nhow many credits will you buy? ")
        try:
          buy_money
        except ValueError:
          print("expected an actual number kid...")
        
        
        mom_credit_card_num = random.randint(1000000000000000, 9999999999999999)
        mom_credit_card_csv = random.randint(100, 999)
        mom_credit_card_mon = random.randint(1, 12)
        mom_credit_card_day = random.randint(20, 24)
        gacha_credits = int(buy_money) + int(credits)

        print("using your moms credit card info...\nnumber: %s\ncsv: %s\nexp date: %s/%s" % (mom_credit_card_num, mom_credit_card_csv, mom_credit_card_mon, mom_credit_card_day))
          
        return(gacha_credits)
      credits_bought = buy(gacha_credits.group())
      GC.write("\n%s" % (credits_bought))
      GC.close()
      print("you now have ", credits_bought, "points")
    else:
      print("you have ", credits_bought, "points")
  
    
  elif menu == "3":
    options = input("\n\n\n\n\n\n\n\n1, clear data\n2, back\n")
    if options == "1":
      try:
        os.remove("character_data.txt")
      except FileNotFoundError:
        print("no data found...")
    else:
      print("going back...")
  else:
    break

#visual output function
output.mainloop()

#saving the log
logging.basicConfig(filename="debug.log", level=logging.INFO)