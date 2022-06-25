import random
comp_turn = ["k", "n", "b"]
game = True
while game:
    print("k - kamen, n - nozhnici, b - bumaga, exit - vyhod")
    turn = input()
    if turn == "k": print("kamen")
    elif turn == "b": print("bumaga")
    elif turn == "n": print("nozhnici")
    elif turn == "exit":
        print("bye")
        game = False
    c_turn = random.choice(comp_turn)
    print(c_turn + " - computer turn")
    if turn == "k" and c_turn == "n":
        print("You win")
    if turn == "n" and c_turn == "b":
            print("You win")
    if turn == "b" and c_turn == "k":
                print("You win")
    if turn == "k" and c_turn == "b":
        print("You lose")
    if turn == "n" and c_turn == "k":
            print("You lose")
    if turn == "b" and c_turn == "n":
                print("You lose")
    if turn == "b" and c_turn == "b":
        print("Draw")
    if turn == "n" and c_turn == "n":
            print("Draw")
    if turn == "k" and c_turn == "k":
                print("Draw")