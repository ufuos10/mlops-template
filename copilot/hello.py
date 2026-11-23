# build a random list of fruit
import random

fruits = [
    "apple",
    "banana",
    "cherry",
    "date",
    "elderberry",
    "fig",
    "grape",
    "honeydew",
    "kiwi",
    "lemon",
    "mango",
    "nectarine",
    "orange",
    "papaya",
    "quince",
    "raspberry",
    "strawberry",
    "tangerine",
    "ugli fruit",
    "watermelon",
]


# build a for loop that prints out each fruit in the list with a running number and a colon with the fruit name
for i, fruit in enumerate(fruits):
    print(f"{i + 1}: {fruit}")