# Python Model Internet

A command-line Python application that simulates a basic model of the internet, allowing users to create servers, establish connections between them, and perform network diagnostic commands like `ping` and `traceroute`.

## 📜 Description

This project provides a simplified, text-based environment to understand fundamental networking concepts. You can define a network topology by creating servers and specifying the "ping" time (latency) for connections between them. Once your network is set up, you can designate an active server and then test connectivity and routes to other servers in your model internet.

## Features

* **Server Creation:** Define servers with unique names and IP addresses.
* **Connection Management:** Establish bi-directional connections between servers with specified ping times.
* **Active Server Designation:** Set a "current" server from which network operations will originate.
* **Ping Functionality:** Measure the round-trip time to a target server from the active server, finding the shortest path.
* **Traceroute Functionality:** Display the path (sequence of servers and cumulative ping times) taken to reach a target server from the active server.
* **Network Configuration Display:** View details of the currently set server (`ip-config`) or all servers in the network (`display-servers`).
* **Command-Line Interface:** Interact with the simulation through text-based commands.

## Getting Started

### Prerequisites

* Python 3.x installed on your system.

### Running the Application

1.  **Clone or Download:**
    * Clone the repository:
        ```bash
        git clone <https://github.com/JCassarino/Little-Model-Internet>
        cd <Little-Model-Internet>
        ```
    * Or download the Python script (`the_internet.py`) to a directory on your computer.
2.  **Run from Terminal:**
    * Navigate to the directory containing the script.
    * Execute the script:
        ```bash
        the_internet.py
        ```
3.  **Interact:**
    * The application will present a `>>> ` prompt. Enter commands as described below.

## Available Commands

Enter commands at the `>>> ` prompt. Arguments should be space-separated.

* **`create-server <server_name> <ip_address>`**
    * Creates a new server.
    * Example: `create-server ServerA 192.168.1.1`

* **`create-connection <server1_name> <server2_name> <ping_time_ms>`**
    * Creates a connection between two existing servers with a specified ping time in milliseconds.
    * Example: `create-connection ServerA ServerB 10`

* **`set-server <server_identifier>`**
    * Sets the current active server from which commands like `ping` and `traceroute` will operate.
    * `<server_identifier>` can be the server's name or its IP address.
    * Example: `set-server ServerA` or `set-server 192.168.1.1`

* **`ping <target_server_identifier>`**
    * Pings the target server from the currently set active server and displays the total ping time for the shortest path.
    * `<target_server_identifier>` can be the server's name or its IP address.
    * Example: `ping ServerB`

* **`traceroute <target_server_identifier>`**
    * Traces the route (path of servers and cumulative ping times at each hop) from the active server to the target server.
    * `<target_server_identifier>` can be the server's name or its IP address.
    * Example: `traceroute ServerC`

* **`ip-config`**
    * Displays the details (name, IP, connections) of the currently set active server.

* **`display-servers`**
    * Displays the details for all servers currently defined in the simulation.

* **`quit`**
    * Exits the application.

## Code Overview

The script is organized into several key functions:

* `create_server()`: Adds a new server to the network.
* `create_connection()`: Establishes a link between two servers.
* `set_server()`: Designates the user's current server.
* `ping()`: Recursively calculates the shortest ping time to a target.
* `traceroute()`: Recursively determines and displays the path to a target.
* `ip_config()`: Shows information about the active server.
* `display_servers()`: Lists all servers and their connections.
* `parse_input()`: Handles user input and calls the appropriate functions.
The main loop in `if __name__ == '__main__':` continuously prompts for user input until "quit" is entered.

## 📝 Project Status

This is a completed project. No further updates are planned at this time.
