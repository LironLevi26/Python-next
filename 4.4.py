# Generator functions for seconds, minutes, and hours
def gen_secs():
    for sec in range(60):
        yield sec

def gen_minutes():
    for minute in range(60):
        yield minute

def gen_hours():
    for hour in range(24):
        yield hour

# Generator for the time
def gen_time():
    for hour in gen_hours():
        for minute in gen_minutes():
            for second in gen_secs():
                yield f"{hour:02}:{minute:02}:{second:02}"

# Generator for years starting from a given year
def gen_years(start=2019):
    year = start
    while True:
        yield year
        year += 1

# Generator for months
def gen_months():
    for month in range(1, 13):
        yield month

# Function to check if a year is a leap year
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Generator for days in a month
def gen_days(month, leap_year=True):
    days_in_month = {
        1: 31, 2: 29 if leap_year else 28, 3: 31, 4: 30, 5: 31,
        6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    for day in range(1, days_in_month[month] + 1):
        yield day

# Generator for full date and time
def gen_date(start_year=2019):
    for year in gen_years(start_year):
        leap_year = is_leap_year(year)
        for month in gen_months():
            for day in gen_days(month, leap_year):
                for time in gen_time():
                    yield f"{day:02}/{month:02}/{year} {time}"

# Main function to test the generator
def main():
    date_gen = gen_date()
    count = 0
    while True:
        date = next(date_gen)
        if count % 1000000 == 0:
            print(date)
        count += 1

if __name__ == '__main__':
    main()
