"""
🧩 Facade Pattern Challenge: Routine Publishing Pipeline

You want to simplify the publishing process for a completed posing routine.

Normally, publishing a routine involves:
- Validating the routine
- Enhancing it with music, lighting, or timer decorators
- Uploading it to cloud storage
- Notifying the coach

🏗 Requirements

1. Subsystems:
   - `RoutineValidator.validate(routine: Routine) -> bool`
   - `RoutineEnhancer.enhance(routine: Routine) -> Routine`
   - `CloudUploader.upload(routine: Routine) -> str` (returns URL)
   - `CoachNotifier.notify(url: str) -> None`

2. Facade Class: `RoutinePublisher`
   - Method: `publish(routine: Routine) -> str`
   - Handles validation, enhancement, upload, and notification
   - Returns the final URL

3. Demo
   - Create a `BaseRoutine`
   - Use `RoutinePublisher` to publish it
   - Show full output trace (validation → enhancement → upload → notify → return URL)

✨ Bonus
- Add logs at each step
- Support custom enhancement config (e.g., song name, light color, duration)

💡 Example

routine = BaseRoutine()
publisher = RoutinePublisher(song="Eye of the Tiger", color="gold", time=90)
url = publisher.publish(routine)
print(url)
# """
from abc import ABC, abstractmethod
from typing import Dict
from designpatterns.structural.decorator.routineenhancer import BaseRoutine, Routine, LightingDecorator, TimeDecorator, MusicDecorator
from threading import Lock

class Logger:
   _instance = None
   _lock = Lock()
   
   def __new__(cls):
      with cls._lock:
         if cls._instance == None:
            cls._instance = super(Logger, cls).__new__(cls)
      
      return cls._instance

   @staticmethod
   def log(level: str, message: str):
      print(f"{level.upper()}: {message}")
         
      
class RoutineValidator:
   def __init__(self):
      self._logger = Logger()
      
   def validate(self, routine: Routine) -> bool:
      if routine and routine.perform():
         self._logger.log("debug", "Valid Routine")
         return True
      self._logger.log("debug", "Invalid Routine")
      return False

class RoutineEnhancer:
   def __init__(self):
      self._logger = Logger()
      
   def enhance(self, routine: Routine, enhancements: Dict[str, any]) -> Routine:
      if "music" in enhancements and enhancements["music"]:
         self._logger.log("DEBUG", f"adding music enhancement: {enhancements['music']}")
         routine = MusicDecorator(routine, enhancements["music"])
      if "color" in enhancements and enhancements["color"]:
         self._logger.log("DEBUG", f"adding lighting enhancement: {enhancements['color']}")
         routine = LightingDecorator(routine, enhancements["color"])
      if "duration" in enhancements and enhancements["duration"]:
         self._logger.log("DEBUG", f"adding time enhancement: {enhancements['duration']} seconds")
         routine = TimeDecorator(routine, enhancements["duration"])
      return routine

class CloudUploader:
   def __init__(self, connection_string: str):
      self._connection_string = connection_string
      self._logger = Logger()
   
   def upload(self, routine: str) -> str:
      url = f"{self._connection_string}/routine"
      self._logger.log("DEBUG", f"uploading to -> {url}")
      return url

class CoachNotifier:
   def __init__(self):
      self._logger = Logger()
      
   def notify(self, url: str) -> None:
      self._logger.log("DEBUG", f"Notifying Coach {url}")
   
class RoutinePublisher:
   def __init__(self, song: str, color: str, duration: int):
      self._song = song
      self._color = color
      self._duration = duration
      self._validator = RoutineValidator()
      self._enhancer = RoutineEnhancer()
      self._notifier = CoachNotifier()
      self._uploader = CloudUploader("10.0.0.8/5000")
      
   def publish(self, routine):
      if not self._validator.validate(routine):
         raise ValueError("Invalid Routine")
      
      enhancements = {}
      if self._song:
         enhancements["song"] = self._song
      if self._color:
         enhancements["color"] = self._color
      if self._duration:
         enhancements["duration"] = self._duration
         
      routine = self._enhancer.enhance(routine, enhancements)
      upload_url = self._uploader.upload(routine)
      self._notifier.notify("george@georgewardfitness.com")
      
      return upload_url

if __name__ == "__main__":
   routine = BaseRoutine()
   publisher = RoutinePublisher(song="Eye of the Tiger", color="gold", duration=90)
   url = publisher.publish(routine)
   print(url)