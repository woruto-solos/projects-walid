class Car:  
    def __init__(self, color, brand, car_type):
        self.color = color
        self.brand = brand
        self.car_type = car_type
        self.speed= 0
        self.engine_on= False

    def describe_car(self):
        print(f"This is a {self.color} {self.brand}, which is a {self.car_type}")
    def start_engine(self):
        if self.engine_on==False:
            self.engine_on==True
            print("Engine Started!!")
        else:
            print("Engine is already on!")
    def stop_engine(self):
         if self.engine_on==True:
            self.speed=0
            self.engine_on==False
         else:
             print("your enginr already stopped")
    def accelaration(self,amount):
        if self.engine_on==True:
           self.speed=self.speed+amount
        else:
             print("your enginr stopped")
    def brake(self):
        if self.engine_on==False:
            print("you car is already stopped")
        else:
            self.speed=0
            print("car stopped")
first_car=Car("red","Tesla Model 3","electic")
second_car=Car("blue","subaru","coupe")
print(first_car.color)
print(second_car.brand)
print(first_car.car_type)
