#!/bin/bash
# Will send a POST request to the provided URL, and displays the body of the response
curl -s -d "email=test@gmail.com&subject=I will always be here for PLD" "${1}"
