# name: Erich Ostendarp, Gabe Pesco
# Date: 9/20/17
# Purpose: Choose your own adventure story

answer = input("You are at a party and someone offers you a cup of punch. Do you\n1) Take the drink\n2) Politely refuse\n")

if (answer == '1'):
    print("You start drinking it, and feel the effects of the alcohol. You go to the dance floor and let loose. A little too loose.\nYou lose consciousness and wake up on a bench in the commons, with class in 6 minutes.")
elif (answer == '2'):
    answer = input("The person makes a frown and walks away. You find some of your friends, and they’re talking about getting out of here to go drive to the commons. Do you\n1) go with them,\n2) stay behind\n")
    if (answer == '1'):
        print("You all go on a drive, forgetting the fact that no one is sober enough to drive. Your friend wraps the car around a tree and the night is ruined.")
    else:
        answer = input("Your friends leave the party, and you get kind of bored. You remember you have a test tomorrow morning, but you want to have some fun. Do you\n1) go back to the dorms to study and sleep\n2) try and make new friends\n")
        if (answer == '1'):
            print("You’re one pretty lame, but you got a B+ on the test and nothing bad happened to you that night.")
        else:
            answer = input("You make some new friends from the lacrosse team. They’re wild and start snorting xanax off of a glass table. Do you\n1) join in\n2)get out of there\n")
            if (answer == '1'):
                print("You do xanax, can’t remember anything else, and regain consciousness feeling violated in a ditch somewhere. Not how you wanted the night to go. You missed your test tomorrow, and fail the course. Eventually you sink so low as to major in music ed.")
            else:
                print("You leave the party, and go back to your dorm to crash. You don’t have enough energy to study and get a C-. Could be worse.")
else:
    print("Go home, you're drunk. You can't even pick 1 or 2.")