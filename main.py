from dataclasses import dataclass
import random

BID = []
ASK = []
mid_price = 12.21
total_budget_bid = 5000
total_budget_ask = 5000
growth_speed = 1.25

@dataclass
class Order:
    price: int
    value: int
    is_brick: bool

def init_build():
    #Generate 7 bricks on BID side
    bricks_budget_bid = 0.7*total_budget_bid
    first_bid_value = bricks_budget_bid / sum([1.25 ** i for i in range(7)])
    dif = [10, 20, 30, 45, 60, 75, 90]
    for i in range(7):
        order = Order(
            price=mid_price-mid_price*dif[i]/100,
            value=first_bid_value * (growth_speed ** i),
            is_brick=True
        )
        BID.append(order)

    #Generate 9 bricks on ASK side
    bricks_budget_ask = 0.7*total_budget_ask
    first_ask_value = bricks_budget_ask / sum([1.25 ** i for i in range(9)])
    dif = [10, 18, 23, 40, 60, 80, 110, 140, 200]
    for i in range (9):
        order = Order(
            price=mid_price+mid_price*dif[i]/100,
            value=first_ask_value * (growth_speed ** i),
            is_brick=True
        )
        ASK.append(order)

def generate_non_bricks():
    min_spread = 0.5
    max_spread = 2.5
    non_bricks_budget_bid = 0.3*total_budget_bid
    non_bricks_budget_ask = 0.3*total_budget_ask
    group_budget_bid = []
    group_budget_ask = []

    first_bid_budget_value = non_bricks_budget_bid / sum([1.25 ** i for i in range(7)])
    for i in range(7):
        group_budget_bid.append(first_bid_budget_value * (growth_speed ** i))
    
    first_ask_budget_value = non_bricks_budget_ask / sum([1.25 ** i for i in range(7)])
    for i in range(9):
        group_budget_ask.append(first_ask_budget_value * (growth_speed ** i))


       
    #     group_budget_bid.append(non_bricks_budget_bid*random.uniform(10, 50)/100)
    #     non_bricks_budget_bid -= group_budget_bid[i]
    # group_budget_bid.append(non_bricks_budget_bid)

    for i in range(7):
        print(group_budget_bid[i])

    BID.sort(key=lambda x: x.price, reverse=True)
    ASK.sort(key=lambda x: x.price)
    

def print_order_book():
    print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format("VALUE", "BID","---------","MID_PRICE","---------","ASK", "VALUE"))
    for i, (bid_order, ask_order) in enumerate(zip(BID, ASK)):
        mid_price_str = mid_price if i == 0 else "" 
        print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(round(bid_order.value, 2) ,round(bid_order.price, 3), "",mid_price_str,"", round(ask_order.price, 3), round(ask_order.value, 2)))

def main():
    init_build()
    generate_non_bricks()
    #print_order_book()

if __name__ == "__main__":
    main()