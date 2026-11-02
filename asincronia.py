
import asyncio

async def tarea():
    print("Iniciando tarea...")
    await asyncio.sleep(2)
    print("Tarea finalizada")

asyncio.run(tarea())
