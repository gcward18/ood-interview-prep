"""
🧩 Strategy Pattern Challenge: Routine Scoring Strategies

You’re building a scoring system for posing routines.

There are different strategies for judging:
- Symmetry-based
- Muscularity-based
- Creativity-based

🏗 Requirements

1. Strategy Interface: `ScoringStrategy`
   - Method: `score(routine: Routine) -> float`

2. Concrete Strategies:
   - `SymmetryScoring` → Returns 80.0
   - `MuscularityScoring` → Returns 92.5
   - `CreativityScoring` → Returns 88.7

3. Context Class: `RoutineScorer`
   - Accepts a `ScoringStrategy`
   - Method: `evaluate(routine: Routine) -> float`

4. Demo:
   - Evaluate one routine with each strategy
   - Output the score and strategy used

✨ Bonus
- Allow strategy switching at runtime
- Add a `__str__()` to strategies for name display

💡 Example

scorer = RoutineScorer(MuscularityScoring())
score = scorer.evaluate(BaseRoutine())
print(score)  # 92.5
"""
from abc import ABC, abstractmethod
from ..structural.decorator.routineenhancer import Routine, BaseRoutine

class ScoringStrategy:
    @abstractmethod
    def score(routine: Routine):
        pass

class SymmetryStrategy(ScoringStrategy):
    @staticmethod
    def score(routine: Routine) -> float:
        return 80.0
    
    def __str__(self):
        return "SymmetryStrategy"
    
class MuscularityStrategy(ScoringStrategy):
    @staticmethod
    def score(routine: Routine) -> float:
        return 92.5
    
    def __str__(self):
        return "MuscularityStrategy"
    
class CreativityStrategy(ScoringStrategy):
    @staticmethod
    def score(routine: Routine) -> float:
        return 88.7
    
    def __str__(self):
        return "CreativityStrategy"

class RoutineScorer:
    def __init__(self, strategy: ScoringStrategy):
        self._strategy = strategy
    
    @property
    def strategy(self) -> ScoringStrategy:
        return self._strategy
    
    @strategy.setter
    def strategy(self, strategy: ScoringStrategy) -> None:
        self._strategy = strategy
        
    def evaluate(self, routine: Routine) -> float:
        return self._strategy.score(routine)
    
if __name__ == "__main__":
    scorer = RoutineScorer(MuscularityStrategy())
    score = scorer.evaluate(BaseRoutine())
    print(score)  # 92.5