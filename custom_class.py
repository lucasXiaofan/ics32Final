import urllib

class CustomError(Exception):
    pass

class Password_Short(CustomError):
    pass

class Password_Too_Long(CustomError):
    pass

class UnExpected_Error(CustomError):
    pass