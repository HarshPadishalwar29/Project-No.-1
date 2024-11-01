import sys           
import requests       
import json           
import socket         

if len(sys.argv) != 2:
    print("Usage: python infotool.py <websiteurl>")
    sys.exit(1)

website_url = sys.argv[1]

try:
   
    ip_address = socket.gethostbyname(website_url)
    print(f"IP Address of {website_url} is: {ip_address}")
    
    api_url = f"https://ipinfo.io/{ip_address}/json"
    response = requests.get(api_url)
    
    if response.status_code == 200:
     
        data = response.json()
        
        
        print("\nLocation and IP Information:")
        print(f"IP: {data.get('ip', 'N/A')}")
        print(f"City: {data.get('city', 'N/A')}")
        print(f"Region: {data.get('region', 'N/A')}")
        print(f"Country: {data.get('country', 'N/A')}")
        print(f"Location (Coordinates): {data.get('loc', 'N/A')}")
        print(f"Organization: {data.get('org', 'N/A')}")
    else:
        print("Error retrieving data. Check the IP address and try again.")

except socket.gaierror:
    print("Error: Unable to retrieve IP address. Check the website URL.")
