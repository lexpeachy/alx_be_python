# Ask the user to input the current weather from a predefined set of conditions: sunny, rainy, or cold.
current_weather = (input("what's the weather like today? (sunny/rainy/cold):")).lower()
# Based on the user’s input, the program will recommend different types of clothing
if current_weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif current_weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif current_weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")