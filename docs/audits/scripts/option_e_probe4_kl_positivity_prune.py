#!/usr/bin/env python3
"""Formalize-first PRUNE of Option-E PROBE 4 (Delta_lambda from a Kazhdan-Lusztig /
crystal multiplicity sum), via KL positivity.

Context (docs/coordination/option-e.md): the deuteron Delta_lambda is CLOSED by the
STRUCTURAL form  Delta_lambda = sgn(w0^{S_{lambda'}}) * dim(V_lambda)  (chirality sign
times the regular-rep dimension).  The remaining in-Option-E path is PROBE 4: derive
Delta_lambda from a sum  Sum_w  n^w_lambda * X_w  weighted by KL multiplicities
n^w_lambda (extend kazhdan_lusztig.py past n<=4 to S_6).  The single-vertex / trivial-
multiplicity candidates were already refuted (= chi^lambda); PROBE 4 hopes NON-trivial
KL multiplicities close it.

PRUNE (no KL engine needed): the target Delta_lambda has MIXED signs (computed below).
KL multiplicities are NON-NEGATIVE integers (Kazhdan-Lusztig positivity; classical for
S_n via intersection cohomology / Elias-Williamson in general).  A sum of non-negative
weights  Sum_w n^w_lambda * X_w  can only produce the negative Delta_lambda blocks if the
sign comes from the X_w (the braid-image traces), NOT from the multiplicities.  So:
  * KL/crystal multiplicities can supply at most the MAGNITUDE |Delta_lambda| = dim(V_lambda)
    -- which is ALREADY the deuteron closure's f^lambda;
  * the chirality SIGN sgn(w0^{S_{lambda'}}) must be supplied exogenously, exactly as the
    deuteron closure already does.
=> PROBE 4 is not a new closure mechanism: at best it re-derives |Delta_lambda| = dim via
   a longer route; it cannot supply the sign.  De-prioritise the S_6 KL extension.

No external deps (pure combinatorics).
"""
from math import factorial
import sys


def partitions(n, mx=None):
    if mx is None:
        mx = n
    if n == 0:
        yield ()
        return
    for k in range(min(n, mx), 0, -1):
        for rest in partitions(n - k, k):
            yield (k,) + rest


def hook_dim(lam):
    n = sum(lam)
    prod = 1
    for i, row in enumerate(lam):
        for j in range(row):
            arm = row - j - 1
            leg = sum(1 for k in range(i + 1, len(lam)) if lam[k] > j)
            prod *= (arm + leg + 1)
    return factorial(n) // prod


def transpose(lam):
    return tuple(sum(1 for r in lam if r > c) for c in range(lam[0])) if lam else ()


def sgn_w0(m):
    """sign of the longest element of S_m."""
    return (-1) ** (m * (m - 1) // 2)


def sgn_w0_young(lamT):
    """sgn(w0 of the Young subgroup S_{lamT}) = product over column lengths lamT."""
    s = 1
    for col in lamT:
        s *= sgn_w0(col)
    return s


print("=" * 70)
print("Target Delta_lambda = sgn(w0^{S_lambda'}) * dim(V_lambda) -- sign pattern")
print("=" * 70)
mixed = {}
for n in (3, 6):
    pos = neg = 0
    for lam in partitions(n):
        d = hook_dim(lam)
        s = sgn_w0_young(transpose(lam))
        val = s * d
        pos += (val > 0)
        neg += (val < 0)
    mixed[n] = (pos, neg)
    print(f"  n={n}: {pos} positive blocks, {neg} negative blocks  -> MIXED: {pos > 0 and neg > 0}")

print()
print("=" * 70)
print("KL-positivity PRUNE of PROBE 4")
print("=" * 70)
print("  KL multiplicities n^w_lambda are NON-NEGATIVE integers (KL positivity).")
print("  The target Delta_lambda has MIXED signs (above).  A non-negative-weighted")
print("  sum  Sum_w n^w_lambda * X_w  cannot supply those signs from the weights;")
print("  the chirality sign must come from the X_w (braid images) exogenously.")
print("  => KL/crystal multiplicities supply at most |Delta_lambda| = dim(V_lambda),")
print("     which is ALREADY the deuteron closure's f^lambda.  PROBE 4 is not a")
print("     new closure mechanism; de-prioritise the S_6 KL extension.")

# Assertions: the prune rests on the target being mixed-sign at both n.
assert mixed[3] == (1, 2), "n=3 target sign pattern drift"
assert mixed[6][0] > 0 and mixed[6][1] > 0, "n=6 target must be mixed-sign"
print("\nKL-POSITIVITY PRUNE ASSERTIONS VERIFIED (target is mixed-sign).")
sys.exit(0)
