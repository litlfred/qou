#!/usr/bin/env python3
"""Engine-verified backing for the Option-E PROBE 4 KL-positivity prune.

The prune (docs/audits/2026-06-16-option-e-probe4-kl-positivity-prune.md, merged)
argued from the KL-positivity THEOREM that a Kazhdan-Lusztig multiplicity sum
Sum_w n^w_lambda * X_w cannot supply the mixed-sign target
Delta_lambda = sgn(w0^{S_{lambda'}}) * dim(V_lambda).

This script makes the two premises ENGINE-VERIFIED (not just theorem-cited), using
the in-repo KL engine `computations/kazhdan_lusztig.py`:

  (P1) KL positivity: every Kazhdan-Lusztig polynomial P_{x,w}(q) for S_4 -- the
       SMALLEST symmetric group with non-trivial KL polynomials -- has
       NON-NEGATIVE integer coefficients.  (The 6 non-trivial ones are all q+1.)
       => any multiplicity n^w_lambda built from the C-basis is a non-negative
          integer.
  (P2) the target Delta_lambda is MIXED-sign already at n=4.

(P1) + (P2) => no non-negative-weighted sum reproduces the target: the prune holds,
now on real KL data, not only the theorem.

deps: computations/kazhdan_lusztig.py (in-repo); stdlib otherwise.
"""
import os
import sys
from math import factorial

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(ROOT, "computations"))

try:
    import kazhdan_lusztig as kl
    import sympy as sp
except ImportError as e:  # pragma: no cover
    print(f"SKIP: KL engine / sympy unavailable ({type(e).__name__}: {e}).")
    if os.environ.get("CI"):
        sys.exit(1)
    sys.exit(0)


# ---------- (P1) KL positivity at S_4 via the real engine ----------
def kl_positivity_S4():
    S4 = kl.permutations_S_n(4)
    q = sp.symbols("q")
    nonneg = True
    nontrivial = []
    pairs = 0
    for w in S4:
        for x in S4:
            P = kl.kl_polynomial(x, w)
            pairs += 1
            poly = sp.Poly(sp.expand(P), q) if P != 0 else None
            coeffs = poly.all_coeffs() if poly is not None else [0]
            if any(sp.nsimplify(c) < 0 for c in coeffs):
                nonneg = False
            s = str(sp.expand(P))
            if s not in ("0", "1"):
                nontrivial.append(s)
    return pairs, nonneg, nontrivial


# ---------- (P2) mixed-sign target Delta_lambda = sgn*dim ----------
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


def sgn_w0_young(lam):
    s = 1
    for col in transpose(lam):
        s *= (-1) ** (col * (col - 1) // 2)
    return s


print("=" * 70)
print("(P1) KL positivity at S_4 (real engine: computations/kazhdan_lusztig.py)")
print("=" * 70)
pairs, nonneg, nontrivial = kl_positivity_S4()
from collections import Counter
print(f"  P_(x,w) computed: {pairs} pairs (= 24^2)")
print(f"  ALL coefficients >= 0 (KL positivity): {nonneg}")
print(f"  non-trivial KL polynomials: {len(nontrivial)} -> {dict(Counter(nontrivial))}")

print()
print("=" * 70)
print("(P2) target Delta_lambda = sgn(w0^{S_lambda'})*dim is mixed-sign at n=4")
print("=" * 70)
pos = neg = 0
for lam in partitions(4):
    val = sgn_w0_young(lam) * hook_dim(lam)
    pos += val > 0
    neg += val < 0
    print(f"  lam={str(lam):<14} Delta={val:+d}")
print(f"  => {pos} positive, {neg} negative -> MIXED: {pos > 0 and neg > 0}")

print()
print("=" * 70)
print("VERDICT")
print("=" * 70)
print("  (P1) KL multiplicities n^w_lambda (built from the C-basis, coeffs >= 0)")
print("       are NON-NEGATIVE -- engine-verified at the smallest non-trivial S_4.")
print("  (P2) the target is mixed-sign.")
print("  => Sum_w n^w_lambda * X_w cannot supply the chirality sign; PROBE 4 is")
print("     not a closure mechanism.  The merged prune is now ENGINE-VERIFIED,")
print("     not only theorem-cited.")

assert nonneg, "KL positivity must hold at S_4"
assert len(nontrivial) == 6 and set(nontrivial) == {"q + 1"}, "S_4 non-trivial KL polys must be six copies of q+1"
assert pos > 0 and neg > 0, "n=4 target must be mixed-sign"
print("\nENGINE-VERIFIED PRUNE ASSERTIONS PASS.")
sys.exit(0)
