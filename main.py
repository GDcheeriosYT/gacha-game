import random
import turtle as t
import re
import os
import logging
from itertools import cycle
import collections

#all turtle config
font_size = 30
font_setup = ("Arial", font_size, "normal")
#please make turtle location no more than 200 or no less than -200 because it could be off the screen depending on your screen resolution
location = 0

#visual output function
output = t.Screen()
output.setup(height=1.0, width=1.0)

#warning turtle
warning_turtle = t.Turtle()
warning_turtle.color("red")
warning_turtle.penup()
warning_turtle.hideturtle()
warning_turtle.goto(-230, -130)
warning_turtle.pendown()
warning_turtle.write("the main menu is work in progress...", font=("Arial", 15, "normal"))
#warning_turtle.penup()
#warning_turtle.goto(-230, -150)
#warning_turtle.write("not interactive...", font=("Arial", 15, "normal"))


#function turtles
'''
def play(location, clear_var):
  play_button = t.Turtle()
  play_button.speed(0)
  play_button.hideturtle()
  play_button.penup()
  play_button.goto(0, location)
  play_button.pendown()
  play_button.write("play", font=(font_setup))
  if clear_var == 1:
    play_button.clear()
  else:
    None

def shop(location, clear_var):
  shop_button = t.Turtle()
  shop_button.speed(0)
  shop_button.hideturtle()
  shop_button.penup()
  shop_button.goto(0, location - font_size)
  shop_button.pendown()
  shop_button.write("shop", font=(font_setup))
  if clear_var == 1:
   shop_button.clear()
  else:
    None

def options(location, clear_var):
  options_button = t.Turtle()
  options_button.speed(0)
  options_button.hideturtle()
  options_button.penup()
  options_button.goto(0, location - (font_size * 2))
  options_button.pendown()
  options_button.write("options", font=(font_setup))
  if clear_var == 1:
    options_button.clear()
  else:
    None

def exit(location, clear_var):
  exit_button = t.Turtle()
  exit_button.speed(0)
  exit_button.hideturtle()
  exit_button.penup()
  exit_button.goto(0, location - (font_size * 3))
  exit_button.pendown()
  exit_button.write("exit", font=(font_setup))
  if clear_var == 1:
    exit_button.clear()
  else:
    None

def initiate_game():
  play(location, 0)
  shop(location, 0)
  options(location, 0)
  exit(location, 0)

def hide_menu():
  play(location, 1)
  shop(location, 1)
  options(location, 1)
  exit(location, 1)
'''
#rolling turtle
rolling_turtle = t.Turtle()
rolling_turtle.pensize(1)
rolling_turtle.speed(1)
rolling_turtle.hideturtle()

#character turtle
#writes down the character you got next to the rarity meter
character_turtle = t.Turtle()

#character count turtle
#writes down total number of characters gotten in the session

character_count_turtle = t.Turtle()
character_count_turtle.speed(0)
character_count_turtle.pensize(1)

def side_leaderboard():

  character_count_turtle.clear()

  #get the number of different total characters you can get
  #sort out the numbers so only the names remain
  
  #count up collected characters
  with open("character_data.txt") as f:
    collected_characters = f.read().split()
  
  collected_people = []
  
  for person in collected_characters:
    if person not in collected_people:
      collected_people.append(person)
    else:
      None
    
  
  depth = 150
  x = 0

  while x < len(collected_people):
    character_count_turtle.penup()
    character_count_turtle.goto(-272, depth)
    character_count_turtle.pendown()
    character_count_turtle.write("%s %s" % (collected_people[x], collected_characters.count(collected_people[x])), font=("arial", len(collected_people), "normal"))
    depth = depth - len(collected_people)*2
    x = x + 1

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
  #initiate_game()

  side_leaderboard()

  menu = input("\n\n\n\n\n\n\n\n1, play\n2, shop\n3, options\n4, exit\n")
  t.clear()
  GC = open("GC.txt", "a+")

  with open("GC.txt") as f:
    GC_read = f.read().splitlines()

  gacha_credits = re.search("\d+", GC_read[len(GC_read)- 1])

  if menu == "1":
    #hide_menu()

    #pulling amount
    pull = input("\n\n\n\n\n\n\n\nyou have %s credits\n\nhow many do you want to pull?\n\n" % (gacha_credits.group()))


    #money function
    def spend(pull_amount, credits):
      if int(pull_amount) < 0:
        print("how do you expect to pull %s characters!?" % (pull_amount))
        ending_credits = int(credits)
        return(ending_credits)
      elif int(credits) >= int(pull_amount):
        ending_credits = int(credits) - int(pull_amount)
        return(ending_credits)
      else: 
        ending_credits = int(credits)
        return(ending_credits)
    
    credits_spent = spend(pull, gacha_credits.group())
    GC.write("\n%s" % (credits_spent))
    GC.close()

    if int(pull) < 0:
      if_num = int(pull)
      pull_reply = 0
    elif int(GC_read[len(GC_read)- 1]) < int(pull):
      print("not enough gacha points")
      if_num = int(pull)
      pull_reply = 0
    else:
      pull_reply = int(pull)
      if_num = 0

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
    character_turtle.clear()
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

        rolling_turtle.goto(rarity_bar_width, int(int(character_rarity.group())/rarity_size_shrinker))

        character_turtle.penup()

        character_turtle.hideturtle()

        character_turtle.goto(rarity_bar_width, int(int(character_rarity.group())/rarity_size_shrinker))

        character_turtle.color(color_for_turtle)

        character_turtle.pendown()
        
        character_turtle.showturtle()

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
        
      else:
        char_picker = random.randint(0, int(list_end))
        chance = random.randint(0, 10000)

    #output
    print("you pulled %s characters!\nyou have %s points left!" % (int(pull_reply), credits_spent))

  elif menu == "2":
    #money function
    shop_buy = input("\n\n\n\n\n\n\n\n1, buy gacha credits\n2, see how many points you have\n")
    if shop_buy == "1":
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
      print("you have ", gacha_credits.group(), "points")
  
    
  elif menu == "3":
    options = input("\n\n\n\n\n\n\n\n1, clear data\n2, back\n")
    if options == "1":
      try:
        file = open("character_data.txt","r+")
        file.truncate(0)
        file.close()
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