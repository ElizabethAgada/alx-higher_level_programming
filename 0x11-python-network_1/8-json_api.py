#!/usr/bin/python3
"""Script that sends POST request to http://0.0.0.0:5000/search_user with given letter
Usage: ./8-json_api.py <letter>
  - Letter is sent as value of variable `q`.
  - If no letter, send `q=""`.
"""
import sys
import requests


if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": letter}

    r = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
