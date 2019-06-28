'''
This program will take a valid Mac Address input from the user and provide the output
about the Vendor. In case of Invalid Mac Address or Error appropriate message is returned
'''
#!/usr/bin/python

import json
import requests

def validate_mac(mac_addr):
    ''' Return True if its a valid MAC address else False '''
    # Check if mac_addr is 6 bytes(48bits)
    msg = "Invalid mac address"
    mac_addr = mac_addr.upper()
    if mac_addr.count(":") != 5:
        print(msg)
        return False
    # Check if mac_addr has valid digits
    for i in mac_addr.split(":"):
        for j in i:
            if j > 'F' or (j < 'A' and not j.isdigit()) or len(i) != 2:
                print(msg)
                return False
    return True
def mac_query(api_key, mac_addr):
    ''' Return Vendor details of a valid MAC address '''
    # validate mac address
    if not validate_mac(mac_addr):
        return False
    # form url string as per url value from macaddress.io & add api key, mac_address
    url = "https://api.macaddress.io/v1?apiKey=" + api_key+ "&output=json&search="+ mac_addr
    # make api request to macaddress.io and pass the api_key and mac_addr to search
    mac_search = requests.get(url)
    if mac_search.status_code == 200:
        # Format the response output of the get request
        result = json.loads(mac_search.text)
        if result['vendorDetails']['companyName']:
            return (result['macAddressDetails']['searchTerm']
                    , result['vendorDetails']['companyName']
                    , result['vendorDetails']['companyAddress'])
        print('The MAC address does not belong to any registered block')
    else:
        print('HTTP Error {}'.format(mac_search.status_code))
if __name__ == '__main__':
    MACADDR = input("Enter Mac Address:")
    APIKEY = input("Enter API KEY:")
    # query the mac address for Vendor details and output it
    Result = mac_query(APIKEY, MACADDR)
    if Result:
        print('*'*10+'Output'+'*'*10)
        print('Mac Address:\t'+Result[0], 'Vendor Name:\t'+ Result[1],\
                                                 'Vendor Address:\t'+Result[2], sep='\n')

