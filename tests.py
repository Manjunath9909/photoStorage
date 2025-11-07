import time
import json

bigDictionaryOfMovies = {"movies":
                         [{"id": 1, "name" : "Transformers 1"},
                         {"id" : 2, "name" : "Transformers 2"},
                         {"id" : 3, "name" : "Transformers 3"}]
                        }

bigDictionaryOfMovies['movies'].append({"id" : 4, "name" : "Transformers 4"})

print(bigDictionaryOfMovies['movies'].__len__())
len = bigDictionaryOfMovies['movies'].__len__()
bigDictionaryOfMovies['movies'].append({"id" : len + 1, "name" : "Transformers 5"})

print(bigDictionaryOfMovies['movies'])

with open ("movies2.json", "w") as jsonFile:
    json.dump(bigDictionaryOfMovies, jsonFile, indent=2)

