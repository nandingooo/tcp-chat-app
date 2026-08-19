# client.py
import socket


class ChatClient:
    """A simple TCP chat client that connects to ChatServer."""

    def __init__(self, server_ip="127.0.0.1", port=65432, buffer_size=1024):
        self.server_ip = server_ip
        self.port = port
        self.buffer_size = buffer_size
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        """Connect to the server and run the send/receive loop."""
        with self.sock as s:
            s.connect((self.server_ip, self.port))
            print(f"Connected to server {self.server_ip}:{self.port}")
            self._handle_conversation(s)

    def _handle_conversation(self, s):
        while True:
            message = input("You: ")
            self._send(s, message)
            if message.lower() == "exit":
                print("Closing connection.")
                break

            data = self._receive(s)
            if data is None:
                break
            print(f"Server: {data}")

    def _receive(self, s):
        data = s.recv(self.buffer_size)
        if not data:
            return None
        return data.decode()

    def _send(self, s, message):
        s.sendall(message.encode())


if __name__ == "__main__":
    ChatClient().start()
