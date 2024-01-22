import csv
from datetime import datetime, timedelta

def generate_schedule(year,Shift):
    schedule = []

    # 讓使用者輸入一月一號至三號的工作情況
    work_days_input = input("請輸入一月一號至四號的工作情況（例如：1001 表示一號上班，二號休息，三號休息...）: ")

    # 一月一號至三號的工作情況
    work_days = [int(day) for day in work_days_input]

    current_date = datetime(year, 1, 1)

    for work_day in work_days:
        # 根據使用者輸入的情況，設定一月一號至三號的行程
        if work_day == 1:
            schedule.append({
                'Subject': f"{Shift}",
                'Start Date': current_date.strftime('%Y/%m/%d'),
                'Start Time': '07:20 AM',
                'End Date': current_date.strftime('%Y/%m/%d'),
                'End Time': '19:20 PM',
                'All Day Event': 'True',
                'Description': 'Work',
                'Location': 'TSMC TW',
            })

        current_date += timedelta(days=1)

    flag = 0
    while current_date.year == year:
        if flag == 4:
                flag =0
        if work_days[flag] == 1:
            schedule.append({
                'Subject': f"{Shift}",
                'Start Date': current_date.strftime('%Y/%m/%d'),
                'Start Time': '07:20 AM',
                'End Date': current_date.strftime('%Y/%m/%d'),
                'End Time': '19:20 PM',
                'All Day Event': 'True',
                'Description': 'Work',
                'Location': 'TSMC TW',
            })
        flag += 1
        current_date += timedelta(days=1)
    
    return schedule

def write_to_csv(schedule, filename):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['Subject', 'Start Date', 'Start Time', 'End Date', 'End Time', 'All Day Event', 'Description', 'Location']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for entry in schedule:
            writer.writerow(entry)

if __name__ == "__main__":
    year = int(input("work's year: "))
    shift_type = input("your shift (A or B): ")

    schedule = generate_schedule(year,shift_type)
    write_to_csv(schedule, f'{shift_type}_schedule_{year}.csv')
