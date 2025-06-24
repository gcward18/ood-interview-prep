"""
🧩 Observer Pattern Challenge: Routine Scoreboard

You’re building a live scoreboard for routines during a posing competition.

Multiple judges (observers) score routines. When a routine is scored, all judges should be notified and can react (log, update UI, etc.).

🏗 Requirements

1. Subject Interface: `RoutineSubject`
   - `attach(observer)`
   - `detach(observer)`
   - `notify()`

2. Concrete Subject: `Routine`
   - Holds state: `name`, `score`
   - Notifies observers when `set_score(score)` is called

3. Observer Interface: `Observer`
   - Method: `update(routine: Routine)`

4. Concrete Observers:
   - `ConsoleJudge` → prints score to console
   - `AnalyticsJudge` → logs to a dict for analysis
   - `CoachTablet` → prints: “Coach view updated: {routine.name} = {score}”

5. Demo
   - Create a routine and attach all 3 observers
   - Change the score and show all outputs

✨ Bonus
- Prevent duplicate observers
- Allow observers to unregister
- Add `__str__()` to `Routine` for debug output

💡 Example

routine = Routine("George")
routine.attach(ConsoleJudge())
routine.attach(CoachTablet())
routine.set_score(91.3)
"""
from abc import ABC, abstractmethod
    
class Observer(ABC):
    @abstractmethod
    def update(self, routine: Routine):
        pass
    
class RoutineSubject(ABC):
    @abstractmethod
    def attach(self, observer: Observer):
        pass
    
    @abstractmethod
    def detach(self, observer: Observer):
        pass
    
    @abstractmethod
    def notify(self):
        pass

class Routine(RoutineSubject):
    def __init__(self, name:str, score:float):
        self._name = name
        self._score = score
        self._observers = set()
        
    def attach(self, observer: Observer):
        self._observers.add(observer)
    
    def detach(self, observer: Observer):
        self._observers.remove(observer)
    
    def notify(self):
        for observer in self._observers:
            observer.update(self)

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score: float):
        self._score = score
        self.notify()
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: float):
        self._name = name
    
    def __str__(self):
        return f"Routine: {self._score} : {self._observers}"
    
class ConsoleJudge(Observer):
    def __init__(self):
        pass
    
    def update(self, routine: Routine):
        print(f"Routine score updated to : {routine.score}")
    
class AnalyticsJudge(Observer):
    def __init__(self):
        self._table = {}
        
    def update(self, routine: Routine):
        self._table[routine._name] = routine
        
class CoachTablet(Observer):
    def __init__(self):
        self._table = {}
        
    def update(self, routine: Routine):
        print(f"Coach view updated: {routine.name} = {routine.score}")

if __name__ == "__main__":
    
    routine = Routine("George")
    routine.attach(ConsoleJudge())
    routine.attach(CoachTablet())
    routine.set_score(91.3)