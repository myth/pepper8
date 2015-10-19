# -*- coding: utf8 -*-
#
# Created by 'myth' on 10/19/15

import os
from sys import stdout, stderr

from jinja2 import Template

from models import FileResult
from parser import Parser


class HtmlGenerator(object):
    """
    The HTML Generator generates the HTML report based off of the data retrieved
    from the Parser object.
    """

    def __init__(self, parser):
        """
        Construct a HtmlGenerator object.

        :param parser: A pepper8 Parser object
        """

        if not isinstance(parser, Parser):
            raise ValueError('Argument <parser> must be an instance of Parser')

        super(HtmlGenerator, self).__init__()
        self.parser = parser
        self.files = []
        self.total_errors = 0
        self.total_warnings = 0
        self.violations = {}

    def generate(self, output_file=None):
        """
        Generates an HTML file based on data from the Parser object and Jinja2 templates
        :param output_file: If specified, output will be written to this file instead of stdout.
        """

        fd = output_file

        # Write to stdout if we do not have a file to write to
        if not fd:
            fd = stdout

        file_result = None
        for path, code, line, char, desc in self.parser.parse():
            # Create a new FileResult and register it if we have changed to a new file
            if not file_result:
                file_result = FileResult(path)
            if file_result.path != path:
                self.update_stats(file_result)
                file_result = FileResult(path)
                self.files.append(file_result)

            file_result.add_error(code, line, char, desc)

        with open(os.path.join(os.path.dirname(__file__), 'templates/base.html')) as template:
            html = Template(template.read())

            # Write our rendered template to the file descriptor
            fd.write(
                html.render(
                    files=self.files,
                    total_warnings=self.total_warnings,
                    total_errors=self.total_errors,
                    violations=sorted(self.violations, key=self.violations.get, reverse=True)
                )
            )

            # If file descriptor is stdout
            if not output_file:
                fd.flush()
            else:
                fd.close()

    def update_stats(self, file_result):
        """
        Reads the data from a FileResult and updates overall statistics
        :param file_result: A FileResult instance
        """

        for code, count in file_result.violations.items():
            if code not in self.violations:
                self.violations[code] = 0

            self.violations[code] += 1

            if 'W' in code.upper():
                self.total_warnings += 1
            else:
                self.total_errors += 1
