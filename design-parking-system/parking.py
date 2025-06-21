import datetime
import math


class Vehicle:
    def __init__(self, size):
        self.size = size
    
    def getSpotSize(self):
        return self.size

class Limo(Vehicle):
    def __init__(self):
        super().__init__(2)

class Car(Vehicle):
    def __init__(self):
        super().__init__(1)

class Semi(Vehicle):
    def __init__(self):
        super().__init__(3)

class Driver:
    id_count = 0
        
    @classmethod
    def updateId(cls) -> int:
        Driver.id_count += 1
        return Driver.id_count
    
    def __init__(self, vehicle):
        self.payment_due = 0
        self.vehicle = vehicle
        self.id = self.updateId()
    
    def getId(self) -> int:
        return self.id

    def getVehicle(self):
        return self.vehicle

    def charge(self, amount):
        self.payment_due += amount
        
class ParkingFloor:
    def __init__(self, spots):
        self.available = spots
        self.spots = [0] * self.available
        self.vehicles = {}
    
    def getParkingSpots(self):
        return self.spots
    
    def addVehicle(self, vehicle: Vehicle) -> bool:
        spotsRequired = vehicle.getSpotSize()
        
        start = 0
        for end in range(len(self.spots)):
            if self.spots[end] != 0:
                start = end + 1
            
            if end - start + 1 == spotsRequired:
                self.vehicles[vehicle] = [start, end]
                for i in range(start, end + 1):
                    self.spots[i] = 1
                return True
            
        return False
    
    def removeVehicle(self, vehicle: Vehicle):
        start, end = self.vehicles[vehicle]
        del self.vehicles[vehicle]
        
        for i in range(start, end + 1):
            self.spots[i] = 0
        
    def getVehicleSpots(self, vehicle: Vehicle):
        return self.vehicles[vehicle] if vehicle in self.vehicles else None
    
class ParkingGarage:
    def __init__(self, floors:int, spotsPerFloor ):
        self.floors = [ParkingFloor(spotsPerFloor) for _ in range(floors)]
    
    def parkVehicle(self, vehicle: Vehicle) -> bool:
        for floor in self.floors:
            added = floor.addVehicle(vehicle)
            if added == True:
                return True
        return False
    
    def removeVehicle(self, vehicle: Vehicle):
        for floor in self.floors:
            hasVehicle = floor.getVehicleSpots(vehicle=vehicle)
            if hasVehicle:
                floor.removeVehicle(vehicle=vehicle)
                return True
        
        return False

class ParkingSystem:
    def __init__(self, garage: ParkingGarage, rate:int):
        self.garage = garage
        self.rate = rate
        self.timeParked = {}
    
    def parkDriver(self, driver: Driver):
        currHour = datetime.datetime.now().hour
        isParked = self.garage.parkVehicle(vehicle=driver.getVehicle())
        if isParked:
            self.timeParked[driver.getId()] = currHour
        return isParked
    
    def removeDriver(self, driver: Driver):
        driverId = driver.getId()
        
        if driverId not in self.timeParked:
            return False
        
        currHour = datetime.datetime.now().hour
        # The line `timeParked = math.ceil()` in the provided code snippet seems to be incomplete and
        # missing the required arguments for the `math.ceil()` function.
        timeParked = math.ceil(currHour - self.timeParked[driverId])
        driver.charge(timeParked * self.rate)
        del self.timeParked[driverId]
        return self.garage.removeVehicle(driver.getVehicle())

if __name__ == "main":
    parkingGarage = ParkingGarage(3, 2)
    parkingSystem = ParkingSystem(parkingGarage, 5)

    driver1 = Driver(1, Car())
    driver2 = Driver(2, Limo())
    driver3 = Driver(3, Semi())

    print(parkingSystem.park_vehicle(driver1))      # true
    print(parkingSystem.park_vehicle(driver2))      # true
    print(parkingSystem.park_vehicle(driver3))      # false

    print(parkingSystem.remove_vehicle(driver1))    # true
    print(parkingSystem.remove_vehicle(driver2))    # true
    print(parkingSystem.remove_vehicle(driver3))    # false