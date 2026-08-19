v# server.py
import socket


class ChatServer:
    """A simple TCP chat server that talks to a single client."""

    def __init__(self, host="127.0.0.1", port=65432, buffer_size=1024):
        self.host = host
        self.port = port
        self.buffer_size = buffer_size
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        """Bind, listen, and accept a single client connection."""
        with self.sock as s:
            s.bind((self.host, self.port))
            s.listen()
            print(f"Server started on {self.host}:{self.port}...")

            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                self._handle_conversation(conn)

    def _handle_conversation(self, conn):
        """Run the receive/send loop for one connected client."""
        while True:
            data = self._receive(conn)
            if data is None or data.lower() == "exit":
                print("Client disconnected.")
                break
            print(f"Client: {data}")

            message = input("You: ")
            self._send(conn, message)
            if message.lower() == "exit":
                print("Server closing connection.")
                break

    def _receive(self, conn):
        data = conn.recv(self.buffer_size)
        if not data:
            return None
        return data.decode()

    def _send(self, conn, message):
        conn.sendall(message.encode())


if __name__ == "__main__":
    ChatServer().start()
EO
# server.py
import socket


class ChatServer:
    """A simple TCP chat server that talks to a single client."""

    def __init__(self, host="127.0.0.1", port=65432, buffer_size=1024):
        self.host = host
        self.port = port
        self.buffer_size = buffer_size
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        """Bind, listen, and accept a single client connection."""
        with self.sock as s:
            s.bind((self.host, self.port))
            s.listen()
            print(f"Server started on {self.host}:{self.port}...")

            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                self._handle_conversation(conn)

    def _handle_conversation(self, conn):
        """Run the receive/send loop for one connected client."""
        while True:
            data = self._receive(conn)
            if data is None or data.lower() == "exit":
                print("Client disconnected.")
                break
            print(f"Client: {data}")

            message = input("You: ")
            self._send(conn, message)
            if message.lower() == "exit":
                print("Server closing connection.")
                break

    def _receive(self, conn):
        data = conn.recv(self.buffer_size)
        if not data:
            return None
        return data.decode()

    def _send(self, conn, message):
        conn.sendall(message.encode())


if __name__ == "__main__":
    ChatServer().start()
