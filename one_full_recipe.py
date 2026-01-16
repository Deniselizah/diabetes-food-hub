# from bs4 import BeautifulSoup
# import json
# import requests

# # URL of the recipe page
# url = "https://diabetesfoodhub.org/recipes/turkey-sausage-and-egg-casserole"
# response = requests.get(url)
# soup = BeautifulSoup(response.content, "html.parser")

# # Extracting the recipe title
# title_tag = soup.find("h1", class_="recipe-hero__headline")
# title = title_tag.find("span").get_text(strip=True) if title_tag else "Title not found"

# # Extracting the recipe description
# description_tag = soup.find("div", class_="dfh-recipe-desc")
# description = description_tag.find("p").get_text(strip=True) if description_tag else "Description not found"

# # Extracting preparation, cook time, and servings
# prep_time_tag = soup.find("div", class_="recipe-preparation-time")
# prep_time = (
#     prep_time_tag.find("span").get_text(strip=True) if prep_time_tag else "N/A"
# )
# cook_time_tag = soup.find("div", class_="recipe-cook-time")
# cook_time = (
#     cook_time_tag.find("span").get_text(strip=True) if cook_time_tag else "N/A"
# )
# servings_tag = soup.find("div", class_="recipe-servings")
# servings = servings_tag.find("span").get_text(strip=True) if servings_tag else "N/A"

# # Extracting recipe steps
# steps_section = soup.find("ol", class_="recipe-steps")
# steps = [li.get_text(strip=True) for li in steps_section.find_all("li")] if steps_section else []

# # Extracting tags
# tags_section = soup.find("div", class_="recipe-tags-section")
# tags = [a.get_text(strip=True) for a in tags_section.find_all("a")] if tags_section else []

# # Extracting ingredients
# ingredients_section = soup.find("div", class_="ingredients-facts-section")
# ingredients = []
# if ingredients_section:
#     for ingredient in ingredients_section.find_all("div", class_="ingredient-wrapper"):
#         label = ingredient.find("div", class_="ingredient-label").get_text(strip=True)
#         us_measure = ingredient.find("div", class_="ingredient-us").get_text(strip=True)
#         metric_measure = ingredient.find("div", class_="ingredient-metric").get_text(strip=True)
#         ingredients.append({
#             "label": label,
#             "us_measure": us_measure,
#             "metric_measure": metric_measure
#         })

# # Extracting nutrition facts
# nutrition_section = soup.find("div", class_="nutrition-facts-section")
# nutrition_data = {}

# if nutrition_section:
#     # Extracting servings
#     servings_tag = nutrition_section.find("span", class_="js-servings-label")
#     servings = servings_tag.get_text(strip=True) if servings_tag else "N/A"

#     # Extracting serving size
#     serving_size_tag = nutrition_section.find("div", itemprop="servingSize")
#     serving_size = serving_size_tag.get_text(strip=True) if serving_size_tag else "N/A"
    
#     # Extracting Amount per Serving (Calories)
#     calories_tag = nutrition_section.find("span", itemprop="calories")
#     calories = calories_tag.get_text(strip=True) if calories_tag else "N/A"

#     # Extracting total fat, saturated fat, and trans fat
#     total_fat_tag = nutrition_section.find("span", itemprop="fatContent")
#     total_fat = total_fat_tag.get_text(strip=True) if total_fat_tag else "N/A"
#     saturated_fat_tag = nutrition_section.find("span", itemprop="saturatedFatContent")
#     saturated_fat = saturated_fat_tag.get_text(strip=True) if saturated_fat_tag else "N/A"
#     trans_fat_tag = nutrition_section.find("span", itemprop="transFatContent")
#     trans_fat = trans_fat_tag.get_text(strip=True) if trans_fat_tag else "N/A"

#     # Extracting cholesterol and sodium
#     cholesterol_tag = nutrition_section.find("span", itemprop="cholesterolContent")
#     cholesterol = cholesterol_tag.get_text(strip=True) if cholesterol_tag else "N/A"
#     sodium_tag = nutrition_section.find("span", itemprop="sodiumContent")
#     sodium = sodium_tag.get_text(strip=True) if sodium_tag else "N/A"

#     # Extracting total carbohydrates, dietary fiber, total sugars, added sugars
#     total_carbohydrate_tag = nutrition_section.find("span", itemprop="carbohydrateContent")
#     total_carbohydrate = total_carbohydrate_tag.get_text(strip=True) if total_carbohydrate_tag else "N/A"
#     dietary_fiber_tag = nutrition_section.find("span", itemprop="fiberContent")
#     dietary_fiber = dietary_fiber_tag.get_text(strip=True) if dietary_fiber_tag else "N/A"
#     total_sugars_tag = nutrition_section.find("span", itemprop="sugarContent")
#     total_sugars = total_sugars_tag.get_text(strip=True) if total_sugars_tag else "N/A"
#     added_sugars_tag = nutrition_section.find("span", itemprop="addedSugarContent")
#     added_sugars = added_sugars_tag.get_text(strip=True) if added_sugars_tag else "N/A"

