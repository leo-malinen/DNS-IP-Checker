import requests
import ipaddress

def geolocate_ip(ip_address):
    try:
        ip_obj = ipaddress.ip_address(ip_address)
    except ValueError:
        print("Invalid IP address format. Please enter a valid IPv4 or IPv6 address.")
        return

    api_url = f"https://ipinfo.io/{ip_address}/json"
    response = requests.get(api_url)
    data = response.json()

    country = data.get("country", "Unknown")
    city = data.get("city", "Unknown")
    region = data.get("region", "Unknown")

    print(f"IP Address: {ip_address}")
    print(f"Country: {country}")
    print(f"City: {city}")
    print(f"Region: {region}")

if __name__ == "__main__":
    user_ip = input("Enter an IP address: ")
    geolocate_ip(user_ip)
