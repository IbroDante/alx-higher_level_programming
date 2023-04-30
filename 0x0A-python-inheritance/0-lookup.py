#!/usr/bin/python3
"""Defines an object attribute lookup func."""


def lookup(obj):
    """return a list of an object avail attr"""
    return (dir(obj))
