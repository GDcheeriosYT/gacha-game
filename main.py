import random
import tkinter
import turtle as t
import re
import os
import logging
import collections

#visual output function
output = t.Screen()

output.setup(height=1.0, width=1.0)

screensize = output.screensize()

screen_width = screensize[0]

screen_height = screensize[1]

screen_area = screen_height * screen_width


#option stuff
debug = 0
ui_scale = 1.5

#pity
rolls = 0
pity = 0

def pity_op(chance):
  global pity_tier
  pity_tier = 0

  if rolls < 25:
    return random.randint(0, 10000)

  elif rolls >= 25:
    pity_tier = 1
    rarity_divider = random.randint(1, 2)
    divided_chance = chance / rarity_divider
    return int(divided_chance)

  elif rolls >= 50:
    pity_tier = 2
    rarity_divider = random.randint(1, 5)
    divided_chance = chance / rarity_divider
    return int(divided_chance)

  elif rolls >= 75:
    pity_tier = 3
    rarity_divider = random.randint(1, 10)
    divided_chance = chance / rarity_divider
    return int(divided_chance)
  
  elif rolls >= 100:
    pity_tier = 4
    rarity_divider = random.randint(1, 20)
    divided_chance = chance / rarity_divider
    return int(divided_chance)

#turtle pulling animation
pulling_area_max = 300

pulling_area_min = 50

pulling_area_start = 50

pulling_area_end = 400

spark_size = 10

sparks_size = 1

trail_size = 1

def pull_animation(rarity_color):
  
  #the main body of the pulling animation
  pull_spark = t.Turtle()
  pull_spark.size(spark_size)
  pull_spark.setheading("circle")
  pull_spark.speed(3)
  pull_spark.color(rarity_color)
  
  #the sparks for the body of the animation
  pull_sparks = t.Turtle()
  pull_sparks.size(pull_sparks)
  pull_sparks.speed(0)
  pull_spark.color(rarity_color)
  
  #the trail of the body of the animation
  pull_trail = t.Turtle()
  pull_trail.size(trail_size)
  pull_trail.color(rarity_color)
  
  #the ending effect of the animation, depending on rarity effect will be more intense

  #animation initiation
  pull_spark.penup()
  
  pull_spark_y_spawn = random.randint(pulling_area_min, pulling_area_max)
  
  pull_spark.goto(pulling_area_start, pull_spark_y_spawn)
  
  pull_spark.circle(pulling_area_end, 180, 25)

#all turtle config
font_size = int(screen_area * ui_scale / screen_width)
font_setup = ("Arial", font_size, "normal")
#please make turtle location no more than 200 or no less than -200 because it could be off the screen depending on your screen resolution
location = 0

#warning turtle
"""warning_turtle = t.Turtle()
warning_turtle.color("red")
warning_turtle.penup()
warning_turtle.hideturtle()
warning_turtle.goto(-290, -150)
warning_turtle.pendown()
warning_turtle.write("the main menu is work in progress...", font=("Arial", 15, "normal"))"""
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
rolling_turtle.pensize(5)
rolling_turtle.speed(1)
rolling_turtle.hideturtle()

#character turtle
#writes down the character you got next to the rarity meter
character_turtle = t.Turtle()
character_turtle.speed(1)
character_turtle.pensize(5)

#character count turtle
#writes down total number of characters gotten in the session
character_count_turtle = t.Turtle()
character_count_turtle.speed(0)
character_count_turtle.pensize(font_size)

#experience counter
"""class experience:

  def __init__(self, xp_multiplier, xp_count, level):

    self.xp_multiplier = 1
    
    self.xp_count = 0

    self.level = 0

with open("experience.txt", "w+") as f:
  experience = f.read().splitlines()

experience_info = {}

for line in experience:

  experience_info[str(line)]

def xp_algorithms()"""

