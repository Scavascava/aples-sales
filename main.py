from datetime import datetime
import random
from time import sleep
from apple_sales_counter import SalesCounterInterface, SalesCounterSlow
from typing import Type

# def add_transactions(transaction_count: int) -> AppleSalesCounter:
#     apple_sales = AppleSalesCounter()
#     for i in transaction_count:
#         apple_sales.save_transaction_info(random.randint(1, 100))
#     return apple_sales


def test_sales_counter(sales_counter_cls: Type[SalesCounterInterface]):
    apple_sales = sales_counter_cls()
    apple_sales.save_transaction_info(4)
    sleep(0.1)
    t1 = datetime.now()
    apple_sales.save_transaction_info(84)
    apple_sales.save_transaction_info(90)
    sleep(0.1)
    t2 = datetime.now()
    sleep(0.1)
    apple_sales.save_transaction_info(1)
    counter = apple_sales.get_apple_sales(t1, t2)
    print(counter)

def main():
    test_sales_counter(SalesCounterSlow)


if __name__ == '__main__':
    main()
