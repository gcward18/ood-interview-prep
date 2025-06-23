"""
🧩 Singleton Pattern Challenge: PosingRulesManager

You’re building a global `PosingRulesManager` to define and enforce posing regulations for competitions.

These rules should be:
- Readable anywhere in the system
- Immutable during a session
- Set once during startup
- Accessed via a singleton instance

🏗 Requirements

1. Create a `PosingRulesManager` class with:
   - `.set_rules(dict)` → Sets the rules only if not set
   - `.get_rules()` → Returns the rules
   - `.reset()` → (Bonus) Reset for testing only

2. Enforce Singleton behavior
   - All parts of the system get the same instance
   - Prevent creating more than one manager

3. Demo
   - Set posing rules once
   - Access rules from multiple places
   - Prove changes to one instance affect all references

✨ Bonus
- Add a `_initialized` flag to prevent reinitialization
- Use a metaclass or decorator-based singleton approach

💡 Example
manager1 = PosingRulesManager()
manager1.set_rules({"duration": 60, "poses": ["Front Double Biceps", "Side Chest"]})

manager2 = PosingRulesManager()
assert manager1 is manager2
print(manager2.get_rules())  # Should reflect the same rules
"""
import threading

class PosingRulesManager:
    _unique_instance = None
    _instance_lock = threading.Lock()
    
    def __new__(cls):
        with cls._instance_lock:
            if cls._unique_instance == None:
                cls._unique_instance = super(PosingRulesManager, cls).__new__(cls)
        
        return cls._unique_instance
        
    def reset(self):
        if hasattr(self, "_rules") and self._rules:
            self._rules = {}
        else: 
            raise ValueError("Rules never were set for the RulesManager")
        
    def set_rules(self, rules: dict) -> None:
        if hasattr(self, "_rules") and self._rules:
            raise ValueError("Rules already set for the RulesManager")
        self._rules = rules

    def get_rules(self) -> dict:
        if not hasattr(self, "_rules"):
            raise ValueError("Rules never were set for the RulesManager")
        return self._rules
    
if __name__ == "__main__":
    
    manager1 = PosingRulesManager()
    manager1.set_rules({"duration": 60, "poses": ["Front Double Biceps", "Side Chest"]})
    print(manager1.get_rules())
    manager2 = PosingRulesManager()
    assert manager1 is manager2
    print(manager2.get_rules())  # Should reflect the same rules