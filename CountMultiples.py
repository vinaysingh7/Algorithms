"""[summary] Sum of all multiples is S(1000, 3) + S(1000, 5) - S(1000, 15)
"""
def count_multiples(n):
    return arithmetic_progression_sum(1000, 3) + arithmetic_progression_sum(1000, 5) - arithmetic_progression_sum(1000, 15)

""" Applying Arithmetic Progression formula to get sum of all multiples of a number
    Sn = n/2 * (a1 + an)
"""
def arithmetic_progression_sum(last, num):
    return ((last//num)/2)*(num + last-(last%num))
print(count_multiples(1000))
