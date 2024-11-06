lst = [1,1,1,2,2,2,3,4,4,5,5,5,6,6,7,7,8,8,8,9,9,]

set_comprehension = {n for n in lst}
print(set_comprehension)

# if statement
set_with_if = {n for n in lst if n%3==0}
print(set_with_if)