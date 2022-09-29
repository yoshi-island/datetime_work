import datetime
import zoneinfo

print("=====date型=====")
type_date = datetime.date(1990, 7, 2)
print(type_date)
print(type(type_date))

print("=====time型=====")
type_time = datetime.time(16, 30, 20, 79060, tzinfo=zoneinfo.ZoneInfo("Asia/Tokyo"))
print(type_time)
print(type_time.tzinfo)
print(type(type_time))

print("=====datetime型=====")
type_datetime = datetime.datetime(1990, 7, 2, 16, 30, 20, 79060)
print(type_datetime)
print(type_datetime.tzinfo)
print(type(type_datetime))

print("=====timedelta型=====")
type_timedelta = datetime.date(2022, 9, 29) - datetime.date(1990, 7, 2)
print(type_timedelta)
print(type(type_timedelta))



print("=====timedeltaを使ってtzinfoを指定する=====")
#type_time = datetime.time(16, 30, 20, 79060, tzinfo=zoneinfo.ZoneInfo("Asia/Tokyo"))
type_time = datetime.time(16, 30, 20, 79060, tzinfo=datetime.timezone(datetime.timedelta(hours=+9), "Asia/Tokyo"))
print(type_time)
print(type_time.tzinfo)
print(type(type_time))



print("=====strftimeを使ってdatetime型からstr型へ変換=====")
type_datetime = datetime.datetime(1990, 7, 2, 16, 30, 20, 79060)
print(type_datetime)
print(type(type_datetime))
type_str = type_datetime.strftime("%Y/%m/%d %H:%M:%S")
print(type_str)
print(type(type_str))

print("=====strptimeを使ってstr型からdatetime型へ変換=====")
type_datetime_2 = datetime.datetime.strptime(type_str, "%Y/%m/%d %H:%M:%S")
print(type_datetime_2)
print(type(type_datetime_2))
