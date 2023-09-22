import requests
import os
import telebot
import telegram
global bot
global TOKEN

TOKEN = "6532498978:AAF-Qw5hPWWzpY8OxdAcxR4QZYf9qYbpdSQ"
bot = "TOKEN"

def get_token_balance(contract_address, wallet_address):
    # Ethereum API endpoint
    api_url= f"https://api.etherscan.io/api?module=account&action=tokenbalance&contractaddress={contract_address}&address={wallet_address}&tag=latest&apikey=12PZC6WTM7EJJFJBSCXE9W67D2XY5I1UZA"

    try:
        response = requests.get(api_url)
        data = response.json()
        balance = int(data['result']) / 10**18  # Convert balance to token units
        return balance
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def main():
    contract_address = input("Enter the Ethereum contract address: ")
    wallet_address = input("Enter the wallet address to check: ")

    balance = get_token_balance(contract_address, wallet_address)
    if balance is not None:
        print(f"The wallet holds {balance} tokens.")
     

    bot.infinity_polling()