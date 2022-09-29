import time

print("=====現在のlocal時間の取得=====")
local_time = time.localtime()
print(local_time)
print(type(local_time))

print("=====struct_time型→str型への変換=====")
type_str = time.strftime("%Y/%m/%d %H:%M:%S", local_time)
print(type_str)
print(type(type_str))

print("=====str型→struct_time型への変換=====")
type_struct_time = time.strptime(type_str, "%Y/%m/%d %H:%M:%S")
print(type_struct_time)
print(type(type_struct_time))
