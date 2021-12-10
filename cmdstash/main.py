import argparse
import sys

import cmdstash


class CommandStash:
    def __init__(self):
        parser = argparse.ArgumentParser(
            prog='COMMAND',
            description="CLI based utility to store commands",
            usage="""
            command <operation> -t [<tag>]
            """
        )

        parser.add_argument(
            'command',
            help='Subcommand'
        )
        parser.add_argument(
            '--version',
            action='version',
            version=cmdstash.__version__,
            help="Command version"
        )
        args = parser.parse_args(sys.argv[1:2])

        if not hasattr(self, args.command):
            print("Unrecognized arguments")
            parser.print_help()
            exit(1)
        getattr(self, args.command)()

    def add(self):
        parser = argparse.ArgumentParser(
            description="Add new commands/tags",
            usage="""
            command add <subcommand> -t [<tag>..]
            """
        )
        subparser = parser.add_subparsers()
        tags_subparser = subparser.add_parser('tags', help='add tags')
        tags_subparser.add_argument('tag', type=str, nargs='+')

        cmds_subparser = subparser.add_parser('cmds', help='add commands')
        cmds_subparser.add_argument('command', type=str)
        cmds_subparser.add_argument(
            '-t', '--tags', type=str, nargs='+', help='add command under a tag'
        )

        args = parser.parse_args(sys.argv[2:])
        if not args._get_kwargs():
            parser.print_help()
            exit(1)
        if hasattr(args, 'command'):
            print("add new command", args.command, args.tags)
        elif hasattr(args, 'tag'):
            print("add new tag", args.tag)

    def list(self):
        parser = argparse.ArgumentParser(
            description="List commands",
            usage="""
            command list -t [<tag>]
            """
        )

        if not sys.argv[2:]:
            parser.print_help()
            exit(1)

        subparser = parser.add_subparsers()

        subparser.add_parser('tags', help='list tags')

        cmds_subparser = subparser.add_parser('cmds', help='list commands')
        cmds_subparser.add_argument(
            '-t', '--tag', type=str, help='based on tags', nargs='+'
        )

        args = parser.parse_args(sys.argv[2:])
        if sys.argv[2] == 'tags':
            print("list all tags")
        elif sys.argv[2] == 'cmds':
            print("print all cmds", args.tag)


if __name__ == "__main__":
    CommandStash()
