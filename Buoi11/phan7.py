character = {
    "Name": "Light",
    "Age": 17,
    "Strength": 8,
    "Defense": 10,
    "HP": 100,
    "Backpack": ["Shield", "Bread Loaf"],
    "Gold": 100,
    "Level": 2,
}

skills = [
    {"Name": "Tackle", "Minimum level": 1, "Damage": 5, "Hit rate": 0.3},
    {"Name": "Quick Attack", "Minimum level": 2, "Damage": 3, "Hit rate": 0.5},
    {"Name": "Strong Kick", "Minimum level": 4, "Damage": 9, "Hit rate": 0.2},
]

i = 0
while (i < len(skills)):
    print("Skill " + str(i + 1) + ": " + skills[i]["Name"])
    i += 1

choosen_skill = int(input("Choose skill by number:")) - 1

# Bai 1 phan 8
if (character["Level"] < skills[choosen_skill]["Minimum level"]):
    print("Cannot deploy. Required level" + str(skills[choosen_skill]["Minimum level"]))
else:
    print("Damage: " + str(skills[choosen_skill]["Damage"]))


# Bai 2 phan 8
import random
rate = random.random() #0.0033

print(rate)
if (rate > skills[choosen_skill]["Hit rate"]):
    print("Cannot deploy")
else:
    print("Damage: " + str(skills[choosen_skill]["Damage"]))