import logging
import sys

from pythonjsonlogger import jsonlogger

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

file_handler = logging.FileHandler("logs.json")
"""file_handler will only log ERROR and above"""
file_handler.setLevel(logging.INFO)
logger.addHandler(file_handler)

normal_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s %(threadName)s %(filename)s:%(lineno)s - %(funcName)s() - %(message)s"
)
json_formatter = jsonlogger.JsonFormatter(
    "%(asctime)s - %(name)s - %(levelname)s %(threadName)s %(filename)s:%(lineno)s - %(funcName)s() - %(message)s"
)

stream_handler.setFormatter(normal_formatter)

file_handler.setFormatter(json_formatter)
