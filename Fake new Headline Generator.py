import random

subjets = [
    "Shahruk Khan",
    "Salman Khan",  
    "Aamir Khan",
    "A Mumbai Cat",
    "Prime Minister",
    "Auto Rickshaw Driver from Mumbai",
    "Mumbai Local Train",
    "Virat Kohli",
    "Sunil Chetri"
   
]


actions = [
    "is eating",
    "is dancing",
    "is singing",
    "orders",
    "is playing",
    "is driving",
    "is running",
    "is flying"
]

places_of_things=[
    "at Red Fort",
    "at Gateway of India",    
    "at Marine Drive",
    "at India Gate",    
    "at CST Station",
    "at Bandra Bandstand",
    "at Juhu Beach",
    "at Chhatrapati Shivaji Maharaj Terminus",
    "at Delhi Airport"
]

while True:
    subject = random.choice(subjets)
    action = random.choice(actions)
    place_of_thing = random.choice(places_of_things)

    print("\nBreaking News: ")
    print(f"{subject} {action} {place_of_thing}")
    
    if input("Press Enter to continue or type 'exit' to quit: ").strip().lower() == 'exit':
        break


print("Thank you for using the Fake News Headline  generator!")
print("Have a great day!")
