"""Dehornoy handle reduction for B_n, and the Dehornoy floor.

Word = list of signed ints: +i is sigma_i, -i is sigma_i^{-1}.

A sigma_i-handle is a subword  sigma_i^e v sigma_i^{-e}  where v contains no
sigma_i and no sigma_j with j < i.  It reduces to v with each sigma_{i+1}^d
replaced by  sigma_{i+1}^{-e} sigma_i^d sigma_{i+1}^{e}.
Dehornoy: this terminates, and the result is sigma-consistent.
"""

def free_reduce(w):
    out = []
    for x in w:
        if out and out[-1] == -x:
            out.pop()
        else:
            out.append(x)
    return out


def find_handle(w):
    for p in range(len(w)):
        i = abs(w[p])
        for q in range(p + 1, len(w)):
            if abs(w[q]) < i:
                break                      # a lower index intervenes
            if abs(w[q]) == i:
                if w[q] == -w[p]:
                    inner = w[p + 1:q]
                    if all(abs(x) > i for x in inner):
                        return p, q
                break                      # same index, same sign: not a handle
    return None


def handle_reduce(w, cap=200000):
    w = free_reduce(w)
    for _ in range(cap):
        h = find_handle(w)
        if h is None:
            return w
        p, q = h
        e = 1 if w[p] > 0 else -1
        i = abs(w[p])
        new = []
        for x in w[p + 1:q]:
            if abs(x) == i + 1:
                d = 1 if x > 0 else -1
                new += [-e * (i + 1), d * i, e * (i + 1)]
            else:
                new.append(x)
        w = free_reduce(w[:p] + new + w[q + 1:])
    raise RuntimeError("handle reduction did not terminate within cap")


def sign_of(w):
    """+1 if w > 1 (sigma-positive), -1 if w < 1, 0 if w == 1."""
    r = handle_reduce(w)
    if not r:
        return 0
    i = min(abs(x) for x in r)
    firsts = [x for x in r if abs(x) == i]
    return 1 if firsts[0] > 0 else -1


def inv(w):
    return [-x for x in reversed(w)]


def less(a, b):
    return sign_of(inv(a) + b) == 1


DELTA2 = [1, 2, 1, 2, 1, 2]          # Delta^2 = (s1 s2)^3 in B_3, central


def power(w, k):
    if k >= 0:
        return w * k
    return inv(w) * (-k)


def dehornoy_floor(beta, max_m=12):
    """Minimal m >= 0 with Delta^{-2m-2} < beta < Delta^{2m+2}  (Ito Def. 1)."""
    for m in range(max_m + 1):
        lo, hi = power(DELTA2, -(m + 1)), power(DELTA2, m + 1)
        if less(lo, beta) and less(beta, hi):
            return m
    return None
