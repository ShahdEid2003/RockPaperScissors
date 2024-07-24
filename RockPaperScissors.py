import random

moves = ['rock', 'paper', 'scissors']


class Player:
    def __init__(self):
        self.score = 0
        self.my_move = random.choice(moves)
        self.their_move = random.choice(moves)

    def move(self):
        pass

    def learn(self, my_move, their_move):
        pass


class RockPlayer(Player):
    def move(self):
        return 'rock'


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        move = input("Enter your move (rock, paper, scissors): ")
        while move not in moves:
            move = input(
                "Invalid move. Enter your move (rock, paper, scissors): ")
        return move


class ReflectPlayer(Player):
    def __init__(self):
        super().__init__()
        self.their_move = random.choice(moves)

    def move(self):
        return self.their_move

    def learn(self, my_move, their_move):
        self.their_move = their_move


class CyclePlayer(Player):
    def __init__(self):
        super().__init__()
        self.my_move = None

    def move(self):
        if self.my_move is None:
            self.my_move = random.choice(moves)
        else:
            self.my_move = moves[(moves.index(self.my_move) + 1) % 3]
        return self.my_move

    def learn(self, my_move, their_move):
        pass


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    def beats(self, one, two):
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if self.beats(move1, move2):
            self.p1_score += 1
            print("Player 1 wins the round!")
        elif self.beats(move2, move1):
            self.p2_score += 1
            print("Player 2 wins the round!")
        else:
            print("It's a tie!")
        print(f"Score: Player 1 - {self.p1_score}, "
              f"Player 2 - {self.p2_score}")
        self.p1.learn(move1, move2)
        self.p2.learn(move1, move2)

    def play_game(self):
        print("Game start!")
        for round_number in range(3):
            print(f"Round {round_number + 1}:")
            self.play_round()
        print("Game over!")
        print(f"Final score: Player 1 - {self.p1_score}, "
              f"Player 2 - {self.p2_score}")
        if self.p1_score > self.p2_score:
            print("Player 1 wins the game!")
        elif self.p2_score > self.p1_score:
            print("Player 2 wins the game!")
        else:
            print("The game is a tie!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), CyclePlayer())
    game.play_game()
