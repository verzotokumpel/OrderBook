from dataclasses import dataclass

BID = []
ASK = []
mid_price = 12.21

@dataclass
class Order:
    price: int
    value: int
    is_brick: bool

def init_build():
    #Generate 7 bricks on BID side
    dif = [10, 15, 30, 45, 60, 75, 90]
    for i in range(7):
        order = Order(
            price=mid_price-mid_price*dif[i]/100,
            value=0,
            is_brick=True
        )
        BID.append(order)

    #Generate 9 bricks on ASK side
    dif = [10, 18, 23, 40, 60, 80, 110, 140, 200]
    for i in range (9):
        order = Order(
            price=mid_price+mid_price*dif[i]/100,
            value=0,
            is_brick=True
        )
        ASK.append(order)

def print_order_book():
    print("{:<10} {:<10} {:<10}".format("BID", "MID_PRICE","ASK"))
    for i, (bid_order, ask_order) in enumerate(zip(BID, ASK)):
        mid_price_str = mid_price if i == 0 else "" 
        print("{:<10} {:<10} {:<10}".format(bid_order.price, mid_price_str, ask_order.price))

def main():
    init_build()
    print_order_book()

if __name__ == "__main__":
    main()