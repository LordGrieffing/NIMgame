import random as rd

def playerTurn():
    # Get player's turn
    player_turn = 0
    while True:
        try:
            player_turn = int(input("How many would you like to remove? "))
            if player_turn not in [1,2,3]:
                print("You have to select 1, 2, or 3")
            else:
                break
        except ValueError:
            print("You have to select 1, 2, or 3")

    return player_turn

def computerTurn(player_turn):
    comp_turn = 4 - player_turn
    return comp_turn



def main():
    
    num_of_pieces = 12
    turn_order = True
    player_turn = 0

    #Turn one is different from the rest of the turns, since the computer might let you win
    print("="*80)
    print("O "* num_of_pieces)
    print("There are %d pieces on the board" %num_of_pieces)
    
    #Player first turn
    player_turn = playerTurn()
    num_of_pieces -= player_turn

    # Upadate board
    print("="*80)
    print("O "* num_of_pieces)
    print("There are %d pieces on the board" %num_of_pieces)

    #Computer first turn
    comp_turn = computerTurn(rd.randint(1,3))
    num_of_pieces -= comp_turn
    print("I take %d pieces" %comp_turn)



    while num_of_pieces > 0:
        print("="*80)
        print("O "* num_of_pieces)
        print("There are %d pieces on the board" %num_of_pieces)

        # Player's turn
        if turn_order:
            
            player_turn = playerTurn()
            num_of_pieces -= player_turn
            # update turn
            turn_order = False

        # Computer takes a turn
        else: 
            
            comp_turn = computerTurn(player_turn)
            num_of_pieces -= comp_turn

            print("I take %d pieces" %comp_turn)

            # update turn
            turn_order = True


    if turn_order:
        print("I win the game")

    else:
        print("You win the game")


































if __name__ == "__main__":
    main()