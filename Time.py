#get the inputs
current_time = int(input("Enter the current time (in hours): "))
hours_to_wait = int(input("Enter the number of hours to wait for the alarm: "))
#calculate time
alarm_time = (current_time + hours_to_wait) % 24
#print output
print(f"The alarm will go off at {alarm_time:02}:00")
