import time 

answer_a = "A".lower()
answer_b = "B".lower()
answer_c = "C".lower()
yes = ["Yes", "yes", "y", "Y"]
no = ["No", "no", "n", "N"]

axe = 0
fallen_branch = 0

required = print("\n\nOnly use A,B and C or Yes and No")
time.sleep(1)

def the_abnormal_clearing():
    return True

def the_galadrielic_tree():
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
    elif choice == answer_c:
        the_abnormal_clearing()
    else:
        return required
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
        return required
        intro()

intro()

