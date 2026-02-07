import asyncio

class EventBroadcaster:
    def __init__(self):
        self.clients = []

    async def broadcast(self, message: str):
        for queue in self.clients:
            await queue.put(message)  # put the message in each client's queue

    async def register(self):
        queue = asyncio.Queue()
        self.clients.append(queue)  # add the queue to clients

        try:
            while True:
                yield await queue.get()  # wait for a message to be put in the queue
        finally:
            if queue in self.clients:
                self.clients.remove(queue)  # clean up the queue when client disconnects

broadcaster = EventBroadcaster()