# A company decided to give bonus of 1000 Rs to 
# employee if his/her service is more than 5 years
# ask user their salary and year of service and print
# the net bonus amount
sal = int(input("Enter the salary"))
year = int(input("Enter the year of service:"))
if year > 5 :
    print("He/She is eligible for the bonus of Rs 1000")
    print("Salary after the bonus is Rs", sal + 1000)
else :
    print("He/She is not eligible for bonus")