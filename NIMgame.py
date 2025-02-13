def main():
    
    num_of_pieces = 12
    turn_order = True

    while num_of_pieces > 0:
        print("="*80)
        print("O "* num_of_pieces)
        print("There are %d pieces on the board" %num_of_pieces)

        # Player's turn
        if turn_order:

            # Get player's turn
            while True:
                try:
                    player_turn = int(input("How many would you like to remove? "))
                    if player_turn not in [1,2,3]:
                        print("You have to select 1, 2, or 3")
                    else:
                        break
                except ValueError:
                    print("You have to select 1, 2, or 3")

            num_of_pieces -= player_turn
            # update turn
            turn_order = False

        # Computer takes a turn
        else: 
            comp_turn = 4 - player_turn
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