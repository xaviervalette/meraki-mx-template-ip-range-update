# Import the required libraries:
# requests: for sending HTTP requests
# json: for encoding and decoding JSON data
# time: for sleeping the script in case of too many requests
import requests
import json
import time
from functions import *
import yaml

# Open the config.yml file and load its contents into the 'config' variable
with open('../config.yml', 'r') as file:
    config = yaml.safe_load(file)

# Loop through each network defined in the config file
for network in config["networksToBeUpdated"]:
    # Create the URL for retrieving all VLANs in the network
    url = f"https://api.meraki.com/api/v1/networks/{network['networkId']}/appliance/vlans"

    # Set the payload to None (not needed for this GET request)
    payload = None

    # Set the HTTP headers
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": config["apiKey"]
    }

    # Send a GET request to retrieve the VLANs
    response = requests.request('GET', url, headers=headers, data = payload)
    # Convert the response to a Python dictionary
    vlans = response.json()

    # Loop through each VLAN in the network
    for vlan in vlans:
        # Update the VLAN details using the 'updateVlan' function
        vlanUpdated = updateVlan(vlan, newThirdByte=network['thirdByte'])
        # Get the URL for this VLAN using the 'getVlanUrl' function
        vlanUrl = getVlanUrl(vlan["id"], network['networkId'])
        # Send a PUT request to update the VLAN
        response = requests.request('PUT', vlanUrl, headers=headers, data = json.dumps(vlanUpdated))
        # Check the status code of the response after updating the VLAN
        if response.status_code == 200:
                # If the status code is 200, it means the update was successful
                # Print a message indicating the updated VLAN id, and the change from its original subnet to the updated subnet
                print("VLAN", vlan["id"], "has been updated from", vlan["subnet"], "to", vlanUpdated["subnet"])
        elif response.status_code == 429:
            # If the status code is 429, it means the API has been rate-limited
            # Wait for 1000 seconds before trying the update again
            time.sleep(1000)