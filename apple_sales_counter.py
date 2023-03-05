from datetime import datetime
from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class Transaction:
    apples_count: int
    time: datetime

class SalesCounterInterface(ABC):
    @abstractmethod
    def save_transaction_info(self, apples_count: int):
        pass

    @abstractmethod
    def get_apple_sales(self, start: datetime, end: datetime) -> int:
        """Returns number of sold apples between start and end."""
        pass

class SalesCounterSlow(SalesCounterInterface):
    def __init__(self):
        self.sales_data = []

    def __repr__(self):
        return f"{self.sales_data}"

    def save_transaction_info(self, apples_count: int):
        transaction = Transaction(apples_count, datetime.now())
        self.sales_data.append(transaction)
        print(f"Sold {apples_count} apples at {transaction.time}")


    def get_apple_sales(self, start: datetime, end: datetime) -> int:
        """Returns number of sold apples between start and end."""
        print(f"Returning apples sold between {start} and {end}")
        counter = 0
        for transaction in self.sales_data:
            if start <= transaction.time <= end:
                counter += transaction.apples_count

        return counter

def binary_search(arr, start, end, x):

    # Check base case
    if start >= end:

        mid = (start + end) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, end, mid - 1, x)

        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, start, x)

    else:
        # Element is not present in the array
        return -1

class SalesCounterFaster(SalesCounterInterface):
    # Znalezc pierwsza date po start, i druga date przed end

    def __init__(self):
        self.sales_data = []

    def __repr__(self):
        return f"{self.sales_data}"

    def save_transaction_info(self, apples_count: int):
        transaction = Transaction(apples_count, datetime.now())
        self.sales_data.append(transaction)
        print(f"Sold {apples_count} apples at {transaction.time}")


    def get_apple_sales(self, start: datetime, end: datetime) -> int:
        """Returns number of sold apples between start and end."""
        print(f"Returning apples sold between {start} and {end}")
        counter = 0
        for transaction in self.sales_data:
            if start <= transaction.time <= end:
                counter += transaction.apples_count

        return counter