coll = {"a": {"b": {"c": 3}}}


def set_(coll, path, value):
    dk = {}
    dk2 = {}
    ll = path
    dk[ll[-1]] = value
    ll = ll[:-1]
    dk2[ll[-1]] = dk
    ll = ll[:-1]
    coll[ll[-1]] = dk2
    return coll
