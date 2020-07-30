# Cliff notes

## Dictionaries 
* a book of words and their definitions 
    * ex: {"name": "Tait", "occupation": "student"}
* the book has a combination of a key paired with a value
* the content of a dictionary can be any form of Python type (lists, tuples, sets, dictionaries)

### Working with Dictionaries
* to access the things in a dictionary:
    * book = {"title": "Clifford the Big Red Dog", "author": "some person"}
        1. book["title"] would return "Clifford the Big Red Dog"
        2. book.get("title") would also
        3. book.values() would return all the values in the dictionaries

* to see if your key is in the dictionary:
    * use the 'in' operator:
        my_variable in my_dictionary
    * you can also do the opposite: 
        my_variable not in my_dictionary

* to update a value:
    * superhero = {
        "name": "Wonder Woman",
        "alias": "Diana Prince", 
        "gear": [
            "Lasso of Truth",
            "Bracelets of Submission"
        ],
        "vehicle": {
            "title": "Invisible Jet",
            "speed": "2000 mph"
        }
    }
    * you are about to assign new values to the key/pairs in the code below
    superhero["alias"] = "Princess Diana of Themyscira"
    superhero["hometown"] = "Themyscira"

* to iterate over a dictionary:
    * for key, value in superhero.items():
        print(f"Superhero's %s is %s" % (key, value))
    * Lee version:
        for key, value in superhero.items():
            print(f"Superhero's {key} is {value}")
