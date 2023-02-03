# Meraki Template Ip Range Update

## What is it ?
A python script to update, via API, the third byte of /24 subnets generated from a /16 subnet configured in a Configuration template to make consistent subnets within networks.
### Without the script
![withoutScript](https://user-images.githubusercontent.com/28600326/216713044-c32dfecb-8b0e-42a9-b49f-eaa3adb52f29.png)
### With the script
![withScript](https://user-images.githubusercontent.com/28600326/216713070-c04f47bf-cbda-40cc-83fb-68eb236c5a20.png)

## Requirements
- Meraki Dashboard access
- Meraki API key
- Meraki network ID
- MX appliance in routed mode with VLANs
- [Configuration template](https://documentation.meraki.com/General_Administration/Templates_and_Config_Sync/Managing_Multiple_Networks_with_Configuration_Templates)

## Get started
- Clone or download this repo
- Add a file called variables.py as follow:
```
└── merakiTemplateIpRangeUpdate/
    ├── functions.py
    ├── merakiTemplateIpRangeUpdate.py
    └── variables.py (need to be created)
```
In the variables.py file, add the following variables:
```python
#variables.py
API_KEY = "<your_api_key>"
NETWORK_ID = "<your_network_id>"
```
Now you can run the code by using the following command:
```console
/usr/local/bin/python3.11 <your_workpath>/merakiTemplateIpRangeUpdate/updateTemplateIpRange.py
```
The output should be as followed:
```console
VLAN <your_network_vlans> has been updated from <old_subnet> to <new_subnet>
```
Example:
```console
VLAN 1 has been updated from 10.1.191.0/24 to 10.1.78.0/24
VLAN 142 has been updated from 10.142.251.0/24 to 10.142.78.0/24
VLAN 143 has been updated from 10.143.23.0/24 to 10.143.78.0/24
VLAN 144 has been updated from 10.144.171.0/24 to 10.144.78.0/24
VLAN 145 has been updated from 10.145.89.0/24 to 10.145.78.0/24
```



