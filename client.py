import asyncio
import websockets
import logging
import setting


logging.basicConfig(filename="client_log.txt", level=logging.DEBUG, format="%(asctime)s %(message)s")
logging.debug("Debug logging test...")


class Client:
    def __init__(self):
        self.connection = None

    async def connect_to_server(self):
        url = "ws://127.0.0.1:" + str(setting.PORT)
        self.connection = await websockets.connect(url, ping_timeout=None)
        if self.connection.open:
            print("Connection with server opened")
            return self.connection

    async def receive_message(self):
        try:
            message = await self.connection.recv()
            return message
        except websockets.exceptions.ConnectionClosed:
            print("Connection with server closed")

    async def send_message(self, number):
        await self.connection.send(number)

    async def run_fibonacci(self):
        while True:
            msg = await self.receive_message()
            try:
                if msg == "OK":
                    start_number = input("Please input a start number")
                    await self.send_message(start_number)
                    end_number = input("Please input an end number")
                    await self.send_message(end_number)
                else:
                    print(msg)
            except websockets.exceptions.ConnectionClosed:
                print("Connection with server closed")
                break


client = Client()
asyncio.get_event_loop().run_until_complete(client.connect_to_server())
asyncio.get_event_loop().run_until_complete(client.run_fibonacci())
asyncio.get_event_loop().run_forever()
