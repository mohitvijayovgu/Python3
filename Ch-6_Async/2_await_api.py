# import time

# def api_call():
#     time.sleep(3)
#     return "orders data"

# def execute():
#     print("Executing API call")
#     result = api_call()
#     print("Data Fetched:", result)

# execute()

#Async API Calss
import asyncio

async def api_call():
    await asyncio.sleep(3)
    return "orders data"

async def execute():
    print("Executing API calls")
    result = await api_call()
    print("Data fetched:", result)

asyncio.run(execute())