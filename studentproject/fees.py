fees={}
def pay_fees(roll,amount):
    fees[roll]=fees.get(roll,0)+amount

def get_fees(roll):
    return fees.get(roll,0)