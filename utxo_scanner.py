"""
UTXO Scanner — утилита для поиска UTXO по Bitcoin-адресу с фильтрацией по сумме.
"""

import requests
import argparse

def get_utxos(address, min_value=0):
    url = f"https://api.blockchair.com/bitcoin/dashboards/address/{address}?limit=100"
    r = requests.get(url)
    if r.status_code != 200:
        raise Exception("❌ Не удалось получить данные по адресу.")

    utxos = r.json()["data"][address]["utxo"]
    filtered = [u for u in utxos if u["value"] >= min_value]
    return filtered

def scan_utxos(address, min_value=0):
    print(f"🔍 Поиск UTXO для адреса: {address}")
    utxos = get_utxos(address, min_value)
    if not utxos:
        print("🕳️ Нет UTXO, соответствующих фильтру.")
        return

    total = sum(u["value"] for u in utxos)
    print(f"🪙 Найдено UTXO: {len(utxos)}")
    print(f"💰 Общая сумма: {total} сатоши")
    print()

    for i, u in enumerate(utxos, 1):
        print(f"{i}. TX: {u['transaction_hash']} | Index: {u['index']} | Сумма: {u['value']} сатоши")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="UTXO Scanner — фильтр по нераспределённым выходам.")
    parser.add_argument("address", help="Bitcoin-адрес")
    parser.add_argument("-m", "--min", type=int, default=0, help="Минимальная сумма (сатоши)")
    args = parser.parse_args()

    scan_utxos(args.address, args.min)
