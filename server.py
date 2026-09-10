import socket


class ChatServer:
    """A simple TCP chat server that communicates with one client."""

    def __init__(self, host="127.0.0.1", port=65432, buffer_size=1024):
        self.host = host
        self.port = port
        self.buffer_size = buffer_size

    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sock.bind((self.host, self.port))
            sock.listen()
            print(f"Server listening on {self.host}:{self.port}")

            conn, addr = sock.accept()
            with conn:
                print(f"Connected by {addr}")
                self._handle_conversation(conn)

    def _handle_conversation(self, conn):
        while True:
            message = self._receive(conn)
            if message is None or message.lower() == "exit":
                print("Client disconnected.")
                return

            print(f"Client: {message}")
            response = input("You: ")
            self._send(conn, response)

            if response.lower() == "exit":
                print("Server closing connection.")
                return

    def _receive(self, conn):
        data = conn.recv(self.buffer_size)
        return None if not data else data.decode("utf-8")

    @staticmethod
    def _send(conn, message):
        conn.sendall(message.encode("utf-8"))


if __name__ == "__main__":
    ChatServer().start()
