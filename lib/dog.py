#!/usr/bin/env python3

# List of approved breeds
APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="Unknown", breed="Unknown"):
        self._name = None
        self._breed = None
        self.name = name  # Using the setter for name
        if self._name:  # Only proceed to breed if name is valid
            self.breed = breed  # Using the setter for breed

    # Name property
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0 or len(value) > 25:
            print("Name must be string between 1 and 25 characters.")
        else:
            self._name = value

    # Breed property
    @property
    def breed(self):
        return self._breed
    
    @breed.setter
    def breed(self, value):
        if value not in APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
        else:
            self._breed = value

    def sit(self):
        print(f"{self._name} is sitting.")

    def get_breed(self):
        return self._breed