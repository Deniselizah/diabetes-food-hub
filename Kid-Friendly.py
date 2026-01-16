import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import json

def scrape_recipe_details(recipe_url):
    try:
        response = requests.get(recipe_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")

        title_tag = soup.find("h1", class_="recipe-hero__headline")
        title = title_tag.find("span").get_text(strip=True) if title_tag and title_tag.find("span") else "Title not found"

        description_tag = soup.find("div", class_="dfh-recipe-desc")
        description = description_tag.find("p").get_text(strip=True) if description_tag and description_tag.find("p") else "Description not found"

        prep_time_tag = soup.find("div", class_="recipe-preparation-time")
        prep_time = (
            prep_time_tag.find("span").get_text(strip=True) if prep_time_tag and prep_time_tag.find("span") else "N/A"
        )

        cook_time_tag = soup.find("div", class_="recipe-cook-time")
        cook_time = (
            cook_time_tag.find("span").get_text(strip=True) if cook_time_tag and cook_time_tag.find("span") else "N/A"
        )

        servings_tag = soup.find("div", class_="recipe-servings")
        servings = servings_tag.find("span").get_text(strip=True) if servings_tag and servings_tag.find("span") else "N/A"

        steps_section = soup.find("ol", class_="recipe-steps")
        steps = [li.get_text(strip=True) for li in steps_section.find_all("li")] if steps_section else []

        tags_section = soup.find("div", class_="recipe-tags-section")
        tags = [a.get_text(strip=True) for a in tags_section.find_all("a")] if tags_section else []

        nutrition_section = soup.find("div", class_="nutrition-facts-section")
        nutrition_facts = {}
        if nutrition_section:
            for item in nutrition_section.find_all("li"):
                key = item.find("strong").get_text(strip=True) if item.find("strong") else None
                value = (
                    item.find("span", itemprop=True).get_text(strip=True)
                    if item.find("span", itemprop=True)
                    else None
                )
                if key and value:
                    nutrition_facts[key] = value

        ingredients_section = soup.find("div", class_="ingredients-facts-section")
        ingredients = []
        if ingredients_section:
            for ingredient in ingredients_section.find_all("div", class_="ingredient-wrapper"):
                label = ingredient.find("div", class_="ingredient-label")
                us_measure = ingredient.find("div", class_="ingredient-us")
                metric_measure = ingredient.find("div", class_="ingredient-metric")
                ingredients.append({
                    "label": label.get_text(strip=True) if label else "N/A",
                    "us_measure": us_measure.get_text(strip=True) if us_measure else "N/A",
                    "metric_measure": metric_measure.get_text(strip=True) if metric_measure else "N/A"
                })

        return {
            "title": title,
            "description": description,
            "prep_time": prep_time,
            "cook_time": cook_time,
            "servings": servings,
            "steps": steps,
            "tags": tags,
            "nutrition_facts": nutrition_facts,
            "ingredients": ingredients,
        }
    except Exception as e:
        print(f"Error scraping recipe details: {e}")
        return None

def scrape_all_recipes(base_url):
    recipes = []
    next_page = base_url

    while next_page:
        response = requests.get(next_page)
        soup = BeautifulSoup(response.content, "html.parser")

        # Extract recipe links from the current page
        recipe_cards = soup.find_all("div", class_="recipe-card")

        for card in recipe_cards:
            try:
                link_tag = card.find("a", href=True)
                recipe_url = link_tag["href"] if link_tag else None

                if recipe_url:
                    full_url = urljoin("https://diabetesfoodhub.org", recipe_url)
                    recipe_details = scrape_recipe_details(full_url)
                    if recipe_details:
                        recipes.append(recipe_details)
                        print(f"Scraping recipe: {recipe_details['title']}")  # Print recipe title as it's being scraped
            except Exception as e:
                print(f"Error processing a recipe card: {e}")

        # Check for the next page link
        next_page_tag = soup.find("a", string="Load more")
        next_page = urljoin("https://diabetesfoodhub.org", next_page_tag["href"]) if next_page_tag else None

    return recipes

# Base URL of the recipes listing page
base_url = "https://diabetesfoodhub.org/recipes/kid-friendly"
all_recipes = scrape_all_recipes(base_url)

# Save the data to a JSON file
with open("Kid-Friendly.json", "w") as json_file:
    json.dump(all_recipes, json_file, indent=4)

print("All recipe data has been saved to Kid-Friendly.json")
