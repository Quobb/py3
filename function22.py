class car:
    def __init__(self,cars,model):
        self.car = cars
        self.car = model
    def getdata(self,cars,model):
        return "my car is a {} and the model {}".format(cars,model) 



class brand(car):
    def __int__(self,cars,model,year,date,time):
        super(). __init__(cars,model)
        self.year = year
        self.date = date
        self.time = time
    def putdata(self):
        self.cars = input("enter the car : ")
        self.model = input("enter the model : ")
        self.year = input("enter the year : ")
        self.date = input("enter the date : ")
        self.time = input("entyer the time : ")
        print(self.cars,self.model,self.year,self.date,self.time)
#newcar = brand('toyata','corolla','1999','24/6/99','2.14')
print(brand.putdata('self'))