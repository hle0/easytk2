import asyncio
import inspect

from . import asynctk


def find_areas(layout):
    s = inspect.cleandoc(layout)
    lines = s.splitlines()
    # remove the first and last lines
    lines = lines[1:len(lines) - 1]
    c2d = [list(line) for line in lines]
    # remove the first and last columns
    first_len = len(c2d[0])
    assert all(len(line) == first_len for line in c2d)
    c2d = [line[1:first_len - 1] for line in c2d]
    # actually do everything
    symbols = set()
    for i in c2d:
        for j in i:
            if j.isalnum():
                symbols.add(j)

    for symbol in symbols:
        start = None
        end = None

        # find the top left
        for x, i in enumerate(c2d):
            for y, j in enumerate(i):
                if j == symbol:
                    start = (x, y)
                    break
            if start is not None:
                break

        # find the bottom right
        for x, i in reversed(list(enumerate(c2d))):
            for y, j in reversed(list(enumerate(i))):
                if j == symbol:
                    end = (x, y)
                    break
            if end is not None:
                break

        assert start is not None
        assert end is not None

        span = (end[0] - start[0] + 1, end[1] - start[1] + 1)

        yield (
            symbol,
            {
                "row": start[0],
                "column": start[1],
                "rowspan": span[0],
                "columnspan": span[1],
            },
        )


def grid(layout, allow_missing=False, **kwargs):
    d = {k: v for (k, v) in find_areas(layout)}

    if not allow_missing:
        assert d.keys() == kwargs.keys()

    for k, v in d.items():
        print(f"{k}: {v}")
        kwargs[k].grid(**v)


class prefab:

    def __init__(self, func):
        self.func = func

    def make_parent(self):
        return asynctk.AsyncTk()

    async def run_async(self, *args, **kwargs):
        tk = self.make_parent()
        self.func(tk, *args, **kwargs)
        return await tk.wait()

    def run(self, *args, **kwargs):
        loop = asyncio.new_event_loop()
        return loop.run_until_complete(self.run_async(*args, **kwargs))
