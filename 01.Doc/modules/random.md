## `random`
- **Random numbers**: Generate random numbers such as integer, float, etc.
- **Random choice**: Randomly select an element from a list or sequence.
- **Shuffling**: Randomly arrange the elements of a list.
- **Range sampling**: Take a random sample from a specified range.
- **Probability simulation**: Simulate things like coin toss, dice roll.

---

## 📘 Example

### Random Number
```python
import random

print(random.randint(1, 10)) # A random integer between 1 and 10
print(random.random()) # A random float between 0 and 1
```

---

### Random Choice
```python
import random

names = ["Mahin", "Hasan", "Rafi", "Nusrat"]
print(random.choice(names)) # Will choose a name randomly
```

---

### Shuffle
```python
import random

cards = ["A", "K", "Q", "J", "10"]
random.shuffle(cards)
print(cards) # Will sort randomly
```

---

### Sample
```python
import random

numbers = list(range(1, 50))
print(random.sample(numbers, 6)) # 6 random numbers from 1 to 49
```