#     # Extracting protein
#     protein_tag = nutrition_section.find("span", itemprop="proteinContent")
#     protein = protein_tag.get_text(strip=True) if protein_tag else "N/A"

#     # Extracting Potassium and Phosphorus (adjusted for structure)
#     potassium_tag = nutrition_section.find("strong", text="Potassium")
#     potassium = potassium_tag.find_next_sibling(text=True).strip() if potassium_tag else None
    
#     phosphorus_tag = nutrition_section.find("strong", text="Phosphorous")
#     phosphorus = phosphorus_tag.find_next_sibling(text=True).strip() if phosphorus_tag else None

#     # Constructing the nested JSON for nutrition facts
#     nutrition_data = {
#         "Nutrition Facts": {
#             "Servings": servings,
#             "Serving Size": serving_size,
#             "Amount per Serving": {
#                 "Calories": calories,
#                 "Total Fat": {
#                     "Amount": total_fat,
#                     "Saturated Fat": saturated_fat,
#                     "Trans Fat": trans_fat if trans_fat != "N/A" else None
#                 },
#                 "Cholesterol": cholesterol,
#                 "Sodium": sodium,
#                 "Total Carbohydrates": {
#                     "Amount": total_carbohydrate,
#                     "Dietary Fiber": dietary_fiber,
#                     "Total Sugars": total_sugars,
#                     "Added Sugars": added_sugars if added_sugars != "N/A" else None
#                 },
#                 "Protein": protein,
#                 "Potassium": potassium,
#                 "Phosphorus": phosphorus
#             }
#         }
#     }

# # Creating the final JSON object for the recipe data
# recipe_data = {
#     "title": title,
#     "description": description,
#     "prep_time": prep_time,
#     "cook_time": cook_time,
#     "servings": servings,
#     "steps": steps,
#     "tags": tags,
#     "ingredients": ingredients,  # Add the ingredients here
#     "nutrition_facts": nutrition_data.get("Nutrition Facts", {})  # Adding nutrition data
# }

# # Outputting the result to a JSON file
# with open("1recipe_with_nutrition_and_ingredients.json", "w") as json_file:
#     json.dump(recipe_data, json_file, indent=4)

# print("Recipe data with nutrition facts and ingredients has been saved to recipe_with_nutrition_and_ingredients.json")
from bs4 import BeautifulSoup
import json
import requests

# URL of the recipe page
url = "https://diabetesfoodhub.org/recipes/turkey-sausage-and-egg-casserole"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Extracting the recipe title
title_tag = soup.find("h1", class_="recipe-hero__headline")
title = title_tag.find("span").get_text(strip=True) if title_tag else "Title not found"

# Extracting the recipe description
description_tag = soup.find("div", class_="dfh-recipe-desc")
description = description_tag.find("p").get_text(strip=True) if description_tag else "Description not found"

# Extracting preparation, cook time, and servings
prep_time_tag = soup.find("div", class_="recipe-preparation-time")
prep_time = (
    prep_time_tag.find("span").get_text(strip=True) if prep_time_tag else "N/A"
)
cook_time_tag = soup.find("div", class_="recipe-cook-time")
cook_time = (
    cook_time_tag.find("span").get_text(strip=True) if cook_time_tag else "N/A"
)
servings_tag = soup.find("div", class_="recipe-servings")
servings = servings_tag.find("span").get_text(strip=True) if servings_tag else "N/A"

# Extracting recipe steps
steps_section = soup.find("ol", class_="recipe-steps")
steps = [li.get_text(strip=True) for li in steps_section.find_all("li")] if steps_section else []

# Extracting tags
tags_section = soup.find("div", class_="recipe-tags-section")
tags = [a.get_text(strip=True) for a in tags_section.find_all("a")] if tags_section else []

# Extracting ingredients
ingredients_section = soup.find("div", class_="ingredients-facts-section")
ingredients = []
if ingredients_section:
    for ingredient in ingredients_section.find_all("div", class_="ingredient-wrapper"):
        label = ingredient.find("div", class_="ingredient-label").get_text(strip=True)
        us_measure = ingredient.find("div", class_="ingredient-us").get_text(strip=True)
        metric_measure = ingredient.find("div", class_="ingredient-metric").get_text(strip=True)
        ingredients.append({
            "label": label,
            "us_measure": us_measure,
            "metric_measure": metric_measure
        })

