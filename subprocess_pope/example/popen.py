import os
import sys
import time
import asyncio

def get_cmds():
    """ Creates tasks """
    workdir = "/github/aigo/map/data/"
    ext = r".img"
    files = [os.path.join(dir,_) for _ in os.listdir(dir) if _.endswith(ext)]
    task = []
    for file in files:
        cmd =  ["/home/ubuntu/miniconda3/bin/python",
                "factory.py",
                f"{file}",]
        task.append(cmd)
    return task

async def run_command(*args):
    """ Run tasks """
    process = await asyncio.create_subprocess_exec(
        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )

    print(
        f"started: {args}, pid: {process.pid}", flush=True
    )

    stdout, stderr = await process.communicate()

    if process.returncode == 0:
        print(
            "Done: {}, pid: {}, result: \n\n{}".format(args, process.pid, stdout.decode()),sep='\n',flush=True
        )
    else:
        print(
            "Failed: {}, pid: {}, result: \n\n{}".format(args, process.pid, stderr.decode()),sep='\n',flush=True
        )


def run_asyncio_commands(tasks, max_concurrent_tasks=0):
    """Run tasks asynchronously using asyncio"""

    if max_concurrent_tasks == 0:
        chunks = [tasks]
        num_chunks = len(chunks)
    else:
        chunks = make_chunks(l=tasks, n=max_concurrent_tasks)
        num_chunks = len(list(make_chunks(l=tasks, n=max_concurrent_tasks)))

    if asyncio.get_event_loop().is_closed():
        asyncio.set_event_loop(asyncio.new_event_loop())
    loop = asyncio.get_event_loop()

    chunk = 1
    for tasks_in_chunk in chunks:
        print(
            "Beginning work on chunk {}/{}".format(chunk, num_chunks), flush=True
        )
        commands = asyncio.gather(*tasks_in_chunk)  # Unpack arguments in list
        loop.run_until_complete(commands)
        print(
            "Completed work on chunk {}/{}".format(chunk, num_chunks), flush=True
        )
        chunk += 1

    loop.close()

def make_chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i : i + n]



def main():
    start = time.time()

    commands = get_cmds()
    tasks = []
    for command in commands:
        tasks.append(run_command(*command))

    run_asyncio_commands(
            tasks, max_concurrent_tasks=5
    )  # At most 20 parallel tasks

    end = time.time()
    rounded_end = "{0:.4f}".format(round(end - start, 4))
    print(
        "Script ran in about {} seconds".format(rounded_end), flush=True
    )


if __name__ == "__main__":
    main()

