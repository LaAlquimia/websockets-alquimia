import asyncio, os
from binance import AsyncClient, BinanceSocketManager 


async def main():
	client = await AsyncClient.create()
	bm = BinanceSocketManager(client)
	sts = bm.symbol_ticker_socket("BTCUSDT")


	async with sts as sm :
		while True:
			res = await sm.recv()
			os.system("clear")
			print(
				f"CHANGE BTC : \n{res['P']}%"
				)


if __name__ == "__main__":
	loop = asyncio.get_event_loop()
	loop.run_until_complete(main())







