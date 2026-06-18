import asyncio
import time

# Coroutine function
async def main():
    print("Hello")
    asyncio.sleep(3)
    print("World")

asyncio.run(main())
