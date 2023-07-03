import logging


def SP_Oracle(SP_name, msg='Stored Procedure', input_val=None, cursor=None):
    """
    INPUT 
        - SP_name: name of stored procedure
        - msg: message printed to console
        - input_val: must be passed as a list
        - conn: engine.raw_connection()
    USE
        with db.engine.raw_connection().cursor() as cur:
            SP_Oracle('name of stored procedure', cursor=cur)
    """
    start_time = time.time() # start time
    out_val = cursor.var(str)
    if input_val: # if we need inputvalue !TODO: figure out how to send more than one value
        input_val.append(out_val)
        cursor.callproc(SP_name, input_val)
    else: # else, no stored procedure
        cursor.callproc(SP_name, [out_val])
    # end print time
    end_time = time.time() - start_time
    logger.info(str(out_val.getvalue())) 
    logger.info(f"{msg} COMPLETED IN {end_time/60} min(s).")


def ls2str(ls_iamids) -> str:
    """converts a python list to a SQL list as a string for query statement"""
    return ', '.join(["'"+x+"'" for x in ls_iamids])