# Leap Year Program
a = "--------------------------------------------------"
print(a)
print(">>>>>>>>>>>>>>> Leap Year Program <<<<<<<<<<<<<<<<")
print(a)
print()
print()
# Leap Year
year = int(input("Please Enter The Year:"))
if year % 4 == 0:
    print(f"\n{year} is leap year")
else:
    print(f"\n{year} is not leap year")
# Previous Leap Year
previous_year = year - (year % 4)
print(f"\nThe Previous Leap Year was: {previous_year}")
# Coming Leap Year
coming_year = year + (year % 4)
print(f"\nThe coming leap year is: {coming_year}")
print()
print()
# Thank You
print(a)
print(">>>>>>>>>>>>>> Thank You For Using <<<<<<<<<<<<<<<")
print(a)
print()
print()
# Press Enter
input("{Press Enter}: To Exit")
