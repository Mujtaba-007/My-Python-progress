#Claude answering Chap 11 PS for me ;)
#Q1
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Vector3D(Vector2D):   # Inherits from Vector2D
    def __init__(self, x, y, z):
        super().__init__(x, y)  # Takes x, y from parent
        self.z = z

v = Vector3D(1, 2, 3)
print(v.x, v.y, v.z)  # → 1 2 3
#My addition:
a=Vector2D(9,8)
print("2d axes:",a.x,a.y)


#2. Animals → Pets → Dog
class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):
    def bark(self):
        print("Woof!")

d = Dog()
d.bark()  # → Woof!

# 3. Employee class with @property
class Employee:
    def __init__(self, salary, increment):
        self.salary = salary
        self._increment = increment

    @property
    def salaryAfterIncrement(self):
        return self.salary + self._increment

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, new_increment):
        if new_increment > self.salary:
            print("Increment can't be more than salary!")
        else:
            self._increment = new_increment

e = Employee(50000, 5000)
print(e.salaryAfterIncrement)  # → 55000

e.salaryAfterIncrement = 60000  # ❌ Increment can't be more than salary!
e.salaryAfterIncrement = 8000   # ✅
print(e.salaryAfterIncrement)   # → 58000

# 4. Complex Number class
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        # (a+bi)(c+di) = ac-bd + (ad+bc)i
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return Complex(real, imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

c1 = Complex(2, 3)
c2 = Complex(1, 4)
print(c1 + c2)   # → 3 + 7i
print(c1 * c2)   # → -10 + 11i

# 5, 6 & 7. N-Dimensional Vector with +, *, __str__, __len__
# These 3 questions are connected so solving together —
class Vector:
    def __init__(self, *args):
        self.components = list(args)  # Stores all values

    def __add__(self, other):
        result = [a + b for a, b in zip(self.components, other.components)]
        return Vector(*result)

    def __mul__(self, other):         # Dot product
        result = sum(a * b for a, b in zip(self.components, other.components))
        return result

    def __str__(self):
        labels = ['i', 'j', 'k']      # For dimension names
        result = " + ".join(f"{val}{labels[i]}" 
                           for i, val in enumerate(self.components))
        return result

    def __len__(self):
        return len(self.components)   # Returns dimension count

v1 = Vector(7, 8, 10)
v2 = Vector(1, 2, 3)

print(v1)          # → 7i + 8j + 10k  ✅ (exactly as asked!)
print(v1 + v2)     # → 8i + 10j + 13k
print(v1 * v2)     # → 57 (dot product)
print(len(v1))     # → 3 (3 dimensions)