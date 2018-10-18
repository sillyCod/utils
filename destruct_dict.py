def check_key(key: str) -> bool:
    return len(key.split(".")) == 1


def check_dicts(values):

    for v in values:
        for k in v:
            if check_key(k):
                return False
    return True


def descruct_dict(source: dict) -> dict:
    target = dict()
    for k, v in source.items():
        print(k, v)
        k_list = k.split(".", 1)
        if len(k_list) > 1:
            if not target.get(k_list[0]):
                target[k_list[0]] = {k_list[1]: v}
            else:
                target[k_list[0]].update({k_list[1]: v})
        else:
            target[k_list[0]] = v
    """
    values = filter(lambda v: isinstance(v, dict), target.values())

    _finish = check_dicts(values)
    if not _finish:
        print("-" * 100)
        for k, v in target.items():
            if isinstance(v, dict):
                target[k] = descruct_dict(v)

    return target
    """
    for k, v in target.items():
        if isinstance(v, dict) and not check_dicts(v):
            target[k] = descruct_dict(v)
    return target

if __name__ == "__main__":
    source = {
        "a.b": 1,
        "c.a": 2,
        "c.t.b": 6, 
        "g.d.a.e.f": 4,
        "c.b": 5
    }

    print(descruct_dict(source))