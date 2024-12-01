# Define the BMW class
class BMW:
    def start(self):
        return "BMW is starting with a roar!"
    
    def drive(self):
        return "BMW is driving smoothly."
    
    def stop(self):
        return "BMW has stopped."

# Define the Ferrari class
class Ferrari:
    def start(self):
        return "Ferrari is starting with a powerful engine!"
    
    def drive(self):
        return "Ferrari is zooming past with high speed."
    
    def stop(self):
        return "Ferrari has stopped gracefully."

# Function to demonstrate polymorphism
def test_car(car):
    print(car.start())
    print(car.drive())
    print(car.stop())

# Create objects of BMW and Ferrari
bmw_car = BMW()
ferrari_car = Ferrari()

# Test the cars using the polymorphic function
print("Testing BMW:")
test_car(bmw_car)
print("\nTesting Ferrari:")
test_car(ferrari_car)
