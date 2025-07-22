import asyncio
import time

def task(id, delay):
    print(f"開始 {id}")
    time.sleep(delay)
    print(f"任務 {id} 完成")

async def main():
    start = time.time()
    tasks =[task(1,1), task(2,2)]
    await asyncio.gather(*tasks)
    print(f"總耗時 :{time.time()-start: .2f} 秒")

asyncio.run(main())


