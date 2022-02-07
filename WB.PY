print("Wayback Machine CLI")
archive = input("Input the URL to archive: ")
print("Calling Wayback Machine request (http)...")
import urllib.request
# HTTP is used to call the Internet Archive Wayback Machine servers, NOT the API!
urllib.request.urlopen("https://web.archive.org/save/" + url) # This saves to the Wayback Machine.
print("Archived to Wayback Machine.")
input("Press Enter to exit...")
exit()
