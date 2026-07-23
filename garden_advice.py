# User inputs the season and plant type, for plant advice.
season = input("What season are you working in?")
plant_type = input("What type of plant are you working with?")

# This variable holds the gardening advice to give to the user.
advice = ""

# This checks against the season the user specified
# and provides advice accordingly.
if season == "summer":
    advice += "Water your plants regularly and provide some shade.\n"
elif season == "winter":
    advice += "Protect your plants from frost with covers.\n"
else:
    advice += "No advice for this season.\n"

# This checks against the plant type the user specified
# and provided advice accordingly.
if plant_type == "flower":
    advice += "Use fertiliser to encourage blooms."
elif plant_type == "vegetable":
    advice += "Keep an eye out for pests!"
else:
    advice += "No advice for this type of plant."

# Print the generated advice
print(advice)

# TODO: Examples of possible features to add:
# - Add detailed comments explaining each block of code.
# - Refactor the code into functions for better readability and modularity.
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.
