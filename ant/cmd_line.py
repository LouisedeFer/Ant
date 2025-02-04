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
    parser.add_argument("--steps", "-N", type = int,
                        default = DEFAULT_NUMBER_STEPS,
                        help=f"Number of steps to run. Must be between"
                        f" {MIN_NUMBER_STEPS} and {MAX_NUMBER_STEPS}.")
    #Way of playing
    parser.add_argument("--play", "-p", action="store_true", help="Enable play mode with interface.")

    #Logging
    parser.add_argument("--verbose", "-v", dest="verbose", action="count", default=0, help="Verbose level. -v for information, -vv for debug, -vvv for trace.")

    return args

