```markdown
# 🔐 Python Password Generator

A clean, extensible password generator built with Python's Abstract Base Classes (ABC). Supports multiple password strategies (Numeric, Letters, Mixed) and makes it easy to add new ones.

---

## ✨ Features

- **Object-Oriented Design**: Uses `abc.ABC` for a clean, extensible interface
- **Three Built-in Generators**:
  - `NumericPasswordGenerator` → digits only (`0-9`)
  - `LetterPasswordGenerator` → letters only (a-z, A-Z)
  - `MixedPasswordGenerator` → letters + digits
- **Customizable length** (default: 8 characters)
- **Easy to extend** — just inherit from `GeneratePasswordAbstract`
- Single-file, zero dependencies

---

## 📁 Project Structure

```
password-generator/
├── password_generator.py     # Main script (copy-paste the code you provided)
└── README.md                 # ← You are here
```

---

## 🚀 Installation

**Option 1: Copy the code**

1. Create a new file `password_generator.py`
2. Paste the entire code you provided
3. Save it

**Option 2: Clone (if you put it in a repo)**

```bash
git clone https://github.com/alahyarlou/python-password-generator.git
cd python-password-generator
```

---

## 💡 Usage

### As a module

```python
from password_generator import (
    NumericPasswordGenerator,
    LetterPasswordGenerator,
    MixedPasswordGenerator
)

# Generate different types of passwords
numeric = NumericPasswordGenerator()
letter  = LetterPasswordGenerator()
mixed   = MixedPasswordGenerator()

print("Numeric :", numeric.generate_password(10))
print("Letters :", letter.generate_password(12))
print("Mixed   :", mixed.generate_password(16))
```

### Run standalone

```bash
python password_generator.py
```

This will print one mixed password of length 8.

---

## 📝 Examples

```python
# 16-character mixed password (recommended)
gen = MixedPasswordGenerator()
print(gen.generate_password(16))

# 6-digit PIN
pin = NumericPasswordGenerator()
print(pin.generate_password(6))

# 20-character strong letter password
strong = LetterPasswordGenerator()
print(strong.generate_password(20))
```

---

## 🛠 Extending the Generator

Add new password types in seconds:

```python
class SymbolPasswordGenerator(GeneratePasswordAbstract):
    letters = string.ascii_letters + string.digits + string.punctuation

    def generate_password(self, length=12):
        return "".join(random.choice(self.letters) for _ in range(length))


# Usage
symbol_gen = SymbolPasswordGenerator()
print(symbol_gen.generate_password(20))
```

---

## ⚠️ Security Note

- This project uses Python's `random` module (fine for demos, learning, and non-critical use).
- For **production/security-critical** applications, replace `random` with the `secrets` module:

```python
import secrets

return "".join(secrets.choice(self.letters) for _ in range(length))
```

---

## 📄 License

This project is open source and available under the **MIT License**.

---

**Made with ❤️ for clean, extensible Python code.**