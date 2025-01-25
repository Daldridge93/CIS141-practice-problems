'''1. Prompt the user for a word. Then, prompt the user for how many times
they'd like that word repeated. Use the skills you learned in this module to
print the word the correct number of times.'''

strg1 = input("Provide me a word:")
strg2 = int(input("How many times would you like me to repeat that?"))
print((strg1 + "\n") * strg2)

'''2. Prompt the user for their name and their age. Calculate their age next year. Use string concatenation to
print "Hello, <name>! You are <age1> years old. Next year, you will be <age2> years old."'''

name = input("Hello, What is your name? ")
age1 = int(input("How old are you?"))
age2 = (age1 + 1)
print(f"Hello, {name}! You are {age1} years old. Next year, you will be {age2} years old.")

'''#3. Prompt the user for a sentence and a word to try to find in that sentence.
Have the program print out whether the word was found in the sentence. (i.e. True or False)'''

sentence = input("Please provide a sentence: ")
word = input("Please provide a word you would like to find in that sentence: ")

print("Is the word in the sentence? ",word in sentence)


'''#4. Prompt the user for: a word, a first index, and a last index.
Slice the word at the indexes provided by the user and print to the screen.'''

word2 = input("Please provide a word: ")
index1 = int(input("Please provide the first index: "))
index2 = int(input("Please provide the first index: "))

print(word2[index1:index2])

'''#5. Print 3 words with a | character (called a pipe) in between them.
Use the appropriate keyword argument in print() to do so.'''

sen1 = "This"
sen2 = "is"
sen3 = "cool"
print(sen1, sen2, sen3, sep= " | ")
