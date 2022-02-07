print("Wayback Machine CLI")
archive = input("Input the URL to archive: ")
print("Calling Wayback Machine request (http)...")
import requests
# HTTP is used to call the Internet Archive Wayback Machine servers, NOT the API!
try:
  r.head("https://web.archive.org/save/" + archive) # This saves to the Wayback Machine.
  if
expect requests.ConnectionError:
  print("Archived to Wayback Machine UNSUCCESSFULLY. Could not establish a working connection.\nAre you sure that there are no current incidents reported by the the Internet Archive?")
  input("Press Enter to exit... ")
  exit(1)
print("Archived to Wayback Machine successfully.")
input("Press Enter to exit... ")
exit()
