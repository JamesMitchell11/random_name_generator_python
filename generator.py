import random

def generate_random_name(length=8):
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"

    name = random.choice(consonants).capitalize()

    for _ in range(length - 2):
        name += random.choice(vowels + consonants)

    return name

if __name__ == "__main__":
    num_names = 5  # You can adjust the number of random names generated

    for _ in range(num_names):
        print(generate_random_name())
