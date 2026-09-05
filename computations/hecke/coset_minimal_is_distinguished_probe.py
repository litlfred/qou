#!/usr/bin/env python3
"""Is the minimal-length element of a right coset of S_mu always DISTINGUISHED?

Mathas' Proposition 3.3 says D_mu is a COMPLETE set of right coset representatives of
S_mu in S_n.  The uniqueness half is proved in Lean
(`CompositionCoset.isDistinguished_unique`).  This probe checks the route proposed for
the EXISTENCE half before any Lean is written, per the formalize-first rule -- the same
discipline that caught the lex-vs-dominance error and the sortPerm orientation error
earlier in this arc.

Two things are checked, and they are different claims:

  (A) every coset contains at least one distinguished element      -- existence itself
  (B) the MINIMAL-LENGTH element of a coset is distinguished       -- the proposed route

(B) implies (A).  If (B) fails but (A) holds, existence is still true and the proof
route has to change, which is exactly the kind of thing worth knowing before formalising.

Also reported, because it is what the Lean proof would actually induct on:

  (C) if d is NOT distinguished, some v in S_mu has ell(v.d) < ell(d)

`IsDistinguished` is the corpus definition: d never inverts two labels landing in the
same block, i.e. `index (d a) = index (d b)` and `a < b` imply `d a < d b`.

Lengths are Coxeter lengths of permutations of Fin n, i.e. inversion counts -- exact
integer arithmetic, no float anywhere in this file.
"""

from itertools import permutations


def compositions(n):
    if n == 0:
        yield ()
        return
    for first in range(1, n + 1):
        for rest in compositions(n - first):
            yield (first,) + rest


def index_map(c):
    """position -> block index, for a composition c."""
    out, blk, filled = [], 0, 0
    for i, part in enumerate(c):
        for _ in range(part):
            out.append(i)
        filled += part
    return out


def length(p):
    n = len(p)
    return sum(1 for a in range(n) for b in range(a + 1, n) if p[a] > p[b])


def compose(p, q):
    """(p . q)(x) = p(q(x))."""
    return tuple(p[q[x]] for x in range(len(q)))


def young_elements(c):
    """Permutations preserving each block of c setwise."""
    starts, s = [], 0
    for part in c:
        starts.append(s)
        s += part
    blocks = [list(range(starts[i], starts[i] + part)) for i, part in enumerate(c)]

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


def is_distinguished(idx, d):
    """d never inverts two labels landing in the same block."""
    n = len(d)
    for a in range(n):
        for b in range(a + 1, n):
            if idx[d[a]] == idx[d[b]] and d[a] > d[b]:
                return False
    return True


def main():
    N_MAX = 6
    cosets = 0
    exist_ok = 0
    minimal_ok = 0
    descent_ok = 0
    exist_fail, minimal_fail, descent_fail = [], [], []

    for n in range(1, N_MAX + 1):
        allperms = list(permutations(range(n)))
        for c in compositions(n):
            idx = index_map(c)
            S = list(young_elements(c))
            seen = set()
            for w in allperms:
                # the right coset S_mu . w  =  { v . w : v in S_mu }
                coset = frozenset(compose(v, w) for v in S)
                if coset in seen:
                    continue
                seen.add(coset)
                cosets += 1

                dist = [d for d in coset if is_distinguished(idx, d)]
                if dist:
                    exist_ok += 1
                elif len(exist_fail) < 5:
                    exist_fail.append((n, c, sorted(coset)[:3]))

                mn = min(length(d) for d in coset)
                minima = [d for d in coset if length(d) == mn]
                if all(is_distinguished(idx, d) for d in minima):
                    minimal_ok += 1
                elif len(minimal_fail) < 5:
                    minimal_fail.append((n, c, [d for d in minima
                                                if not is_distinguished(idx, d)][:2]))

                # (C): every non-distinguished element is shortenable inside S_mu
                ok_c = True
                for d in coset:
                    if is_distinguished(idx, d):
                        continue
                    if not any(length(compose(v, d)) < length(d) for v in S):
                        ok_c = False
                        if len(descent_fail) < 5:
                            descent_fail.append((n, c, d, length(d)))
                        break
                if ok_c:
                    descent_ok += 1

    print(f"Right cosets of S_mu tested (n = 1..{N_MAX}, all compositions): {cosets}")
    print(f"  (A) coset contains a distinguished element      : {exist_ok}"
          f"   fails {cosets - exist_ok}")
    print(f"  (B) every minimal-length element is distinguished: {minimal_ok}"
          f"   fails {cosets - minimal_ok}")
    print(f"  (C) non-distinguished => shortenable within S_mu : {descent_ok}"
          f"   fails {cosets - descent_ok}")
    for label, fails in (("(A)", exist_fail), ("(B)", minimal_fail), ("(C)", descent_fail)):
        if fails:
            print(f"\n  First {label} failures:")
            for f in fails:
                print("   ", f)

    ok = (exist_ok == cosets) and (minimal_ok == cosets) and (descent_ok == cosets)
    print()
    if ok:
        print("VERDICT: existence holds, the minimal-length element IS distinguished,\n"
              "         and the shortening step the induction needs is available.")
    else:
        print("VERDICT: at least one claim FAILS -- see the cases above before formalising.")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
