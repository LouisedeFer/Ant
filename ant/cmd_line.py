#Standard  # noqa: D100, ERA001
import argparse
import logging
import sys

import colorlog
import pygame

from .exceptions import IntRangeError  # type: ignore

#Global constants
DEFAULT_NUMBER_STEPS=10
MIN_NUMBER_STEPS=0
MAX_NUMBER_STEPS=10000

DEFAULT_TILE_SIZE=50
MIN_TILE_SIZE=30
MAX_TILE_SIZE=70

WHITE=pygame.Color("white")
BLACK=pygame.Color("black")
RED=pygame.Color("red")

DEFAULT_FPS=10
MIN_FPS=5
MAX_FPS=300



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


def read_args() -> argparse.Namespace:
    """Read command line arguments."""
    # Create parser & set description
    parser = argparse.ArgumentParser(
            description = "Langton's Ant.",
            formatter_class = argparse.ArgumentDefaultsHelpFormatter)


    #Movement
    parser.add_argument("--steps", "-s", type = int,
                        default = DEFAULT_NUMBER_STEPS,
                        help=f"Number of steps to run. Must be between"
                        f" {MIN_NUMBER_STEPS} and {MAX_NUMBER_STEPS}.")
    #Way of playing
    parser.add_argument("--play", "-p", action="store_true", default =False, help="Enable play mode with interface.")

    #If no GUI interface
    parser.add_argument("--final", "-f", default="final_state.yml", help="The path where the final state of the ant is stored.")
    #If GUI interface
    parser.add_argument("--size", "-si", type=int,
                        default = DEFAULT_TILE_SIZE,
                        help = f"The default size of a tile. Must be between {MIN_TILE_SIZE} and {MAX_TILE_SIZE}")

    parser.add_argument("--frame-per-second", "-fps", default=DEFAULT_FPS, help = "The number of frame per second.")
    #Logging
    parser.add_argument("--verbose", "-v", dest="verbose", action="count", default=0, help="Verbose level. -v for information, -vv for debug, -vvv for trace.")

    # Parse
    args = parser.parse_args()


    # Check integer range
    for chk in [{"lbl": "Tile size", "val": args.size,
                 "min": MIN_TILE_SIZE, "max": MAX_TILE_SIZE},
                {"lbl": "Frame per second", "val": int(args.frame_per_second),
                 "min": MIN_FPS, "max": MAX_FPS},
                {"lbl": "Number of steps", "val": args.steps,
                 "min": MIN_NUMBER_STEPS, "max": MAX_NUMBER_STEPS},
                ]:
        if not (chk["min"] <= chk["val"] <= chk["max"]):
            logger.debug("Unproper values")
            raise IntRangeError(chk["lbl"], chk["val"], chk["min"], chk["max"])

    if args.verbose == 1:
        logger.setLevel(logging.INFO)
    elif args.verbose == 2:
        logger.setLevel(logging.DEBUG)

    return args



