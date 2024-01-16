from dataclasses import dataclass

BID = []
ASK = []
mid_price = 12.21
growth_speed = 1.25
total_budget_bid = 5000
total_budget_ask = 5000

@dataclass
class Order:
    price: int
    value: int
    is_brick: bool

def init_build():
    #Generate 7 bricks on BID side
    bricks_budget_bid = 0.7*total_budget_bid
    first_bid_value = bricks_budget_bid / sum([1.25 ** i for i in range(7)])
    dif = [10, 15, 30, 45, 60, 75, 90]
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

def print_order_book():
    print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format("VALUE", "BID","---------","MID_PRICE","---------","ASK", "VALUE"))
    for i, (bid_order, ask_order) in enumerate(zip(BID, ASK)):
        mid_price_str = mid_price if i == 0 else "" 
        print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(round(bid_order.value, 2) ,round(bid_order.price, 3), "",mid_price_str,"", round(ask_order.price, 3), round(ask_order.value, 2)))

def main():
    init_build()
    print_order_book()

if __name__ == "__main__":
    main()