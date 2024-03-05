#!/bin/bash
# sends a GET request to the URL, and displays the body of the response 
curl -I -s "${1}" |grep "^Allow: .*" | cut -d " " -f 2-
