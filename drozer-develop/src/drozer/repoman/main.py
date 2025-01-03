#!/usr/bin/env python

import os
import sys

from drozer.repoman.repository_builder import RepositoryBuilder


def main():
    if len(sys.argv) != 2:
        print("usage: drozer-repository TARGET")
        sys.exit(-1)
    else:
        RepositoryBuilder(os.getcwd(), sys.argv[1]).build()
