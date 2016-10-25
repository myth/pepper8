# -*- coding: utf8 -*-
#
# Created by 'myth' on 10/19/15

import argparse
from os import fstat
from stat import S_ISFIFO, S_ISREG
from sys import stdin, stderr, exit, argv

from pepper8 import VERSION
from pepper8.generator import HtmlGenerator
from pepper8.parser import Parser


def main(arguments=None):

    args = arguments or argv[1:]

    fileparser = None
    argparser = argparse.ArgumentParser(
        description='Convert pep8 or flake8 output to HTML',
        prog='pepper8',
        epilog='pepper8 accepts input either from stdin or from a filename argument.\n' +
               'Unless specified otherwise with -o OUTPUT_FILE, pepper8 outputs to stdout.'
    )
    argparser.add_argument(
        'filename',
        nargs='?',
        type=str,
        help='Path to file containing pep8 or flake8 results.'
    )
    argparser.add_argument(
        '-v',
        '--verbose',
        action='store_true',
        help='Enable verbose output (only if --output-file is specified)'
    )
    argparser.add_argument(
        '--version',
        action='store_true',
        help='Prints pepper8 version and exists'
    )
    argparser.add_argument(
        '-o',
        '--output-file',
        type=str,
        help='Outputs the HTML data to the specified file and enables the use of the --verbose option.'
    )

    # Fetch the provided arguments from sys.argv
    args = argparser.parse_args(args)
    if args.version:
        print('Pepper8 version %s' % VERSION)
        exit(0)

    if args.filename:
        try:
            f = open(args.filename)
            fileparser = Parser(f)
        except IOError as e:
            stderr.write('Could not open file: %s' % e)
            stderr.flush()
            exit(1)

    else:
        # We need to check if stdin is piped or read from file, since we dont want
        # stdin to hang at terminal input
        mode = fstat(0).st_mode

        if S_ISFIFO(mode) or S_ISREG(mode):
            fileparser = Parser(stdin)
        else:
            # stdin is terminal input at this point
            argparser.print_help()
            exit(0)

    # Generate the HTML report to output_file if not None, else print to stdout
    generator = HtmlGenerator(fileparser)
    generator.analyze(output_file=args.output_file)

if __name__ == '__main__':
    main()
