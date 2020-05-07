class Fraction:
    """Обыкновенные дроби и операции с ними"""

    def __init__(self, a, b):
        self.num = int(a)
        self.den = int(b)
        conditions = any([a < 0 and b > 0, a > 0 and b < 0])
        self.negative = '-' if conditions else ''
        if self.den <= 0:
            self.res = 'Error'
            self.reduced_num = 0
        else:
            self.int = abs(self.num) // abs(self.den)
            self.reduced_num = abs(self.num) % abs(self.den)
            if self.reduced_num == 0:
                self.res = -self.int if self.negative else self.int
            if abs(self.num) == abs(self.den):
                self.res = -1 if self.negative else 1
            if self.num == 0:
                self.res = 0

    def reduction(self):
        if abs(self.num) != abs(self.den):
            for com_factor in range(abs(self.num) if abs(self.num) < abs(self.den) else abs(self.den), 1, -1):
                if self.reduced_num % com_factor == 0 and self.den % com_factor == 0:
                    self.reduced_num //= com_factor
                    self.den //= com_factor if self.den > 0 else -(abs(self.den) // com_factor)
                    self.num //= com_factor if self.num > 0 else -(abs(self.num) // com_factor)

    def __add__(self, other):
        if isinstance(other, int):
            other = Fraction(a=other * self.den, b=self.den)
        if abs(self.den) == abs(other.den):
            sum_den = abs(self.den)
            sum_num = self.num + other.num
        else:
            sum_den = abs(self.den) * abs(other.den)
            sum_num = self.num * abs(other.den) + other.num * abs(self.den)
        result = Fraction(a=sum_num, b=sum_den)
        return result

    def __radd__(self, other):
        if isinstance(other, int):
            other = Fraction(a=other * self.den, b=self.den)
        if abs(self.den) == abs(other.den):
            sum_den = abs(self.den)
            sum_num = self.num + other.num
        else:
            sum_den = abs(self.den) * abs(other.den)
            sum_num = self.num * abs(other.den) + other.num * abs(self.den)
        result = Fraction(a=sum_num, b=sum_den)
        return result

    def __sub__(self, other):
        if isinstance(other, int):
            other = Fraction(a=other * self.den, b=self.den)
        if abs(self.den) == abs(other.den):
            sub_den = abs(self.den)
            sub_num = self.num - other.num
        else:
            sub_den = abs(self.den) * abs(other.den)
            sub_num = self.num * abs(other.den) - other.num * abs(self.den)
        result = Fraction(a=sub_num, b=sub_den)
        return result

    def __rsub__(self, other):
        if isinstance(other, int):
            other = Fraction(a=other * self.den, b=self.den)
        if abs(self.den) == abs(other.den):
            sub_den = abs(self.den)
            sub_num = other.num - self.num
        else:
            sub_den = abs(self.den) * abs(other.den)
            sub_num = other.num * abs(other.den) - self.num * abs(self.den)
        result = Fraction(a=sub_num, b=sub_den)
        return result

    def __mul__(self, other):
        if isinstance(other, int):
            mul_den = self.den
            mul_num = self.num * other
        else:
            mul_den = abs(self.den) * abs(other.den)
            mul_num = self.num * other.num
        result = Fraction(a=mul_num, b=mul_den)
        return result

    def __rmul__(self, other):
        if isinstance(other, int):
            mul_den = self.den
            mul_num = self.num * other
        else:
            mul_den = abs(other.den) * abs(self.den)
            mul_num = other.num * self.num
        result = Fraction(a=mul_num, b=mul_den)
        return result

    def __int__(self):
        if 0 < abs(self.num) < abs(self.den):
            return 0
        elif self.den <= 0:
            print('Error')
            return 0
        elif abs(self.num) > abs(self.den):
            return -self.int if self.negative else self.int
        else:
            return self.res

    def __float__(self):
        if self.den == 0:
            print('Error')
            return 0.0
        else:
            return self.num / self.den

    def __str__(self):
        self.reduction()
        if 0 < abs(self.num) < abs(self.den):
            return f"{self.negative}{self.reduced_num}{chr(0x2044)}{abs(self.den)}"
        elif abs(self.num) > abs(self.den):
            if self.reduced_num:
                return f"{self.negative}{self.int} {self.reduced_num}{chr(0x2044)}{abs(self.den)}"
            else:
                return str(self.res)
        else:
            return str(self.res)


fraction1 = Fraction(-3, 6)
# fraction2 = Fraction(-3, 6)
# fraction = fraction1 * fraction2

print(fraction1)
print(float(fraction1))