"""
File:    the_internet.py
Author:  Joseph Cassarino
Date:    12/2/2024
Section: 11
E-mail:  jcassar1@umbc.edu
Description:
  This program
"""

servers = {}

current_server = [None]

# Creates a server and corresponding IP address
def create_server(server_name, ip):

    if server_name in servers:
        print(f"Error: Server '{server_name}' already exists.")
        return

    servers[server_name] = {
        'ip': ip,
        'connections': {}
   
    }

    print(f'A server with the name [{server_name}] has been created at the IP address [{ip}]')

    return

# Creates a connection between 2 servers
def create_connection(server1, server2, connection_time):
    if len(servers) < 2:
        print("Error: There must be at least two servers to create a connection.")
        return

    if server1 not in servers:
        print(f"Error: Server '{server1}' does not exist.")
        return

    if server2 not in servers:
        print(f"Error: Server '{server2}' does not exist.")
        return

    if server1 == server2:
        print("Error: Cannot create a connection between a server and itself.")
        return

    servers[server1]['connections'][server2] = int(connection_time)
    servers[server2]['connections'][server1] = int(connection_time)

    print(f"Connection created: [{server1}] <-> [{server2}] with ping time {connection_time} ms.")

# Sets the server that user traffic will be coming from
def set_server(server_identifier):
    if len(servers) < 1:
        print('Error: There must be at least one server to set a server.')

    for server, details in servers.items():
        if server == server_identifier or details['ip'] == server_identifier:
            print(f'Setting current server to: [{server}] at IP [{details['ip']}]')
            return server

    print('Error: Specified server not found.')
    return None

# Checks the response time of a server
def ping(active_server, target_server, visited_servers):

    # If there is no set server
    if active_server is None:
        print('Error: There is no current server.')
        return float('inf')

    # If there is no target server
    if target_server is None:
        print('Error: There is no target server.')
        return float('inf')

    # If we try to ping the server we're currently on, we get a ping time of 0 ms
    if active_server == target_server:
        return 0

    # If the target server is connected to the active server, it returns the connection time between them
    if target_server in servers[active_server]['connections']:
        ping_time = servers[active_server]['connections'][target_server]
        visited_servers.append(target_server)
        return ping_time

    # If the targeted server is not connected to the active, it recursively checks all other connections
    for connection, connection_time in servers[active_server]['connections'].items():
        if connection not in visited_servers:
            visited_servers.append(connection)

            recursive_ping = ping(connection, target_server, visited_servers)
            if recursive_ping != float('inf'):
                return recursive_ping + connection_time

    # If no valid path is found, float('inf') is returned, marking the ping as failed
    return float('inf')

# Traces a path from one server to another using connections
def traceroute(active_server, target_server, visited_servers, jump_count, previously_traced):

    # If there is no set server
    if active_server is None:
        print('Error: There is no current server.')
        return False

    # If there is no target server
    if target_server is None:
        print('Error: There is no target server.')
        return False

    # If we try to trace a route to the server we're currently on, we get a ping time of 0 ms
    if active_server == target_server and jump_count == 0:
        print('Error: You cannot trace a route from a server to itself.')
        return False

    # If the active server is the same as the target server, we've completed the trace and the function returns true
    if active_server == target_server:
        print(f'[{jump_count}] - [{active_server}]: {ping(previously_traced, active_server, visited_servers=[current_server[0]])} ms')
        return True

    # If the active server is not the target server, iterate through all potential connections that have not yet been visited
    for connection, connection_time in servers[active_server]['connections'].items():
        if connection not in visited_servers:

            # Displays trace progress
            print(f'[{jump_count}] - [{active_server}]: {ping(previously_traced, active_server, visited_servers=[current_server[0]])} ms')

            jump_count += 1
            visited_servers.append(connection)
            previously_traced = active_server

            recursive_trace = traceroute(connection, target_server, visited_servers, jump_count, previously_traced)

            if recursive_trace:
                return True

    return False


# Displays the details of the current server
def ip_config():
    if current_server[0] is None:
        print('Error: No current server set.')
        return

    print('=' * 40)

    for server, details in servers.items():
        if server == current_server[0]:
            print(f'Server: [{server}]')
            print(f'   IP Address: [{details['ip']}]')
            print(f'  Connections:')

            if details['connections']:
                for connected_server, ping in details['connections'].items():
                    print(f'    - {connected_server} (Ping: {ping} ms)')

            else:
                print('    None')

    print('=' * 40)


# Displays all servers and their details
def display_servers():

    if not servers:
        print('No servers available.')
        return

    print('=' * 40)
    for server, details in servers.items():
        print(f'Server: [{server}]')
        print(f'   IP Address: [{details['ip']}]')
        print(f'  Connections:')

        if details['connections']:
            for connected_server, ping in details['connections'].items():
                print(f'    - {connected_server} (Ping: {ping} ms)')

        else:
            print('    None')
        print('=' * 40)


# Takes the user's input and directs the program to the correct action
def parse_input():
    user_input = input('>>> ').lower().split()
    directive = user_input[0]


    if directive == "create-server":
        create_server(user_input[1], user_input[2])
        return True


    elif directive == "create-connection":
        create_connection(user_input[1], user_input[2], user_input[3])
        return True


    elif directive == "set-server":
        current_server[0] = set_server(user_input[1])
        return True


    elif directive == "ping":
        # Using the given identifier to grab the name of the server we want to ping
        target_server = None
        server_identifier = user_input[1]
        visited_servers = [current_server[0]]

        for server, details in servers.items():
            if server == server_identifier or details['ip'] == server_identifier:
                target_server = server

        print(f'Pinging [{servers[target_server]['ip']}]...')

        total_ping = ping(current_server[0], target_server, visited_servers)

        if total_ping == float('inf'):
            print('Error: Ping Unsuccessful. No valid path found.')

        else:
            print(f'Ping Successful: [{current_server[0]}] ---> [{target_server}]: {total_ping} ms')
        return True


    elif directive == "traceroute":
        target_server = None
        server_identifier = user_input[1]
        visited_servers = [current_server[0]]
        jump_count = 0
        previously_traced = current_server[0]

        for server, details in servers.items():
            if server == server_identifier or details['ip'] == server_identifier:
                target_server = server

        print(f'Tracing route from [{current_server[0]}] to [{target_server}]...')

        valid_path = traceroute(current_server[0], target_server, visited_servers, jump_count, previously_traced)

        if valid_path:
            print(f'Trace successful.')

        else:
            print('Trace failed. No valid path found')

        return True


    elif directive == "ip-config":
        ip_config()
        return True


    elif directive == "display-servers":
        display_servers()
        return True


    elif directive == "quit":
        return False


    else:
        print('Error: Invalid command. Please try again.')
        return True



if __name__ == '__main__':

    user_active = True

    # Prompts input until the user quits
    while user_active is True:
        user_active = parse_input()