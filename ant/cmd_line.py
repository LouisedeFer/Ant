#Standard
import argparse
import logging
import sys

#import colorlog
#Third party
import pygame

#Global constants
DEFAULT_NUMBER_STEPS=10
MIN_NUMBER_STEPS=5
MAX_NUMBER_STEPS=150

DEFAULT_TILE_SIZE=20
MIN_TILE_SIZE=10
MAX_TILE_SIZE=50

WHITE=pygame.Color("white")
BLACK=pygame.Color("black")
RED=pygame.Color("red")

DEFAULT_FPS=5




"""
#Log messsages
logger = logging.getLogger("foo")


handler = logging.StreamHandler(sys.stderr)
logger.addHandler(handler) # Registration of the new handler
logger.setLevel(logging.INFO)

color_fmt = colorlog.ColoredFormatter(
    "%(log_color)s[%(asctime)s][%(levelname)s] %(message)s",
    log_colors={
        "DEBUG": "yellow",
        "INFO": "green",
        "WARNING": "purple",
        "ERROR": "red",
        "CRITICAL": "red",
        })

color_handler = colorlog.StreamHandler()
color_handler.setFormatter(color_fmt)
logger.addHandler(color_handler)
"""
def read_args() -> argparse.Namespace:
    """Read command line arguments."""
    # Create parser & set description
    parser = argparse.ArgumentParser(
            description = "Langton's Ant.",
            formatter_class = argparse.ArgumentDefaultsHelpFormatter)

    args = parser.parse_args()
    #Movement
    parser.add_argument("--steps", "-s", type = int,
                        default = DEFAULT_NUMBER_STEPS,
                        help=f"Number of steps to run. Must be between"
                        f" {MIN_NUMBER_STEPS} and {MAX_NUMBER_STEPS}.")
    #Way of playing
    parser.add_argument("--play", "-p", action="store_true", help="Enable play mode with interface.")

    #If no GUI interface 
    parser.add_argument("--final", "-f", default="final_state.yml", help="The path where the final state of the ant is stored.")
    #If GUI interface 
    parser.add_argument("--size", "-si", type=int, 
                        default = DEFAULT_TILE_SIZE, 
                        help = f"The default size of a tile. Must be between {MIN_TILE_SIZE} and {MAX_TILE_SIZE}")

    parser.add_argument("--color-ant", "-c", default= RED, help="The color of the ant. Must be a pygame.Color. ")
    parser.add_argument("--frame-per-second", "-fps", default=DEFAULT_FPS, help = "The number of frame per second.")
    #Logging
    parser.add_argument("--verbose", "-v", dest="verbose", action="count", default=0, help="Verbose level. -v for information, -vv for debug, -vvv for trace.")

    return args

