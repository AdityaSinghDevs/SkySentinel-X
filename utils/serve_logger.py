import logging
import os 
from typing import Optional


def get_serve_logger(name:str, console:bool =True,
                     file_name = Optional[str], log_level:str = "INFO")-> logging.logger:
    
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, log_level.upper(), logging.INFO))
    logger.propagate = False

    if not logger.hasHandlers():
