days, hours, min, sec, = 0, 0, 0, 0,
input = int(input("Enter the seconds: "))
if input >= 86400:
   days = input/86400
   input %= 86400
print("1", input)
if input >= 3600:
   hours = input/3600
   input %= 3600
print("2", input)
if input >= 60:
   min = input/60
   input %= 60
print("3", input)
sec = input
print(f"{int(days)}d, {int(hours)}h, {int(min)}m, {int(sec)}s")