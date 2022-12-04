inp = open("input", 'r')

# A = Rock
# B = Paper
# C = Scissors
# X = Lose
# Y = Tie
# Z = Win

result = {
    'A':{'X':3+0,'Y':1+3,'Z':2+6},
    'B':{'X':1+0,'Y':2+3,'Z':3+6},
    'C':{'X':2+0,'Y':3+3,'Z':1+6},

}


score = 0
for match in inp:
    they  = match[0]
    you = match[2]
    score+= result[they][you]

print(score)

# Part 1
'''
inp = open("input", 'r')

# A = X = Rock
# B = Y = Paper
# C = Z = Scissors

result = {
    'A':{'X':1+3,'Y':2+6,'Z':3+0},
    'B':{'X':1+0,'Y':2+3,'Z':3+6},
    'C':{'X':1+6,'Y':2+0,'Z':3+3},

}


score = 0
for match in inp:
    they  = match[0]
    you = match[2]
    score+= result[they][you]

print(score)
'''
