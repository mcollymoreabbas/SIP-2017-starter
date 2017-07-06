start = '''
you're an Instagram baddie and want a cute picture on Mission Peak for your main.
'''


print(start)


print("type 'left' to go left or 'right' to go right.")
user_input = input()
if user_input == "left":
    print("you decide to go left and it's gorgeous but there's a difficult hike ahead") # finished the story by writing what happens
    print("there's a big snake up ahead that's blocking your path")
    print("type 'down' to turn around and run down the hill and quit or 'up' to step over the snake and keep going")
    user_input1 = input()
    if user_input1 == "down":
        print("you turned around and quit! Game Over!!!")
    elif user_input1 == "up":
        print("you ran away from the snake and straight into a cave")
        print("there are two glowing orbs in front of you")
        print("type 'run' to leave the cave and get that picture!!!")
        print("type 'orbs' to go towards the light")
        user_input4 = input()
        if user_input4 == "run":
            print ("nice job! go get that pic insta baddie!")
        elif user_input4 == "orbs":
            print("its an angry deer and it runs over you, RIP. GAMEOVER!!!!")


elif user_input == "right":
    print("you choose to go right and it's pretty ugly, not a lot of foliage, but it's a smooth and easy path ahead") # finished the story writing what happens
    print("there's an aggressive bull ahead, he looks angry")
    print("type 'up' to run away from the bull up the hill for your picture or 'down' to run down the hill and quit")
    user_input2 = input()
    if user_input2 == "down":
        print ("you turned around and quit, GAMEOVER!!")
    elif user_input2 == "up":
        print("dodge the bull and run into a ditch")
        print("type 'nap' to lay down and take a nap because your tired or type 'climb' to get out of ditch")
        user_input3 = input()
        if user_input3 == "nap":
            print ("you take 2 hours longer, but you get the picture! Nice job!")
        elif user_input3 == "climb":
            print ("you're spooked from all of the scary stuff during your hike, you climb out and go home. GAME OVER!!!!")
else:
    print ("umm wyd")

 