def side_leaderboard():

  character_count_turtle.clear()

  #get the number of different total characters you can get
  #sort out the numbers so only the names remain
  
  #count up collected characters
  with open("character_data.txt", "r") as f:
    collected_characters = f.read().split()
  
  collected_people = []
  
  for person in collected_characters:
    if person not in collected_people:
      collected_people.append(person)
    else:
      None
    
  non_depth = (screen_width - screen_width * 2) + 10
  depth = screen_height / 2
  x = 0

  #make sure that leaderboard is always a certain value before shrinking
  threshold = font_size * 1.5
  print(threshold)

  if len(collected_people) < threshold:
    leaderboard_size = threshold
  else:
    leaderboard_size = (len(collected_people) / (len(collected_people)) - threshold)

  file = open("leaderboard.txt", "w+")

  def always_write_the_file(x):
    while x < len(collected_people):
      file.write("%s %s\n" % (collected_people[x], collected_characters.count(collected_people[x])))
      x = x + 1
  
  always_write_the_file(x)
  file.close()

  x = 0

  with open("leaderboard.txt", "r") as f:
    leaderboard = f.read().splitlines()
  f.close()

  while x < len(collected_people):
    character_count_turtle.penup()
    character_count_turtle.goto(non_depth, depth)
    character_count_turtle.pendown()
    
    sorted_leaderboard = sorted(leaderboard, key=lambda x: int(x.rsplit(" ", maxsplit=1)[-1]))

    
    character_count_turtle.write("%s" % (sorted_leaderboard[x]), font=("arial", font_size, "normal"))

    depth = depth - threshold
    x = x + 1

side_leaderboard()

#rarity bar turtle
rarity_bar = t.Turtle()
rarity_bar.penup()
rarity_bar.speed(0)
rarity_bar.pensize(1)
rarity_bar_width = 50
rarity_size_shrinker = 30.5
rarity_bar_xval = 100
rarity_bar_yval = -125

