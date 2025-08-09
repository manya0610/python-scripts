import os
import socket
from pythonjsonlogger import jsonlogger

import logging
import sys

# always create one
logger = logging.getLogger(__name__)


logger.setLevel(logging.DEBUG)

# creating handler
"""if you don't create any handler, python fallbacks to sys.stderr, which logs at WARNING level"""

"""creating stream handler, which writes to stdout"""
stream_handler = logging.StreamHandler(stream=sys.stdout)
logger.addHandler(stream_handler)
"""If you don't set level to handler, it fallbacks to loggers default level"""
# stream_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler("errors.log")
"""file_handler will only log ERROR and above"""
file_handler.setLevel(logging.ERROR)
logger.addHandler(file_handler)

""" in this setup  
All records  DEBUG and above are created.
stream_handler processes all events
file_handler processes ERROR and above
"""


formatter = jsonlogger.JsonFormatter("%(asctime)s %(name)s %(levelname)s %(message)s %(funcName)")
""" possible keys are 
{"message": "an info message", "name": "__main__", "msg": "an info message", "args": [], "levelname": "INFO", "levelno": 20, "pathname": "/Users/manishraut/Documents/python-scripts/scripts/logging_setup/json_logging.py", "filename": "json_logging.py", "module": "json_logging", "exc_info": null, "exc_text": null, "stack_info": null, "lineno": 38, "funcName": "<module>", "created": 1754635702.138525, "msecs": 138.0, "relativeCreated": 58.484, "thread": 8218507328, "threadName": "MainThread", "processName": "MainProcess", "process": 79788, "taskName": null}
"""
stream_handler.setFormatter(formatter)

class ContextFilter(logging.Filter):
    def __init__(self, name=''):
        super().__init__(name)
        self.hostname = socket.gethostname()
        self.process_id = os.getpid()

    def filter(self, record):
        record.hostname = self.hostname
        record.process_id = self.process_id
        return True

stream_handler.addFilter(ContextFilter())
logger.debug("a debug message", extra={"ouid": 1234, "details": {"qwe": "Qweqweqw"}})
logger.info("an info message")
logger.warning("a warning message")
logger.error("a error message")
logger.critical("a crit message")
print(0)