# Extracting nutrition facts
nutrition_section = soup.find("div", class_="nutrition-facts-section")
nutrition_data = {}

if nutrition_section:
    # Extracting servings
    servings_tag = nutrition_section.find("span", class_="js-servings-label")
    servings = servings_tag.get_text(strip=True) if servings_tag else "N/A"

    # Extracting serving size
    serving_size_tag = nutrition_section.find("div", itemprop="servingSize")
    serving_size = serving_size_tag.get_text(strip=True) if serving_size_tag else "N/A"
    
    # Extracting Amount per Serving (Calories)
    calories_tag = nutrition_section.find("span", itemprop="calories")
    calories = calories_tag.get_text(strip=True) if calories_tag else "N/A"

    # Extracting total fat, saturated fat, and trans fat
    total_fat_tag = nutrition_section.find("span", itemprop="fatContent")
    total_fat = total_fat_tag.get_text(strip=True) if total_fat_tag else "N/A"
    saturated_fat_tag = nutrition_section.find("span", itemprop="saturatedFatContent")
    saturated_fat = saturated_fat_tag.get_text(strip=True) if saturated_fat_tag else "N/A"
    trans_fat_tag = nutrition_section.find("span", itemprop="transFatContent")
    trans_fat = trans_fat_tag.get_text(strip=True) if trans_fat_tag else "N/A"

    # Extracting cholesterol and sodium
    cholesterol_tag = nutrition_section.find("span", itemprop="cholesterolContent")
    cholesterol = cholesterol_tag.get_text(strip=True) if cholesterol_tag else "N/A"
    sodium_tag = nutrition_section.find("span", itemprop="sodiumContent")
    sodium = sodium_tag.get_text(strip=True) if sodium_tag else "N/A"

    # Extracting total carbohydrates, dietary fiber, total sugars, added sugars
    total_carbohydrate_tag = nutrition_section.find("span", itemprop="carbohydrateContent")
    total_carbohydrate = total_carbohydrate_tag.get_text(strip=True) if total_carbohydrate_tag else "N/A"
    dietary_fiber_tag = nutrition_section.find("span", itemprop="fiberContent")
    dietary_fiber = dietary_fiber_tag.get_text(strip=True) if dietary_fiber_tag else "N/A"
    total_sugars_tag = nutrition_section.find("span", itemprop="sugarContent")
    total_sugars = total_sugars_tag.get_text(strip=True) if total_sugars_tag else "N/A"
    added_sugars_tag = nutrition_section.find("span", itemprop="addedSugarContent")
    added_sugars = added_sugars_tag.get_text(strip=True) if added_sugars_tag else "N/A"

    # Extracting protein
    protein_tag = nutrition_section.find("span", itemprop="proteinContent")
    protein = protein_tag.get_text(strip=True) if protein_tag else "N/A"

    # Extracting Potassium and Phosphorus (adjusted for structure)
    potassium_tag = nutrition_section.find("strong", text="Potassium")
    potassium = potassium_tag.find_next_sibling(text=True).strip() if potassium_tag else None
    
    phosphorus_tag = nutrition_section.find("strong", text="Phosphorous")
    phosphorus = phosphorus_tag.find_next_sibling(text=True).strip() if phosphorus_tag else None

    # Constructing the nested JSON for nutrition facts
    nutrition_data = {
        "Nutrition Facts": {
            "Servings": servings,
            "Serving Size": serving_size,
            "Amount per Serving": {
                "Calories": calories,
                "Total Fat": {
                    "Amount": total_fat,
                    "Saturated Fat": saturated_fat,
                    "Trans Fat": trans_fat if trans_fat != "N/A" else None
                },
                "Cholesterol": cholesterol,
                "Sodium": sodium,
                "Total Carbohydrates": {
                    "Amount": total_carbohydrate,
                    "Dietary Fiber": dietary_fiber,
                    "Total Sugars": total_sugars,
                    "Added Sugars": added_sugars if added_sugars != "N/A" else None
                },
                "Protein": protein,
                "Potassium": potassium,
                "Phosphorus": phosphorus
            }
        }
    }

# Creating the final JSON object for the recipe data
recipe_data = {
    "title": title,
    "description": description,
    "prep_time": prep_time,
    "cook_time": cook_time,
    "servings": servings,
    "steps": steps,
    "tags": tags,
    "nutrition_facts": nutrition_data.get("Nutrition Facts", {}),  # Nutrition facts first
    "ingredients": ingredients  # Ingredients next
}

# Outputting the result to a JSON file
with open("2recipe_with_nutrition_and_ingredients.json", "w") as json_file:
    json.dump(recipe_data, json_file, indent=4)

print("Recipe data with nutrition facts and ingredients has been saved to recipe_with_nutrition_and_ingredients.json")
