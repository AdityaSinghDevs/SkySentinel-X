import logging
import os
from typing import Optional

def train_logger(name:str, log_level: str = 'INFO',
                 )->logging.Logger:

    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, log_level.upper(), logging.INFO))
    logger.propagate = False

    if not logger.hasHandlers():

        if console:
            console_handler = logging.StreamHandler()
