# sys contains methods to manipulate python runtime environment
import sys
import logging

def error_message_details(error, error_detail:sys):
    # exc_tb shows the file and line number where the exception has occured
    _, _, exc_tb = error_detail.exc_info()

    file_name = exc_tb.tb_frame.f_code.co_filename
    line_no = exc_tb.tb_lineno
    error_msg = str(error)

    error_message = "Error occured in Python script, Name = [{0}], Line Number = [{1}],\
     Error Message = [{2}]".format(file_name, line_no, error_msg)
    
    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message        


if __name__=="__main__":
    try:
        a = 1/0
    except Exception as e:
        logging.info("Divide by Zero")
        raise CustomException(e, sys)
    finally:
        print("Exception handelled successfully!!!")