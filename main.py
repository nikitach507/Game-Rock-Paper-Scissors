import random
comp_turn = ["k", "n", "b"]
game = True
while game:
    print("k - kamen, n - nozhnici, b - bumaga, exit - vyhod")
    turn = input()
    if turn == "k": print("kamen - your turn")
    elif turn == "b": print("bumaga - your turn")
    elif turn == "n": print("nozhnici - your turn")
    elif turn == "exit":
        print("bye")
        game = False
    c_turn = random.choice(comp_turn)
    if c_turn == "k":
        c_turn = "kamen"
    elif c_turn == "b":
        c_turn = "bumaga"
    elif c_turn == "n":
        c_turn = "nozhnici"
    print(c_turn + " - computer turn")
    if turn == "k" and c_turn == "nozhnici":
        print("You win")
    if turn == "n" and c_turn == "bumaga":
            print("You win")
    if turn == "b" and c_turn == "kamen":
                print("You win")
    if turn == "k" and c_turn == "bumaga":
        print("You lose")
    if turn == "n" and c_turn == "kamen":
            print("You lose")
    if turn == "b" and c_turn == "nozhnici":
                print("You lose")
    if turn == "b" and c_turn == "bumaga":
        print("Draw")
    if turn == "n" and c_turn == "nozhnici":
            print("Draw")
    if turn == "k" and c_turn == "kamen":
                print("Draw")