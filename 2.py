from collections.abc import Hashable


def adda(x):
    st = {item for item in x if isinstance(item, Hashable)}
    print(st)


adda([66, [8], 55, 56])
