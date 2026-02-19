```python
import yfinance as yf
import pandas as pd
import numpy as np

class GoldAgent:
    def __init__(self):
        self.gold_data = yf.download('GC=F', period='1d')

    def get_gold_price(self):
        return self.gold_data['Close'][-1]

    def get_gold_history(self):
        return self.gold_data

    def update_gold_data(self):
        self.gold_data = yf.download('GC=F', period='1d')

def main():
    agent = GoldAgent()
    print("Текущая цена золота: ", agent.get_gold_price())
    print("История цен золота: \n", agent.get_gold_history())

if __name__ == "__main__":
    main()
```