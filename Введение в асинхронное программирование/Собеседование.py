import asyncio
import time


async def do_task(name, task_num, prep_time, defend_time):
    print(f"{name} started the {task_num} task.")
    await asyncio.sleep(prep_time)
    print(f"{name} moved on to the defense of the {task_num} task.")
    await asyncio.sleep(defend_time)
    print(f"{name} completed the {task_num} task.")


async def interviews(*candidates):
    tasks = []
    for i, candidate in enumerate(candidates, start=1):
        name, prep_time1, defend_time1, prep_time2, defend_time2 = candidate
        task1 = asyncio.create_task(do_task(name, 1, prep_time1, defend_time1))
        tasks.append(task1)
        await asyncio.sleep(0)  # Allow other tasks to run while waiting
        task2 = asyncio.create_task(do_task(name, 2, prep_time2, defend_time2))
        tasks.append(task2)
        await asyncio.sleep(0)  # Allow other tasks to run while waiting
    await asyncio.gather(*tasks)


data = [('Ivan', 5, 2, 7, 2), ('John', 3, 4, 5, 1), ('Sophia', 4, 2, 5, 1)]
t0 = time.time()
asyncio.run(interviews(*data))
print(time.time() - t0)
