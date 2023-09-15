def execute(ff, sf=None, arg=None):
    ff()
    if sf is not None:
        if arg is not None:
            sf(arg)
        else:
            sf()


def get_name():
    with open('user_info.txt') as f:
        return f.readlines()[0]


def get_table_name(name_1, name_2):
    name_tuple = sorted([name_1, name_2])
    return f'{name_tuple[0]}_{name_tuple[1]}_messages'

