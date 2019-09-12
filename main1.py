import time 

answer_a = "A".lower()
answer_b = "B".lower()
answer_c = "C".lower()
yes = ["Yes", "yes", "y", "Y"]
no = ["No", "no", "n", "N"]

axe = 0
fallen_branch = 0

required = print("\n\nOnly use A,B and C or Yes and No")

def intro():
    print("The Amazon rainforest"
    ""
    "This is the great Amazon rainforest. There are trees and rich foliage everywhere."
    "Everything seems to be.... alive."
    ""
    )
    print("You open your eyes and find yourself here."
    "You can't seem to remember anything about how you came to be in this absurd situation."
    ""
    "You try to stand and..."
    "There's something watching you, you feel it. Somehow you know..."
    "You stand up so quick it makes you dizzy."
    "You ignore the pain and irritation in your head and..."
    "You see blood on the tree infront of you."
    ""
    "What will you do?"
    ""
    )
    time.sleep(2)
    print("A. Run"
    "B. Stay and embrace the danger"
    "C. Let the pain in your body take over"
    )
    choice = input(">>> ")
    if choice in answer_a:
        the_galadrielic_tree()
    elif choice in answer_b:
        print("You decide to stand your ground and fight."
        "You scream in rage and raise your fists."
        "Suddenly you feel something go through you at an tremendous speed and you fall."
        "You are dead."
        ""
        "Try again"
        )
        intro()
    elif choice in answer_c:
        print("You let the pain in your head, in your legs, in your chest take over."
        "You fall to the ground withought even feeling it and"
        "You never wake up again."
        "You are dead."
        ""
        "Try again."
        )
        intro()
    else:
        return required
        intro()
def the_galadrielic_tree():
    print("You ran and ran until you could no longer."
    "You finally stop and catch your breath, hunched on your knees you can see nothing infront of you."
    "You look up to get an idea of where you are now and you see..."
    "a
    "An enourmous magnificent biennil." 
    "It has gleaming leaves and a hardned bark like a tree born in gods own park." 
    "After shaking yourself out of this reverent stupor you realise what lied below this enormous structre," 
    "were not it's roots but several heaps of creatures.... humans which you somehow knew." 
    "You then realize the reason for its abnormal size and you realize..."
    "You were not the only ones."
    "Only one word comes to your mind after this shaking sight..'Galadriellic'."
    ""
    "What will you do now?"
    ""
    )
    time.sleep(2)
    print("A.")


   

