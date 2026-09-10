# TCP Chat Application

A lightweight client-server chat application built in Python using TCP sockets.

## Why I Built It

I wanted a hands-on way to understand how networked applications establish connections and exchange messages below the HTTP layer.

## Features

- TCP client-server communication
- IPv4 sockets with `AF_INET`
- Reliable byte-stream transport with `SOCK_STREAM`
- Configurable host, port, and buffer size
- Message encoding/decoding
- Graceful disconnect handling
- Object-oriented client and server implementations

## Tech Stack

Python · TCP/IP · `socket`

## Architecture

```text
Client  <---- TCP connection ---->  Server
```

## Run Locally

Start the server:

```bash
python server.py
```

Then run the client in another terminal:

```bash
python client.py
```

Default endpoint: `127.0.0.1:65432`

## What I Practiced

Socket programming, TCP/IP, connection lifecycle management, client-server architecture, and debugging network communication.

## Next Improvements

- Multi-client support
- Threading / asyncio
- Message framing
- Automated tests
- Docker support
- Cloud deployment
