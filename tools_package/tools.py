from inspect import getmembers, isclass


def is_subclass(_class, parent_class):
    subclass = issubclass(_class, parent_class)
    equally = (parent_class == _class)
    if not equally and subclass:
        return True
    return False


def get_col(arr2d, col):
    res = [0] * len(arr2d)
    for i in range(len(arr2d)):
        res[i] = (arr2d[i][col])
    return res


def get_classes(module, parent_class):
    classes = get_col(getmembers(module, isclass), 1)
    filter_func = lambda x: is_subclass(x, parent_class)
    return list(filter(filter_func, classes))


if __name__ == '__main__':
    pass