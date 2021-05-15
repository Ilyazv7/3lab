num = str(input())

gcd = lambda a, b: a if not b else gcd(b, a % b)
int_n, frac_n = num.split('.')
frac_n1, frac_n2 = frac_n[:-1].split('(')

d = int('9' * len(frac_n2))
frac = (int(frac_n1) * d if frac_n1 else 0) + int(frac_n2)
denom = d * (10 ** len(frac_n1))

g = gcd(frac, denom)
print("Целая часть: ", int_n, " Числитель: ", frac // g, "Знаменатель: ", denom // g)