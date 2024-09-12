# Task 1

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
additional_equipment = "projector" if attendees > 100 else "audio system"

print(venue)
print(additional_equipment)

catering = input("Would you like vegetarian food? (yes/no): ").lower()

if catering == "yes":
    print("I would recommend Veggie Delight Caterers.")
elif catering == "no":
    print("I would recommend Gourmet Meals Caterers.")
else:
    print("Invalid option, please choose yes or no.")
