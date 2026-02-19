Код агента для проверки цен на золото может выглядеть следующим образом:
```python
import requests
import json

# URL API для получения текущей цены золота
url = 'https://api.example.com/gold-price'

# Функция для получения цены золота
def get_gold_price():
    response = requests.get(url)
    data = json.loads(response.text)
    return data['price']

# Функция для сравнения текущей цены с предыдущей ценой
def compare_price(current_price, previous_price):
    if current_price > previous_price:
        return 'Цена золота увеличилась'
    elif current_price < previous_price:
        return 'Цена золота уменьшилась'
    else:
        return 'Цена золота не изменилась'

# Основная функция агента
def main():
    previous_price = None
    while True:
        current_price = get_gold_price()
        if previous_price is not None:
            print(compare_price(current_price, previous_price))
        previous_price = current_price
        # Задержка между запросами (например, 1 минута)
        import time
        time.sleep(60)

if __name__ == '__main__':
    main()
```
Этот код агента использует библиотеку `requests` для отправки GET-запроса к API для получения текущей цены золота. Затем он сравнивает текущую цену с предыдущей ценой и выводит сообщение о изменении цены.

Обратите внимание, что в этом примере используется фиктивный URL API, и вам необходимо заменить его на реальный URL API для получения цены золота.

Также, для реализации задержки между запросами, используется функция `time.sleep()`, которая приостанавливает выполнение программы на указанное время.

Вы можете изменить этот код для своих нужд и добавить дополнительную функциональность, например, отправку уведомлений при изменении цены или сохранение истории цен.