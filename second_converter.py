total_second = input ("Please type the number of second: \n")
int_second = int(total_second)

hours = int_second // 3600
minutes = (int_second % 3600) // 60
second = (int_second % 60)

print("The time is: " + str(hours) + " hours and " + str(minutes) + " minutes and " + str(second) + " second.")
