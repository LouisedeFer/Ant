from ant.tile import Tile
import pygame
from .ant import Ant
from .board import Board

#GLOBAL CONSTANTS
MIN_COL=3
MIN_ROW=3

TILE_SIZE=20

WHITE=pygame.Color("white")
BLACK = pygame.Color("black")

class LangtonAnt :
    """The class in which you decide wether you play with an interface or not."""

    def ant_auto(self, ant : Ant, board : Board,  step : int) -> None :
        """The movement of the ant."""  # noqa: D401
        for _loop in range(step) :
            ant.move_and_change_color(board)

        min_c, min_r, max_c, max_r = 0,0,0,0
        for key in board.dictionary :
            max_r = max(key[0], max_r)
            min_r = min(key[0], min_r)
            max_c = max(key[1], max_c)
            min_c = min(key[1], min_c)

        print(f"STEP {step}")
        print(f"{ant.row-min_r}, {ant.column-min_c}, {ant.dir.texte()}")
        max_r = max(MIN_ROW//2, max_r)
        min_r = min(-(MIN_ROW//2), min_r)
        max_c = max(MIN_COL//2, max_c)
        min_c = min(-(MIN_COL//2), min_c)

        for row in range(min_r, max_r + 1) :
            for col in range(min_c, max_c+1) :
                if (row,col) in board.dictionary :
                    print(board.dictionary[(row,col)].text, end = "")
                else :
                    print (" ", end="")
            print()


    def dict_pygame(self, ant : Ant, board : Board, step : int) -> tuple[tuple[int,int], dict[(tuple[int,int], Tile)]] :
        """The movement of the ant with an interface."""

        for _loop in range(step) :
            ant.move_and_change_color(board)

        min_c, min_r, max_c, max_r = 0,0,0,0
        for key in board.dictionary :
            max_r = max(key[0], max_r)
            min_r = min(key[0], min_r)
            max_c = max(key[1], max_c)
            min_c = min(key[1], min_c)

        max_r = max(MIN_ROW//2, max_r)
        min_r = min(-(MIN_ROW//2), min_r)
        max_c = max(MIN_COL//2, max_c)
        min_c = min(-(MIN_COL//2), min_c)

        screen_size = (TILE_SIZE*max_c, TILE_SIZE*max_r)

        for row in range(min_r, max_r + 1) :
            for col in range(min_c, max_c+1) :
                if (row,col) not in board.dictionary :
                    board.dictionary[(row,col)]=Tile(" ", WHITE)

        return (screen_size, board.dictionary)
    
    def ant_play(self, ant : Ant, board : Board, step : int) -> None :
        """The ant with the pygame interface."""
        screen_size, dict_0=self.dict_pygame(ant, board, step)
        board=Board(dict_0)

        pygame.init()
        screen=pygame.display.set_mode(screen_size)
        clock = pygame.time.Clock()
        while True : 

            clock.tick(1)
            for event in pygame.event.get() :
                # Closing window (Mouse click on cross icon or OS keyboard shortcut)
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    pygame.quit()


            board=Board(dict_0).draw(screen, TILE_SIZE)

            

        # Display
        pygame.display.update()
    #pygame.quit



    







