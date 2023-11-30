import logging

from pyftpdlib.authorizers import WindowsAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def main():
    authorizer = WindowsAuthorizer()
    # Use Guest user with empty password to handle anonymous sessions.
    # Guest user must be enabled first, empty password set and profile
    # directory specified.
    #authorizer = WindowsAuthorizer(anonymous_user="Guest", anonymous_password="")

    # Instantiate FTP handler class
    handler = FTPHandler
    handler.authorizer = authorizer

    # Configure logging
    logging.basicConfig(level=logging.INFO)

    # Define a customized banner (string returned when client connects)
    handler.banner = "pyftpdlib based ftpd ready."

    # Specify a masquerade address and the range of ports to use for
    # passive connections.  Decomment in case you're behind a NAT.
    #handler.masquerade_address = '151.25.42.11'
    #handler.passive_ports = range(60000, 65535)

    # Instantiate FTP server class and listen on 0.0.0.0:2121
    address = ('', 2121)
    server = FTPServer(address, handler)

    # set a limit for connections
    server.max_cons = 256
    server.max_cons_per_ip = 5

    # start ftp server
    server.serve_forever()

if __name__ == '__main__':
    main()