# Числа Фибоначчи — числовой ряд, при котором каждое последующее число равно сумме двух предыдущих


# Получить число Фибоначчи по его номеру
def fib(n: int):
    if not isinstance(n, int) or n < 0 or n in (0, float("inf"), float("-inf")):
        return None
    if n <= 2:
        return n - 1
    a, b = 0, 1
    for _ in range(n - 2):
        a, b = b, a + b
    return b