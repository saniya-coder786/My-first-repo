print("hello world")
#Practicing user input and output 💬

name = input("What's your name? ")
age = input("How old are you? ")

print("Nice to meet you, " + name + "!")
print("You are " + age + " years old.")

# next step practice python 

hobby = input("What's your favorite hobby? ")
food = input("What's your favorite food? ")
#\n used for next line.
print("\nSummary of your responses:")
print("- Name: " + name)
print("- Age: " + age)
print("- Hobby: " + hobby)
print("- Favorite Food: " + food)

# next topic Conditional statement
if int(age) < 18:
    print("Wow, you're quite young and already coding!")
else:
    print("That's awesome! It's never too late to learn.")

# f-string applied
print(f"\n{name}, imagine coding while enjoying {food} and thinking about {hobby} 😄")