def rarity_bar_draw():
  #common values
  rarity_bar.color("grey")
  rarity_bar.fillcolor("gray")
  rarity_bar.goto(rarity_bar_xval, rarity_bar_yval + int(5001/rarity_size_shrinker))
  rarity_bar.pendown()
  rarity_bar.begin_fill()
  rarity_bar.goto(rarity_bar_xval + rarity_bar_width, rarity_bar_yval + int(5001/rarity_size_shrinker))
  rarity_bar.goto(rarity_bar_xval + rarity_bar_width, rarity_bar_yval + int(10000/rarity_size_shrinker))
  rarity_bar.goto(rarity_bar_xval, rarity_bar_yval + int(10000/rarity_size_shrinker))
  rarity_bar.goto(rarity_bar_xval, rarity_bar_yval + int(5001/rarity_size_shrinker))
  rarity_bar.end_fill()
  rarity_bar.penup()
  
  #normal-lucky value
  rarity_bar.color("lime")
  rarity_bar.fillcolor("lime")
  rarity_bar.goto(rarity_bar_xval, rarity_bar_yval + int(5000/rarity_size_shrinker))
  rarity_bar.pendown()
  rarity_bar.begin_fill()
  rarity_bar.goto(rarity_bar_xval + rarity_bar_width, rarity_bar_yval + int(5000/rarity_size_shrinker))
  rarity_bar.goto(rarity_bar_xval + rarity_bar_width, rarity_bar_yval + int(2001/rarity_size_shrinker))
  rarity_bar.goto(rarity_bar_xval, rarity_bar_yval + int(2001/rarity_size_shrinker))
  rarity_bar.goto(rarity_bar_xval, rarity_bar_yval + int(5000/rarity_size_shrinker))
  rarity_bar.end_fill()
  rarity_bar.penup()

  #rare-exceptional value
  rarity_bar.color("blue")
  rarity_bar.fillcolor("blue")
  rarity_bar.goto(rarity_bar_xval, rarity_bar_yval + int(2000/rarity_size_shrinker))
  rarity_bar.pendown()
  rarity_bar.begin_fill()
  rarity_bar.goto(rarity_bar_xval + rarity_bar_width, rarity_bar_yval + int(2000/rarity_size_shrinker))
  rarity_bar.goto(rarity_bar_xval + rarity_bar_width, rarity_bar_yval + int(301/rarity_size_shrinker))
  rarity_bar.goto(rarity_bar_xval, rarity_bar_yval + int(301/rarity_size_shrinker))
  rarity_bar.goto(rarity_bar_xval, rarity_bar_yval + int(2000/rarity_size_shrinker))
  rarity_bar.end_fill()
  rarity_bar.penup()

  #epic value
  rarity_bar.color("purple")
  rarity_bar.fillcolor("purple")
  rarity_bar.goto(rarity_bar_xval, rarity_bar_yval + int(300/rarity_size_shrinker))
  rarity_bar.pendown()
  rarity_bar.begin_fill()
  rarity_bar.goto(rarity_bar_xval + rarity_bar_width, rarity_bar_yval + int(300/rarity_size_shrinker))
  rarity_bar.goto(rarity_bar_xval + rarity_bar_width, rarity_bar_yval + int(151/rarity_size_shrinker))
  rarity_bar.goto(rarity_bar_xval, rarity_bar_yval + int(151/rarity_size_shrinker))
  rarity_bar.goto(rarity_bar_xval, rarity_bar_yval + int(300/rarity_size_shrinker))
  rarity_bar.end_fill()
  rarity_bar.penup()

  #legendary value
  rarity_bar.color("pink")
  rarity_bar.fillcolor("pink")
  rarity_bar.goto(rarity_bar_xval, rarity_bar_yval + int(150/rarity_size_shrinker))
  rarity_bar.pendown()
  rarity_bar.begin_fill()
  rarity_bar.goto(rarity_bar_xval + rarity_bar_width, rarity_bar_yval + int(150/rarity_size_shrinker))
  rarity_bar.goto(rarity_bar_xval + rarity_bar_width, rarity_bar_yval + int(51/rarity_size_shrinker))
  rarity_bar.goto(rarity_bar_xval, rarity_bar_yval + int(51/rarity_size_shrinker))
  rarity_bar.goto(rarity_bar_xval, rarity_bar_yval + int(150/rarity_size_shrinker))
  rarity_bar.end_fill()
  rarity_bar.penup()

  #supreme value
  rarity_bar.color("red")
  rarity_bar.fillcolor("red")
  rarity_bar.goto(rarity_bar_xval, rarity_bar_yval + int(50/rarity_size_shrinker))
  rarity_bar.pendown()
  rarity_bar.begin_fill()
  rarity_bar.goto(rarity_bar_xval + rarity_bar_width, rarity_bar_yval + int(50/rarity_size_shrinker))
  rarity_bar.goto(rarity_bar_xval + rarity_bar_width, rarity_bar_yval + int(11/rarity_size_shrinker))
  rarity_bar.goto(rarity_bar_xval, rarity_bar_yval + int(11/rarity_size_shrinker))
  rarity_bar.goto(rarity_bar_xval, rarity_bar_yval + int(50/rarity_size_shrinker))
  rarity_bar.end_fill()
  rarity_bar.penup()

  #godly value
  rarity_bar.color("gold")
  rarity_bar.fillcolor("gold")
  rarity_bar.goto(rarity_bar_xval, rarity_bar_yval + int(10/rarity_size_shrinker))
  rarity_bar.pendown()
  rarity_bar.begin_fill()
  rarity_bar.goto(rarity_bar_xval + rarity_bar_width, rarity_bar_yval + int(10/rarity_size_shrinker))
  rarity_bar.goto(rarity_bar_xval + rarity_bar_width, rarity_bar_yval + int(4/rarity_size_shrinker))
  rarity_bar.goto(rarity_bar_xval, rarity_bar_yval + int(4/rarity_size_shrinker))
  rarity_bar.goto(rarity_bar_xval, rarity_bar_yval + int(10/rarity_size_shrinker))
  rarity_bar.end_fill()
  rarity_bar.penup()

  #devine value
  rarity_bar.color("black")
  rarity_bar.fillcolor("white")
  rarity_bar.goto(rarity_bar_xval, rarity_bar_yval + int(3/rarity_size_shrinker))
  rarity_bar.pendown()
  rarity_bar.begin_fill()
  rarity_bar.goto(rarity_bar_xval + rarity_bar_width, rarity_bar_yval + int(3/rarity_size_shrinker))
  rarity_bar.goto(rarity_bar_xval + rarity_bar_width, rarity_bar_yval + int(0/rarity_size_shrinker))
  rarity_bar.goto(rarity_bar_xval, rarity_bar_yval + int(0/rarity_size_shrinker))
  rarity_bar.goto(rarity_bar_xval, rarity_bar_yval + int(3/rarity_size_shrinker))
  rarity_bar.end_fill()
  rarity_bar.penup()



