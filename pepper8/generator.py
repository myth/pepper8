# -*- coding: utf8 -*-
#
# Created by 'myth' on 10/19/15

import os
from sys import stdout, stderr

from jinja2 import Template

from pepper8.models import FileResult
from pepper8.parser import Parser


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
        self.files = {}
        self.total_errors = 0
        self.total_warnings = 0
        self.total_other = 0
        self.violations = {}

    def analyze(self, output_file=None):
        """
        Analyzes the parsed results from Flake8 or PEP 8 output and creates FileResult instances
        :param output_file: If specified, output will be written to this file instead of stdout.
        """

        fr = None
        for path, code, line, char, desc in self.parser.parse():

            # Create a new FileResult and register it if we have changed to a new file
            if path not in self.files:
                # Update statistics
                if fr:
                    self.update_stats(fr)
                fr = FileResult(path)
                self.files[path] = fr

            # Add line to the FileResult
            fr.add_error(code, line, char, desc)

        # Add final FileResult to statistics, if any were parsed
        if fr:
            self.update_stats(fr)

        # Generate HTML file
        self.generate(output_file=output_file)

    def generate(self, output_file=None):
        """
        Generates an HTML file based on data from the Parser object and Jinja2 templates
        :param output_file: If specified, output will be written to this file instead of stdout.
        """

        fd = output_file

        # Write to stdout if we do not have a file to write to
        if not fd:
            fd = stdout
        else:
            try:
                fd = open(output_file, 'w')
            except IOError as e:
                stderr.write('Unable to open outputfile %s: %s' % (output_file, e))

        with open(os.path.join(os.path.dirname(__file__), 'templates/base.html')) as template:
            html = Template(template.read())

            # Write potential build messages to stdout if we are writing to HTML file
            # If dest is stdout and supposed to be piped or redirected, build messages like TeamCity's will
            # have no effect, since they require to read from stdin.
            if output_file:
                self.report_build_messages()

            # Write our rendered template to the file descriptor
            fd.write(
                html.render(
                    files=sorted(self.files.values(), key=lambda x: x.path),
                    total_warnings=self.total_warnings,
                    total_errors=self.total_errors,
                    total_other=self.total_other,
                    violations=sorted(
                        ((code, count) for code, count in self.violations.items()),
                        key=lambda x: x[1],
                        reverse=True,
                    )
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
            self.violations[code] += file_result.violations[code]

            if 'E' in code.upper():
                self.total_errors += file_result.violations[code]
            elif 'W' in code.upper():
                self.total_warnings += file_result.violations[code]
            else:
                self.total_other += file_result.violations[code]

    def report_build_messages(self):
        """
        Checks environment variables to see whether pepper8 is run under a build agent such as TeamCity
        and performs the adequate actions to report statistics.

        Will not perform any action if HTML output is written to OUTPUT_FILE and not stdout.
        Currently only supports TeamCity.

        :return: A list of build message strings destined for stdout
        """

        if os.getenv('TEAMCITY_VERSION'):
            tc_build_message_warning = "##teamcity[buildStatisticValue key='pepper8warnings' value='{}']\n"
            tc_build_message_error = "##teamcity[buildStatisticValue key='pepper8errors' value='{}']\n"

            stdout.write(tc_build_message_warning.format(self.total_warnings))
            stdout.write(tc_build_message_error.format(self.total_errors))
            stdout.flush()
