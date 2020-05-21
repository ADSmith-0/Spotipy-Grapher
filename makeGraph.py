from neo4j import GraphDatabase, basic_auth

driver = GraphDatabase.driver(
    "bolt://54.87.236.196:36145",
    auth=basic_auth("neo4j", "differences-davit-offset"))
session = driver.session()

rel_artists = []
with open('artists.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        artists = line.split(':')
        m_artist = artists[0]
        for artist in artists[1].split(','):
            cypher_query = "MERGE (a:Artist {{name:'{0}'}}) MERGE (b:Artist {{name:'{1}'}}) CREATE (a)-[:RELATED_TO]->(b)".format(m_artist, artist.strip())
            results = session.run(cypher_query,parameters={})
