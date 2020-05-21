import spotipy
import json
import os
from spotipy.oauth2 import SpotifyClientCredentials
from neo4j import GraphDatabase, basic_auth

client_id = "5eb716ba1db04dada2ecb45d75d8a71f"
client_secret = "30431e447d474d6091ee214ceaf927be"

with open("openList.txt", "r") as file:
    f_line = file.readline()
    f_line = f_line.strip()

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
main_artist = sp.artist(f_line)
m_artist_name = main_artist['name']
returned_artists = sp.artist_related_artists(f_line)
rel_artists = returned_artists['artists']
rel_art_ids = []
rel_art_names = []

with open("artists.txt", "a") as file:
    file.write(m_artist_name + ": ")
    for x in rel_artists:
        if(x['popularity'] >= 50):
            rel_art_ids.append(x['id'])
            rel_art_names.append(x['name'])
            file.write(x['name'] + ", ")
    file.write("\n")

with open("closedList.txt", "r+") as file:
    cl_lines = file.readlines()
    for id in rel_art_ids:
        for cl_line in cl_lines:
            if id.strip() == cl_line.strip():
                rel_art_ids.remove(id)

    file.write(f_line + "\n")

with open("openList.txt", "r") as file:
    lines = file.readlines()
    #Append other lines, but check them against closed list first
    for val in rel_art_ids:
        lines.append(val + "\n")

os.remove("openList.txt")

with open("openList.txt", "w") as file:
    for line in lines[1:]:
            file.write(str(line))
