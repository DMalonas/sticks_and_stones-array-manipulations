# Stavroula Foteini Mytafidou 5430

import random

from board import draw_board, empty_board
from board import empty_point

board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
valid_moves = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
has_won = False


def get_x_or_o(player):
    if player == 1:
        return 'X'
    return 'O'


def get_row_from_coordinate(coordinates):
    return int(coordinates[0])


def get_column_from_coordinate(coordinates):
    return int(coordinates[1])


def check_if_three_in_any_winning_combination(coordinates, x_or_o):
    three_in_row = check_if_three_in_a_row(coordinates, x_or_o)

    three_in_column = check_if_three_in_a_column(coordinates, x_or_o)

    is_on_the_diagonal = check_if_pick_is_on_the_diagonal(coordinates)
    three_in_a_diagonal = False
    if is_on_the_diagonal:
        three_in_a_diagonal = check_if_three_in_a_diagonal(coordinates, x_or_o)

    is_on_the_antidiagonal = check_if_pick_in_on_the_antidiagonal(coordinates)
    three_in_the_antidiagonal = False
    if is_on_the_antidiagonal:
        three_in_the_antidiagonal = check_if_three_in_the_antidiagonal(coordinates, x_or_o)

    if three_in_column or three_in_row or three_in_a_diagonal or three_in_the_antidiagonal:
        return True
    return False


def check_if_three_in_a_row(coordinates, x_or_o):
    cnt = 0
    board_length = len(board[0])
    for column_number in range(board_length):
        row_number = get_row_from_coordinate(coordinates)
        board_value_x = board[row_number][column_number]
        if board_value_x == get_x_or_o(x_or_o):
            cnt += 1
            if cnt == 3:
                return True
    return False


def check_if_three_in_a_column(coordinates, x_or_o):
    cnt = 0
    for i in range(len(board)):
        if board[i][int(coordinates[1])] == get_x_or_o(x_or_o):
            cnt += 1
            if cnt == 3:
                return True
    return False


def check_if_three_in_a_diagonal(coordinates, x_or_o):
    cnt = 0
    board_number_of_rows = len(board)
    for row in range(board_number_of_rows):
        diagonal_element = board[row][row]
        if diagonal_element == get_x_or_o(x_or_o):  # and board[row][row] != '-':
            cnt += 1
        if cnt == 3:
            return True
    return False


def check_if_three_in_the_antidiagonal(coordinates, x_or_o):
    cnt = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if ((i + j) == get_antidiagonal_sum()) and get_x_or_o(x_or_o) == board[i][j]:
                cnt += 1
                if cnt == 3:
                    return True
    return False


def check_if_pick_is_on_the_diagonal(coordinates):
    if int(coordinates[0]) == int(coordinates[1]):
        return True


def check_if_pick_in_on_the_antidiagonal(coordinates):
    i_plus_j = get_antidiagonal_sum()
    if (get_row_from_coordinate(coordinates) + get_column_from_coordinate(coordinates)) == i_plus_j:
        return True
    return False


def get_antidiagonal_sum():
    row = board[0]
    anti_diagonal_element = row[-1]
    column_index_of_top_antidiagonal_element = len(row) - 1
    # antidiagonal elements have the same i + j
    i_plus_j = column_index_of_top_antidiagonal_element + 0
    return i_plus_j


def convert_input_to_numerical_coordinates(choice):
    row = int(ord(choice[0]) - 65)  # because A=65 in ASCII
    col = int(choice[1]) - 1
    return [row, col]


def choose_who_plays_first():
    return random.randint(1, 2)


def load_player_info(player):
    if player == 1:
        return ["1", "X"]
    else:
        return ["2", "O"]


def check_that_length_of_input_is_2(choice):
    if len(choice) != 2:
        print("{} doesnt have length equal to 2\n".format(choice))
        return False
    return True


def check_if_destination_position_is_occupied(row, column):
    position_we_requested_to_occupy = board[row][column]
    if position_we_requested_to_occupy != '-':
        print("Position taken by another peg. Please re-enter.\n")
        return True
    return False


def check_if_player_wants_to_play_again():
    choice = input("Type 'Y' or 'y' to play again: ")
    if (choice != 'Y' and choice != 'y'):
        exit(1)
    return True


def allocate_peg_for_player(player, choice, is_first_round):
    # pegs_cnt = 0
    # result = True
    # result = check_that_length_of_input_is_2(choice)
    if ('A' <= choice[0] <= 'C') and ('1' <= choice[1] <= '3'):
        coordinates = convert_input_to_numerical_coordinates(choice)
        row = coordinates[0]
        column = coordinates[1]
        print("row {} column {}".format(row, column))
        result = check_if_destination_position_is_occupied(row, column)
        if not result:
            board[row][column] = get_x_or_o(player)
            is_winning_combination = check_if_three_in_any_winning_combination(coordinates, player)
            if is_winning_combination and is_first_round:
                print("Invalid position. Cannot complete 3-in-a-row at this stage.\n")
                board[row][column] = '-'
                return False
            elif is_winning_combination and not is_first_round:
                board[row][column] = get_x_or_o(player)
                print("Player {} wins\n".format(player))
                allocation_was_successful = True
                draw_board(choice, get_x_or_o(player), allocation_was_successful)
            elif not is_winning_combination:
                board[row][column] = get_x_or_o(player)
                return True
        else:
            return False
    else:
        print("Invalid position. Not a board position. Please re-enter.\n")
        return False


