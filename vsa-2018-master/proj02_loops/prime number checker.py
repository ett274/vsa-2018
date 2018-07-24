import math

def solution(n):
    numerals = []
    while n > 0:
        first_digit = n // 10 ** (int(math.log(n, 10))
        if n >= 1000:
            numerals.append('M')
            n -= 1000
        elif n >= 900 and first_digit == 9:
            numerals.append('CM')
            n -= 900
        elif n >= 500:
            numerals.append('D')
            n -= 500
        elif n >= 400 and first_digit == 4:
            numerals.append('CD')
            n -= 400
        elif n >= 100:
            numerals.append('C')
            n -= 100
        elif n >= 90 and first_digit == 9:
            numerals.append('XC')
            n -= 90
        elif n >= 50:
            numerals.append('L')
            n -= 50
        elif n >= 40 and first_digit == 4:
            numerals.append('XL')
            n -= 40
        elif n >= 10:
            numerals.append('X')
            n -= 10
        elif n == 9:
            numerals.append('IX')
            n -= 9
        elif n == 5:
            numerals.append('V')
            n -= 5
        elif n == 4:
            numerals.append('IV')
            n == 4
        elif n >= 1:
            numerals.append('I')

    return ''.join(numerals)