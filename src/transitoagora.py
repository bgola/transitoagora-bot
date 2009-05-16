#!/usr/bin/python
# coding: utf-8

import urllib2, re, os

from datetime import datetime
from BeautifulSoup import BeautifulSoup as BS

URL = "http://cetsp1.cetsp.com.br/monitransmapa/agora/"

class TransitoAgora(object):
    """
    Gets information about the traffic from transito agora

    >>> html = open("fake_ta.html")
    >>> ta = TransitoAgora(html)
    >>> ta.time.minute
    23
    >>> ta.time.hour
    21
    >>> ta.watched
    835
    >>> ta.jam_size
    63
    """

    def __init__(self, html):
        self.bs = BS(html)
        now = datetime.now()
        hour, min = self._get_time()
        self.time = datetime(now.year, now.month, now.day, hour, min)
        self.watched = int(self.bs.find('div', {'id':'tamanhoTotal'}).b.string)
        self.jam_size = int(self.bs.find('div', {'id':'lentidao'}).b.string)

    def _get_time(self):
        time_str = self.bs.find('div', {'id':'hora'}).b.string
        hour, min = re.match(r"(\d{2})h(\d{2})m", time_str).groups()
        return (int(hour), int(min))

    def dumps(self, fmt, f):
        f.write("%d; %d; %d; %d; %d; %d; %d%s" % ( 
                                        self.time.year,
                                        self.time.month,
                                        self.time.day,
                                        self.time.hour,
                                        self.time.minute,
                                        self.watched,
                                        self.jam_size,
                                        os.linesep)
              )

if __name__ == "__main__":
    import doctest
    doctest.testmod()

