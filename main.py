# pip install jinja2, requests, json for better performance
import json
from jinja2 import Environment, FileSystemLoader, select_autoescape
import requests

def facts():
    """
    Function  to get Facts from cats and save in database
    """
    try:
        response = requests.get("https://catfact.ninja/facts") # Get elements from API
        cat_fact_json = json.loads(response.content)  # Transform to json format
        fact = []  # Initializing the variable
        for facts in cat_fact_json['data']:  # looping through each element of the variable
            fact.append(facts['fact'])  # Add to a list each elements
        return fact
    except Exception as e:
        print(e)
        print("The conection with the URL to API have some error")


if __name__ == '__main__':
    facts()

# Render the template and load a template
fileloader = FileSystemLoader("templates")
env = Environment(
    loader=fileloader,
    autoescape=select_autoescape()
)
# Getting the template
template = env.get_template("index.html")
# Creating the content to show
content = {
     'facts': facts()
}
# Print the rendered template in the terminal
print(template.render(**content))

