"""
 The Plague RCON
 Copyright 2018 Frosty Elk AB
 Author: Arne Sikstrom
"""

from srcds.rcon import RconConnection, RconPacketError, RconAuthError
import argparse

tp_description = "The Plague RCON Client"

parser = argparse.ArgumentParser(description=tp_description)
parser.add_argument('-ip', help='The IP adress of the server', type=str, default='127.0.0.1')
parser.add_argument('-port', help='The Port the RCON server is listening on', type=int, default=27888)
parser.add_argument('-pw', help='The RCON password for the server', type=str, default='ServerPw')
args = parser.parse_args()

conn = {}
try:
    conn = RconConnection(args.ip, port=args.port, password=args.pw)
except ConnectionRefusedError:
    print("No Connection")
    exit(1)
except RconPacketError:
    print("Packet Error")
    exit(2)
except ConnectionResetError:
    print("Connection Reset")
    exit(3)
except RconAuthError:
    print("Bad Password")
    exit(4)
except TimeoutError:
    print("Timeout")
    exit(5)

if conn:
    print("Logged in. Type 'Q' to quit")

    input_line = ""
    while conn:
        input_line = input("> ")

        if len(input_line.strip()) == 0:
            continue

        if input_line.lower().startswith("q"):
            break

        try:
            response = conn.exec_command(input_line)
            print(response)
        except ConnectionResetError:
            print("Server closed the connection!")
            break
