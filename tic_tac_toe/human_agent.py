import random


class RandomAgent(object):
    def select_board(self, boards, turn):
        print('enter move')
        selected_board = random.choice(boards)
        return selected_board