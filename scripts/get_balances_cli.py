import requests


def get_stkaave_balance(api_key, address):
    url = "https://api.etherscan.io/v2/api?chainid=1"
    params = {
        "module": "account",
        "action": "tokenbalance",
        "contractaddress": "0x4da27a545c0c5b758a6ba100e3a049001de870f5",  # Adresse du contrat stkAAVE
        "address": address,
        "tag": "latest",
        "apikey": api_key
    }
    response = requests.get(url, params=params)
    data = response.json()
    print(data)  # Affiche la réponse complète de l'API pour le débogage
    if data['status'] == '1':
        balance = int(data['result']) / 10**18  # Supposant que le token a 18 décimales
        return balance
    else:
        print(f"Erreur: {data['result']}")
        return None
    
def get_ether_balance(api_key, address):
    url = "https://api.etherscan.io/v2/api?chainid=1"
    params = {
        "module": "account",
        "action": "balance",
        "address": address,
        "tag": "latest",
        "apikey": api_key
    }
    response = requests.get(url, params=params)
    data = response.json()
    print(data)  # Affiche la réponse complète de l'API pour le débogage
    if data['status'] == '1':
        balance = int(data['result']) / 10**18  # Supposant que le token a 18 décimales
        return balance
    else:
        print(f"Erreur: {data['result']}")
        return None
 