"""Example of using threads in python."""
import time
import logging
import pandas as pd
import yfinance as yf


def download_data(ticker: str, excel_writer: pd.ExcelWriter):
    """Download data from Yahoo Finance and save it to an excel file."""
    ticker_data = yf.Ticker(ticker=ticker)
    history = ticker_data.history()
    history.to_excel(excel_writer, sheet_name=ticker)


if __name__ == "__main__":
    start = time.perf_counter()
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    excel_writer = pd.ExcelWriter("ticker_data.xlsx", engine="xlsxwriter")

    tickers = [
        "3MINDIA.NS",
        "ABB.NS",
        "POWERINDIA.NS",
        "ACC.NS",
        "AIAENG.NS",
        "APLAPOLLO.NS",
        "AUBANK.NS",
        "AARTIDRUGS.NS",
        "AARTIIND.NS",
        "AAVAS.NS",
        "ABBOTINDIA.NS",
        "ADANIENT.NS",
        "ADANIGREEN.NS",
        "ADANIPORTS.NS",
        "ATGL.NS",
        "ADANITRANS.NS",
        "ABCAPITAL.NS",
        "ABFRL.NS",
        "ADVENZYMES.NS",
        "AEGISCHEM.NS",
        "AFFLE.NS",
        "AJANTPHARM.NS",
        "AKZOINDIA.NS",
        "ALEMBICLTD.NS",
        "APLLTD.NS",
        "ALKEM.NS",
        "ALKYLAMINE.NS",
        "ALOKINDS.NS",
        "AMARAJABAT.NS",
        "AMBER.NS",
        "AMBUJACEM.NS",
        "APOLLOHOSP.NS",
        "APOLLOTYRE.NS",
        "ASHOKLEY.NS",
        "ASHOKA.NS",
        "ASIANPAINT.NS",
        "ASTERDM.NS",
        "ASTRAZEN.NS",
        "ASTRAL.NS",
        "ATUL.NS",
        "AUROPHARMA.NS",
        "AVANTIFEED.NS",
        "DMART.NS",
        "AXISBANK.NS",
        "BASF.NS",
        "BEML.NS",
        "BSE.NS",
        "BAJAJ-AUTO.NS",
        "BAJAJCON.NS",
        "BAJAJELEC.NS",
        "BAJFINANCE.NS",
        "BAJAJFINSV.NS",
        "BAJAJHLDNG.NS",
        "BALKRISIND.NS",
        "BALMLAWRIE.NS",
        "BALRAMCHIN.NS",
        "BANDHANBNK.NS",
        "BANKBARODA.NS",
        "BANKINDIA.NS",
        "MAHABANK.NS",
        "BATAINDIA.NS",
        "BAYERCROP.NS",
        "BERGEPAINT.NS",
        "BDL.NS",
        "BEL.NS",
        "BHARATFORG.NS",
        "BHEL.NS",
        "BPCL.NS",
        "BHARATRAS.NS",
        "BHARTIARTL.NS",
        "BIOCON.NS",
        "BIRLACORPN.NS",
        "BSOFT.NS",
        "BLISSGVS.NS",
        "BLUEDART.NS",
        "BLUESTARCO.NS",
        "BBTC.NS",
        "BOMDYEING.NS",
        "BOSCHLTD.NS",
        "SBIN.NS",
        "HDFCBANK.NS",
    ]

    for ticker in tickers:
        download_data(ticker=ticker, excel_writer=excel_writer)

    end = time.perf_counter()
    excel_writer.save()
    logging.info(f"Data downloaded for all tickers in {end - start}")
