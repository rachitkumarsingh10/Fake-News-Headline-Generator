import random

subjects = [
    "Shahrukh Khan", "Salman Khan", "Aamir Khan", "A Mumbai Cat", "Prime Minister",
    "Auto Rickshaw Driver from Mumbai", "Mumbai Local Train", "Virat Kohli", "Sunil Chetri",
    "An Indian Farmer", "A Street Vendor", "A Bollywood Dancer", "A Cricket Umpire",
    "A Yoga Instructor", "A Bollywood Director", "A Tech Startup CEO", "A College Student",
    "A School Teacher", "An IT Professional", "A Traffic Police Officer", "A Taxi Driver",
    "A News Reporter", "A Street Musician", "A Film Producer", "An Author",
    "A Marathon Runner", "A Chef", "A Photographer", "A DJ", "A Software Developer",
    "An Archaeologist", "A Pilot", "A Doctor", "A Nurse", "A Firefighter",
    "A Police Officer", "A Librarian", "A Fashion Designer", "A Carpenter",
    "A Plumber", "A Mechanic", "A Shopkeeper", "A Lawyer", "A Judge",
    "A Scientist", "A Historian", "A Student Leader", "A Social Activist",
    "A Wildlife Photographer", "A Park Ranger", "A Taxi Passenger", "A Street Cleaner"
]

actions = [
    "is eating", "is dancing", "is singing", "orders", "is playing", "is driving",
    "is running", "is flying", "is jogging", "is studying", "is cooking",
    "is shopping", "is painting", "is meditating", "is laughing", "is reading",
    "is teaching", "is writing", "is chatting", "is swimming", "is hiking",
    "is gardening", "is fishing", "is cycling", "is photographing", "is repairing",
    "is knitting", "is volunteering", "is cleaning", "is collecting", "is sketching",
    "is experimenting", "is presenting", "is debating", "is exploring", "is tweeting",
    "is blogging", "is coding", "is rehearsing", "is directing", "is producing",
    "is driving a rickshaw", "is selling vegetables", "is making coffee", "is delivering",
    "is booking tickets", "is organizing an event", "is fixing a car", "is checking emails", "is answering calls"
]

places_of_things = [
    "at Red Fort", "at Gateway of India", "at Marine Drive", "at India Gate", "at CST Station",
    "at Bandra Bandstand", "at Juhu Beach", "at Chhatrapati Shivaji Maharaj Terminus",
    "at Delhi Airport", "at Connaught Place", "at Lalbagh Botanical Garden", "at Victoria Memorial",
    "at Haji Ali Dargah", "at Qutub Minar", "at Charminar", "at Mysore Palace",
    "at Cubbon Park", "at India Habitat Centre", "at Salt Lake City", "at Birla Mandir",
    "at Kamala Nehru Park", "at Marine Lines", "at Worli Sea Face", "at Versova Beach",
    "at Elephanta Caves", "at Sion Fort", "at Girgaum Chowpatty", "at Mahim Beach",
    "at Bandra Worli Sea Link", "at Powai Lake", "at Sanjay Gandhi National Park",
    "at Lalbaug Market", "at Chor Bazaar", "at Film City", "at Nehru Planetarium",
    "at Jantar Mantar", "at Lotus Temple", "at Humayun's Tomb", "at Rashtrapati Bhavan",
    "at Parliament House", "at Rajpath", "at India Gate Lawns", "at Gandhi Smriti",
    "at Hauz Khas Village", "at Dilli Haat", "at Cyber Hub", "at Sector 18 Market",
    "at Connaught Place Metro Station", "at Delhi University", "at IIT Bombay", "at Mumbai University"
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
