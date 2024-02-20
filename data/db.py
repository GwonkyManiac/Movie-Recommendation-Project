import csv
import requests
from config import token

base_url = "https://api.themoviedb.org/3"

headers = {
    'accept': 'application/json',
    'Authorization': f'Bearer {token}'
}
params = {
    "page": 10001,
    "language": "en-US"
}

all_movies = []

while True:
    response = requests.get(f"{base_url}/discover/movie", headers=headers, params=params)
    if response.status_code != 200:
        print(f"Failed to fetch data: {response.status_code}")
        break

    page_data = response.json()
    movies_on_page = page_data.get("results", [])
    all_movies.extend(movies_on_page)

    if page_data["page"] < page_data["total_pages"]:
        params["page"] += 1
    else:
        break

# Save data to CSV file
csv_filename = "movies_data.csv"
fieldnames = ["title", "release_date", "popularity", "genre_ids", "vote_average"]

with open(csv_filename, mode="w", newline="", encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for movie in all_movies:
        writer.writerow({
            "title": movie["title"],
            "release_date": movie["release_date"],
            "popularity": movie["popularity"],
            'genre_ids': movie['genre_ids'],
            "vote_average": movie["vote_average"]
        })

print(f"Data saved to {csv_filename}")
