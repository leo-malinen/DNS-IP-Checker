import requests
import ipaddress
import tkinter as tkin

# Function to get the geolocation of an IP address through IPINFO
def geolocateIp(ipAddress):
    try:
        ipObj = ipaddress.ip_address(ipAddress)
    except ValueError:
        print("Invalid IP. Please enter an address in IPV4 or IPV6 form.")
        return

    apiUrl = f"https://ipinfo.io/{ipAddress}/json"
    response = requests.get(apiUrl)
    data = response.json()

    # Get the data and if it does not work, output Unknown
    country = data.get("country", "Unknown")
    city = data.get("city", "Unknown")
    region = data.get("region", "Unknown")
    latitude = data.get("loc", "Unknown").split(',')[0] if data.get("loc") else "Unknown"
    longitude = data.get("loc", "Unknown").split(',')[1] if data.get("loc") else "Unknown"

    return f"IP Address: {ipAddress}\n Country: {country}\n City: {city}\n Region: {region}\n Latitude: {latitude}\n Longitude: {longitude}"

# Function to check if the IP address is a proxy
def isProxy(ipAddress):
    apiUrl = f"https://proxycheck.io/v2/{ipAddress}"
    response = requests.get(apiUrl)
    data = response.json()
    proxyStatus = data.get(ipAddress, {}).get('proxy', "Not Detected")
    ipType = data.get(ipAddress, {}).get('type', "Unknown")

    return f"\nProxy: {proxyStatus} \nType: {ipType}"

# Main function for the program
if __name__ == "__main__":
    userIp = input("Enter an IP address: ")
    geolocationInfo = geolocateIp(userIp)
    proxyInfo = isProxy(userIp)

    # Create a simple Tkinter window
    root = tkin.Tk()
    root.title("IP, DNS, Geolocation and Proxy Checker")

    # Create and display the TKinter text box with data
    textBox = tkin.Text(root, bg="black", fg="white")
    textBox.pack(fill="both", expand=True)
    textBox.insert("end", geolocationInfo + "\n" + proxyInfo)
    root.mainloop()
