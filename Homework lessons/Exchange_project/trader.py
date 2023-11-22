import json
import argparse
import random
import os

def read_config():
    with open('config.json', 'r') as config_file:
        config_data = json.load(config_file)
    return config_data

def read_system_status():
    if os.path.exists('System_status.json'):
        with open('System_status.json', 'r') as status_file:
            return json.load(status_file)
    return None

def save_system_status(system_status):
    rounded_system_status = {
        "rate": round(system_status["rate"], 2),
        "uah_amount": round(system_status["uah_amount"], 2),
        "usd_amount": round(system_status["usd_amount"], 2)
    }
    with open('System_status.json', 'w') as status_file:
        json.dump(rounded_system_status, status_file, indent=2)

def get_rate(system_status):
    print(system_status["rate"])

def get_available_balance(system_status):
    usd_amount_rounded = round(system_status['usd_amount'], 2)
    uah_amount_rounded = round(system_status['uah_amount'], 2)
    print(f"USD {usd_amount_rounded} UAH {uah_amount_rounded}")

def get_buy_usd(system_status, amount):
    required_balance_uah = amount * system_status["rate"]
    if system_status["uah_amount"] >= required_balance_uah:
        system_status["uah_amount"] -= required_balance_uah
        system_status["usd_amount"] += amount
        print("Purchase successful.")
        save_system_status(system_status)
    else:
        print(f"UNAVAILABLE, REQUIRED BALANCE UAH {required_balance_uah:.2f}, AVAILABLE {system_status['uah_amount']:.2f}")

def get_sell_usd(system_status, amount):
    if system_status["usd_amount"] >= amount:
        system_status["uah_amount"] += amount * system_status["rate"]
        system_status["usd_amount"] -= amount
        print("Sale successful.")
        save_system_status(system_status)
    else:
        print(f"UNAVAILABLE, REQUIRED BALANCE USD {amount:.2f}, AVAILABLE {system_status['usd_amount']:.2f}")

def get_sell_all(system_status):
    get_sell_usd(system_status, system_status["usd_amount"])

def get_buy_all(system_status):
    max_buy_usd = system_status["uah_amount"] / system_status["rate"]
    get_buy_usd(system_status, max_buy_usd)

def get_next_rate(system_status, initial_config):
    new_rate = round(random.uniform(system_status["rate"] - initial_config["delta"], system_status["rate"] + initial_config["delta"]), 2)
    system_status["rate"] = new_rate
    print("New rate:", new_rate)
    save_system_status(system_status)

def get_restart(initial_config):
    save_system_status(initial_config)
    print("Game restarted.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Amount Trader Last lesson")
    parser.add_argument('action', nargs='?', choices=['RATE', 'AVAILABLE', 'BUY_X', 'SELL_X', 'BUY_ALL', 'SELL_ALL', 'NEXT', 'RESTART'],
                        help='Specify the action you want to perform!')
    parser.add_argument('amount', nargs='?', type=float, help='USD Amount to buy or sell')
    args = parser.parse_args()

    initial_config = read_config()
    system_status = read_system_status()

    if system_status is None:
        system_status = {
            "rate": initial_config["rate"],
            "uah_amount": initial_config["initial_balance_uah"],
            "usd_amount": initial_config["initial_balance_usd"],
        }

    if args.action == 'RATE':
        get_rate(system_status)
    elif args.action == 'AVAILABLE':
        get_available_balance(system_status)
    elif args.action == 'BUY_X':
        if args.amount is not None:
            get_buy_usd(system_status, args.amount)
        else:
            print("Please provide the amount for BUY_XXX")
    elif args.action == 'SELL_X':
        if args.amount is not None:
            get_sell_usd(system_status, args.amount)
        else:
            print("Please provide the amount for SELL_XXX")
    elif args.action == 'SELL_ALL':
        get_sell_all(system_status)
    elif args.action == 'BUY_ALL':
        get_buy_all(system_status)
    elif args.action == 'NEXT':
        get_next_rate(system_status, initial_config)
    elif args.action == 'RESTART':
        get_restart(initial_config)
    else:
        print("Unknown action:", args.action)