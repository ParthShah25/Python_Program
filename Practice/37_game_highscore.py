def game():
    return 4

score = game()

with open("game.txt") as f:
    highscore = f.read()

if highscore == '':
    with open("game.txt","w") as f:
        f.write(str(score))

elif int(highscore) < score:
    with open("game.txt","w") as f:
        f.write(str(score))