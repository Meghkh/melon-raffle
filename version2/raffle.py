"""Randomly pick customer and print customer info"""

# Add code starting here
from customers import get_customers_from_file
from random import choice

# Hint: remember to import any functions you need from
# other files or libraries


def pick_winner(customers):
    raffle_winner = choice(customers)

    print "Tell {name} at {email} that they won.".format(
        name=raffle_winner.name,
        email=raffle_winner.email
        )


def run_raffle():

    customers_from_file = get_customers_from_file("customers.txt")
    pick_winner(customers_from_file)


run_raffle()
