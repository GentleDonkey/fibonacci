import asyncio
import websockets
import logging
import setting


logging.basicConfig(filename="server_log.txt", level=logging.DEBUG, format="%(asctime)s %(message)s")
logging.debug("Debug logging test...")


async def echo(websocket):
    print("A client just connected")
    await send_message(websocket, "OK")
    while True:
        try:
            await run_fibonacci(websocket)
        except websockets.exceptions.ConnectionClosed:
            print("A client just disconnected")
            break


def sub_fibonacci(sn, en):
    a, b = 0, 1
    result = []
    gap = en - sn
    while sn > 0:
        a, b = b, a + b
        sn = sn - 1
    while gap > 0:
        result.append(a)
        a, b = b, a + b
        gap = gap - 1
    return result


async def run_fibonacci(ws):
    start_number = await ws.recv()
    end_number = await ws.recv()
    if not start_number.isnumeric() or not end_number.isnumeric():
        print("Error: The numbers should be positive integers")
        await send_message(ws, "Error: The numbers should be positive integers")
        await send_message(ws, "OK")
    elif int(start_number) == 0 or int(end_number) == 0:
        print("Error: The numbers should be bigger than 0")
        await send_message(ws, "Error: The numbers should be bigger than 0")
        await send_message(ws, "OK")
    elif int(start_number) > int(end_number):
        print("Error: The end number should be bigger than or equal to start number")
        await send_message(ws, "Error: The end number should be bigger than or equal to start number")
        await send_message(ws, "OK")
    else:
        result = sub_fibonacci(int(start_number) - 1, int(end_number))
        await send_message(ws, "Your result is "+str(result))
        print("Substring " + start_number + " to " + end_number + " of Fibonacci sequence is " + str(result))
        await send_message(ws, "OK")


async def receive_message(ws):
    try:
        message = await ws.recv()
        print(message)
    except websockets.exceptions.ConnectionClosed:
        print("A client just disconnected")


async def send_message(websocket, message):
    await websocket.send(message)


print("Server listening on Port " + str(setting.PORT))
start_server = websockets.serve(echo, "localhost", setting.PORT, ping_timeout=None)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
