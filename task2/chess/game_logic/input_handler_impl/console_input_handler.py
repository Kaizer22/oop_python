from task2.chess.game_logic.base_elements.base_input_handler import InputHandler

'''Реализация класса InputHandler для обработки консольного ввода'''


class ConsoleInputHandler(InputHandler):
    def get_game_attributes(self):
        is_correct = False
        while not is_correct:
            args = str(input())
            if args == "":
                return None
            else:
                args = args.split(" ")
                try:
                    if len(args) == 3:
                        field_height = int(args[0])
                        field_width = int(args[1])
                        positioning = {'standard': 'standard',
                                       'reverse': 'reverse'}.get(args[2], 'standard')
                        return field_height, field_width, positioning
                    else:
                        raise ValueError("Incorrect input format")
                except ValueError:
                    print("Log : Error incorrect input format")

    def get_next_turn(self):
        is_correct = False
        fig_x = 0
        fig_y = 0
        new_x = 0
        new_y = 0
        while not is_correct:
            try:
                user_input = input()
                if user_input == "q":
                    return fig_x, fig_y, new_x, new_y, False
                else:
                    args = user_input.split(" ")
                    if len(args) == 4:
                        fig_x = int(args[0]) - 1
                        fig_y = int(args[1]) - 1
                        new_x = int(args[2]) - 1
                        new_y = int(args[3]) - 1
                    else:
                        raise ValueError("Incorrect input format")
                    return fig_x, fig_y, new_x, new_y, True

            except ValueError:
                print("Log : Error - incorrect input format")
