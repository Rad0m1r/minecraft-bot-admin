from mcrcon import MCRcon
import sys

input_arg = sys.argv[1]


def main():

    try:

        mcr = MCRcon('SERVER_IP', 'RCON_PASSWORD', port=YOUR_RCON_PORT_DEFAULT_25575)

        mcr.connect()

        resp = mcr.command(input_arg)
        
        mcr.disconnect()

        print(resp)

    except Exception as e: print(e)

    




if __name__ == "__main__":
    main()
