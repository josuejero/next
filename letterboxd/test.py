import json

with open('letterboxd/movie_data.json') as f:
    data = json.load(f)

for state in data['actors']:
    print(state['name'])