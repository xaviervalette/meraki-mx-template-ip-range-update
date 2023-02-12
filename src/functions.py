# Function to update the third byte of an IP address
def updateThirdByteIp(ip, newThirdByte):
    # Split the IP into its 4 bytes
    ipSplit = ip.split(".")
    # Update the third byte
    ipSplit[2] = str(newThirdByte)
    # Join the 4 bytes back into an IP
    ipUpdated = '.'.join(ipSplit)
    # Return the updated IP
    return (ipUpdated)

# Function to update the subnet and appliance IP of a VLAN
def updateVlan(vlan, newThirdByte):
    # Create a dictionary to store the updated VLAN details
    vlanUpdated = {}
    # Update the subnet
    vlanUpdated["subnet"] = updateThirdByteIp(vlan["subnet"], newThirdByte)
    # Update the appliance IP
    vlanUpdated["applianceIp"] = updateThirdByteIp(vlan["applianceIp"], newThirdByte)
    # Store the interface ID (which is unchanged)
    vlanUpdated["interfaceId"] = vlan["interfaceId"]
    # Return the updated VLAN details
    return vlanUpdated

# Function to get the URL for a specific VLAN
def getVlanUrl(vlanId, networkId):
    # Create the URL using the network ID and VLAN ID
    vlanUrl = f"https://api.meraki.com/api/v1/networks/{networkId}/appliance/vlans/{vlanId}"
    # Return the URL
    return vlanUrl