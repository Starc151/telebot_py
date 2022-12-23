import random

status_game = list(range(1, 10))
free_position = list(range(1, 10))
victory_list = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

def set_global():
    global status_game, free_position
    status_game = list(range(1, 10))
    free_position = list(range(1, 10))

def view_xo(pos):
    pos = int(pos)
    sym = str(status_game[pos-1])
    return sym

def victory(s):
    for i in victory_list:
        if s == status_game[i[0]] == status_game[i[1]] == status_game[i[2]]:
            if s == 'x':
                return "Победа за вами"
            elif s == 'o':
               return "Победа за компьютером"
    return "empty"

def print_log(pos, sym):
    print(f'Ход {sym}: {pos}')
    print(status_game)
    print(free_position)

def comp_move():
    cp = random.choice(free_position)
    # Логика бота выключена, т.к. где-то ошибка.
    # Пофиксить не успеваю. Бот ходит рандомно 
    # for i in victory_list:
    #     if status_game[i[0]] == status_game[i[1]] == 'o' and status_game[i[2]] != ('x' or 'o'):
    #         cp = i[2]
    #         break
    #     elif status_game[i[0]] == status_game[i[2]] == 'o' and status_game[i[1]] != ('x' or 'o'):
    #         cp = i[1]
    #         break
    #     elif status_game[i[1]] == status_game[i[2]] == 'o' and status_game[i[0]] != ('x' or 'o'):
    #         cp = i[0]
    #         break
    #     elif (status_game[i[0]] == status_game[i[1]] == 'x') and status_game[i[2]] != ('x' or 'o'):
    #         cp = i[2]
    #         break
    #     elif (status_game[i[0]] == status_game[i[2]] == 'x') and status_game[i[1]] != ('x' or 'o'):
    #         cp = i[1]
    #         break
    #     elif (status_game[i[1]] == status_game[i[2]] == 'x') and status_game[i[0]] != ('x' or 'o'):
    #         cp = i[0]
    #         break
    #     elif status_game[i[0]] == 'o' and (status_game[i[1]] == status_game[i[2]] != ('x' or 'o')):
    #         cp = i[1]
    #         break
    #     elif status_game[i[2]] == 'o' and (status_game[i[0]] == status_game[i[1]] != ('x' or 'o')):
    #         cp = i[1]
    #         break
    #     elif status_game[i[1]] == 'o' and (status_game[i[0]] == status_game[i[2]] != ('x' or 'o')):
    #         cp = i[0]
    #         break
    status_game[cp-1]  = "o"
    print(f"Бот пытается взять: {cp}")
    free_position.remove(cp)
    print_log(cp, 'o')

def human_move(pos):
    pos = int(pos)-1
    status_game[pos] = 'x'
    free_position.remove(pos+1)
    print_log(pos+1, 'x')
