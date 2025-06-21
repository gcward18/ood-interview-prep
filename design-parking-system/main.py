from parking import ParkingFloor,ParkingGarage,Car,Limo,Semi,Driver, ParkingSystem
parkingGarage = ParkingGarage(3, 2)
parkingSystem = ParkingSystem(parkingGarage, 5)

driver1 = Driver(Car())
driver2 = Driver(Limo())
driver3 = Driver(Semi())

print(parkingSystem.parkDriver(driver1))      # true
print(parkingSystem.parkDriver(driver2))      # true
print(parkingSystem.parkDriver(driver3))      # false

print(parkingSystem.removeDriver(driver1))    # true
print(parkingSystem.removeDriver(driver2))    # true
print(parkingSystem.removeDriver(driver3))    # false