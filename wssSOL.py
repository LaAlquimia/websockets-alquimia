import asyncio, os
from binance import AsyncClient, BinanceSocketManager 


async def main():
	client = await AsyncClient.create()
	bm = BinanceSocketManager(client)
	sts = bm.trade_socket("SOLUSDT")


	async with sts as sm :
		while True:
			res = await sm.recv()
			os.system("clear")
			print(
				f"SOL price: \n{float(res['p'])}"
				)


if __name__ == "__main__":
	loop = asyncio.get_event_loop()
	loop.run_until_complete(main())







