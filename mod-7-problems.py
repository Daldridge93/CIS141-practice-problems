'''
#1. Write a function called count_vowels(input) that takes a string
    and returns the number of vowels (a, e, i, o, u) in it.
'''
#Test: Demasha (3), forest (2)
#input: string (cv)
#output: count
#Function body: lowercase cv, all vowels as a variable, set up counter with for loop. use return to get count.

'''def count_vowels(cv):
    cv = cv.lower()
    vowels = "aeiou"
    count = 0
    for char in cv:
        if char in vowels:
            count +=1
    return count

print(count_vowels("Demasha"))
print(count_vowels("forest"))'''

'''
#2. Write a function called is_palindrome(s) that checks whether a string is a palindrome
    (reads the same forward and backward, ignoring case). The function should returns
    either True or False.
'''
#Test: racecar (True), pikachu (False), Racecar (True)
#Input: string (s)
#Output: boolean
#Function body: lowercase s, flip s and save to new variable(flipped_s), an then compare s & flipped_s
'''def is_palindrome(s):
    lower_s = s.lower()
    flipped_s = lower_s[::-1]
    return lower_s == flipped_s

print(is_palindrome("racecar"))
print(is_palindrome("pikachu"))
print(is_palindrome("Racecar"))'''

'''
#3. In the game Pokemon, certain types of Pokemon do extra damage to other types.
    For example, water is very effective to fight fire.
    Write a function called type_advantage(attacker, defender) that takes two Pokémon types as
    strings and returns "Super Effective", "Not Very Effective", or "Neutral" based on
    simple type effectiveness rules. Your solution only needs to work for these three sets of input:
    print(type_advantage("Water", "Fire"))  # "Super Effective"
    print(type_advantage("Fire", "Water"))  # "Not Very Effective"
    print(type_advantage("Electric", "Grass"))  # "Neutral"
'''
#Test: input attacker vs. defender  = effectiveness
#input: string
#output: string
#Function body: else and elif statements providing effectiveness. use return to determine effectiveness.
'''
def type_advantage(attacker,defender):
    if attacker == "Water" and defender == "Fire":
        return "Super Effective"
    elif attacker == "Fire" and defender == "Water":
        return "Not Very Effective"
    elif attacker == "Electric" and defender == "Grass":
        return "Neutral"

print(type_advantage("Water", "Fire"))  # "Super Effective"
print(type_advantage("Fire", "Water"))  # "Not Very Effective"
print(type_advantage("Electric", "Grass"))  # "Neutral"
'''
'''
#4. Write a function called ferry_fare(age, vehicle) that calculates the Washington State Ferry fare
    based on age and whether the person has a vehicle. Assume the following rates:
    * Adults (19-64): $10 without a vehicle, $20 with a vehicle.
    * Seniors (65+): $5 without a vehicle, $15 with a vehicle.
    * Children (0-18): Free.
'''
#Test: age will determine cost with or without vehicle using true/false.
#Input:int & boolean
#Output: int
#Function body: if, elif, else statements that capture age and if vehicle. use return to display correct price.
'''def ferry_fare(age,vehicle):
    if age >= 19 and age <= 64:
        if vehicle:
            return 20
        else:
            return 10


    elif age >= 65:
        if vehicle:
            return 15
        else:
            return 5

    elif age >= 0 and age <= 18:
        return "free"

print(ferry_fare(70, True))
print(ferry_fare(20, False))'''
'''
#5. Write a function called level_up(experience) that takes a player's experience points
    and returns their new level based on these rules:
    * 0-99 XP → Level 1
    * 100-199 XP → Level 2
    * 200+ XP → Level 3
'''
#Test: xp entered determines certain level
#input: int
#output: string
#function body: utilize if and elif statements. capture xp in ranges and determine level with a return.
'''def level_up(experience):
    if experience >=0 and experience <= 99:
        return "Level 1"

    elif experience >=100 and experience <= 199:
        return "Level 2"

    elif experience >=200:
        return "Level 3"

print(level_up(199))'''
