#!/usr/bin/env python3
"""Corner algebra over each eigenline of sigma_1 in H_n: where does an sl2 live?

Bean qou-wkcd, owner decision 1 follow-up (Furey-type test, coordinator relay 2026-11-15).
For generic q, H_n(q) = (+)_lambda M_{f^lambda}(K) (Wedderburn; cited, [humphreys1990]
§7.4 / Dipper-James). In the block lambda the q-eigenline of sigma_1 has rank a_lambda =
#SYT(lambda) with 2 in the FIRST row, and the (-q^-1)-line has rank b_lambda = #SYT with 2
in the SECOND row (Young's seminormal form: sigma_1 acts by q / -q^-1 on a tableau with
1,2 in the same row / same column). So the corner P H_n P = (+)_lambda M_{rank}(K).
It contains sl2 iff some rank >= 2. Convention D gives zero trace weight to every shape with
>= 3 rows (corpus lemma ocneanuWeight_conventionD_eq_zero_of_three_rows).

Exact integer combinatorics; no floats; no witness; nothing fitted.
"""
import sys
from itertools import permutations


def partitions(n, m=None):
    m = n if m is None else m
    if n == 0:
        yield ()
        return
    for k in range(min(n, m), 0, -1):
        for rest in partitions(n - k, k):
            yield (k,) + rest


def syt(shape):
    """All standard Young tableaux of the shape, as row lists."""
    n = sum(shape)
    out = []

    def rec(rows, k):
        if k > n:
            out.append([list(r) for r in rows])
            return
        for i, r in enumerate(rows):
            if len(r) < shape[i] and (i == 0 or len(rows[i - 1]) > len(r)):
                r.append(k)
                rec(rows, k + 1)
                r.pop()

    rec([[] for _ in shape], 1)
    return out


def row_of(t, k):
    return next(i for i, r in enumerate(t) if k in r)


ok = True
print("lambda | dim | rank q-line (L) | rank -q^-1 line (R) | D weight")
summary = {}
for n in range(2, 7):
    left2, right2 = [], []
    for lam in partitions(n):
        T = syt(lam)
        a = sum(1 for t in T if row_of(t, 2) == 0)
        b = len(T) - a
        dkeep = len(lam) <= 2
        print(f"n={n} {lam} | {len(T)} | {a} | {b} | {'kept' if dkeep else 'ZERO'}")
        if a >= 2:
            left2.append((lam, a, dkeep))
        if b >= 2:
            right2.append((lam, b, dkeep))
    summary[n] = (left2, right2)

print()
for n, (L, R) in summary.items():
    Lk = [x for x in L if x[2]]
    Rk = [x for x in R if x[2]]
    print(f"n={n}: corner sl2 on L in {[(x[0],x[1]) for x in L]} (D-kept {[(x[0]) for x in Lk]}); "
          f"on R in {[(x[0],x[1]) for x in R]} (D-kept {[(x[0]) for x in Rk]})")

# checks
L3, R3 = summary[3]
ok &= (L3 == [] and R3 == [])
print("PASS n=3: both corners commutative (no rank >= 2)" if (L3 == [] and R3 == []) else "FAIL n=3")
L4, R4 = summary[4]
c4 = ([x[0] for x in L4 if x[2]] == [(3, 1)] and [x[0] for x in R4] == [(2, 1, 1)]
      and not any(x[2] for x in R4))
print(("PASS" if c4 else "FAIL") +
      " n=4: L-corner sl2 in (3,1) (D-kept); R-corner sl2 only in (2,1,1) (D weight zero)")
ok &= c4
L5, R5 = summary[5]
c5 = any(x[2] for x in R5)
print(("PASS" if c5 else "FAIL") +
      " n=5: the R-corner ALSO has a D-kept sl2 carrier -> the n=4 one-sidedness does not persist")
ok &= c5
print("\nALL PASS" if ok else "\nSOME FAIL")
sys.exit(0 if ok else 1)
