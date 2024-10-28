import random

jokes = [
    "Why did the samosa go to school? Because it wanted to be a little 'patt'!",
    "Why don’t Indians ever play hide and seek? Because good luck hiding when everyone’s honking at the traffic!",
    "Why do Indian parents love arranged marriages? Because they can finally get a 'better half' without compromising on the 'half'!",
    "Why did the cousin come to the wedding? Because he heard there would be free food!",
    "Why did the biryani break up with the pulao? Because it found someone more 'spiced up'!",
    "Why did the cricket player bring string to the game? To tie the score!",
    "Why do Indian IT professionals always carry a ladder? Because they always want to reach the next level!",
    "What do you call an Indian festival that never ends? A 'Diwali' with too many sweets!",
    "Why don’t trains ever get lost in India? Because they always follow the 'track' of their life!",
    "Why did the chai refuse to work? Because it couldn’t find a 'cup' of motivation!"
]

def tell_joke():
    return random.choice(jokes)

def main():
    print("Welcome to the Random Joke Generator!")
    while True:
        user_input = input("\nPress Enter to hear a joke or type 'exit' to quit: ")
        if user_input.lower() == 'exit':
            print("Thanks for laughing with us! Goodbye!")
            break
        else:
            print("\nHere's a joke for you:")
            print(tell_joke())

if __name__ == "__main__":
    main()
