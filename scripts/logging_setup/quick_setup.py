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

logger.debug("a debug message")
logger.info("an info message")
logger.warning("a warning message")
logger.error("a error message")
logger.critical("a crit message")