
s = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
def output():
    print("-"*10)
    for i in range(0, 9, 3):
        print("|", s[i], s[i + 1], s[i + 2], "|")
    print("-"*10)

def winner(s):
    dia_1 = s[0] + s[4] + s[8]
    dia_2 = s[2] + s[4] + s[6]

    c1 = s[0] + s[3] + s[6]
    c2 = s[1] + s[4] + s[7]
    c3 = s[2] + s[5] + s[8]

    r1 = s[0] + s[1] + s[2]
    r2 = s[3] + s[4] + s[5]
    r3 = s[6] + s[7] + s[8]

    combn = (dia_1, dia_2, c1, c2, c3, r1, r2, r3)

    x_trio = "XXX"
    o_trio = "OOO"
    
    result = None
    
    if x_trio in combn and o_trio in combn or abs(s.count("X") - s.count("O")) >= 2:
        result = "Impossible"
    elif x_trio not in combn and o_trio not in combn:
        if s.count("_") != 0:
            result = "Game not finished"
        else:
            result = "Draw"
    elif x_trio in combn and o_trio not in combn:
        result = "X wins"
    elif x_trio not in combn and o_trio in combn:
        result = "O wins"
    
    return result
    
# print(winner(s))

def user_move(mark):
    while True:
        user = input().split()
        try:
            user = list(map(int, user))
        except TypeError:
            print("You should enter numbers!")
        else:
            for num in user:
                if num not in (1, 2, 3):
                    print("Coordinates should be from 1 to 3!")
                    continue
        coordinates = {0:[1, 1], 1: [1, 2], 2: [1, 3],
                        3: [2, 1], 4: [2, 2], 5: [2, 3],
                        6: [3,1], 7: [3, 2], 8: [3, 3]}
        for key, value in coordinates.items():
            if user == value:
                if s[key] in ("X", "O"):
                    print("This cell is occupied! Choose another one!")
                    continue
                else:
                    s[key] = mark
                    return output()

def check_stop():
    x = winner(s)
    stop = x in ("X wins", "O wins", "Draw")
    return stop
                    
def play():
    output()                    
    while True:
        m = check_stop()
        if m:
            break
        user_move("X")
        m = check_stop()
        if m:
            break
        user_move("O")
        
        
play()
print(winner(s))
