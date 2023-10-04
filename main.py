import unittest

class ProgramProduct1:
    def add(self, a, b):
        """Складывает два числа и возвращает результат."""
        return a + b

    def subtract(self, a, b):
        """Вычитает второе число из первого и возвращает результат."""
        return a - b

def test_add():
    # Подготовка (Arrange)
    product = ProgramProduct1()
    a, b = 5, 4

    # Действие (Act)
    result = product.add(a, b)

    # Проверка (Assert)
    assert result == 8, f"Ожидалось 8, но получено {result}"

class ProgramProduct2:
    def multiply(self, a, b):
        """Умножает два числа и возвращает результат."""
        return a * b

    def divide(self, a, b):
        """Делит первое число на второе и возвращает результат.
        Если второе число равно нулю, возвращает 'Нельзя делить на ноль'."""
        if b == 0:
            return "Нельзя делить на ноль"
        return a / b

class ProgramProduct3:
    def to_upper(self, text):
        """Преобразует строку в верхний регистр и возвращает результат."""
        return text.upper()

    def to_lower(self, text):
        """Преобразует строку в нижний регистр и возвращает результат."""
        return text.lower()

class ProgramProduct4:
    def fibonacci(self, n):
        """Возвращает n-ное число Фибоначчи."""
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

def test_subtract():
    # Подготовка (Arrange)
    product = ProgramProduct1()
    a, b = 5, 3

    # Действие (Act)
    result = product.subtract(a, b)

    # Проверка (Assert)
    assert result == 2, f"Ожидалось 2, но получено {result}"

# 2
def test_multiply():
    # Подготовка (Arrange)
    product = ProgramProduct2()
    a, b = 5, 3

    # Действие (Act)
    result = product.multiply(a, b)

    # Проверка (Assert)
    assert result == 15, f"Ожидалось 15, но получено {result}"

def test_divide():
    # Подготовка (Arrange)
    product = ProgramProduct2()
    a, b = 6, 3

    # Действие (Act)
    result = product.divide(a, b)

    # Проверка (Assert)
    assert result == 2, f"Ожидалось 2, но получено {result}"

def test_divide_by_zero():
    # Подготовка (Arrange)
    product = ProgramProduct2()
    a, b = 5, 0

    # Действие (Act)
    result = product.divide(a, b)

    # Проверка (Assert)
    assert result == "Нельзя делить на ноль", f"Ожидалось 'Нельзя делить на ноль', но получено {result}"

# 3
def test_to_upper():
    # Подготовка (Arrange)
    product = ProgramProduct3()
    text = "hello"

    # Действие (Act)
    result = product.to_upper(text)

    # Проверка (Assert)
    assert result == "HELLO", f"Ожидалось 'HELLO', но получено {result}"

def test_to_lower():
    # Подготовка (Arrange)
    product = ProgramProduct3()
    text = "HELLO"

    # Действие (Act)
    result = product.to_lower(text)

    # Проверка (Assert)
    assert result == "hello", f"Ожидалось 'hello', но получено {result}"

# 4
def test_fibonacci():
    # Подготовка (Arrange)
    product = ProgramProduct4()
    n = 5

    # Действие (Act)
    result = product.fibonacci(n)

    # Проверка (Assert)
    assert result == 5, f"Ожидалось 5, но получено {result}"

def test_fibonacci_zero():
    # Подготовка (Arrange)
    product = ProgramProduct4()
    n = 0

    # Действие (Act)
    result = product.fibonacci(n)

    # Проверка (Assert)
    assert result == 0, f"Ожидалось 0, но получено {result}"

class ProgramProduct1Tests(unittest.TestCase):
    def test_add(self):
        product = ProgramProduct1()
        self.assertEqual(product.add(5, 3), 8)

    def test_subtract(self):
        product = ProgramProduct1()
        self.assertEqual(product.subtract(5, 3), 2)

class ProgramProduct2Tests(unittest.TestCase):
    def test_multiply(self):
        product = ProgramProduct2()
        self.assertEqual(product.multiply(5, 3), 15)

    def test_divide(self):
        product = ProgramProduct2()
        self.assertEqual(product.divide(6, 3), 2)

    def test_divide_by_zero(self):
        product = ProgramProduct2()
        self.assertEqual(product.divide(5, 0), "Нельзя делить на ноль")

class ProgramProduct3Tests(unittest.TestCase):
    def test_to_upper(self):
        product = ProgramProduct3()
        self.assertEqual(product.to_upper("hello"), "HELLO")

    def test_to_lower(self):
        product = ProgramProduct3()
        self.assertEqual(product.to_lower("HELLO"), "hello")

class ProgramProduct4Tests(unittest.TestCase):
    def test_fibonacci(self):
        product = ProgramProduct4()
        self.assertEqual(product.fibonacci(5), 5)

    def test_fibonacci_zero(self):
        product = ProgramProduct4()
        self.assertEqual(product.fibonacci(0), 0)

if __name__ == "__main__":
    unittest.main()
