import pyautogui
from mines import Mine
# x, y = pyautogui.position()    #mouseun bulunduğu güncel kutucuğun pikselini verir.
X = 76
Y = 852

chosen_square_number = 0
mine = Mine()
mine.show_design()
mine.place_the_bomb()

is_game_on = True
while is_game_on:
    box_number = int(input('Which numbered box do you wanna open: '))
    pyautogui.click(X, Y)
    chosen_square_number += 1
    mine.select_number(box_number)
    mine.show_design()
    if '💣' in mine.design:
        print('You lose')
        mine.show_score()
        is_game_on = False

    elif chosen_square_number >= 8:
        print('You won')
        is_game_on = False

    else:
        mine.increase_score()
        mine.show_score()



