names = ["Python","Olympic","Dog","College","School","Sun","Olympic"]
numbers = [30, 54, 67, 23, 74, 92, 10]
numbers2 = [30, -54, 67, -23, 74, -92, 10]

#1. Given a list of numbers, write code to iterate through the list and
#calculate the sum of all even numbers. Print the resulting sum.

even_num = 0

for number in numbers:
    if number % 2 == 0:
        even_num += number

print(even_num)

#2. With a list of strings provided, write code that counts how
#many times the word "Olympic" appears in the list, and then print the count.

count = 0

for word in names:
    if word == "Olympic":
        count += 1

print(count)

#3. Given a list of strings, write code to create a new list that includes
#only the strings longer than three characters. Print the resulting filtered list.

names1 = []
for name in names:
    if len(name) > 3:
        names1.append(name)
print(names1)

#4. For a list of integers, write code that counts how
#many numbers are positive and how many are negative, then print both counts.

positve = 0
negative = 0

for num in numbers2:
    if num > 0:
        positve +=1
for num in numbers2:
    if num < 0:
        negative +=1
print(positve)
print(negative)

#5. For a list of integers, use a loop to build a new list where
#each element is the square of the corresponding element in the original list. Print the new list.

square = []

for sqr in numbers:
    square.append(sqr ** 2)

print(square)
