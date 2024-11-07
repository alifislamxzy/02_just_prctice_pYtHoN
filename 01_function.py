# Function Definition
def GoodDay():
    name = input("What's your name? ")
    print(f"Good Morning, {name}")

GoodDay() # This is Function Call

# Function Aurgument

def Day(name, ending= "Thank you"):
    print(f"Good Day, {name}")
    print(ending)

Day("Apon")
Day("Sakib", "Thanks")