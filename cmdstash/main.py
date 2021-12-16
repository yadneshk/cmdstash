import argparse
import sys

import cmdstash
from cmdstash.utils import db


def parse_args(args=None):
    parser = argparse.ArgumentParser(
        description='Command Stash: A CLI tool \
            to manage your everyday commands'
    )
    parser.add_argument(
        '-v', '--version', action='version', version=cmdstash.__version__
    )
    subparser = parser.add_subparsers(help='Manage commands')

    create_add_subparser(subparser)
    create_list_subparser(subparser)

    if not args:
        parser.print_help()
        exit(1)

    return parser


def create_add_subparser(subparser):
    add_parser = subparser.add_parser('add')
    add_subparser = add_parser.add_subparsers(help='Add help')
    add_parser.set_defaults(parser='add')

    command_parser = add_subparser.add_parser('command')
    command_parser.set_defaults(sub_parser='command')
    command_parser.add_argument('cmd', type=str)
    command_parser.add_argument('-t', '--tag', type=str)

    tag_parser = add_subparser.add_parser('tags')
    tag_parser.set_defaults(sub_parser='tags')
    tag_parser.add_argument('tags', type=str, nargs='+')


def create_list_subparser(subparser):
    list_parser = subparser.add_parser('list')
    list_subparser = list_parser.add_subparsers()
    list_parser.set_defaults(parser='list')

    command_parser = list_subparser.add_parser('command')
    command_parser.set_defaults(sub_parser='command')
    command_parser.add_argument('-t', '--tags', type=str, nargs='+')

    tags_parser = list_subparser.add_parser('tags')
    tags_parser.set_defaults(sub_parser='tags')


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    parser = parse_args(argv)
    args = parser.parse_args()
    db.process_arguments(args)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
