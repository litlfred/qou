#!/usr/bin/env python3
"""Is the block-sorting permutation `sortPerm` a MINIMAL-LENGTH coset representative?

The next step of Mathas' Lemma 3.9 is the intertwining `T_d . x_mu = x_nu . T_d`.
It holds when `T_v T_d = T_{vd}` for every `v` in the Young subgroup, i.e. when

    ell(v . d) = ell(v) + ell(d)   for all v in S,

which is exactly the statement that `d` is of minimal length in its coset `S d` --
Mathas' `d in D_mu`.  `QOU.BraidKnot.CompositionYoung.sortPerm` constructs a `d`
carrying one composition's blocks onto another's, but **nothing so far shows it is
the minimal-length one**, and the intertwining is false without that.

This probe answers it before any Lean is written, per the formalize-first rule --
the same discipline that caught the lex-vs-dominance error two commits ago.

`sortPerm` is reimplemented here exactly as the Lean builds it: read a position in
`c'`'s block coordinates (block index, offset), rename the block along the matching,
write it back in `c`'s coordinates.  Lengths are Coxeter lengths of permutations of
`Fin n`, i.e. inversion counts -- exact integer arithmetic, no float anywhere.
"""

from itertools import permutations


def compositions(n):
    """All compositions of n as tuples of positive ints."""
    if n == 0:
        yield ()
        return
    for first in range(1, n + 1):
        for rest in compositions(n - first):
            yield (first,) + rest


def starts(c):
    """Prefix sums: the first position of each block."""
    out, s = [], 0
    for part in c:
        out.append(s)
        s += part
    return out


def coords(c):
    """position -> (block index, offset within block)."""
    st = starts(c)
    out = {}
    for i, part in enumerate(c):
        for j in range(part):
            out[st[i] + j] = (i, j)
    return out


def sort_perm(c, cprime, pi):
    """The Lean `sortPerm`, as a tuple d with d[l] = image of l.

    `pi` maps a block index of `cprime` to one of `c`, with matching sizes.  The Lean
    defines `e` (c'-coords -> c-coords) and sets `sortPerm = e.symm`; both are tested.
    """
    n = sum(c)
    cp_coords = coords(cprime)
    c_starts = starts(c)
    e = [0] * n
    for l in range(n):
        i, j = cp_coords[l]
        e[l] = c_starts[pi[i]] + j
    d = [0] * n
    for l in range(n):
        d[e[l]] = l          # d = e^{-1}
    return tuple(e), tuple(d)


def length(p):
    """Coxeter length = number of inversions."""
    n = len(p)
    return sum(1 for a in range(n) for b in range(a + 1, n) if p[a] > p[b])


def compose(p, q):
    """(p . q)(x) = p(q(x))."""
    return tuple(p[q[x]] for x in range(len(q)))


def young_elements(c):
    """Every permutation preserving each block of `c` setwise."""
    st = starts(c)
    blocks = [list(range(st[i], st[i] + part)) for i, part in enumerate(c)]
    def rec(k, acc):
        if k == len(blocks):
            perm = [0] * sum(c)
            for blk, img in acc:
                for a, b in zip(blk, img):
                    perm[a] = b
            yield tuple(perm)
            return
        for img in permutations(blocks[k]):
            yield from rec(k + 1, acc + [(blocks[k], img)])
    yield from rec(0, [])


def matchings(c, cprime):
    """Every size-preserving bijection blocks(c') -> blocks(c)."""
    k = len(cprime)
    if k != len(c):
        return
    for pi in permutations(range(k)):
        if all(cprime[i] == c[pi[i]] for i in range(k)):
            yield pi


def main():
    N_MAX = 6
    tested = 0
    add_e = 0
    add_d = 0
    fail_examples = []

    for n in range(2, N_MAX + 1):
        comps = list(compositions(n))
        for c in comps:
            for cprime in comps:
                for pi in matchings(c, cprime):
                    e, d = sort_perm(c, cprime, pi)
                    tested += 1
                    # d minimal in S_c . d  <=>  ell(v.d) = ell(v) + ell(d) for all v in S_c
                    ok_d = all(length(compose(v, d)) == length(v) + length(d)
                               for v in young_elements(c))
                    ok_e = all(length(compose(v, e)) == length(v) + length(e)
                               for v in young_elements(c))
                    if ok_d:
                        add_d += 1
                    if ok_e:
                        add_e += 1
                    if not ok_d and len(fail_examples) < 6:
                        fail_examples.append((n, c, cprime, pi, d, length(d)))

    print(f"(composition, composition, matching) triples tested, n = 2..{N_MAX}: {tested}")
    print(f"  ell(v.d) = ell(v) + ell(d) for all v in S_c   [d = sortPerm]  : {add_d}")
    print(f"  ell(v.e) = ell(v) + ell(e) for all v in S_c   [e = its inverse]: {add_e}")
    print(f"  failures for d: {tested - add_d}")
    if fail_examples:
        print("\n  First failures (n, c, c', pi, d, ell(d)):")
        for f in fail_examples:
            print("   ", f)
    print()
    if add_d == tested:
        print("VERDICT: sortPerm IS length-minimal in its coset on the whole sample --"
              "\n         the intertwining T_d . x_mu = x_nu . T_d has its hypothesis.")
    else:
        print("VERDICT: sortPerm is NOT always length-minimal. The intertwining does NOT"
              "\n         follow from the construction as it stands; a minimality argument"
              "\n         or a different d is required.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
