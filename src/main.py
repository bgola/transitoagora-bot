#!/usr/bin/python
# coding: utf-8

import urllib2, sys
from transitoagora import TransitoAgora

URL = "http://cetsp1.cetsp.com.br/monitransmapa/agora/"

if __name__ == "__main__":
    TransitoAgora(urllib2.urlopen(URL)).dumps('csv', f=sys.stdout)
