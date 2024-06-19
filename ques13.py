from datetime import date
def func1(year):
    current_year=date.today().year
    age=current_year-year

    return age



year=int(input("Enter your birth year"))

res=func1(year)
print("the age of the person is",res)