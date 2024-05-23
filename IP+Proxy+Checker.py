import requests
import ipaddress

# Function to get the geolocation of an IP address through IPAPI
def geolocate_ip(ip_address):
    try:
        ip_obj = ipaddress.ip_address(ip_address)
    except ValueError:
        print("Invalid IP. Please enter an address in IPV4 or IPV6 form.")
        return

    api_url = f"https://ipinfo.io/{ip_address}/json"
    response = requests.get(api_url)
    data = response.json()

    # Get the data and if it does not work, output Unknown
    country = data.get("country", "Unknown")
    city = data.get("city", "Unknown")
    region = data.get("region", "Unknown")
    latitude = data.get("loc", "Unknown").split(',')[0] if data.get("loc") else "Unknown"
    longitude = data.get("loc", "Unknown").split(',')[1] if data.get("loc") else "Unknown"

    # Print statements to display the necessary information
    print(f"IP Address: {ip_address}")
    print(f"Country: {country}")
    print(f"City: {city}")
    print(f"Region: {region}")
    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")

# Function to check if the IP address is a proxy
def is_proxy(ip_address):
    api_url = f"https://proxycheck.io/v2/{ip_address}"
    response = requests.get(api_url)
    data = response.json()
    proxy_status = data.get(ip_address, {}).get('proxy', "No")

    print(f"Proxy: {proxy_status}")

# Main function for the program
if __name__ == "__main__":
    user_ip = input("Enter an IP address: ")
    geolocate_ip(user_ip)
    is_proxy(user_ip)
