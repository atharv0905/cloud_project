import requests
import threading
import time
import random
import dotenv
import os
dotenv.load_dotenv()

POST_API_KEY = os.getenv("POST_API_KEY")
GET_API_KEY  = os.getenv("GET_API_KEY")

POST_URL = "http://127.0.0.1:8000/random"
GET_URL  = "http://127.0.0.1:8000/random?limit=10"


# ----------------------------
# INSERT DATA (POST)
# ----------------------------
def start_sending_data():
    while True:
        try:
            random_num = random.randint(1, 100)

            response = requests.post(
                POST_URL,
                headers={
                    "Content-Type": "application/json",
                    "x-api-key": POST_API_KEY
                },
                json={
                    "ranint": random_num
                }
            )

            response.raise_for_status()
            data = response.json()
            print("Inserted:", data)

        except Exception as e:
            print("Insert failed:", e)

        time.sleep(10)  # every 15 minutes


# ----------------------------
# READ DATA (GET)
# ----------------------------
def start_fetching_data():
    while True:
        try:
            response = requests.get(
                GET_URL,
                headers={
                    "x-api-key": GET_API_KEY
                }
            )

            response.raise_for_status()
            data = response.json()
            print("Fetched:", data)

        except Exception as e:
            print("Fetch failed:", e)

        time.sleep(60*15)  # every 15 minutes


# ----------------------------
# START BOTH LOOPS
# ----------------------------
if __name__ == "__main__":
    sender_thread = threading.Thread(target=start_sending_data, daemon=True)
    fetcher_thread = threading.Thread(target=start_fetching_data, daemon=True)

    sender_thread.start()
    fetcher_thread.start()

    # Keep main thread alive
    while True:
        time.sleep(1)