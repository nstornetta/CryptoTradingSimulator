#!/usr/bin/env python
import sqlite3
from simulator import run_simulation
from drama import dramatic_typing


def fetch_coins():
    connection = sqlite3.connect('./currency_monitor.db')
    cursor = connection.cursor()
    query = "SELECT first_leg, ask FROM prices WHERE timestamp='1520408341.52' AND second_leg='USD';"
    cursor.execute(query)
    coin_ask_prices = cursor.fetchall()
    coins = {}
    for coin_ask_price in coin_ask_prices:
        if coin_ask_price[0] in coins:
            continue
        coins[coin_ask_price[0]] = {"price": coin_ask_price[1], "curreny": coin_ask_price[0]}
        dramatic_typing("{} - ${} \n".format(coin_ask_price[0], round(coin_ask_price[1], 4)))
    return coins


def welcome():
    print("\n")
    dramatic_typing("Simple Crypto Trading Simulator \n")
    dramatic_typing("Hey Yo, you are back in time. It's Wednesday, March 7, 2018 7:39 AM \n")
    dramatic_typing("Here are the crypto currencies you can invest. \n")
    dramatic_typing("Fetching prices ... \n")


def input_buy():
    dramatic_typing("Select the crypto currency you want to buy? \n")
    currency = input("").upper()
    dramatic_typing("That's great. How much quantity you want to buy? \n")
    quantity = float(input(""))
    return currency, quantity

def quitMenu():
    dramatic_typing("Do you want to try again? Y/N ")
    answer = input("").upper()
    if answer == 'Y':
        main()
    else:
        exit()


def main():
    welcome()
    coins = fetch_coins()
    currency, quantity = input_buy()
    try:
        price = coins[currency]['price']
    except Exception as e:
        dramatic_typing("Invalid currency entered, please try again \n")
        input_buy()
    run_simulation(coins[currency]['price'], quantity, currency)
    quitMenu()

main()
