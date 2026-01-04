import asyncio
from temporalio.client import Client

async def main():
    client = await Client.connect("temporal.motaniq.com:7233",tls=True)

    result = await client.execute_workflow(
        "SayHello",
        "Gemini",
        id="new_hello-workflow-id",
        task_queue="hello-queue",
    )

    print(f"Result: {result}")

if __name__ == "__main__":
    asyncio.run(main())