#!/bin/bash
# task 100 
curl -so /dev/null -w "%{http_code}" "${1}"
