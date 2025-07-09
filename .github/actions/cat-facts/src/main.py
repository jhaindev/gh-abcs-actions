import requests
import random
import sys
import os

# Make an HTTP GET request to the cat-fact API
# Using a more reliable API endpoint that returns an array of cat facts
cat_url = "https://catfact.ninja/facts?limit=10"
r = requests.get(cat_url)
r_obj_list = r.json()

# Create an empty list to store individual facts in
# This will make it easy to select a random one later
fact_list = []

# Add each fact to our fact_list
for fact in r_obj_list["data"]:
    fact_list.append(fact["fact"])

# Select a random fact from the fact_list and return it
# into a variable named random_fact so we can use it
def select_random_fact(fact_arr):
    return fact_arr[random.randint(0, len(fact_arr)-1)]

random_fact = select_random_fact(fact_list)

# Print the individual randomly returned cat-fact
print(random_fact)

# Set the fact-output of the action as the value of random_fact
# This is the correct format for GitHub Actions outputs from a Docker container
print(f"::set-output name=fact::{random_fact}")
