from ant.tile import Tile
import pygame
from .ant import Ant
from .board import Board

import yaml
from pathlib import Path


#GLOBAL CONSTANTS
MIN_COL_PLAY=11
MIN_ROW_PLAY=11

MIN_COL=3
MIN_ROW=3

TILE_SIZE=50
SCREEN_SIZE_INIT=(MIN_ROW_PLAY*TILE_SIZE, MIN_COL_PLAY*TILE_SIZE)

WHITE=pygame.Color("white")
RED= pygame.Color("red")

class LangtonAnt :
    """The class in which you decide wether you play with an interface or not."""

    def __init__(self, size : int) -> None :
        """Initialize the Langton's ant."""
        self._tile_size=size
        self._screen_size=(MIN_ROW_PLAY*size, MIN_COL_PLAY*size)

    def dic_ant_auto(self, ant : Ant, board : Board,  step : int) -> tuple[int, int, str, dict[tuple[int, int], Tile]] :
        """The movement of the ant."""
        for _loop in range(step) :
            ant.move_and_change_color(board)

        min_c, min_r, max_c, max_r = 0,0,0,0
        for key in board.dictionary :
            max_r = max(key[0], max_r)
            min_r = min(key[0], min_r)
            max_c = max(key[1], max_c)
            min_c = min(key[1], min_c)
        #MinimumSize for the board

        ant.row-=min_r
        ant.column-=min_c

        max_r = max(MIN_ROW//2, max_r)
        min_r = min(-(MIN_ROW//2), min_r)
        max_c = max(MIN_COL//2, max_c)
        min_c = min(-(MIN_COL//2), min_c)

        for row in range(min_r, max_r + 1) :
            for col in range(min_c, max_c+1) :
                if (row,col) not in board.dictionary :
                    board.dictionary[(row,col)]=Tile(" ", WHITE)

        return (ant.row, ant.column, ant.dir.texte(), board.dictionary)

    def save_final(self, step : int, coord : tuple[int, int], 
                   dir : str, dict :dict[tuple[int, int], Tile], final_state : Path ) -> list[str] :
        """Save the file with final state."""
        file=[]

        file.append(f"Step {step}")
        file.append(f"{coord[0]} {coord[1]} {dir}")

        min_row, min_col = min(coord[0] for coord in dict), min(coord[1] for coord in dict)

        nb_row=max(coord[0] for coord in dict)-min_row+1
        nb_col=max(coord[1] for coord in dict)-min_col+1

        #store the datas
        temp=[[" " for _loop in range(nb_col)] for _loop in range(nb_row)]

        for (row, col), tile in dict.items() :
            temp[row-min_row][col-min_col]=tile.text #sort the items

        for i in range (len(temp)):
            file.append("".join(temp[i])) #add every row as a neaw row in the YAML file 


        with final_state.open("w+") as fd : #(file descriptor), create a file if it doesn't exist
            yaml.safe_dump(file,fd)

        return file


    def ant_auto(self, ant: Ant, board : Board, step : int, final_state : Path) -> None :
        """When it is authomatic."""
        res=self.dic_ant_auto(ant, board, step)
        file=self.save_final(step, (res[0], res[1]), res[2], res[3], final_state)
        for row in range(len(file)) :
            for col in range(len(file[row])) :
                print(file[row][col], end = "")
            print()



    def coord_pygame(self, board : Board) -> tuple[tuple[int, int],tuple[int, int]] :
        """Coordonates of the board."""
        return (board.top_corner, board.bottom_corner)

    def ant_play(self, ant : Ant, board : Board, step : int) -> None :
        """The ant with the pygame interface."""
        #ScrollBar=pygame_menu.widgets.ScrollBar
        pygame.init()
        screen=pygame.display.set_mode(self._screen_size)
        pygame.display.set_caption(f"Langton's ant with {step} steps.")

        clock = pygame.time.Clock()
        for _loop in range(step):

            clock.tick(10)
            for event in pygame.event.get() :
                # Closing window (Mouse click on cross icon or OS keyboard shortcut)
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    pygame.quit()

            ant.move_and_change_color(board)
            (min_r, min_c), (max_r, max_c)=self.coord_pygame(board)
            board.draw(screen, self._tile_size, min_r, max_r, min_c, max_c)
            ant.draw_ant(screen, self._tile_size, min_r, min_c)



        # Display
            pygame.display.update()

        #Print the board when ended
        while True :
            clock.tick(10)
            for event in pygame.event.get() :
                # Closing window (Mouse click on cross icon or OS keyboard shortcut)
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    pygame.quit()

            (min_r, min_c), (max_r, max_c)=self.coord_pygame(board)
            board.draw(screen, self._tile_size, min_r, max_r, min_c, max_c)
            ant.draw_ant(screen, self._tile_size, min_r, min_c)

            pygame.display.update()










