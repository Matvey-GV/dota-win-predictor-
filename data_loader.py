import requests
import pandas as pd
import time

BASE_URL = "https://api.opendota.com/api/publicMatches"

def get_matches(n_matches=200):
    matches = []
    last_match_id = None

    while len(matches) < n_matches:
        params = {}
        if last_match_id:
            params["less_than_match_id"] = last_match_id

        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if not data:
            break

        matches.extend(data)
        last_match_id = data[-1]["match_id"]

        print(f"Собрано матчей: {len(matches)}")
        time.sleep(1)  # чтобы не словить лимит

    return matches[:n_matches]


def save_to_csv(matches):
    df = pd.DataFrame(matches)
    df.to_csv("data/matches.csv", index=False)
    print("Сохранено в data/matches.csv")


if __name__ == "__main__":
    matches = get_matches(300)
    save_to_csv(matches)