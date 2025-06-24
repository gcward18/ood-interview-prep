# 🧠 Design Patterns in Python – Posing Clinic Edition

This repository showcases 10 essential software design patterns using real-world concepts from a posing routine management system (e.g., bodybuilding competitions).

Each pattern is implemented in Python with a focus on clarity, extensibility, and clean architecture.

## 📦 Patterns Covered

| Pattern       | Summary                                   | Filename                                                     |
|---------------|-------------------------------------------|--------------------------------------------------------------|
| Factory       | Creates notification senders              | `/designpatterns/creational/factory/notification-factory.py` |
| Prototype     | Clones posing routines via a registry     | `/designpatterns/creational/prototype/posing-prototypes.py`  |
| Singleton     | Manages global posing rules               | `/designpatterns/creational/singleton/posing-rules.py`       |
| Builder       | Constructs routine screens step-by-step   | `/designpatterns/creational/builder/ui-builder.py`           |
| Adapter       | Adapts 3rd-party pose engine              | `/designpatterns/structural/adapter/pose-analyzer.py`        |
| Decorator     | Enhances routines with music/lighting     | `/designpatterns/structural/decorator/routineenhancer.py`    |
| Facade        | Publishes routines via a unified interface| `/designpatterns/structural/facade/publishing-pipeline.py`   |
| Strategy      | Scores routines via interchangeable logic | `/designpatterns/behavioural/strategy/routine_scoring.py`    |
| Observer      | Notifies judges of score updates          | `/designpatterns/behavioural/observer/routine_scoreboard.py` |
| State         | Manages routine lifecycle transitions     | `/designpatterns/behavioural/state/routine_management.py`    |

## 📚 How to Use

Each file is self-contained with a `__main__` demo block. Just run:
```bash
python filename.py
