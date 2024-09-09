import asyncio
import websockets


STOP_WORD = "disconnect"


async def send_message():
    uri = "ws://localhost:8000/ws/my_client"  # Replace 'my_client' with your client id or any identifier
    async with websockets.connect(uri) as websocket:
        print("Connected to the WebSocket server.")
        while True:
            message = input("Enter a message: ")
            await websocket.send(message)
            if message.lower() == STOP_WORD:
                break

            while True:
                try:
                    # Wait for a response from the server with a 5-second timeout
                    response = await asyncio.wait_for(websocket.recv(), timeout=5.0)
                    print(f"Response from server: {response}")
                except asyncio.TimeoutError:
                    print("No response from server in the last 5 seconds. Exit the session.")
                    break


if __name__ == "__main__":
    asyncio.run(send_message())