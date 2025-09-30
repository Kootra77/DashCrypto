from scripts.get_balances_cli import get_stkaave_balance, get_ether_balance
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")
address = os.getenv("ADDRESS")

ether_balance = get_ether_balance(api_key, address)
stkaave_balance = get_stkaave_balance(api_key, address)


if stkaave_balance is not None:
    print(f"Balance de stkAAVE: {stkaave_balance}")
else:
    print("Échec de la récupération de la balance.")

if stkaave_balance is not None:
    print(f"Balance d'Ether: {ether_balance}")
else:
    print("Échec de la récupération de la balance.")


