from itertools import permutations

num = ['0', '2', '3', '4', '5', '6', '7', '8', '9']
contact_numbers = []
count = 0

for i in permutations(num, 5):
    contact_numbers.append('98765' + ''.join(i))
    count += 1
with open("contact.txt", 'w') as file:
    
    for i in contact_numbers:
        file.write(i + "\n")
print("Total count:", count)