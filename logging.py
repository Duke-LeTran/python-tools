import logging
import pandas as pd
from io import StringIO

log = logging.getLogger(__name__)

def logger_df_info(df_input:pd.DataFrame, msg:str=None):
    """ logs df.info() """
    name_df = [ k for k,v in locals().items() if v is df_input][0] # gets var name
    log.info(f"{name_df}.info() " +  msg) # prints message df.info() + msg
    buffer = StringIO() # creates stringIO buffer
    df_input.info(buf=buffer) # writes to buffer (rather than console)
    log.info(buffer.getvalue()) # send buffer to logger

def log_df_itself(df_input):
    """ converts dataframe to text, makes it logable as string"""
    df_result = df_input.copy()
    log.info(' name of df '.center(80,'-'))
    text_df = '\n\t'+ df_result.to_string().replace('\n', '\n\t')
    log.info(' end '.center(80,'-'))


import sys
import logging
import traceback

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