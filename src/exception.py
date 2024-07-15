import sys 
#it is a library to manipulate variables within the runtime enviroment 
import logging 

#handling errors or exceptions 
def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info() #store error's info
    file_name =exc_tb.tb_frame.f_code.co_filename
    error_msg="Error occured in python script [{0}] and line number[{1}] error message [{2}]".format(
     file_name,exc_tb.tb_lineno,str(error)
    )
    
    return error_msg

class CustomException(Exception):
    def __init__(self,error_msg,error_detail:sys):
        super().__init__(error_msg)
        self.error_msg=error_message_detail(error_msg,error_detail=error_detail)

    def __str__(self):
        return self.error_msg
