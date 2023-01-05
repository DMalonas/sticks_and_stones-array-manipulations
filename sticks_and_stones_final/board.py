# Stavroula Foteini Mytafidou 5430

initial_board = {"0": "      1   2   3 \n",
         "1": " A",
         "A1": " ",
         "2": "---",
         "A2": " ",
         "3": "---",
         "A3": " ",
         "4": "\n  ",
         "5":  "   |\  |  /| \n  "
              "    | \ | / | \n  "
              "    |  \|/  | \n"
              "  B",
         "B1": " ",
         "6": "---",
         "B2": " ",
         "7": "---",
         "B3": " ",
         "8": "\n  "
              "    |  /|\  | \n  "
              "    | / | \ | \n  "
              "    |/  |  \| \n"
              " C ",
         "C1": " ",
         "9": "---",
         "C2": " ",
         "10": "---",
         "C3": " ",
         "11": "\n"
         }

board = {"0": "      1   2   3 \n",
         "1": " A",
         "A1": " ",
         "2": "---",
         "A2": " ",
         "3": "---",
         "A3": " ",
         "4": "\n  ",
         "5":  "   |\  |  /| \n  "
              "    | \ | / | \n  "
              "    |  \|/  | \n"
              "  B",
         "B1": " ",
         "6": "---",
         "B2": " ",
         "7": "---",
         "B3": " ",
         "8": "\n  "
              "    |  /|\  | \n  "
              "    | / | \ | \n  "
              "    |/  |  \| \n"
              " C ",
         "C1": " ",
         "9": "---",
         "C2": " ",
         "10": "---",
         "C3": " ",
         "11": "\n"
         }

def empty_point(choice):
    board[choice] = ' '
def draw_board(choice, x_or_o, allocation_was_successful):
    if allocation_was_successful:
        board[choice] = x_or_o
    b = ' '.join(map(str, board.values()))
    print(b)

def empty_board():
    global board
    board = dict(initial_board)