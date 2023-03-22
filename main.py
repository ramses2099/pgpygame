from game import Game

g = Game()


def main():
    while g.running:
        g.playing = True
        g.game_loop()


if __name__ == "__main__":
    main()
