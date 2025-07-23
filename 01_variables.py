print("hello world")
#Practicing user input and output 💬

name = input("What's your name? ")
age = input("How old are you? ")

print("Nice to meet you, " + name + "!")
print("You are " + age + " years old.")

# Let's make it more fun and interactive

hobby = input("What's your favorite hobby? ")
food = input("What's your favorite food? ")

print("\nSummary of your responses:")
print("- Name: " + name)
print("- Age: " + age)
print("- Hobby: " + hobby)
print("- Favorite Food: " + food)

# Conditional message based on age
if int(age) < 18:
    print("Wow, you're quite young and already coding!")
else:
    print("That's awesome! It's never too late to learn.")

# Fun interaction
print(f"\n{name}, imagine coding while enjoying {food} and thinking about {hobby} 😄")
