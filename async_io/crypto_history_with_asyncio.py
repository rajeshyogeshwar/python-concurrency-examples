"""Asyncio example.

Downloading history for cryptocurrencies using free apis at https://docs.coincap.io
"""

import time
import asyncio
import aiohttp
import logging
import pandas as pd

async def fetch(session: aiohttp.ClientSession, crypto_id: str):
    async with session.get(f"https://api.coincap.io/v2/assets/{crypto_id}/history?interval=d1") as response:
        if response.status == 200:
            response_data = await response.json()
            return crypto_id, response_data["data"]
        return None


async def download_history() -> None:

    crypto_ids = ["bitcoin", "ethereum", "ripple", "bitcoin-cash", "eos", "stellar", "litecoin", "cardano", "tether", "iota", "tron", "ethereum-classic", "monero", "neo", "dash", "binance-coin", "nem", "tezos", "zcash", "omisego", "vechain", "qtum", "0x", "bitcoin-gold"]
    
    excel_writer = pd.ExcelWriter("data_file.xlsx", engine="xlsxwriter")
    
    tasks = list()
    async with aiohttp.ClientSession() as session:
        for crypto_id in crypto_ids:
            task = asyncio.ensure_future(fetch(session, crypto_id))
            tasks.append(task)
        
        results = await asyncio.gather(*tasks)
        for item in results:
            if item is not None:
                crypto_id = item[0]
                data = item[1]
                pd.DataFrame(data).to_excel(excel_writer=excel_writer, sheet_name=crypto_id)
    
    excel_writer.save()

    
if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")    
    
    start_time = time.perf_counter()
    asyncio.run(download_history())
    end_time = time.perf_counter()
    logging.info(f"Execution done in {end_time - start_time} seconds")