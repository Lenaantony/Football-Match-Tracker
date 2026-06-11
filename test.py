import requests

API_KEY ="bcf4590cebdb4c619fa1cf7b3e371cbe"

headers = {
    "X-Auth-Token": API_KEY
}

response = requests.get(
    "https://api.football-data.org/v4/competitions",
    headers=headers
)

print("Status:", response.status_code)
print(response.text)