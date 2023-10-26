import logging
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def run(debug=False):
    authorizer = DummyAuthorizer()
    handler = FTPHandler
    handler.authorizer = authorizer
    handler.banner = "Welcome to the FTP server"
    address = ('', 21)
    server = FTPServer(address, handler)
    server.max_cons = 2
    server.max_cons_per_ip = 2
    if debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)
    server.serve_forever()