def check_if_origin_position_is_occupied_by_players_peg(player, origin):
    cartesian_point = convert_input_to_numerical_coordinates(origin)
    row = cartesian_point[0]
    column = cartesian_point[1]
    origin_position_requested = board[row][column]
    if origin_position_requested != get_x_or_o(player):
        print("Invalid move. Origin is not occupied by player's %d peg\n" % (player))
        return False
    return True


def check_data_is_four_characters_that_exist_as_coordinates(choice):
    length_of_choice = len(choice)
    if length_of_choice != 4:
        return False
    else:
        origin_point = choice[0] + choice[1]
        destination_point = choice[2] + choice[3]
        if valid_moves.__contains__(origin_point) and valid_moves.__contains__(destination_point):
            return True
        return False


def points_have_distance_1_and_in_same_diagonal_or_antidiagonal(col_1, col_2, row_1, row_2):
    return ((abs(row_1 - row_2) == 1) and (abs(col_1 - col_2) == 1))


def points_have_distance_1_and_in_same_row(col_1, col_2, row_1, row_2):
    return ((abs(row_1 - row_2) == 0) and (abs(col_1 - col_2) == 1))


def points_have_distance_1_and_in_same_column(col_1, col_2, row_1, row_2):
    return ((abs(row_1 - row_2) == 1) and (abs(col_1 - col_2) == 0))


def check_move_has_range_1(choice):
    point1 = convert_input_to_numerical_coordinates(choice[0] + choice[1])
    point2 = convert_input_to_numerical_coordinates(choice[2] + choice[3])
    row_1 = point1[0]
    col_1 = point1[1]
    row_2 = point2[0]
    col_2 = point2[1]
    if points_have_distance_1_and_in_same_column(col_1, col_2, row_1, row_2) \
            or points_have_distance_1_and_in_same_diagonal_or_antidiagonal(col_1, col_2, row_1, row_2) \
            or points_have_distance_1_and_in_same_row(col_1, col_2, row_1, row_2):
        return True
    return False


def move_peg_for_player(player, choice, is_first_round):
    # Invalid move. Enter origin and destination positions in 4 characters.
    coordinates_provided_are_valid = check_data_is_four_characters_that_exist_as_coordinates(choice)
    if not coordinates_provided_are_valid:
        print('Invalid move. Enter origin and destination positions in 4 characters.')
        return False
    move_has_range_1 = check_move_has_range_1(choice)
    if not move_has_range_1:
        print('Invalid move. Destination position is not connected to origin position. Please re-enter move.\n')
        return False

    origin = choice[0] + choice[1]
    destination = choice[2] + choice[3]
    origin_is_occupied_by_players_peg = check_if_origin_position_is_occupied_by_players_peg(player, origin)
    # Invalid move. Origin is not occupied by player's _ peg
    if not origin_is_occupied_by_players_peg:
        return False

    destination_coordinates = convert_input_to_numerical_coordinates(destination)
    destination_position_is_occupied = check_if_destination_position_is_occupied(destination_coordinates[0],
                                                                                 destination_coordinates[1])
    if destination_position_is_occupied:
        print("Invalid move. Destination position is not empty. Please re-enter move.")
        return False
        # Invalid move. Destination position is not empty. Please re-enter move.

    origin_coordinates = convert_input_to_numerical_coordinates(origin)
    board[destination_coordinates[0]][destination_coordinates[1]] = board[origin_coordinates[0]][origin_coordinates[1]]
    board[origin_coordinates[0]][origin_coordinates[1]] = '-'

    is_winning_combination = check_if_three_in_any_winning_combination(destination_coordinates, player)
    if is_winning_combination:
        empty_point(choice[0] + choice[1])
        draw_board(choice[2] + choice[3], get_x_or_o(player), True)
        print("Player {} wins!\n".format(player))
        global has_won
        has_won = True
        players_wants_to_play_again = check_if_player_wants_to_play_again()
        if players_wants_to_play_again:
            return True
    return True





def play_game():
    player = choose_who_plays_first()
    print("Player " + str(player) + " plays first.")
    is_first_round = True
    for i in range(2):
        j = 0
        while j < 3:
            player_info = load_player_info(player)
            choice = input(print(
                "Player {} peg no. {}. Enter the board position to put your peg: ".format(player_info[0], j + 1)));
            allocation_was_successful = allocate_peg_for_player(player, choice, is_first_round)
            draw_board(choice, get_x_or_o(player), allocation_was_successful)
            if not allocation_was_successful:
                j -= 1
            j += 1
        player = swap_players(player)
    there_is_a_winner = False
    is_first_round = False
    while not there_is_a_winner:
        player_info = load_player_info(player)
        choice = input(print("Player {} enter your move (origin-destination): ".format(player_info[0])));
        allocation_was_successful = move_peg_for_player(player, choice, is_first_round)
        global has_won
        if has_won:
            has_won = False
            global  board
            board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
            empty_board()
            return True
        if allocation_was_successful:
            # destination_coordinates = convert_input_to_numerical_coordinates(choice[2] + choice[3])
            origin_to_be_emptied = convert_input_to_numerical_coordinates(choice[0] + choice[1])
            empty_point(choice[0] + choice[1])
            draw_board(choice[2] + choice[3], get_x_or_o(player), allocation_was_successful)
            # is_winning_combination = check_if_three_in_any_winning_combination(destination_coordinates, player)
            player = swap_players(player)
        else:
            print("\n")


def swap_players(player):
    if player == 1:
        player = 2
    else:
        player = 1
    return player


if __name__ == '__main__':
    while True:
        play_game()
