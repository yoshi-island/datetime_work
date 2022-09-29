import calendar

print("=====calendar出力=====")
print(calendar.month(2022, 9))

print("=====datetime.date型で週リスト出力=====")
C = calendar.Calendar(firstweekday=0)
print(C.monthdatescalendar(2022, 9))
