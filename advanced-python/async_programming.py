import asyncio


async def task(name):
    print(f"Starting task {name}")
    await asyncio.sleep(2)
    print(f"Finished task {name}")


async def main():
    await asyncio.gather(task("Task-1"), task("Task-2"))


asyncio.run(main())