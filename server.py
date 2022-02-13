#!/usr/bin/env python

import asyncio
import datetime
import json
import random
import websockets

async def show_time(websocket):
    while websocket.open:
        #await websocket.send(datetime.datetime.utcnow().isoformat() + "Z")
        print("sending data")

        coords = [int(random.random() * 400),  int(random.random() * 400)]

        await websocket.send(json.dumps(coords))
        await asyncio.sleep(random.random() * 2 + 1)

async def main():
    async with websockets.serve(show_time, "localhost", 5678):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())