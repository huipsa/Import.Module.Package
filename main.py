import datetime as dt
from application.salary import calculate_salary
from application.db.people import get_employees


if __name__ == "__main__":
    calculate_salary()
    get_employees()
    print(f"Текущее время - {dt.datetime.now()}")