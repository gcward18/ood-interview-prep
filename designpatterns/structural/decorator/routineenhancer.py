"""
🧩 Decorator Pattern Challenge: Routine Enhancer

You’re enhancing posing routines dynamically with add-on features like music, lighting, and timers.

🏗 Requirements

1. Base Class: `Routine`
   - Method: `perform() -> str`

2. Concrete Class: `BaseRoutine`
   - Returns: "Performing base routine"

3. Decorators:
   - `MusicDecorator` → adds " with music"
   - `LightingDecorator` → adds " under stage lighting"
   - `TimerDecorator` → adds " timed to 60 seconds"

4. Each decorator wraps a `Routine` and extends its `perform()` output.

5. Demo:
   - Compose a routine with multiple decorators
   - Show layered effects
   - Example: Base → Music → Lighting → Timer

✨ Bonus
- Allow passing parameters to decorators (e.g., song name, light color, time duration)
- Support `__str__()` to view routine stack

💡 Example

routine = TimerDecorator(LightingDecorator(MusicDecorator(BaseRoutine())))
print(routine.perform())  # "Performing base routine with music under stage lighting timed to 60 seconds"
"""
from abc import ABC, abstractmethod

class Routine(ABC):
    @abstractmethod
    def perform(self) -> str:
        pass

class BaseRoutine(Routine):
    def perform(self):
        return "Performing base routine"
    
    def __str__(self):
        return "BaseRoutine"

class LightingDecorator(Routine):
    def __init__(self, routine: Routine, color: str=""):
        self._routine = routine
        self._color = color
        
    def perform(self):
        return self._routine.perform() + f" under {self._color + ' ' if self._color else ''}stage lighting"
    
    def __str__(self):
        return f"{self._routine} -> LightingDecorator({self._color})"

class MusicDecorator(Routine):
    def __init__(self, routine: Routine, song: str=""):
        self._routine = routine
        self._song = song 
        
    def perform(self):
        return self._routine.perform() + f" with music{' ' + self._song if self._song else ''}"
    
    def __str__(self):
        return f"{self._routine} -> MusicDecorator({self._song})"
    
class TimeDecorator(Routine):
    def __init__(self, routine: Routine, time: int=60):
        self._routine = routine
        self._time = time
        
    def perform(self):
        return self._routine.perform() + f" timed to {self._time} seconds"

    def __str__(self):
        return f"{self._routine} -> TimeDecorator({self._time})"

if __name__ == "__main__":    
    routine = TimeDecorator(LightingDecorator(MusicDecorator(BaseRoutine()), "blue"))
    print(routine.perform())  # "Performing base routine with music under stage lighting timed to 60 seconds"
    print(routine)
