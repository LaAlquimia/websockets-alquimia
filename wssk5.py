import asyncio, os
from binance import AsyncClient, BinanceSocketManager 
from binance.enums import *

async def main():
	client = await AsyncClient.create()
	bm = BinanceSocketManager(client)
	sts = bm.kline_socket("KDJUSDT", interval = KLINE_INTERVAL_1HOUR)


	async with sts as sm :
		while True:
			res = await sm.recv()
			os.system("clear")
			cl = float(res['k']['c'])
			op = float(res['k']['o'])
			hi = float(res['k']['h'])
			lo = float(res['k']['l'])
			pct = cl/100


			print(
				f"BITCOIN H1\nPorcentaje Open/Close:\n{float(cl-op)/pct}\nPorcentaje High/Low:\n{float(hi-lo)/pct}"
				)


if __name__ == "__main__":
	loop = asyncio.get_event_loop()
	loop.run_until_complete(main())







