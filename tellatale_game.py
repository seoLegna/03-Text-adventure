import time 

answer_a = "A".lower()
answer_b = "B".lower()
answer_c = "C".lower()
yes = ["Yes", "yes", "y", "Y"]
no = ["No", "no", "n", "N"]

axe = 0
fallen_branch = 0

print("Only use A, B and C or Yes and No or you will be sent back to your recent check point.")
time.sleep(1)

axe = 0

def the_abnormal_clearing1():
    print("""
    The abnormal clearing

    Tired and spent you lean against a tree for some relief, you close your eyes and collect yourself.
    You open your eyes very gently and see...
    a vast open feild with no trees. It is such an unsual sight from what you consider now to be the regular 
    that you slap yourself to wake from what you think is the consequence of exhaustion,
    but this impossible sight does not vanish. You are baffled and belive this to be somekind of abnormailty untill...
    you look at the scenery infront of you a little diffretnly. You now see the enormous numbers of stumps 
    that throng the ground infront of you, 
    the shear number of them pushes you back as you start to 
    remember the story you and your friends heard before comeing here.
    One stump per person.... 
    That is the only line that flashes through your head. 

    """
    )
    print("The stump nearest to you has an axe burried in it.")
    time.sleep(2)
    fallen_branch = 1
    if fallen_branch == 1:
        print("""
        Do you want to pick up the axe?
        Please answer with yes or no.
        """
        )
        fool = input(">>> ")
        if fool in yes: 
            print("""
            Sorry you can't pick it up
            should have waited huh?
            Lol.

            """
            )
        elif fool in no:
            print("""
            You decline it, your smart, you know your mistakes.
            Should have waited huh?
            Lol.

            """
            )
        else:
            the_abnormal_clearing()
    else: 
        print("That was not a valid input. Please answer with yes and no only.")
        the_abnormal_clearing()

    if fallen_branch == 1:
        time.sleep(7)
        print("""
        You run right past the axe and keep running for a while, untill....
        It appears, almost from nowhere. 
        It was an abomination something so horrendous only looking at it made you uneasy.
        It was an humanoid... thing, coverd with green coloured rags, hunched and holding something
        very... unusual, it was holding just a very sharp branch, about the size of it's own body.

        You step-back cowering at this ugly monster.
        'You are going to kill me aren't you. Then do it just like you slaughtred all my fellow 
        resarchers and archeologists. We should have heeded the warnings of the people of the closeby village.
        What even are you?' You ask in a very shakey and angry voice.

        It replies, 'I.... I am thy death... thee shall scream and grow the great tree. 
        All the others I shall cut and... remain only shall the great tree.'

        You realize that this is a mad-man.

        You remember the branch that you hold and run at it while brandishing it, 
        desperately trying to protect your life.

        With a flick of it's wrist it skweers you.

        You vomit blood while screeming with agony and anger.
        It laughs and watches you bleed to death.

        You bleekly see the ground before loosing all sense.


        You open your eyes...
        You remember nothing


        This is the amazon rainforest. There are rich trees and foliage everywhere.......

        THE END



        """
        )
        time.sleep(30)
        print("Do you want to play again? ")
        choose = input(">>> ")
        if choose in yes:
            intro()
        elif choose in no:
            print("Thank you for playing.")
    else:
        the_abnormal_clearing()

def the_abnormal_clearing():
    fallen_branch = 0
    print("""
    The abnormal clearing

    Tired and spent you lean against a tree for some relief, you close your eyes and collect yourself.
    You open your eyes very gently and see...
    a vast open feild with no trees. It is such an unsual sight from what you consider now to be the regular 
    that you slap yourself to wake from what you think is the consequence of exhaustion,
    but this impossible sight does not vanish. You are baffled and belive this to be somekind of abnormailty untill...
    you look at the scenery infront of you a little diffretnly. You now see the enormous numbers of stumps 
    that throng the ground infront of you, 
    the shear number of them pushes you back as you start to 
    remember the story you and your friends heard before comeing here.
    One stump per person.... 
    That is the only line that flashes through your head. 

    """
    )
    print("The stump nearest to you has an axe burried in it.")
    time.sleep(2)
    print("""
        Do you want to pick up the axe?
        Please answer with yes or no.
        """
        )
    fool = input(">>> ")
    if fool in yes:
        axe = 1
    elif fool in no:
        axe = 0
    else:
        the_abnormal_clearing()
        

    if axe == 1:
        time.sleep(7)
        print("""
        You pulled the axe out of the tree stump near you and turned around fast.
        You could see nothing but the feeling of dread and being watched was still present, 
        you were just wating for one movement to hack your enemy into pices.
        

        Then you saw it...

        An abomination, something so horrendous only looking at it made you uneasy.
        It was an humanoid... thing, coverd with green coloured rags, hunched and holding something
        very... unusual, it was holding just a very sharp branch, about the size of it's own body.

        You asked it with the raw anger you were feeling, 'Why? why do you do this to people?'.

        In a very cold and raw voice it replied, 'answer the dead men I do not'
        and suddeny jumped at you with terrifying speed and agility with you did not expect or belive this 
        morbid thing could achive.

        You countered his speedy jab by springing back. It immidietly changed the 'spears' direction and 
        stabbed you in your stomach.

        You fell on the ground, blood driping from the corners of your mouth.
        It was so close to you that now you could smell it and god did it smell disgusting.
        You looked at it and saw it laughing. 

        That was it, something snapped inside of you and you swinged your axe at his feet with blinding speed.
        It tried to jump but it just didn't expect it, you cleanly chopped off both of it's legs from under it.
        It howled in agony and fell to the ground beside you. You, somehow with what felt like superhuman 
        reflexes did not miss this opportunity and sliced it's head clean off.

        It was now dead. 
        You were happy but quickly dying due to bloodloss and internal bleeding.

        You try to stand but you can't...

        You lie on the ground beside this dead abomination and look up at the sky,
        then suddenly everything goes blank.



        You open your eyes and you remember nothing


        This is the amazon rainforest. There are rich trees and foliage everywhere.......

        THE END


        """
        ) 
        time.sleep(30)
        print("Do you want to play again? ")
        choose = input(">>> ")
        if choose in yes:
            intro()
        elif choose in no:
            print("Thank you for playing.")
    elif axe == 0:
        time.sleep(7)
        print("""
        You run right past the axe and keep running for a while, untill....
        It appears, almost from nowhere. 
        It was an abomination something so horrendous only looking at it made you uneasy.
        It was an humanoid... thing, coverd with green coloured rags, hunched and holding something
        very... unusual, it was holding just a very sharp branch, about the size of it's own body.

        You step-back cowering at this ugly monster.
        You have no weapon.

        You fall to  your knees and close your eyes, accepting your fate.

        You are dead

        Try again


        """
        )
        time.sleep(10)
        intro()
    else:
        the_abnormal_clearing()
    


