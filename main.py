from scripts.get_balances_cli import get_stkaave_balance
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")
address = os.getenv("ADDRESS")
stkaave_balance = get_stkaave_balance(api_key, address)
if stkaave_balance is not None:
    print(f"Balance de stkAAVE: {stkaave_balance}")
else:
    print("Échec de la récupération de la balance.")