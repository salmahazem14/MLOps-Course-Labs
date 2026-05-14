"""
Logging configuration.
"""

import logging

def setup_logging():
    # TODO 1: Set up basic logging with level INFO using logging.basicConfig()
    logging.basicConfig(
        level = logging.INFO , 
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s")
        #time of the log , level of the log , logger name , log message 
            
    # TODO 2: Create a named logger using logging.getLogger() and return it
    logger = logging.getLogger("ChurnModelLogger")

    return logger
