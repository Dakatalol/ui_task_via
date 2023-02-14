import logging

# create logger
logger = logging.getLogger('app')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('recorder.log')
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)
