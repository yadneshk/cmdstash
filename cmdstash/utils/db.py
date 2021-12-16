from cmdstash.db.dbcore import CommandStashDB
from cmdstash.db.dbcore import TABLE_TAGS, TABLE_COMMANDS


def process_arguments(arguments=None):
    if getattr(arguments, 'parser') == "list":
        list_records(arguments)
    elif getattr(arguments, 'parser') == "add":
        add_records(arguments)


def add_records(args):
    if getattr(args, 'sub_parser') == "command":
        if getattr(args, 'tag') is not None:
            get_tag_id = (
                'SELECT id FROM {} WHERE '
                'tag_name="{}"'.format(TABLE_TAGS, args.tag)
            )
            query = (
                'INSERT INTO {} (command, tag_id) '
                'VALUES ("{}",({}))'.format(
                    TABLE_COMMANDS, args.cmd, get_tag_id
                )
            )
        else:
            query = (
                'INSERT INTO {} (command) '
                'VALUES ("{}")'.format(TABLE_COMMANDS, args.cmd)
            )
    elif getattr(args, 'sub_parser') == "tags":
        tags_list = validate_tags(args.tags)
        for tag in tags_list:
            query = (
                'INSERT INTO {} (tag_name) '
                'VALUES ("{}")'.format(TABLE_TAGS, tag)
            )
    CommandStashDB()._execute_query(query)


def list_records(args):
    if getattr(args, 'sub_parser') == "command":
        if getattr(args, 'tags') is not None:
            get_tag_id = (
                'SELECT id FROM {} '
                'WHERE tag_name="{}"'.format(TABLE_TAGS, args.tags)
            )
            query = (
                'SELECT * FROM {} WHERE '
                'tag_id=({})'.format(TABLE_COMMANDS, get_tag_id)
            )
        else:
            query = (
                'SELECT * FROM {}'.format(TABLE_COMMANDS)
            )
    elif getattr(args, 'sub_parser') == "tags":
        query = (
            'SELECT * FROM {}'.format(TABLE_TAGS)
        )
    print(CommandStashDB()._execute_query(query))


def validate_tags(tags):
    if len(tags) == 1 and ',' in tags[0]:
        tags = tags[0].split(',')
    for tag in tags:
        if not tag.isalpha():
            print("Tags must only contain alphabets")
            exit(1)
    return tags
