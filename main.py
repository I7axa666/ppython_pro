from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime as dt


def start_program():
    print(f'\n{dt.now().strftime("%d-%m-%Y")}')
    time = dt.time(dt.now()).replace(microsecond=0)
    print(f'\nThe program the program is launched at {time}')


print('для dirty_main')

if __name__ == '__main__':
    start_program()
    calculate_salary()
    get_employees()
