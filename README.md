# UTXO Scanner

**UTXO Scanner** — инструмент для анализа нераспределённых выходов (UTXO) конкретного Bitcoin-адреса.

## Возможности

- Получает все UTXO заданного адреса
- Фильтрует по минимальной сумме
- Показывает hash, индекс, сумму

## Установка

```bash
pip install -r requirements.txt
```

## Использование

```bash
python utxo_scanner.py <address> --min 1000
```

## Пример

```bash
python utxo_scanner.py 1BoatSLRHtKNngkdXEeobR76b53LETtpyT --min 500
```

## Применение

- Отладка кошельков
- Подготовка к сбору UTXO
- Анализ распределения остатков

## Лицензия

MIT License
