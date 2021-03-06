print("Wayback 1.0, a command line interface for the Wayback Machine")
archive = input("Input the URL to archive: ")
print("Calling Wayback Machine request (http)...")
import requests
# HTTP is used to call the Internet Archive Wayback Machine servers, NOT the API!
try:
  r = requests.head("https://web.archive.org/save/" + archive) # This saves to the Wayback Machine.
  if not r.status_code.startswith("20") and not r.statuscode.startswith("30"): # 20X is OK, 30X is redirect. Other codes are ERRORs.
    print("Archived to Wayback Machine UNSUCCESSFULLY. web.archive.org returned HTTP code " + r.status_code + ".")
    input("Press Enter to exit... ")
    exit(1)
except requests.ConnectionError:
  print("Archived to Wayback Machine UNSUCCESSFULLY. Could not establish a working connection.\nAre you sure that there are no current incidents reported by the the Internet Archive?")
  input("Press Enter to exit... ")
  exit(1)
print("Archived to Wayback Machine successfully.")
input("Press Enter to exit... ")
exit()
