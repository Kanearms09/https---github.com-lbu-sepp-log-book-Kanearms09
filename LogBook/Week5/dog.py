class dog:

    def __init__(self, name, breed, score):

        self.name = name
        self.breed = breed
        self.score = score

    def display_details(self):
        return f"Name: {self.name}, Breed: {self.breed}, Score: {self.score}"

dog1 = dog('Pierre', 'GreyHound', 15)
dog2 = dog('Pascal', 'Bulldog', 12)
dog3 = dog('Pedro', 'Patterdale', 20)

dogs = [dog1, dog2, dog3]





magic_dog_arranger = sorted(dogs, key = lambda dog: dog.score, reverse = True)

print("Dogs sorted by score: ")
for dog in magic_dog_arranger:
    print(dog.display_details())
