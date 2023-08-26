from termcolor import colored 
import random
import time
import os


# initialize
size = 26
rock_color = 'green'
scissor_color = 'red'
paper_color = 'yellow'

rock = colored('r', rock_color)
scissor = colored('s', scissor_color)
paper = colored('p', paper_color)
game_floor = '.'


def show_game(b:list) -> list:
    """Show the game screen"""
    for item in b:
        for sub_item in item:
            print(sub_item , end=' ')
        print()

def evaluation(b:list, size:int) -> list:
    """Leading a generation of gaming"""

    for y, item in enumerate(b):
        for x, current_item in enumerate(item):

            if current_item != game_floor:

                neighbors = []

                for i in range(y-1 , y+2):
                    for j in range(x-1 , x+2):
                        if i in range(size) and j in range(size):
                            # if i == y or j == x: # Find neighbors that are only above, below, left and right of the current home (you can enable this condition for this)
                            if (i,j) != (y,x):
                                neighbors.append((b[i][j], i, j))
                
                enemy, ye, xe = random.choice(neighbors) # ye => y enemy , xe => x enemy
                    
                if current_item == rock and enemy == scissor:
                    b[ye][xe] = rock
                elif current_item == rock and enemy == paper:
                    b[y][x] = paper
                elif current_item == paper and enemy == scissor:
                    b[y][x] = scissor
                elif current_item == paper and enemy == rock:
                    b[ye][xe] = paper
                elif current_item == scissor and enemy == paper:
                    b[ye][xe] = scissor
                elif current_item == scissor and enemy == rock:
                    b[y][x] = rock
    
    return b

def generation_review(b:list) -> tuple[str, str]:
    """Count the number of rocks, paper and scissors in each evolution"""

    number_of_rock = 0
    number_of_scissor = 0
    number_of_paper = 0

    for item in b:
        for sub_item in item:
            if sub_item == rock:
                number_of_rock += 1
            elif sub_item == scissor:
                number_of_scissor += 1
            elif sub_item == paper:
                number_of_paper += 1
    
    if number_of_rock == 0 and number_of_paper == 0 and number_of_scissor > 0:
        return 'Scissors', scissor_color
    elif number_of_rock == 0 and number_of_scissor == 0 and number_of_paper > 0:
        return  'Papers', paper_color
    elif number_of_scissor == 0 and number_of_paper == 0 and number_of_rock > 0:
        return 'Rocks', rock_color
         
def game(b:list, page_update_delay_value=0):
    """Run game"""

    os.system("")

    number_of_generation = 0

    
    while True:

        check_end_game = generation_review(b)
        
        os.system('cls')

        show_game(b)
        evaluation(b, size)

        
        number_of_generation += 1


        time.sleep(page_update_delay_value)

        if check_end_game:
            print()
            print(f"After {colored(number_of_generation, 'blue')} years of war, {colored(check_end_game[0], check_end_game[1])} finally ruled the world.")
            break
        


if __name__ == '__main__': 

    # make game board
    board = [[random.choice([rock, paper, scissor, game_floor]) for _ in range(size)] for _ in range(size)]  

    game(board)