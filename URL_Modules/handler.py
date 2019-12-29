__author__ = "Benjamin"
__github__  = "https://github.com/MrSSHH/"

# Run this on server side

import sys
import os
import socket
from errors import *
from url import url


class handler():
    main_ip = socket.gethostbyname(socket.gethostname())

    """

    Class purpose:
        This class redirects the user to the shorten website.

    Notes:
        It's important to note this class will create an infinte loop,
        unless you stop it,
        (You can use the KillSwitch by <Your IP>/closeconnection)
        you may use threading to run this module with your script.
        Also if you don't supply any arguments in to the class
        the class will automatically supply it for you.

    Usage outside of module:
        import handler
        server = handler(host=<Your IP>, port=80, database=<Database location>)
        server.start()

    """

    def __init__(self, database=url.main_dir, host=main_ip, port=80):
        self.host = host
        self.port = port
        self.database = database

    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as site:
            site.bind((self.host, self.port))
            print(f"Running on: {self.host}:{self.port}")

            while True:
                site.listen()
                conn, addr = site.accept()

                with conn:
                    data = conn.recv(1024)

                    # Parssing the GET request into the direct code[1][1]
                    code = str(data).split()
                    print(f"[{code[0]}-Request] - from {addr[0]}:{addr[1]}")
                    if code[1] == '/closeconnection':
                        conn.send(bytes("Socket Closed", "utf-8"))
                        raise KillSwitch("KillSwitch Activated")

                    with open(self.database, "r+") as database:
                        urls = [line.split() for line in database.readlines()]

                        try:
                            link = [url[0] for url in urls if code[1] in url[2]]
                            print(f'Redirecting user to {link[0]}')
                        except IndexError:
                            continue

                        try:
                            redirect = f"""
                                        <html lang="en-US">
                                            <head>
                                            <meta charset="UTF-8">
                                            <meta http-equiv="refresh" content="0; url={link[0]}">
                                            <script type="text/javascript">
                                                window.location.href = {link[0]}
                                            </script>
                                            <title>Page Redirection</title>
                                             </head>
                                             <body>
                                                If you are not redirected automatically,
                                                follow this <a href={link[0]}>link to website</a>.
                                            </body>
                                         </html>"""
                        except IndexError:
                            conn.close()
                    conn.send(bytes(redirect, "utf-8"))

handler(host=<your-ip>).start()
