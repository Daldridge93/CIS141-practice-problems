'''
#1. Create a file called gardening_tips.txt and add at least 3 gardening tips to it.
    Write a Python script that reads a file gardening_tips.txt and prints
    out each tip one by one.
'''

with open("gardening_tips.txt", "r") as file:
    for line in file:
        print(line)
    content = file.read()
print(content)


'''
#2. Write a Python program that allows users to log their hiking trips. The program should:
    - Use a while loop to repeatedly ask for a hike name and distance in miles
    - Save each entry to hiking_log.txt (each hike on a new line)
    - When the user presses 0, exit the loop & print the contents of hiking_log.txt
'''

file = open("hiking_log.txt", "w")
file.write("")
file.close()

file = open("hiking_log.txt", "a")

while True:
    name = input("What is the hikers name? ")
    if name == "0":
        break
    miles = input("How many miles were hiked? ")
    if miles == "0":
        break
    file.write(name + "\t" + miles + "\n")
file.close()


'''
#3. Create a text file called song_lyrics.txt and copy the lyrics of a song into it. Write a Python program that:
    - Reads the file
    - Requests 5 inputs from the user: 5 words the user would like to count the frequency of
    - Counts how many times each word appears
    - Creates a dictionary of the words and their counts
    - Print the dictionary to the console
'''


file = open("song_lyrics.txt", "r")
lyrics = file.read()
file.close()

lyrics = lyrics.lower()

words_to_count = []
for i in range(5):
    word = input(f"Enter word {i+1} to count: ").lower()
    words_to_count.append(word)


word_counts = {}
for word in words_to_count:
    count = lyrics.split().count(word)
    word_counts[word] = count

print("\nWord count:")
print(word_counts)



'''
#4. Create a poll.txt file that contains a list of "yea" or "nay" votes separated by commas.
    Write a program that reads the poll.txt file
    Count how many votes "yea" or "nay" received and print the results.
'''


with open("poll.txt", "r") as file:
    votes = file.read()


votes_list = votes.split(",")

yea_count=0
nay_count=0

for vote in votes_list:
    vote = vote.strip()
    if vote == "yea":
        yea_count+=1
    elif vote == "nay":
        nay_count+=1

print("Yea votes:", yea_count)
print("Nay votes:", nay_count)

