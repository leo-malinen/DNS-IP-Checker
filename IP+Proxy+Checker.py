import requests
import ipaddress

#function call to get the ip address through IPAPI
def geolocate_ip(ip_address):
    try:
        ip_obj = ipaddress.ip_address(ip_address)
    except ValueError:
        print("Invalid IP. Please enter an address in IPV4 or IPV6 form.")
        return

    api_url = f"https://api.ipapi.com/api/{ip_address}?access_key=YOUR_ACCESS_KEY"
    response = requests.get(api_url)
    data = response.json()

    #get the data and if it does not work, output N/A
    country = data.get("country_name", "Unknown")
    city = data.get("city", "Unknown")
    region = data.get("region", "Unknown")
    latitude = data.get("latitude", "Unknown")
    longitude = data.get("longitude", "Unknown")

    #all print statements to print whatever is necessary
    print(f"IP Address: {ip_address}")
    print(f"Country: {country}")
    print(f"City: {city}")
    print(f"Region: {region}")
    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")

#main function for the program
if __name__ == "__main__":
    user_ip = input("Enter an IP address: ")
    geolocate_ip(user_ip)
