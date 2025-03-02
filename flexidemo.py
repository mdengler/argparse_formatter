#!/usr/bin/python3
# Copyright (c) 2019 David Steele <dsteele@gmail.com>
#
# SPDX-License-Identifier: GPL-2.0-or-later
# License-Filename: LICENSE
#

import argparse
from argparse_formatter import FlexiFormatter

test_cases = (
    ("Default", argparse.HelpFormatter),
    ("Flexi", FlexiFormatter),
)


def argparse_demo(formatter):
    parser = argparse.ArgumentParser(
        epilog="""
            This is a multi-paragraph epilog. It is presenting data that would
            benefit by being visually broken up into pieces.

            It sure would be nice if it was represented that way.

              1. This is a pretty long line, in a bullet list - getting longer
                 and longer and longer
              2. this isn't
            """,
        formatter_class=formatter,
    )

    parser.add_argument(
        "--arg",
        help="""
            This same feature would be useful for arguments that would
            benefit from
            more explanation.

              1. It looks nicer
              2. It is easier to read, even if some of the bullets get to be a little long.
              3. Also, there is a table:
                 | Feature      | ParagraphFormatter | FlexiFormatter |
                 | :---         | :---:              | :---:          |
                 | Outputs text |        Yes         |       Yes      |
                 | Bullets?     |        Yes         |       Yes      |
                 | Tables       |        No          |       Yes      |
              4. Bullets can follow tables.

        """,  # noqa
    )

    return parser.format_help()


for (name, formatter) in test_cases:
    print("*************************")
    print("Using the {} formatter".format(name))
    print("*************************")
    print()
    print(argparse_demo(formatter))
    print()
