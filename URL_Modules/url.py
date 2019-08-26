__author__ = "Benjamin"
__github__  = "https://github.com/MrSSHH/"

import random
import string
import sys
import requests
import os
from errors import *

class url:

    main_dir = os.path.join(os.path.dirname(__file__)) + "\database\database.data"
    if not os.path.exists(main_dir):
        os.mkdir(url.main_dir.replace("\database.data", "\\"))
        data = open(main_dir, "w+")
        data.close()

    def __init__(self, link, database=main_dir):
        self.link = link
        self.database = database

    def __str__(self):
        return "<URL Object An Instance Of '{}'>".format(
            self.__class__.__name__)

    def __repr__(self):
        return "'{}(\"{}\")'".format(self.__class__.__name__,
                                     self.link)

    @staticmethod
    def randomize():
        chars = [random.choice([random.choice(string.ascii_lowercase),
                                random.choice(string.ascii_uppercase)])
                 for letter in range(5)] + list(
            str(random.randint(1, 9))
            for num in range(3))
        random.shuffle(chars)
        return chars

    def short(self):
        if not self.link.startswith("http://") and not self.link.startswith("https://"):
            self.link = "http://" + self.link

        try:
            response = requests.get(self.link)
        except Exception as e:
            raise WebsiteNotFound("Can't reach the website, please check the link.")

        loc = self.database
        with open(loc, "r+") as link:
            tokens = [''.join(expr).split() for expr in link.readlines()]
            try:
                token = [token[2] for token in tokens if token[0] == self.link]
                return token[0]
            except IndexError:
                pass
            code = url.randomize()
            full_link = "short.link/" + ''.join(code)
            link.write("{} - {}\n".format(self.link, full_link))
            return full_link
l = url("www.google.com")
print(l.short())
