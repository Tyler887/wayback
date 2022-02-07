print("Wayback Machine CLI")

archive = "https://tyler887.github.io"

print("Calling Wayback Machine request (http)...")
os.system("pip install --upgrade requests")
import requests

# HTTP is used to call the Internet Archive Wayback Machine servers, NOT the API!



r = requests.head("https://web.archive.org/save/" + archive) # This saves to the Wayback Machine.

if not r.status_code.startswith("20") and not r.statuscode.startswith("30"): # 20X is OK, 30X is redirect. Other codes are ERRORs.

    print("Archived to Wayback Machine UNSUCCESSFULLY. web.archive.org returned HTTP code " + r.status_code + ".")

    

    exit(1)



  

print("Archived to Wayback Machine successfully.")


exit()
