# ----------------------------------JSON-------------------
import json

# Python has a built-in package called json, which can be used to work with JSON data.

# 1. Parsing JSON
# Convert a JSON string to a Python dictionary using json.loads():
# import json
#
# json_data = '{"name": "Dipam", "age": 21, "country": "Monaco"}'
# data = json.loads(json_data)
# print(data["name"])
#
# # 2. Reading JSON from a file
#
# with open("sample1.json", "r") as file:
#     data = json.load(file)
# print(data)

# 3. Writing to a JSON file

# data = {"name": "Bob", "age": 30, "city": "Los Angeles"}
#
# with open("sample1.json", "w") as file:
#     json.dump(data, file, indent=4)

# 4. Converting Python Object to JSON String

# json_string = json.dumps(data, indent=4)
# print(json_string)


#------------------------------ Handling XML in Python ---------------------

import xml.etree.ElementTree as ET

# 1. Parsing XML form a string

#
# xml_data = """<person>
#                 <name>Dipam Shah</name>
#                 <country>Italy</country>
#                 </person>"""
#
# root = ET.fromstring(xml_data)
# print(root.find("name").text)

import xml.etree.ElementTree as ET

# Parse the XML file
tree = ET.parse("sample1.xml")
root = tree.getroot()

# Extract and print all persons
def extract_persons():
    print("Persons:")
    for person in root.findall("person"):
        name = person.find("name").text
        age = person.find("age").text
        email = person.find("email").text
        print(f"Name: {name}, Age: {age}, Email: {email}")
    print()

# Extract and print book details
def extract_books():
    print("Books:")
    for book in root.findall("book"):
        title = book.find("title").text
        author = book.find("author").text
        year = book.find("year").text
        print(f"Title: {title}, Author: {author}, Year: {year}")

# Run extraction functions
extract_persons()
extract_books()
