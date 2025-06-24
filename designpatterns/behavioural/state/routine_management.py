"""
🧩 State Pattern Challenge: Routine Lifecycle Management

You want to model a posing routine’s lifecycle using the State pattern.

A routine can be in one of three states:
- Draft
- Finalized
- Published

Each state has its own behavior for:
- `edit(content: str)`
- `submit_for_review()`
- `publish()`

🏗 Requirements

1. State Interface: `RoutineState`
   - Methods:
     - `edit(routine, content)`
     - `submit_for_review(routine)`
     - `publish(routine)`

2. Context: `Routine`
   - Attributes: `name`, `content`, `state`
   - Delegates behavior to current state
   - Method: `set_state(new_state)`

3. States:
   - `DraftState`:
     - `edit()` modifies content
     - `submit_for_review()` moves to `FinalizedState`
     - `publish()` raises error
   - `FinalizedState`:
     - `edit()` raises error
     - `submit_for_review()` raises error
     - `publish()` moves to `PublishedState`
   - `PublishedState`:
     - All operations are no-ops or raise errors (routine is locked)

4. Demo
   - Create a routine, edit it, finalize it, then publish it
   - Show state transitions and errors when operations are invalid

✨ Bonus
- Add `__str__()` to each state to reflect current status
- Log transitions or raise custom exceptions for invalid actions

💡 Example

"""
from abc import ABC, abstractmethod
from threading import Lock

class Logger:
    _instance = None
    _lock = Lock()
    
    def __new__(cls):
        with cls._lock:
            if not cls._instance:
                cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance

    def log(self, level: str, message: str) -> str:
        print(f"{level.strip().upper()}: {message}")
        
class State(ABC):
    @abstractmethod
    def edit(self, routine: Routine, content: str):
        pass
    
    @abstractmethod
    def submit_for_review(self, routine):
        pass
    
    @abstractmethod
    def publish(self, routine):
        pass
    
class DraftState(State):
    def __init__(self):
        self._logger = Logger()

    def __str__(self):
        return "DraftState"

    def edit(self, routine: Routine, content):
        self._logger.log("debug", f"DraftState edit called...")
        routine.content = content
    
    def submit_for_review(self, routine):
        self._logger.log("debug", f"DraftState submit_for_review() called...")
        routine.state = FinalizedState()
    
    def publish(self, routine):
        self._logger.log("debug", f"DraftState publish() called...")
        raise Exception("Cannot Publish from the Draft State.")
    
class FinalizedState(State):
    def __init__(self):
        self._logger = Logger()

    def __str__(self):
        return "FinalizedState"

    def edit(self, routine: Routine, content):
        self._logger.log("debug", f"FinalizedState edit called...")
        raise Exception("Cannot Edit from the Finalized State.")
    
    def submit_for_review(self, routine):
        self._logger.log("debug", f"FinalizedState submit_for_review() called...")
        raise Exception("Cannot Submit For Review from the Finalized State.")
    
    def publish(self, routine):
        self._logger.log("debug", f"FinalizedState publish() called...")
        routine.state = PublishedState()
    
class PublishedState(State):
    def __init__(self):
        self._logger = Logger()

    def __str__(self):
        return "PublishedState"

    def edit(self, routine: Routine, content):
        self._logger.log("debug", f"PublishedState edit called...")
        raise Exception("Cannot Edit from the Published State.")
    
    def submit_for_review(self, routine):
        self._logger.log("debug", f"PublishedState submit_for_review() called...")
        raise Exception("Cannot Submit For Review from the Published State.")
    
    def publish(self, routine):
        self._logger.log("debug", f"PublishedState publish() called...")
        raise Exception("Cannot Publish from the Published State.")


class Routine:
    def __init__(self, name: str, content: str="", state: State=DraftState()):
        self._name = name
        self._content = content
        self._state = state
        
    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self, state: State):
        self._state = state 
        
    @property
    def content(self):
        return self._content
    
    @content.setter
    def content(self, content: str):
        self._content = content

if __name__ == "__main__":
    
    routine = Routine("Olympia")
    routine.edit("Front Lat Spread → Side Chest")
    routine.submit_for_review()
    routine.publish()
    print(routine.content)  # Locked in