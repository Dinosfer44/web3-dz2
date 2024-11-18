from web3 import Web3
from datetime import datetime

w3 = Web3(Web3.HTTPProvider("https://rpc.ankr.com/eth"))
if w3.is_connected():
    print("Соединение установлено!")
else:
    print("Не удалось установить соединение.")
block_number = input("Введите номер блока: ")
block = w3.eth.get_block(block_number)
block_hash = block['hash']
print(f"Хэш блока: {block_hash}")
block_time = datetime.utcfromtimestamp(block['timestamp']).strftime('%Y-%m-%d %H:%M:%S')
print (f"Время создания блока: {block_time}")
transaction_count = len(block['transactions'])
print (f"Количество транзакций в блоке: {transaction_count}")