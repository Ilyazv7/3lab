from fractions import Fraction

a = input('Введите числитель первой дроби:')
b = input('Введите знаменатель первой дроби:')
firstper = Fraction(int(a), int(b))

a2 = input('Введите числитель второй дроби:')
b2 = input('Введите знаменатель второй дроби:')
secondper = Fraction(int(a2), int(b2))
plus = firstper + secondper
minus = firstper - secondper
composition = firstper * secondper
division = firstper / secondper
remains = firstper % secondper
print("Сумма рациональный чисел:",plus,"\nРазность рациональный чисел:",minus,"\nПроизведение рациональный чисел:",composition,
"\nДеление рациональный чисел:", division,"\nОстаток от деления рациональный чисел:",remains)
#Предполагается, что firstper имеет большее влияние, чем secondper