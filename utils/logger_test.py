from train_logger import get_train_logger

logger = get_train_logger(__name__)

logger.info("hello")

# test_file.py
import time
from serve_logger import get_serve_logger, log_request, log_response  # Assuming you saved it as serve_logger.py

# Initialize logger
serve_logger = get_serve_logger(log_level="INFO", log_file="serve.log")

# Simulate a fake request
if __name__ == "__main__":
    req_id, start_time = log_request("/classify")
    
    # Simulate some processing time
    time.sleep(0.15)  # 150 ms inference time
    
    # Simulate response
    log_response(req_id, "/classify", status_code=200, start_time=start_time)

    # Simulate another request that fails
    req_id, start_time = log_request("/classify")
    time.sleep(0.05)
    serve_logger.error("Inference failed", extra={"request_id": req_id, "path": "/classify"})
    log_response(req_id, "/classify", status_code=500, start_time=start_time)
