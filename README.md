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
1. Clone or download this repo
```console
git clone https://github.com/xaviervalette/meraki-mx-template-ip-range-update
```
2. Install required packages
```console
pip3 install -r requirements.txt
```
3. Add a file called config.yml as follow:
```diff
└── merakiTemplateIpRangeUpdate/
+   ├── config.yml
    └── src/
         ├── functions.py
         └── merakiTemplateIpRangeUpdate.py      
```
4. In the config.yml file, add the following variables:
```yaml
#config.yml
---

# Specify the API key used to authenticate on the Meraki API.
apiKey: "<yourApiKey>"

networksToBeUpdated:
  # This is the first network in the list.
  - networkId: <yourNetworkId1>
    thirdByte: <yourThirdByte1>
  
  # This is the second network in the list.
  - networkId: <yourNetworkId2>
    thirdByte: <yourThirdByte2>
    
  # [...]

  # This is the Nth network in the list.
  - networkId: <yourNetworkIdN>
    thirdByte: <yourThirdByteN>

...

```
5. Now you can run the code by using the following command:
```console
python3 src/main.py
```
⚠ Using this script will change your VLAN subnets. Thus, it will broke the connectivity of the connected users, so be careful to use it on unused VLANs

## Output
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



