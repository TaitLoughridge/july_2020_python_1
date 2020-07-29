# pets_names = ["Ash", "King", "Gigi", "Yasu"]
#########
# # count = 0

# # while count < len(pets_names):
# #     print(pets_names[count])
# #     count += 1
#########
# print(len(pets_names))
# print(pets_names[0])
#########
# pet_names = []
# print(pet_names)

# pet_names.append("Ash")
# pet_names.append("King")
# pet_names.append("Gigi")
# print(pet_names)

# pet_names.append("Yasu")
# print(pet_names)
#########

# for every [needle] in a [haystack]
pets_names = ["Ash", "King", "Gigi", "Yasu"]

count = 0
# print("WHIAL LOOP")
# while count < len(pets_names):
#     print(pets_names[count])
#     count += 1

print("FOR LOOP")
for animal in pets_names:
    print(animal)
    if animal == "King":
        break