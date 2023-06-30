import sys
import logging
import traceback

log = logging.getLogger(__name__)

def logging_traceback():
    try:
        'a' + 1
    except TypeError as e:
        log.error(e,  exc_info=True) # exec_info=True will include traceback in logging
        exc_type, exc_value, exc_traceback = sys.exc_info() # if you
        print(exc_type, exc_value, exc_traceback)
        log.info(exc_type, exc_value, exc_traceback)
        traceback_in_var = traceback.format_tb(exc_traceback)
        log.info(' traceback_in_var '.center(80, '-'))
        log.info(traceback_in_var)
        log.info(' << Custom Warning Message Here >> '.center(80, '='))