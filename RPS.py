import random
l=["Rock","Scissor","Paper"]
while True:
    ccount=0
    ucount=0
    uc=int(input('''
Game Start...
 1 Yes
 2 No|Exit
                 '''))
    if uc==1:
        for a in range(1,6):
            userinput=int(input('''
1 Rock
2 Scissor
3 Paper
                                '''))
            if userinput==1:
                uchoice='Rock'
            elif userinput==2:
                uchoice="Scissor"
            elif userinput==3:
                uchoice="Paper"
            Cchoice=random.choice(l)
            if Cchoice==uchoice:
                print("Computer value",Cchoice)
                print("User value",uchoice)
                print("Game Draw")
                ucount=ucount+1
                ccount=ccount+1
            elif (uchoice=="Rock" and Cchoice=="Scissor") or (uchoice=="Paper" and Cchoice=="Rock") or (uchoice=="Scissor" and Cchoice=="Paper"):
               
                print("Computer value",Cchoice)
                print("User value",uchoice)
                print("You win")
                ucount=ucount+1
            else:
                print("Computer value",Cchoice)
                print("User value",uchoice)
                print("Computer win")
                ccount=ccount+1
        if ucount==ccount:
            print("Final Game Draw...")
            print("User Score",ucount)  
            print("Computer Score",ccount)
        elif ucount>ccount:
            print("Final  You win the Game...")
            print("User Score",ucount)  
            print("Computer Score",ccount)
        else:
            print("Final Computer win the Game...")
            print("User Score",ucount)  
            print("Computer Score",ccount)
    else:
        break


        


            