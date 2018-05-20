#!/usr/bin/env python

import sqlite3
from drama import dramatic_typing
import datetime


def fetch_best_bid(currency):
    connection = sqlite3.connect('./currency_monitor.db')
    cursor = connection.cursor()
    query = """
            SELECT 
                max(bid),
                timestamp 
            FROM prices 
            WHERE 
                first_leg = '{}' and 
                second_leg = 'USD' and 
                timestamp > '1520408341.52'
            """.format(currency)
    cursor.execute(query)
    rows = cursor.fetchone()
    return rows[0], rows[1]


def run_simulation(bought_price, quantity, currency):
    value_then = bought_price * quantity
    best_price, timestamp = fetch_best_bid(currency)
    best_value = best_price * quantity
    price_difference = (best_value - value_then)/float(value_then) * 100
    time = datetime.datetime.fromtimestamp(timestamp).strftime('%A, %B %-d, %Y %I:%M %p')
    print("The best bid price for {} was ${} at {} \n".format(currency, best_price, time))
    if price_difference > 0:
        dramatic_typing("Your total asset value is ${}, it has increased by {}% \n".format(round(best_value, 4), round(price_difference, 2)))
    else:
        dramatic_typing("Your total asset value is ${}, it has decreased by {} \n".format(round(best_value, 4), round(price_difference, 2)))
