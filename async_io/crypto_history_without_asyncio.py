"""Asyncio example.

Downloading history for cryptocurrencies using free apis at https://docs.coincap.io
"""

import time
import requests
import logging
import pandas as pd


def download_history() -> None:

    crypto_ids = ["bitcoin", "ethereum", "ripple", "bitcoin-cash", "eos", "stellar", "litecoin", "cardano", "tether", "iota", "tron", "ethereum-classic", "monero", "neo", "dash", "binance-coin", "nem", "tezos", "zcash", "omisego", "vechain", "qtum", "0x", "bitcoin-gold"]

    excel_writer = pd.ExcelWriter("data_file.xlsx", engine="xlsxwriter")

    session = requests.Session()
    for crypto_id in crypto_ids:
        logging.info(f"Fetching history for {crypto_id}")
        response = session.get(f"https://api.coincap.io/v2/assets/{crypto_id}/history?interval=d1")

        if response.status_code == 200:
            response_data = response.json()
            pd.DataFrame(response_data["data"]).to_excel(excel_writer, sheet_name=crypto_id)
            logging.info(f"Fetched history for {crypto_id}")
    
    excel_writer.save()

    
if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")    
    
    start_time = time.perf_counter()
    download_history()
    end_time = time.perf_counter()
    logging.info(f"Execution done in {end_time - start_time} seconds")