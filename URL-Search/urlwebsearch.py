
import webbrowser
from urllib.parse import urlparse

url = input("Please enter your website URL: ").strip()

if not url.startswith(("https://", "http://")):
    url = "https://" + url

parsed_url = urlparse(url)

if parsed_url.netloc and "." in parsed_url.netloc:
    print("Opening your website...")
    webbrowser.open(url)
else:
    print("Invalid URL. Please try again.")
