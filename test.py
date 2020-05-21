my_string = "MERGE (a:Artist {{name:'{0}'}}) CREATE (a)-[:RELATED_TO]->(:Artist {{name: '{1}'}})".format("Kanye West", "Ceelo Green")
print(my_string)
