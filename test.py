import requests

res = requests.post(
    "https://airesearch.onrender.com",
    json={
        "query": "learning with ai in corporate world"
    }
).json()

print(res)