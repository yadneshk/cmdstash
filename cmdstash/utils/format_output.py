from prettytable import PrettyTable


def pretty_output(columns=[], data=[]):
    table = PrettyTable(columns)
    for row in data:
        table.add_row(row)
    print(table)
