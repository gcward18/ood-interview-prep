"""
🧩 Adapter Pattern Challenge: Third-Party Pose Estimation Integration

You’ve decided to use a third-party pose estimation library (`PoseLibX`) in your Posing Clinic app.

Unfortunately, PoseLibX’s API is incompatible with your internal interface.

🏗 Requirements

1. Existing Interface: `PoseAnalyzer`
   - Method: `analyze_pose(image_path: str) -> List[str]`

2. Third-Party Class: `PoseLibXEngine`
   - Method: `run(image_path: str) -> Dict[str, float]` 
     (returns confidence scores for pose labels)

3. Adapter Class: `PoseLibXAdapter`
   - Implements `PoseAnalyzer`
   - Wraps `PoseLibXEngine`
   - Converts confidence scores > 0.8 into pose labels

4. Demo
   - Create a dummy `PoseLibXEngine` implementation
   - Use the adapter to analyze a sample image
   - Output: List of pose labels above confidence threshold

✨ Bonus
- Add a config threshold in the adapter constructor
- Allow easy swapping of PoseLibX with other engines later

💡 Example

engine = PoseLibXEngine()
adapter = PoseLibXAdapter(engine, threshold=0.8)
poses = adapter.analyze_pose("posing.jpg")
print(poses)  # ['Front Double Biceps', 'Side Chest']
"""

from typing import Dict, List
from abc import ABC, abstractmethod

class PoseAnalyzer(ABC):
    @abstractmethod
    def analyze_pose(image_path: str) -> List[str]:
        pass
    
class PoseLibXEngine:
    def run(self, image_path: str) -> List[Dict[str, float]]:
        with open(image_path, 'r') as file_out:
            if file_out:
                return [{"pose": "Front Double Biceps", "confidence": 0.92}, {"pose": "Side Chest", "confidence": 0.8}, {"pose": "Rear Double", "confidence": 0.45}]
            else:
                raise ValueError("Image not found.")


class PoseLibXAdapter(PoseAnalyzer):
    def __init__(self, engine: PoseLibXEngine, threshold: float):
        self._engine = engine
        self._threshold = threshold
    
    def analyze_pose(self, image_path):
        results = self._engine.run(image_path)
        results = [res["pose"] for res in results if res["confidence"] >= self._threshold]
        return results

if __name__ == "__main__":
    
    engine = PoseLibXEngine()
    adapter = PoseLibXAdapter(engine, threshold=0.8)
    poses = adapter.analyze_pose("design-patterns/structural/adapter/posing.jpg")
    print(poses)  # ['Front Double Biceps', 'Side Chest']