# -*- coding: utf8 -*-
#
# Created by 'myth' on 10/19/15

import re

POSITION = re.compile('^[\d]+$')
ERROR_CODE = re.compile('^[a-zA-Z][0-9]{3,4}$')
FILEPATH = re.compile('[\S\s]+\.py$')


class Parser(object):
    """
    The Parser class is responsible for reading and parsing the lines from
    a PEP8 input source. This can be either piped through stdin or read from a file.
    """

    def __init__(self, data):
        """
        Constructs a Parser object.

        :param data: An input source of PEP 8 results. Can be either a file descriptor or stdin.
        """
        self.data = data

    def parse(self):
        """
        Reads all lines from the current data source and yields each FileResult objects
        """

        if self.data is None:
            raise ValueError('No input data provided, unable to parse')

        for line in self.data:
            parts = line.strip().split()
            try:
                path = parts[0]
                code = parts[1]
                path, line, char = path.split(':')[:3]

                if not re.match(POSITION, line):
                    continue
                if not re.match(POSITION, char):
                    continue
                if not re.match(ERROR_CODE, code):
                    continue
                if not re.match(FILEPATH, path):
                    continue

            # For parts mismatch
            except IndexError:
                continue
            # For unpack mismatch
            except ValueError:
                continue

            yield path, code, line, char, ' '.join(parts[2:])