def the_galadrielic_tree():
    fallen_branch = 0
    print("""
    You ran and ran until you could no longer.
    You finally stop and catch your breath, hunched on your knees you see blood on the ground.
    You look up and see...
    An enourmous magnificent biennil.
    It has gleaming leaves and a hardned bark like a tree born in gods own park.
    After shaking yourself out of this reverent stupor you realise what lied below this enormous structre,
    were not it's roots but several heaps of creatures.... humans some of which you somehow knew, now fallen near a broken branch.
    You then apprehend the reason for its abnormal size and you realize...
    You were not the only ones.
    Only one word comes to your mind after this shaking sight..'Galadriellic'.
    """
    )
    print("""
    Do you want to pick up the branch?
    
    You should know that you can only pick up one weapon throught the game.
    Please enter Yes or No
    """
    )
    time.sleep(1)
    weapon_choice = input(">>> ")
    if weapon_choice in yes:
        fallen_branch = 1
        print("You chose to pick up the branch")
    else: 
        print("You did not pick up the branch")


    print("""
    What will you do now?

    """
    )    
    time.sleep(2)
    print("""
    A. Go near the tree and see if someone is alive
    B. Stay and rest a bit more
    C. Run until you find somethig to properly protect yourself
    """
    )
    choice = input(">>> ") 
    if choice == answer_a and fallen_branch == 1:
        print("""
        You go near the tree to check on your fallen comrades
        You check each of them even the other people you didn't know but...
        They were all dead.
        As you start to rise from near your comrades, you feel a movement behind you...
        You feel like someone is standing behind you, and then you hear it...
        A voice as rough, shrill and inhumane as scratching a blackboard with your nails.
        I will kill you to death it said...
        You want to laugh but you don't, considering its feelings and this story's tone so far.
        You realize that you are holding the branch and turn around as fast as you could but...
        Suddenly you feel something go through you at a tremendous speed and you fall.
        Even before witnessing the creature that stood behind you...
        You are dead.
        
        Try again"""
        )
        time.sleep(25)
        intro()
    elif choice == answer_a and fallen_branch != 1:
        print("""
        You go near the tree to check on your fallen comrades
        You check each of them even the other people you didn't know but...
        They were all dead.
        As you start to rise from near your comrades, you feel a movement behind you...
        You feel like someone is standing behind you, and then you hear it...
        A voice as rough, shrill and inhumane as scratching a blackboard with your nails.
        I will kill you to death it said...
        You want to laugh but you don't considering its feelings and this storys tone so far.
        You ask it 'Who are you?'
        You hear it say 'You'r death'.
        You feel a slight pain somewhere around your neck before everything goes dark.
        You are dead.
        
        Try again
        """
        )
        time.sleep(25)
        intro()   
    elif choice == answer_b:
        print("""
        You rest a bit more and then die.
        The end.
        
        You are dead
        
        Of course, come on now, you knew that was going to happen
        What else did you expect?
        
        Try again
        """
        )
        time.sleep(5)
        intro()
    elif choice == answer_c and fallen_branch == 1:
        the_abnormal_clearing1()
    elif choice == answer_c and fallen_branch == 0:
        the_abnormal_clearing()
    else:
        intro()



def intro():
    print("""
    The Amazon rainforest
    
    This is the great Amazon rainforest. There are trees and rich foliage everywhere.
    Everything seems to be.... alive.
    """
    )
    time.sleep(5)
    print("""
    You open your eyes and find yourself here.
    You can't seem to remember anything about how you came to be in this absurd situation.
    
    You try to stand and...
    There's something watching you, you feel it. Somehow you know...
    You stand up so quick it makes you dizzy."
    You ignore the pain and irritation in your head and..."
    You see blood on the tree infront of you."
    
    What will you do?
    """
    )
    time.sleep(2)
    print("""
    A. Run
    B. Stay and embrace the danger
    C. Let the pain in your body take over
    """
    )
    choice = input(">>> ")
    if choice == answer_a:
        the_galadrielic_tree()
    elif choice == answer_b:
        print("""
        You decide to stand your ground and fight.
        You scream in rage and raise your fists.
        Suddenly you feel something go through you at a tremendous speed and you fall.
        You are dead.
        
        Try again
        """
        )
        time.sleep(15)
        intro()
    elif choice == answer_c:
        print("""
        You let the pain in your head, in your legs, in your chest take over.
        You fall to the ground withought even feeling it and...
        You never wake up again.
        You are dead.
        
        Try again.
        """
        )
        time.sleep(15)
        intro()
    else:
        intro()

intro()