with open("characters.txt") as f:
  characters = f.read().splitlines()

list_end = len(characters) - 1

while True:

  #menu
  #initiate_game()
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

    def rarity_color(rarity, name):
      global color_for_turtle
      color_for_turtle = "blue"
      divine_colors = ["red", "green", "orange", "blue", "purple"]
      if 9000 <= int(rarity):
        color_for_turtle = "grey"
        return("\033[1;31;40mSuper dooper common %s\033[1;37;40m\n" % (name))
      elif 8000 <= int(rarity):
        color_for_turtle = "grey"
        return("\033[1;31;40mVery common %s\033[1;37;40m\n" % (name))
      elif 7000 <= int(rarity):
        color_for_turtle = "grey"
        return("\033[1;31;40mPretty common %s\033[1;37;40m\n" % (name))
      elif 6000 <= int(rarity):
        color_for_turtle = "grey"
        return("\033[1;32;40mCommon %s\033[1;37;40m\n" % (name))
      elif 5000 <= int(rarity):
        color_for_turtle = "lime"
        return("\033[1;32;40mNormal %s\033[1;37;40m\n" % (name))
      elif 4000 <= int(rarity):
        color_for_turtle = "lime"
        return("\033[1;33;40mUncommon %s\033[1;37;40m\n" % (name))
      elif 3000 <= int(rarity):
        color_for_turtle = "lime"
        return("\033[1;33;40mLucky %s\033[1;37;40m\n" % (name))
      elif 2000 <= int(rarity):
        color_for_turtle = "blue"
        return("\033[1;34;40mRare %s\033[1;37;40m\n" % (name))
      elif 1000 <= int(rarity):
        color_for_turtle = "blue"
        return("\033[1;34;40mOutstanding %s\033[1;37;40m\n" % (name))
      elif 500 <= int(rarity):
        color_for_turtle = "blue"
        return("\033[1;36;40mExceptional %s\033[1;37;40m\n" % (name))
      elif 300 <= int(rarity):
        color_for_turtle = "purple"
        return("\033[1;35;40mepic %s\033[1;37;40m\n" % (name))
      elif 150 <= int(rarity):
        color_for_turtle = "pink"
        return("\033[1;35;40mLegendary %s\033[1;37;40m\n" % (name))
      elif 50 <= int(rarity):
        color_for_turtle = "red"
        return("\033[1;31;47mSupreme %s\033[1;37;40m\n" % (name))
      elif 10 <= int(rarity):
        color_for_turtle = "gold"
        return("\033[1;30;43mGodly %s\033[1;37;40m\n" % (name))
      elif 3 <= int(rarity):
        color_for_turtle = 0
        return("\033[1;31;40mD\033[1;32;40mi\033[1;33;40mv\033[1;34;40mi\033[1;35;40mn\033[1;36;40m\033[1;37;40me %s" % (name))
      else:
        color_for_turtle = 0
        return("\033[1;31;40mD\033[1;32;40mi\033[1;33;40mv\033[1;34;40mi\033[1;35;40mn\033[1;36;40m\033[1;37;40me %s" % (name))

    #character pulling sequence
    character_turtle.clear()
    rarity_bar_draw()
    x = if_num
    while x < int(pull):
      #random character data
      char_picker = random.randint(0, int(list_end))
      non_pity_chance = random.randint(0, 10000)
      if pity == 0:
        chance = non_pity_chance
      
      else:
        chance = pity_op(non_pity_chance)


      #character and rarity grabber
      character_name = re.search("\D+", characters[int(char_picker)])
      character_rarity = re.search("\d+", characters[int(char_picker)])
      if chance <= int(character_rarity.group()):

        #gacha results

        if int(character_rarity.group()) > 150:
          rolls = rolls + 1
        
        else:
          rolls = 0

        print("you pulled a(n) %swhich has a %s out of 10000 chance!" % (rarity_color(character_rarity.group(), character_name.group()), character_rarity.group()))

        if debug == 1:
          print("\ndebug\npity on:%s\nrolls:%s\nchance without pity:%s\npity chance:%s\npity tier:%s\n" % (pity, rolls, non_pity_chance, chance, pity_tier))
        else:
          None

        file = open("pull_history.txt", "a+")
        file.write("%s %s\n" % (character_name.group(), character_rarity.group()))
        file.close()

        print(character_name.group(), "\n")

        #saving caracter data
        character_data = open("character_data.txt", "a+")
        character_data.write("%s\n" % (character_name.group()))
        character_data.close()

        rolling_turtle.penup()

        rolling_turtle.goto(rarity_bar_xval, rarity_bar_yval + int(int(character_rarity.group())/rarity_size_shrinker))

        rolling_turtle.pendown()

        rolling_turtle.goto(rarity_bar_xval + rarity_bar_width, rarity_bar_yval + int(int(character_rarity.group())/rarity_size_shrinker))

        character_turtle.penup()

        character_turtle.hideturtle()

        character_turtle.goto(rarity_bar_xval + rarity_bar_width, rarity_bar_yval + int(int(character_rarity.group())/rarity_size_shrinker))

        character_turtle.pendown()
        
        character_turtle.showturtle()

        if color_for_turtle == 0:
          while x < len(list(character_name.group()[x])):
            divine_colors = ["red", "green", "orange", "blue", "purple"]

            character_turtle.color(divine_colors[x])

            character_turtle.write(list(character_name.group()[x]))

            x = x + 1

        else:
          character_turtle.color(color_for_turtle)

          character_turtle.write(character_name.group(), font=("Calibri", font_size, "bold"), move=True)

          character_count_turtle.color(color_for_turtle)
        
        rolling_turtle.penup()

        rolling_turtle.goto(0, 0)

        x = x + 1
        char_picker = random.randint(0, int(list_end))
        chance = random.randint(0, 10000)

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

        side_leaderboard()
        
      else:
        char_picker = random.randint(0, int(list_end))
        chance = random.randint(0, 10000)

    #output
    print("you pulled %s characters!\nyou have %s points left!\nit has been %s rolls since a good roll" % (int(pull_reply), credits_spent, rolls))

    

    rolling_turtle.clear()

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

    """#reading config and options
    with open("config.txt", "a+") as f:
      config = f.read().splitlines()"""

    options = input("\n\n\n\n\n\n\n\n1, reset data\n2, pity %s\n3, debug %s\n4, back\n" % (pity, debug))

    if options == "1":
      file = open("character_data.txt","r+")
      file.truncate(0)
      file.close()

      file = open("GC.txt", "w+")
      file.truncate(0)
      file.write("20")
      file.close()

      file = open("leaderboard.txt", "r+")
      file.truncate(0)
      file.close()

      file = open("pull_history.txt", "r+")
      file.truncate(0)
      file.close()

      rolls = 0

      """config[0].write("pity = 0")
      config.close"""

    elif options == "2":
      if pity != 1:
        pity = 1

      else:
        pity = 0

    elif options == "3":
      if debug != 1:
        debug = 1
      
      else:
        debug = 0

    else:
      print("going back...")
      #config.close()

  else:
    break

#visual output function
output.mainloop()

#saving the log
logging.basicConfig(filename="debug.log", level=logging.INFO)