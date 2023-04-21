#!/usr/bin/python3
import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

filename = "add_item.json"

# Load existing list from file if it exists, otherwise create a new list
try:
    my_list = load_from_json_file(filename)
except FileNotFoundError:
    my_list = []

# Add all arguments passed to the script to the list
my_list += sys.argv[1:]

# Save the updated list to file
save_to_json_file(my_list, filename)
