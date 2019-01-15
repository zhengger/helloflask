# coding=utf-8


from contextlib import contextmanager


@contextmanager
def custome_open(filename):
    fn = open(filename)
    try:
        yield fn
    finally:
        fn.close()


with custome_open('test.py') as f:
    contents = f.read()
    print(contents)
