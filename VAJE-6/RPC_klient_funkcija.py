import requests
import json    

def main():
        # definiraj VARIABLE nase skripte
        # API URL od infure za Ethereum mainnet
    node_url = "https://mainnet.infura.io/v3/21e65883b51645798d6481cb6dbf6948"
        
        # JSON-RPC request payload  (pogledamo dokumentacijo!)
    payload = {
        "jsonrpc": "2.0",
        "method": "eth_getBlockByNumber",
        "params": ["latest", True],
        "id": 0
    }

        # Nastavimo headerje za JSON-RPC request
    headers = {
        "Content-Type": "application/json"
    }
    data = getBlock(node_url, payload, headers)
    print(count(data))

def getBlock(node_url, payload, headers):
    # Pošljemo request (uporabimo requests.post mdetodo)
    response = requests.post(node_url, data=json.dumps(payload), headers=headers)

    # Error handling. POgledamo če smo dobili pravilen odgovor.
        # ce ni error-ja (status code 200) sprintamo sporocilo in shranimo dobljeno sporocilo v json
    if response.status_code==200:
        block_data = response.json()
        print("Dobili smo blok!")
        with open('blockData.json', 'w') as f:
            json.dump(response.json(), f, indent=4)
        # else, sprintaj sporocilo da nam ni uspelo dobiti zadnji block in dodaj kateri error oz. code-status code smo dobili
    else:
        print(f"Ni uspelo! Error code: {response.status_code}")
    
    return block_data

def count(block_data):
    # naredimo kopijo podatkov - .copy() metoda
    data = block_data.copy()

    # definiramo counter
    counter = 0

    # Iteriramo čez transakcije in povečujemo counter
    for transaction in data["result"]["transactions"]:
        counter += 1
    
    # Izpišemo/sprintamo counter (število transakcij)
    print(counter)

    return counter
