# Months={
#     "January":1,
#
# }
# January=February=March=1
# April=May=June=2
# July=August=September=3
# October=November=December=4

Month=input("Enter the Month: ")

date=int(input("Enter the date: "))

if Month=="January" or Month=="Febraury" or Month=="March":
    print("The season is currently summer")
if Month == "April" or Month == "May" or Month == "June":
    print("The season is currently Spring")
if Month == "July" or Month == "August" or Month == "September":
    print("The season is currently Fall")
if Month == "October" or Month == "November" or Month == "December":
    print("The season is currently Winter")
