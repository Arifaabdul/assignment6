# Task: Explore in Google and Make a document :

# 1. Why we use loops?
'''Loops are a programming element that repeat a portion of code a set number of times until the desired process is complete. 
Repetitive tasks are common in programming, and loops are essential to save time and minimize errors.'''

# 2 What is while loop?
'''A "While" Loop is used to repeat a specific block of code an unknown number of times, until a condition is met. 
For example, if we want to ask a user for a number between 1 and 10, we don't know how many times the user may enter a larger number, 
so we keep asking "while the number is not between 1 and 10". 
If we (or the computer) knows exactly how many times to execute a section of code (such as shuffling a deck of cards) we use a for loop.'''

# 3. What is iterator in loop?
'''An Iterator is an object that can be used to loop through collections, like ArrayList and HashSet. 
It is called an "iterator" because "iterating" is the technical term for looping.'''

# 4. What is increment in loop?
'''Increment is an expression that determines how the loop control variable is incremented each time the loop repeats successfully 
(that is, each time condition is evaluated to be true).'''

# 5. why we use range function?
'''Whenever an action needs to be performed a certain number of times, 
then you must make use of range in Python to generate a sequence of numbers within a given range. 
The range() function is used in loops like for loop, while loop etc. to iterate through the sequences.'''

# 6. Create a list(friend_names) with your friends names(atleaste 10 names)?
# print all names with in loop 
# Expected Output: my friend name is "ravi"
# 		     my friend name is "shanker"
friend_names=["Lalitha","Mounika","Harsha","SaiLakshami","Supriya","Bindu","Anusha","Sowmya","Raji","Kamala"]
def friendNames(friend_names):
    for friends in friend_names:
        print("my friend name is",friends)
friendNames(friend_names)

# 7. Create a list(family_members) with your family members names(atleaste 10 names)?
# print all names with in loop
family_members=["Samad", "Aktharunnisa", "Anwar","Arifa", "Asma", "Sheerin", "Azeem", "Fareed", "Fazeelath", "Ayaan"]
for a in family_members:
    print(a)    


# 8. Create a list(food_names) with your favorite food names(atleaste 10 names only veg)?
# print all names with in loop 
food_names=["Veg Biryani","Veg Manchurian","Veg FriedRice","Veg Salad", "Palak Paneer", "Mattar Paneer", "Gobi Manchurian", "Dal Makhani",
            "Pav Bhaji", "Paneer Tikka Masala"]
for p in food_names:
    print(p)

# 9. Create a tuple(food_names) with your favorite food names(atleaste 10 names only nonveg)?
# print all names with in loop 
food_names=("Mutton Biryani","Chicken Biryani","Chicken Manchurian","Chicken Tikka","Keema Matar","Haleem","Prawns Biryani","Butter Chicken",
            "Fish Biryani","Mutton Kabaab")
for nonveg in food_names:
    print(nonveg)

# 10. Create a set(colour_names) with your colour names(atleaste 10 names)?
# print all names with in loop 
colour_names={"Red","Green","Yellow","Pink","Blue","Maroon","Purple","Orange","Gray","Brown"}
for col in colour_names:
    print(col)

# 11. Create a list(month_names) with your month names(atleaste 10 names)?
# print all names with in loop 
month_names=["January","February","March","April","May","June","July","August","September","October"]
for month in month_names:
    print(month)

# 12. print 9th table (1 to 90)
for t in range(9,91,9):
    print(t)

# 13. print(12th table (1 to 120)
for table in range(12,121,12):
    print(table)
