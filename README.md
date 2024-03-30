# Concurrent Echo Server and Client

## Author

Chenghao Hu

## Course

BTP405 - Software Development Technologies

## Activity 5

This project consists of a concurrent echo server and a client, developed in Python. The server is capable of handling multiple client connections simultaneously, utilizing threads to manage concurrent communications. Each client can send messages to the server, which then echoes the messages back. The implementation demonstrates basic concepts of socket programming and concurrency in Python.

## Features

- TCP-based communication between server and client.
- Multi-threaded server to handle concurrent client connections.
- Echo functionality: the server echoes back any message received from clients.
- Special command (`quit`) handling for gracefully closing client connections.

## Prerequisites

Ensure you have Python 3.x installed on your system to run the server and client scripts.

## Installation

Clone this repository to your local machine to get started:

git clone <repository-url>

Navigate to the cloned directory before running the scripts.

## Usage

### Running the Server

To start the server, execute the following command in a terminal:

python server.py

The server will listen on `localhost` and port `65432` by default.

### Running the Client

Open another terminal window to start a client:

python client.py

After establishing the connection, you can type messages to send to the server. To close the connection, type `quit`.

## Contributing

If you are interested in contributing to this project, please fork the repository and submit a pull request with your proposed changes.

## License

This project is open-sourced under the MIT License. See the LICENSE file for more details.
