import random
comp_turn = ["kamen", "nozhnici", "bumaga"]
game = True
comp_points = 0
user_points = 0
while game:
    print("k - kamen, n - nozhnici, b - bumaga, exit - vyhod")
    turn = input()
    c_turn = random.choice(comp_turn)
    if turn == "k":
        print("kamen - your turn")
        print(c_turn + " - computer turn")
    elif turn == "b":
        print("bumaga - your turn")
        print(c_turn + " - computer turn")
    elif turn == "n":
        print("nozhnici - your turn")
        print(c_turn + " - computer turn")
    elif turn == "exit":
        print("bye")
        game = False
    elif turn != "k" and turn != "n" and turn != "b":
        print("You wrote wrong")
    if turn == "k" and c_turn == "nozhnici":
        user_points = user_points + 1
        print("You win. Game score", user_points, ":", comp_points)
    if turn == "n" and c_turn == "bumaga":
        user_points = user_points + 1
        print("You win. Game score", user_points, ":", comp_points)
    if turn == "b" and c_turn == "kamen":
        user_points = user_points + 1
        print("You win. Game score", user_points, ":", comp_points)
    if turn == "k" and c_turn == "bumaga":
        comp_points = comp_points + 1
        print("You lose. Game score", user_points, ":", comp_points)
    if turn == "n" and c_turn == "kamen":
        comp_points = comp_points + 1
        print("You lose. Game score", user_points, ":", comp_points)
    if turn == "b" and c_turn == "nozhnici":
        comp_points = comp_points + 1
        print("You lose. Game score", user_points, ":", comp_points)
    if turn == "b" and c_turn == "bumaga":
        comp_points = comp_points + 1
        user_points = user_points + 1
        print("Draw. Game score", user_points, ":", comp_points)
    if turn == "n" and c_turn == "nozhnici":
        comp_points = comp_points + 1
        user_points = user_points + 1
        print("Draw. Game score", user_points, ":", comp_points)
    if turn == "k" and c_turn == "kamen":
        comp_points = comp_points + 1
        user_points = user_points + 1
        print("Draw. Game score", user_points, ":", comp_points)

