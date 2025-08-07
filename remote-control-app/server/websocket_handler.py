import asyncio
import websockets
import json

clients = set()

async def handler(websocket, path):
    clients.add(websocket)
    try:
        async for message in websocket:
            pass
    finally:
        clients.remove(websocket)

def broadcast(data):
    asyncio.run(_broadcast(data))

async def _broadcast(data):
    for client in clients:
        await client.send(json.dumps(data))

def start_server():
    loop = asyncio.get_event_loop()
    server = websockets.serve(handler, "0.0.0.0", 8765)
    loop.run_until_complete(server)
    threading.Thread(target=loop.run_forever).start()
