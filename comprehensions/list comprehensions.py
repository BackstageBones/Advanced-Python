#squares practice

squares= [n**2 for n in range(1,6)]
print(squares)

# intersection
lst1 = [1,2,3,4,5,6,7,8,9]
lst2 = [3,5,6,7,9]

intersection = [n for n in lst1 for y in lst2 if n==y]
print(intersection)

outer_section = [n for n in lst1 if n not in lst2]
print(outer_section)

non_common_elements = [(x,y) for x in lst1 for y in lst2 if x!=y]
print(non_common_elements)

capital_letters = ["Hello World", "Python", "Java"]
str_normalized = [string.lower() for string in capital_letters]
print(str_normalized)

cubes = [(n**2, n**3) for n in lst1]
print(cubes)

#lambda expressions
lam_square = list(map(lambda x: x**2, lst1))
print(lam_square)

lam_intersection = list(filter(lambda x: x in lst2, lst1))
print(lam_intersection)

def square_root(a: int):
    return  a**2

print([square_root(x) for x in range(10)])