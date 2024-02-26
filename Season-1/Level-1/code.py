'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''

from collections import namedtuple

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

MAX_AMOUNT=100000
MAX_TOTAL=1000000

def validorder(order: Order):
    product = float(0)
    payment = float(0)
    
    
    print("calcul order id :" + order.id)
    for item in order.items:
        print("ITEM Type : " + item.type + " Amount :" + "{:10.2f}".format(item.amount))
        if item.type == 'payment':
            if -MAX_AMOUNT < item.amount < MAX_AMOUNT:
                payment += float("{:10.2f}".format(item.amount))
                print("Payment :" + "{:10.2f}".format(payment))
        elif item.type == 'product':
            if -MAX_AMOUNT < item.amount < MAX_AMOUNT:
                product += float(item.amount) * float(item.quantity)
                
        else:
            return "Invalid item type: %s" % item.type

    print("PAYMENT : "+ "{:10.2f}".format(payment) + " PRODUCT :" + "{:10.2f}".format(product) )
    if payment > MAX_TOTAL:
        return "Total amount payable for an order exceeded" 
    if "{:10.2f}".format(payment) != "{:10.2f}".format(product) :
        return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, payment-product)
    else:
        return "Order ID: %s - Full payment received!" % order.id