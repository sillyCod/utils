
def descruct_dict(source: dict) -> dict:
    target = dict()
    for k, v in source.items():
        print(k, v)
        k_list = k.split(".", 1)
        if len(k_list) > 1:
            if not target.get(k_list[0]):
                target[k_list[0]] = descruct_dict({k_list[1]: v})
            else:
                target[k_list[0]].update(**descruct_dict({k_list[1]: v})
        else:
            target[k_list[0]] = v
    # for k, v in target

    return target


if __name__ == "__main__":
    source = {
        "a.b": 1,
        "c.a": 2,
        "d.a.e": 4,
        "c.b": 5
    }

    print(descruct_dict(source))