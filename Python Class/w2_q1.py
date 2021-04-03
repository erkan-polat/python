currrent_time_str=input("Whatt is the current time (in hours)? =")
waiting_time_str=input("How many hours do you have to wait ? =")
current_time_int=int(currrent_time_str)
waiting_time_int=int(waiting_time_str)
hours=current_time_int + waiting_time_int
timeofday=hours % 24
print(timeofday)
