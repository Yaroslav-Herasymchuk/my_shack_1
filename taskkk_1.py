Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>>
import re
str = input("Введіть рядок: ")
rd = re.findall(r'\d+', str)
str = re.sub(r"\d+", "", str, flags=re.UNICODE)
rd = [int(i) for i in rd]
print("Рядок без чисел:\n", str, sep='')
def function(str):
    str, result = str.title(), ""
    for word in str.split():
        result += word[:-1] + word[-1].upper() + " "
    return result[:-1]
print("\nЗаміна букв:\n", function(str), sep='')
print("Масив чисел з рядка:\n", rd, sep='')
maxNomer = max(rd)
index = rd.index(maxNomer)
print("\nМаксимальне число:", maxNomer)
mass = []
for i in range(len(rd)):
    if rd[i]!= max(rd):
        mass.append(pow(rd[i],i))
print(" Числа піднесені до степеня:\n", mass, sep='')
