def game():
    return 464

score=game()

with open("hiscore.txt") as f:
    hiScoreStr=int(f.read())
if hiScoreStr=='':
    with open("hiscore.txt","w") as f:
        f.write(str(score))


if int(hiScoreStr)<score or hiScoreStr=='':


    with open("hiscore.txt","w") as f:
        f.write(str(score))
    
   