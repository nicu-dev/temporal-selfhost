import asyncio
from temporalio import workflow
from temporalio.client import Client
from temporalio.worker import Worker

@workflow.defn
class SayHello:
    @workflow.run
    async def run(self, name: str) -> str:
        return f"Hello, {name}!"

async def main():
    client = await Client.connect("127.0.0.1:7233")
    print("Directly connected to Temporal Server on 127.0.0.1:7233")
    
    worker = Worker(
        client,
        task_queue="hello-queue",
        workflows=[SayHello],
    )
    print("Worker started. Check your Temporal UI!")
    await worker.run()

if __name__ == "__main__":
    asyncio.run(main())