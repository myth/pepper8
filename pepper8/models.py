# -*- coding: utf8 -*-
#
# Created by 'myth' on 10/19/15


class ResultContainer(object):
    """
    Basic model that keeps the required fields for File and Package objects
    """

    def __init__(self):
        super(ResultContainer, self).__init__()
        self.lines = []
        self.violations = {}

    def add_error(self, code, line, char, description):
        """
        Registers an error for this container with code on line at char.
        :param code: The PEP 8 error code
        :param line: The line number of the reported error
        :param char: Line location of first offending character
        :param description: The human readable description of the thrown error/warning
        """

        if code not in self.violations:
            self.violations[code] = 0
        self.violations[code] += 1
        self.lines.append((code, line, char, description))


class FileResult(ResultContainer):
    """
    The FileResult class keeps the PEP 8 results for a single file
    """

    def __init__(self, path):
        super(FileResult, self).__init__()
        self.path = path
