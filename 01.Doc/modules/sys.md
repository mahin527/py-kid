## `sys`

**Python's `sys` module is a collection of system-specific parameters and functions, which helps to interact directly with the Python interpreter.**

---

## 🔑 `sys` module functions
- **Command line arguments**: `sys.argv` provides command line arguments to the script.
- **Exit program**: `sys.exit()` can be used to terminate the program.
- **Interpreter info**: Python version, platform, path etc. can be found.
- **Standard I/O control**: `sys.stdin`, `sys.stdout`, `sys.stderr` can be used to control the input/output stream.
- **Module path management**: `sys.path` can be used to change the module search path.
- **Recursion limit**: `sys.getrecursionlimit()` and `sys.setrecursionlimit()` can be used to control the recursion depth.
- **Memory management**: `sys.getsizeof()` is used to find the memory size of an object.

---

## 📘 Example

### Command Line Arguments
```python
import sys

print(sys.argv)
# Arguments given while running the script will be available in the form of a list
```

---

### Exit Program
```python
import sys

print("Before exit")
sys.exit()
print("After exit") # It will not be executed again
```

---

### Python Version
```python
import sys

print(sys.version) # Shows the version of Python
```

---

### Module Path
```python
import sys

print(sys.path) # List of where Python will look for modules
```

### stdin
```python
import sys

print("Enter text (Press Ctrl+D or Ctrl+Z to stop):")

# Iterating directly over sys.stdin reads line by line
for line in sys.stdin:
    # .strip() removes trailing newlines and spaces
    clean_line = line.strip()
    print(f"Processed: {clean_line}")

```

---

## 📝 Things to remember
- `sys` is a **built-in module**, you don't have to install it separately.
- It provides low-level interaction with the Python interpreter.
- It is usually used for **command line tools, debugging, and environment control**.
