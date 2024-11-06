from string import ascii_letters

my_dict = {'a': 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6}

square_values = {k:v**2 for (k,v) in my_dict.items()}
print(square_values)

ascii_dict = {char: bin(ord(char)) for char in ascii_letters}
print(ascii_dict)

modulo_dict = {k:k**2 for k in range(10) if k%2==0}
print(modulo_dict)

farenheit_dict = {"temp1": 10, "temp2": 20, "temp3: 30":30, "temp4": 40}
celsius_dict = {k:(float(5)/9) * (v-32) for (k,v) in farenheit_dict.items()}
print(celsius_dict)


#if statement inside dict
print({k:v for (k,v) in my_dict.items() if v>3})
odd_numbers = {k:("even number" if v%2==0 else "Odd number") for (k,v) in my_dict.items()}
print(odd_numbers)

# multiple if conditions
filtered = {k:v for (k,v)in my_dict.items() if v>3 if v%2 == 0}
print(filtered)

nested_dict = {'a': {'one': 10}, 'b': {'two': 20}, 'c': {"three": 30}}
