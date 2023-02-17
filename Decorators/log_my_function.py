from main import start_program
from decorator_with_logger import logger

@logger('log.log')
def new_start_program():
    return

if __name__ == '__main__':
    new_start_program()