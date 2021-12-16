from cmdstash.db.dbcore import CommandStashDB


def process_arguments(arguments=None):
    if getattr(arguments, 'parser') == "list":
        list_records(arguments)
    elif getattr(arguments, 'parser') == "add":
        add_records(arguments)


def add_records(args):
    if getattr(args, 'sub_parser') == "command":
        if getattr(args, 'tag') is not None:
            get_tag_id = (
                'SELECT id from tags where '
                'tag_name="{}"'.format(args.tag)
            )
            query = (
                'INSERT INTO commands (command, tag_id) '
                'VALUES ("{}",({}))'.format(args.cmd, get_tag_id)
            )          
        else:
            query = (
                'INSERT INTO commands (command) '
                'VALUES ("{}")'.format(args.cmd)
            )
    elif getattr(args, 'sub_parser') == "tags":
        tags_list = validate_tags(args.tags)
        for tag in tags_list:
            query = (
                'INSERT INTO tags (tag_name) '
                'VALUES ("{}")'.format(tag)
            )
    CommandStashDB('tags')._execute_query(query)


def list_records(args):
    if getattr(args, 'sub_parser') == "command":
        query = (
            'SELECT * from commands'
        )
        # if args.tags:
        #     query += ' WHERE tag_name={}'.format(args.tags)
    elif getattr(args, 'sub_parser') == "tags":
        query = (
            'SELECT * from tags'
        )
    print(CommandStashDB('tags')._execute_query(query))


def validate_tags(tags):
    if len(tags) == 1 and ',' in tags[0]:
        tags = tags[0].split(',')
    for tag in tags:
        if not tag.isalpha():
            print("Tags must only contain alphabets")
            exit(1)
    return tags
