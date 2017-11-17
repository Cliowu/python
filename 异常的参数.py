#!/usr/bin/python
# -*- coding: UTF-8 -*-

def temp_convert(var):
    try:
        return int(var)
    except ValueError, Argument:
        print "parameter does not contain numbers\n", Argument
