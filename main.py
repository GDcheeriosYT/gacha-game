import random
import turtle as t
import re
import os

#turtle config
font_setup = ("Arial", 20, "normal")

#rolling turtle
rolling_turtle = t.Turtle()
rolling_turtle.penup()
rolling_turtle.goto(-50, 75)
rolling_turtle.pensize(5)

#rolling turtle inner color
rolling_inner_turtle = t.Turtle()
rolling_inner_turtle.color("white")
rolling_inner_turtle.penup()
rolling_inner_turtle.goto(-50, 75)
rolling_inner_turtle.pensize(2)

with open("characters.txt") as f:
  characters = f.read().splitlines()

list_end = len(characters) - 1

pull = 5
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
    pull = input("\n\n\n\n\n\n\n\nhow much do you want to pull?\n\n ")


    #money function
    def spend(x, y):
      z = re.search("\d+", GC_read[len(GC_read)- 1])
      if int(z.group()) >= int(y):
        z = int(y) - int(x)
      else:
        z = int(y) - int(x)
        print("not enough points")
      return(z)
    
    gacha_credits = spend(pull, gacha_credits.group())
    GC.write("\n%s" % (gacha_credits))
    GC.close()

    if gacha_credits < int(pull):
      print("not enough gacha points")
      if_num = int(pull)
    else:
      if_num = 0

    def rarity_color(x, y):
      if 9000 <= int(x):
        return("\033[1;31;40mSuper dooper common %s\033[1;37;40m\n" % (y))
      elif 8000 <= int(x):
        return("\033[1;31;40mVery common %s\033[1;37;40m\n" % (y))
      elif 7000 <= int(x):
        return("\033[1;31;40mPretty common %s\033[1;37;40m\n" % (y))
      elif 6000 <= int(x):
        return("\033[1;32;40mCommon %s\033[1;37;40m\n" % (y))
      elif 5000 <= int(x):
        return("\033[1;32;40mNormal %s\033[1;37;40m\n" % (y))
      elif 4000 <= int(x):
        return("\033[1;33;40mUncommon %s\033[1;37;40m\n" % (y))
      elif 3000 <= int(x):
        return("\033[1;33;40mLucky %s\033[1;37;40m\n" % (y))
      elif 2000 <= int(x):
        return("\033[1;34;40mRare %s\033[1;37;40m\n" % (y))
      elif 1000 <= int(x):
        return("\033[1;34;40mOutstanding %s\033[1;37;40m\n" % (y))
      elif 500 <= int(x):
        return("\033[1;36;40mExceptional %s\033[1;37;40m\n" % (y))
      elif 300 <= int(x):
        return("\033[1;35;40mepic %s\033[1;37;40m\n" % (y))
      elif 150 <= int(x):
        return("\033[1;35;40mLegendary %s\033[1;37;40m\n" % (y))
      elif 50 <= int(x):
        return("\033[1;31;47mSupreme %s\033[1;37;40m\n" % (y))
      elif 10 <= int(x):
        return("\033[1;30;43mGodly %s\033[1;37;40m\n" % (y))
      elif 3 <= int(x):
        return("\033[1;31;40mD\033[1;32;40mi\033[1;33;40mv\033[1;34;40mi\033[1;35;40mn\033[1;36;40m\033[1;37;40me %s" % (y))
      

    #character pulling sequence
    x = if_num
    while x < int(pull):
      #random character data
      char_picker = random.randint(0, int(list_end))
      chance = random.randint(0, 10000)


      #character and rarity grabber
      character_name = re.search("\D+", characters[int(char_picker)])
      character_rarity = re.search("\d+", characters[int(char_picker)])
      if chance <= int(character_rarity.group()):
        print("you pulled a(n) %swhich has a %s out of 10000 chance!" % (rarity_color(character_rarity.group(), character_name.group()), character_rarity.group()))
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

        #gacha results
        #animation
        #picking the color
        def rolling_animation():
          x = 0
          while x < 1:
            def color_picker():
              if 10000 <= int(character_rarity.group()):
                return "black"
              elif 9000 <= int(character_rarity.group()):
                return "black"
              elif 8000 <= int(character_rarity.group()):
                return "red"
              elif 7000 <= int(character_rarity.group()):
                return "red"
              elif 6000 <= int(character_rarity.group()):
                return "green"
              elif 5000 <= int(character_rarity.group()):
                return "green"  
              elif 4000 <= int(character_rarity.group()):
                return "yellow"
              elif 3000 <= int(character_rarity.group()):
                return "gold"
              elif 2000 <= int(character_rarity.group()):
                return "blue"
              elif 1000 <= int(character_rarity.group()):
                return "blue"
              elif 500 <= int(character_rarity.group()):
                return "cyan"
              elif 300 <= int(character_rarity.group()):
                return "purple"
              elif 150 <= int(character_rarity.group()):
                return "purple"
              elif 50 <= int(character_rarity.group()):
                return "red"
              elif 10 <= int(character_rarity.group()):
                return "yellow"
              elif 3 <= int(character_rarity.group()):
                return "joe"

              #turtle basics
            
              t.speed(100)

              t.color("red")

              for i in range(10):
                x = random.randint(-250, 250)
                y = random.randint(-250,250)
                t.penup()
                t.goto(x,y)
                t.pendown()

                if color_picker() == "joe":
                  t.color()

                t.color(color_picker())

                size = 10000 - character_rarity.group()
                for i in range(36):
                  t.forward(size)
                  t.backward(size)
                  t.left(10)

                t.bgpic(picname="brian.png")


            pull_location = random.randint(-50, 100)
            rolling_inner_turtle.goto(-50, pull_location)
            rolling_turtle.goto(-50, pull_location)
            rolling_turtle.color(color_picker())
            if color_picker() == "joe":
              rolling_inner_turtle.pendown()
              rolling_turtle.pendown()
              rolling_turtle.goto(50, pull_location)
              pp = 0
              while pp < 5:
                rolling_inner_turtle.goto(1, pull_location)
                rolling_turtle.penup()
                rolling_inner_turtle.penup()
                colors = ["green", "blue", "purple", "orange", "yellow"]
                inner_color = colors[pp - 1]
                
            else:
              rolling_inner_turtle.pendown()
              rolling_turtle.pendown()
              rolling_turtle.goto(50, pull_location)
              rolling_inner_turtle.goto(50, pull_location)
              rolling_turtle.penup()
              rolling_inner_turtle.penup()
            x = x + 1

        #output
        rolling_animation()
        print("you pulled %s characters!\n you have %s points left!" % (int(if_num), gacha_credits))

        
      else:
        char_picker = random.randint(0, int(list_end))
        chance = random.randint(0, 10000)

  elif menu == "2":
    #money function
    shop = input("\n\n\n\n\n\n\n\n1, buy gacha credits\n2, see how many points you have\n")
    if shop == "1":
      def buy(x, y):
        buy_money = input("\n\n\n\n\n\n\n\nhow many credits will you buy? ")
        try:
          buy_money
        except ValueError:
          print("expected an actual number kid...")
        
        buy_money2 = int(buy_money) + int(y)
        spend_money = int(x) - int(y)
        mom_credit_card_num = random.randint(1000000000000000, 9999999999999999)
        mom_credit_card_csv = random.randint(100, 999)
        mom_credit_card_mon = random.randint(1, 12)
        mom_credit_card_day = random.randint(20, 24)
        gacha_credits = buy_money2

        if int(gacha_credits) <= 0:
          print("not enough money")
        else:
          print("using your moms credit card info...\nnumber: %s\ncsv: %s\nexp date: %s/%s" % (mom_credit_card_num, mom_credit_card_csv, mom_credit_card_mon, mom_credit_card_day))
          
        return(gacha_credits)
      gacha_credits = buy(pull, gacha_credits.group())
      GC.write("\n%s" % (gacha_credits))
      GC.close()
    else:
      print("you have ", gacha_credits.group(), "points")
  
    
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
output = t.Screen()
output.bgcolor("black")
output.mainloop()