def fah_to_cel(fah):
       celsius = (fah- 32) * 5/9
       return celsius
def cel_to_fah(cel):
      fahrenheit = (cel * 9/5) + 32
      return fahrenheit

num=int(input("Enter 1 to convert F to C, 2 to convert C to F "))
if num==1:
    fah=float(input("Enter fahrenheit value"))
    res=fah_to_cel(fah)
    print("The conversion from f to c is",res)

elif num==2:
        cel=float(input("Enter celsius value"))
        res=cel_to_fah(cel)
        print("The conversion from f to c is",res)
else:
      print("invalid input")        