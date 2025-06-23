"""
🧩 Builder Pattern Challenge: Posing Clinic UI Screen Builder

You’re building a modular UI screen builder for your Posing Clinic app.
Each screen (e.g., “Routine Viewer”, “Pose Analyzer”, “Judge Feedback”) can be built step-by-step with various optional modules.

🏗 Requirements

1. Builder Interface (`ScreenBuilder`)
   - Methods:
     - `set_title(title: str)`
     - `add_section(name: str, content: str)`
     - `enable_live_feedback()`
     - `enable_pose_overlay()`
     - `build() -> Screen`

2. Product Class (`Screen`)
   - Should contain:
     - `title: str`
     - `sections: List[Dict[str, str]]`
     - `live_feedback_enabled: bool`
     - `pose_overlay_enabled: bool`
   - Include a `__str__()` for display

3. Concrete Builder (`RoutineScreenBuilder`)
   - Implements the builder interface
   - Accumulates configuration internally and builds a `Screen` object

4. Director (Optional)
   - A class `ScreenDirector` with methods like `build_judge_feedback_screen()` or `build_pose_analysis_screen()` to automate standard flows

5. Demo
   - Manually build one screen with the builder
   - Use the director to build a second screen
   - Print both to show differences

✨ Bonus
- Support method chaining (`return self`)
- Raise errors if required components (e.g., title) are missing before `build()`

💡 Example Usage

builder = RoutineScreenBuilder()
screen = (
    builder
    .set_title("Olympia Routine Review")
    .add_section("Intro", "Routine overview and flow")
    .add_section("Judges Notes", "Needs more expression in side tricep")
    .enable_live_feedback()
    .build()
)

print(screen)
"""
from abc import ABC, abstractmethod

class Product:
    def __init__(self, title: str, sections: list[str, str], live_feedback_enabled: bool, pose_overlay_enabled: bool):
        self._title = title
        self._sections = sections
        self._live_feedback_enabled = live_feedback_enabled
        self._pose_overlay_enabled = pose_overlay_enabled
    
    def __str__(self):
        result = []
        result.append(f"title: {self._title}")
        result.append(f"sections:")
        
        for section in self._sections:
            result.append(f"\t{section}")
        
        result.append(f"live_feedback_enabled: {self._live_feedback_enabled}")
        result.append(f"pose_overlay_enabled: {self._pose_overlay_enabled}")
        return '\n'.join(result)
    
class ScreenBuilder(ABC):
    @abstractmethod    
    def set_title(self, title: str):
        pass
    
    @abstractmethod
    def add_section(self, name: str, content: str):
        pass
    
    @abstractmethod
    def enable_live_feedback(self):
        pass
    
    @abstractmethod
    def enable_pose_overlay(self):
        pass
    
    @abstractmethod
    def build(self):
        pass


class RoutineScreenBuilder(ScreenBuilder):
    def __init__(self):
        self._title = None
        self._sections = []
        self._live_feedback_enabled = None
        self._pose_overlay_enabled = None
        
    def set_title(self, title: str):
        self._title = title
        return self

    def add_section(self, name: str, content: str):            
        self._sections.append({"name": name, "content": content})
        return self

    def enable_live_feedback(self):
        self._live_feedback_enabled = True
        return self

    def enable_pose_overlay(self):
        self._pose_overlay_enabled = True
        return self

    def build(self):
        if self._title is None:
            raise ValueError("Title required to build a screen.")
        return Product(self._title, self._sections, self._live_feedback_enabled, self._pose_overlay_enabled)

class RoutineDirector:
    @staticmethod
    def construct_classic_routine(builder: RoutineScreenBuilder):
        builder.set_title("Classic Routine")
        builder.add_section("Intro", "Arms Crossed")
        builder.add_section("Outro", "Favorite Classic Pose")
        builder.enable_pose_overlay()
        return builder.build()
        
    @staticmethod
    def construct_open_routine(builder: RoutineScreenBuilder):
        builder.set_title("Open Routine")
        builder.add_section("Intro", "Front Lat Spread")
        builder.add_section("Outro", "Back Lat Spread")
        builder.enable_live_feedback()
        builder.enable_pose_overlay()
        return builder.build()
        
    @staticmethod
    def construct_wellness_routine(builder: RoutineScreenBuilder):
        builder.set_title("Wellness Routine")
        builder.add_section("Intro", "Front Relaxed")
        builder.add_section("Outro", "Rear Relaxed")
        builder.enable_live_feedback()
        return builder.build()
        
        

if __name__ == "__main__":
    director = RoutineDirector()
    builder = RoutineScreenBuilder()
    screen = (
        builder
        .set_title("Olympia Routine Review")
        .add_section("Intro", "Routine overview and flow")
        .add_section("Judges Notes", "Needs more expression in side tricep")
        .enable_live_feedback()
        .build()
    )

    print(screen, '\n')
    
    builder = RoutineScreenBuilder()
    classic = director.construct_classic_routine(builder)
    print(classic, '\n')
    
    builder = RoutineScreenBuilder()
    open_bb = director.construct_open_routine(builder)
    print(open_bb, '\n')
    
    builder = RoutineScreenBuilder()
    wellness = director.construct_wellness_routine(builder)
    print(wellness, '\n')