print("Wayback Machine CLI")
import os
archive = "https://github.com"

print("Calling Wayback Machine request (http)...")
os.system("pip install --upgrade requests")
import requests

# HTTP is used to call the Internet Archive Wayback Machine servers, NOT the API!



r = requests.head("https://web.archive.org/save/" + archive) # This saves to the Wayback Machine.


    
  

print("Archived to Wayback Machine")



