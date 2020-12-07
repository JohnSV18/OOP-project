from car import Dog
class Owner(Dog):
    def __init__(self, name, breed, age, years_trained):
    
        Dog.__init__(self, breed, age, years_trained)
        self.name = name
      

    def warmup(self):
        self.points += 2
    
    def show(self):
        Dog.show(self)
        print(f"I have trained {self.name} for {self.years_trained} years")
    

yo = Owner('rex','pitbull', 5, 6)

print(yo.show())

    
    
    


    



    
