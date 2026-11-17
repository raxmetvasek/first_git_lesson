import asyncio 
async def task(name, delay):
	print(f"[{name}] начал работу")
	await asyncio.sleep(delay)
	print(f"[{name}] закончил работу")
async def main():
	await asyncio.gather(
		task("A", 2),
		task("B", 1),
		task("C", 5)
		)
asyncio.run(main())
