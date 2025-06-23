from abc import ABC, abstractmethod
import copy
from enum import Enum
from typing import Dict, Type

"""
🧩 Prototype Pattern Challenge: Posing Routine Templates

You're building a posing routine system for bodybuilding competitors. 
Each competitor can choose a base posing template (e.g., Classic Physique, Men’s Open, Wellness), 
then clone and customize it for their unique routine.

🏗 Requirements

1. Prototype Interface
   - `PosingRoutine` interface with:
     - `clone() -> PosingRoutine`
     - `customize(name: str = None, poses: list[str] = None) -> None`

2. Concrete Routines
   - `ClassicRoutine`, `OpenRoutine`, and `WellnessRoutine`
   - Each should have:
     - `name`: str
     - `poses`: List[str]

3. Prototype Registry
   - A `RoutineRegistry` that stores base prototypes and allows cloning via `get_clone(name: str)`

4. Demo
   - Register base routines in the registry
   - Clone a routine
   - Modify the clone (e.g., add new pose, rename)
   - Show that original remains unchanged

✨ Bonus
- Use `copy.deepcopy()` where needed to ensure independence of objects.
- Include a `__str__()` method to show routines clearly.
- Optionally allow loading custom templates from JSON and registering them as prototypes.

💡 Example Usage

registry = RoutineRegistry()
registry.register("classic", ClassicRoutine())

my_routine = registry.get_clone("classic")
my_routine.customize(name="George's Olympia Routine", poses=["Front Double Biceps", "Side Chest", "Victory Pose"])
print(my_routine)

print(registry.get_clone("classic"))  # should remain unchanged
"""
class RoutineType(Enum):
    OPEN = "OPEN"
    CLASSIC = "CLASSIC"
    WELLNESS = "WELLNESS"
    
class PosingRoutine(ABC):
    @abstractmethod
    def clone(self):
        pass
    
    @abstractmethod
    def customize(self, name: str, poses: list[str]):
        pass

class OpenRoutine(PosingRoutine):
    def __init__(self, name: str="Open Routine",poses: str=None):
        self.poses = poses
        self.name = name
    
    def __str__(self):
        result = f"{self.name}: {self.poses}"
        return result

    def clone(self):
        return OpenRoutine(self.name, copy.deepcopy(self.poses))
    
    def customize(self, name: str, poses: list[str]):
        self.name = name
        self.poses = poses

class ClassicRoutine(PosingRoutine):
    def __init__(self, name: str="Classic Routine",poses: str=None):
        self.poses = poses
        self.name = name
    
    def __str__(self):
        result = f"{self.name}: {self.poses}"
        return result

    def clone(self):
        return ClassicRoutine(self.name, copy.deepcopy(self.poses))
    
    def customize(self, name: str, poses: list[str]):
        self.name = name
        self.poses = poses

class WellnessRoutine(PosingRoutine):
    def __init__(self, name: str="Wellness Routine",poses: str=None):
        self.poses = poses
        self.name = name
    
    def __str__(self):
        result = f"{self.name}: {self.poses}"
        return result

    def clone(self):
        return WellnessRoutine(self.name, copy.deepcopy(self.poses))
    
    def customize(self, name: str, poses: list[str]):
        self.name = name
        self.poses = poses

class RoutineRegistry:
    def __init__(self, routines: Dict[str, Type[PosingRoutine]]={}):
        self.routines = routines
    
    def normalize(self, key) -> str:
        return key.strip().lower()
    
    def register(self, key: str, routine_instance: PosingRoutine) -> None:
        normalized_key = self.normalize(key)
        if normalized_key in self.routines:
            raise ValueError(f"{key} already in the Registry")    
        self.routines[normalized_key] = routine_instance
        
    def get_clone(self, key: str) -> PosingRoutine:
        normalized_key = self.normalize(key)
        if normalized_key not in self.routines:
            raise ValueError(f"{key} not in the Registry")    
        return self.routines[normalized_key].clone()

if __name__ == "__main__":
    registry = RoutineRegistry()
    registry.register("classic", ClassicRoutine())

    my_routine = registry.get_clone("classic")
    my_routine.customize(name="George's Olympia Routine", poses=["Front Double Biceps", "Side Chest", "Victory Pose"])

    new_routine = registry.get_clone("classic")
    new_routine.customize(name="George's Universe Routine", poses=["Front Relaxed", "Archer", "Back Double Biceps"])
    print(my_routine)
    print(new_routine)
    print(registry.get_clone("classic"))  # should remain unchanged