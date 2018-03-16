def _smsh(xs, n):
    return xs if n <= 1 or len(xs) <= 1 else [xs[0]] + _smsh(xs[1], n-1)

class _C:

    def __getattr__(self, fn):
        n = len(fn) - 3
        if fn[:2] == "mo" and fn[-2:] == "sh" and fn[1:-2] == n*"o":
            return lambda xs: _smsh(xs, n)
        else:
            raise NameError(fn)

s = _C()
