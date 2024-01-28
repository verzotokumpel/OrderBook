from dataclasses import dataclass
import random

BID = []
ASK = []
mid_price = 1
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
    non_bricks_budget_bid = 0.3*total_budget_bid
    non_bricks_budget_ask = 0.3*total_budget_ask
    group_budget_bid = []
    group_budget_ask = []

    first_bid_budget_value = non_bricks_budget_bid / sum([1.25 ** i for i in range(7)])
    for i in range(7):
        group_budget_bid.append(first_bid_budget_value * (growth_speed ** i))
    
    first_ask_budget_value = non_bricks_budget_ask / sum([1.25 ** i for i in range(9)])
    for i in range(9):
        group_budget_ask.append(first_ask_budget_value * (growth_speed ** i))
    
    #min_spread = 0.01
    for i in range(7):
        if(i==0):
            price1 = mid_price
        else:
            price1 = BID[i-1].price
        price2 = BID[i].price
        #min_spread += i/5
        dif = (price2 - price1)*100
        #max_spread = dif 
        num_orders = 50-len(BID) if i == 6 else int(random.uniform(4, 8))
        for j in range(num_orders):  
            x = random.uniform(price1, price2)
            while x in BID:
                x = random.uniform(price1, price2)
            order = Order(
                price=(x),
                value=group_budget_bid[i] if j == num_orders-1 else group_budget_bid[i] * (random.uniform(10, 50) / 100),
                is_brick=False
            )
            group_budget_bid[i] -= order.value
            BID.append(order)
    
    #min_spread = 0.01
    for i in range(9):
        if(i==0):
            price1 = mid_price
        else:
            price1 = ASK[i-1].price
        price2 = ASK[i].price
        #min_spread += i/7
        dif = (price2 - price1)/mid_price*100
        #max_spread = dif - min_spread
        num_orders = 50-len(ASK) if i == 8 else int(random.uniform(4, 6))
        for j in range(num_orders):
            x = random.uniform(price1, price2)
            while x in ASK:
                random.uniform(price1, price2)
            order = Order(
                price=(x),
                value=group_budget_ask[i] if j == num_orders-1 else group_budget_ask[i] * (random.uniform(10, 50) / 100),
                is_brick=False
            )
            group_budget_ask[i] -= order.value
            ASK.append(order)
  
    BID.sort(key=lambda x: x.price, reverse=True)
    ASK.sort(key=lambda x: x.price)
    

def print_order_book():
    total_bid_value = 0
    for order in BID:
        total_bid_value += order.value
    total_ask_value = 0
    for order in ASK:
        total_ask_value += order.value
    print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format("TOTAL BID VALUE:", round(total_bid_value, 2), "-----","-----","-------","-------","-----","-----", "TOTAL ASK VALUE:", round(total_ask_value, 2)))
    print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format("CTV", "AMOUNT", "VALUE", "BID","---------","MID_PRICE","---------","ASK", "VALUE", "AMOUNT", "CTV"))
    cumulative_ask = 0
    cumulative_bid = 0
    for i, (bid_order, ask_order) in enumerate(zip(BID, ASK)):
        cumulative_bid += bid_order.value
        cumulative_ask += ask_order.value
        mid_price_str = mid_price if i == 0 else "" 
        print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(f"{round(cumulative_bid/total_bid_value*100, 2)}%" ,round(bid_order.value/bid_order.price, 2),round(bid_order.value, 2) ,round(bid_order.price, 3), "",mid_price_str,"", round(ask_order.price, 3), round(ask_order.value, 2), round(ask_order.value/ask_order.price, 2), f"{round(cumulative_ask/total_ask_value*100, 2)}%"))

def main():
    init_build()
    generate_non_bricks()
    print_order_book()

if __name__ == "__main__":
    main()