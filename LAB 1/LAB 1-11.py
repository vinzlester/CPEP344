hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.

total_minutes = hour * 60 + mins
total_minutes = total_minutes + dura

end_hour = (total_minutes // 60) % 24
end_mins = total_minutes % 60

print(end_hour, ":", end_mins, sep="")
