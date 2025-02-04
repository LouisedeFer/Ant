from ant.tile import Tile
import pygame
from .ant import Ant
from .board import Board

import yaml
from pathlib import Path


#GLOBAL CONSTANTS
MIN_COL=3
MIN_ROW=3

TILE_SIZE=20

WHITE=pygame.Color("white")
BLACK = pygame.Color("black")

class LangtonAnt :
    """The class in which you decide wether you play with an interface or not."""

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

        return (ant.row, ant.column, ant.dir.texte, board.dictionary)

    def save_final(self, step : int, coord : tuple[int, int], 
                   dir : str, dict :dict[tuple[int, int], Tile], final_state : Path ) -> list[list[str]] :
        """Save the file with final state."""
        file=[]

        file.append(f"Step {step}")
        file.append(f"{coord[0]} {coord[1]} {dir}")

        max_row=max(coord[0] for coord in dict)
        max_col=max(coord[1] for coord in dict)

        #store the datas
        temp=[[" " for _loop in range(max_col)] for _loop in range(max_row)]

        for (row, col), tile in dict.items() :
            temp[row][col]=tile.text #sort the items

        for row in temp :
            file.append(" ".join(row)) #add every row as a neaw row in the YAML file


        with final_state.open("w+") as fd : #(file descriptor), create a file if it doesn't exist
            yaml.safe_dump(file,fd)

        return file


    def ant_auto(self, ant: Ant, board : Board, step : int, final_state : Path) -> None :
        """When it is authomatic."""
        res=self.dic_ant_auto(ant, board, step)
        file=self.save_final(step, (res[0], res[1]), res[2], res[3], final_state)
        for row in range(len(file)) :
            for col in range(len[file[row]]) :
                print(file[row][col])



    def dict_pygame(self, ant : Ant, board : Board, 
                    step : int) -> tuple[tuple[int,int],
                                         dict[int, tuple[dict[tuple[int,int], Ant]]]] :
        """Dictionary of the movement."""
        dic_sol={0 : (board.dictionary, ant)}
        for step in range(step) :
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


            for row in range(min_r, max_r + 1) :
                for col in range(min_c, max_c+1) :
                    if (row,col) not in board.dictionary :
                        board.dictionary[(row,col)]=Tile(" ", WHITE)

            dic_sol{step+1}=(board.dictionary, ant)


        screen_size = (TILE_SIZE*max_c, TILE_SIZE*max_r)
        return (screen_size, dic_sol)

    def ant_play(self, ant : Ant, board : Board, step : int) -> None :
        """The ant with the pygame interface."""
        (screen_size, dict)= self.dict_pygame(ant, board, step)

        pygame.init()
        screen=pygame.display.set_mode(screen_size)
        clock = pygame.time.Clock()
        count=0
        while True : 

            clock.tick(1)
            for event in pygame.event.get() :
                # Closing window (Mouse click on cross icon or OS keyboard shortcut)
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    pygame.quit()

            dict[count][0].draw() #draw the board
            dict[count][1].draw_ant() #draw the ant






        # Display
            pygame.display.update()
    #pygame.quit



    







