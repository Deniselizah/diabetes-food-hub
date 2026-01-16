from bs4 import BeautifulSoup
import json
import requests

# URL of the recipe page (replace with the desired recipe URL)
url = "https://diabetesfoodhub.org/recipes/sugar-free-yogurt-parfait-fresh-berries"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Extracting the nutrition facts section
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

    # Constructing the nested JSON
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

# Outputting the result to a JSON file
with open("5nutrition_facts.json", "w") as json_file:
    json.dump(nutrition_data, json_file, indent=4)

print("Nutrition facts data has been saved to nutrition_facts.json")
