import logging
import os
from typing import Optional

def get_train_logger(name:str, log_level: str = 'INFO',
                 console : bool = True,
                 )->logging.Logger:

    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, log_level.upper(), logging.INFO))
    logger.propagate = False

    if not logger.hasHandlers():

        if console:
            console_handler = logging.StreamHandler()
        console_format = logging.Formatter("{name}- {levelname} - {message}" , style='{')

        console_handler.setFormatter(console_format)
        logger.addHandler(console_handler)

        base_log_dir = "../logs"

        log_file = os.path.join(base_log_dir, "train.log")
        os.makedirs(os.path.dirname(log_file), exist_ok=True)

        file_handler = logging.FileHandler(log_file, mode="a" , encoding= 'utf-8')

        file_format = logging.Formatter("{asctime}-{levelname}-{name}:{funcName}:L{lineno}:{message}" , style="{")

        file_handler.setFormatter(file_format)
        logger.addHandler(file_handler)
        
    return logger
            
