import asyncio
import time

# first task
async def api_call(url:str, delay:int=3):
    print("Fetching data from:", url)
    await asyncio.sleep(delay)
    print("Data fetched from:", url)

# second task
async def execution():
    time.sleep(5)
    print("Execution completed")

# third task

async def transformation():
    time.sleep(4)
    print("Data transformation completed")


async def main():
    tasks = await asyncio.gather(
        api_call("https://api1.com"),
        execution(),
        transformation()
    )

    print("All API calls and tasks completed:")

asyncio.run(main())