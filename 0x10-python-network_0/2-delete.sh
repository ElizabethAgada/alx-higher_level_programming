#!/bin/bash
# Send  DELETE request to exact URL passed as the first argument and displays the body of the respons
curl -s -X DELETE "${1}"
