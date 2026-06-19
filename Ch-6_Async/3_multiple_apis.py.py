import asyncio

async def api_call(url:str, delay:int):
    print("Fetching data from:", url)
    await asyncio.sleep(delay)
    print("Data fetched from:", url)
    return f"{url} data"

# async def execute():
#     result = await api_call("orders")
#     print("Data fetched:", result)

async def main():
    tasks = await asyncio.gather(
        api_call("https://api1.com", 3),
        api_call("https://api2.com", 2),
        api_call("https://api3.com", 1)
    )

    print("All data fetched:", tasks)



asyncio.run(main())