#!/bin/bash
# sends a GET request to the URL, and displays the body of the response 
curl -I -s -X "${1}" | cut -d " " -f 2-
