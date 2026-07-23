# Dictionary including advice for each season.
season_advice = {
    "summer": "Water your plants regularly and provide some shade.\n",
    "winter": "Protect your plants from frost with covers.\n",
    "spring": "Watch for weeds and start planting new seeds.\n",
    "autumn": "Clear fallen leaves and prepare soil for winter.\n",
}

# Dictionary including advice for the plant type.
plant_advice = {
    "flower": "Use fertiliser to encourage blooms.",
    "vegetable": "Keep an eye out for pests!",
    "herb": "Trim regularly to encourage growth.",
}

# Inputs requiring the user to input the season they're
# working with, as well as the plant type.
season = input("Enter the season: ").lower()
plant_type = input("Enter the plant type: ").lower()

# Build the advice for the season and plant type, and
# stores it in the 'advice' variable.
advice = season_advice.get(season, "No advice for this season.\n")
advice += plant_advice.get(plant_type, "No advice for this type of plant.")

print(advice)

# TODO: Examples of possible features to add:
# - Add detailed comments explaining each block of code.
# - Refactor the code into functions for better readability and modularity.
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.
