import sys
import logging
import os
from datetime import datetime
from src.logger import logging


# Configure logging to write to a file
LOG_FILE = f"log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)


def error_message_detail(error, error_detail:sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message = f"Error occurred in script name [{file_name}] line number [{exc_tb.tb_lineno}] error message [{str(error)}]"

    return error_message
    

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message



if __name__ == "__main__":

    try:
        a = 1/0
    except Exception as e:
        logging.info("Divide by zero error occurred")
        raise CustomException(e, sys)
    



