import logging
import json
import sys
import time
import uuid
from typing import Optional

class JSONFormatter(logging.Formatter):

    def format(self, record):

        log_record = {
            "timestamp" : self.formatTime(record, "%Y-%m-%dT%H:%M:%S"),
            "level" : record.levelname,
            "logger" : record.name,
            "message" : record.getMessage(),
        }

        if hasattr(record, "request_id"):
            log_record["request_id"] = record.request_id
        if hasattr(record, "path"):
            log_record["path"] = record.path
        if hasattr(record, "status_code"):
            log_record["status_code"] = record.status_code
        if hasattr(record, "latency_ms"):
            log_record["latency_ms"] = record.latency_ms
        
        return json.dump(log_record)
    
def get_serve_logger(log_level : str = "INFO", log_file : Optional[str] = None)-> logging.Logger: 
        
        logger = logging.getLogger("serving")
        logger.setLevel(getattr(logging, log_level.upper(), logging.INFO))
        logger.propagate = False 

        if not logger.hasHandlers(): 

            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.setFormatter(JSONFormatter())
            logger.addHandler(console_handler) 

            if log_file:
                file_handler = logging.FileHandler(log_file, mode='a', encoding="utf-8")
                file_handler.setFormatter(JSONFormatter())
                logger.addHandler(file_handler) 

        return logger

serve_logger = get_serve_logger()

def log_request(path:str):
    req_id = str(uuid.uuid4())
    start_time = time.time()
    serve_logger.info("Incoming Request", extra = {"request_id":req_id, "path":path})
    return req_id, start_time

def log_response(req_id:str, path: str, status_code:int, start_time : float):
    latency = round((time.time() - start_time) * 1000, 2)
    serve_logger.info(
        "Response sent", 
        extra={"requwst_id":req_id, "path" : path, "status_code":status_code, "latency_ms": latency},
    )
        
        