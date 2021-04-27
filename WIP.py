#leveling system
experience = open("experience.txt", "w+")
xp = chance + chance / 2
xp = xp + xp
level = 0
max_xp = 10000
level_xp = 10000 * 2
level_xp = max_xp + max_xp * 2
experience.write("%s\n%s\n%s" % (level, xp, level_xp))
if level_xp <= xp:
  level = level + level
  level_xp = level_xp + level_xp  

#--------------------------------------------------------------------

#getting the right data
with open("experience.txt") as f:
  xptab = f.read().splitlines()

lvl = re.search("\d+", xptab[0])
exp = re.search("\d+", xptab[1])
emxp = re.search("\d+", xptab[2])
print("DEBUG:%s %s %s" % (lvl.group(), exp.group(), emxp.group()))