import json
import pickle

json_string = json.dumps([1, 2, 3, "a", "b", "c"])
print(json_string)

pickled_string = pickle.dumps([1, 2, 3, "a", "b", "c"])
print(pickle.loads(pickled_string))

# To load JSON back to a data structure, use the "loads" method. This method takes a string and turns it back into
# the json object data structure
#
# To encode a data structure to JSON, use the "dumps" method. This method takes an
# object and returns a String

# fix this function, so it adds the given name
# and salary pair to salaries_json, and return it


def add_employee(salaries_json, name, salary):
    # Add your code here
    salaries = json.loads(salaries_json)
    salaries[name] = salary

    return json.dumps(salaries)


# test code
salaries = '{"Alfred" : 300, "Jane" : 400 }'
new_salaries = add_employee(salaries, "Me", 800)
decoded_salaries = json.loads(new_salaries)
print(decoded_salaries["Alfred"])
print(decoded_salaries["Jane"])
print(decoded_salaries["Me"])
