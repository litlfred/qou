#!/usr/bin/env python3
"""`b_7/b_6` is a TRANSIENT, not an asymptote — the tower does not stop at A = 7.

`binding_magnitude_is_not_validatable_probe.py` measures the resolution of every
quantity in the body-order tower under all 27 mirror conventions and concludes:

    "Resolution IMPROVES with order, inverting where the arc has looked. The best
     determined quantity in the entire tower is b7/b6 = 2.2468 +- 5.0%
     (1.305 digits), and nothing in the corpus has ever looked at it."

That measurement is correct and this probe does not dispute it.  What it measures
is **convention-robustness** -- how much `b_7/b_6` moves when you swap 3H for 3He
and so on.  It does not ask whether the value is CONVERGED IN k, and `k = 7` is
simply where that probe's window ends: A = 2..7.

The vendored AME table does not stop at A = 7.

## The measurement

Extending the same construction to A = 16 (mirror-average the odd-A pair, take the
N=Z nuclide at even A -- the same convention, just further):

    k      mu_k              mu_k / mu_(k-1)
    7     -373.242955        -2.2468     <- where the earlier window ends
    8      725.379111        -1.9435
    9    -1325.31606         -1.8271
   10     2422.71872         -1.8280
   12     9004.22883         -1.9626
   14    35651.8426          -1.9860
   16   135275.123           -1.9355

The sequence of ratios runs -6.03, -2.98, **-2.2468**, -1.94, -1.83, -1.83, -1.89,
-1.96, -1.99, -1.99, -1.96, -1.94.  It is still in transit at k = 7 and settles
near **-1.9**.

So a closed form matched to -2.2468 would be matched to the k = 7 term of a moving
sequence, not to a limit.

## It is not an artifact of the convention

Two conventions that differ in kind, not degree, agree:

    mirror-average / N=Z (parity-switching)   mean ratio k>=10 = -1.9371
    most-bound nuclide at each A (no parity)  mean ratio k>=10 = -1.9046

The second never switches on the parity of A, so it cannot manufacture an
odd-even staggering.  The tail survives it.

## What -2 would mean, stated as a candidate and not a result

`Delta[(-1)^n] = -2(-1)^n`, so a term `c*(-1)^A` in `B(A)` contributes `mu_k` with
ratio tending to -2.  Measured here on a pure staggering: -2.058, -2.032, -2.018,
-2.010, ... -> -2 (NOT exactly -2 at finite k -- the B(0)=B(1)=0 convention adds
boundary terms that decay; an earlier draft of this docstring said "exactly" and
that was wrong).

The observed tail near -1.9 is consistent with odd-even pairing dominating the
high-k coefficients.  That is a CANDIDATE reading, not established: -1.9 is not
-2, the data oscillate more than the pure model, and no mechanism is derived here.

## Scope

(a).  It refutes nothing.  It adds one fact the earlier probe's window could not
see -- that its recommended target is not converged -- and thereby narrows what
that target is worth.

The earlier probe's central conclusion is untouched and, if anything, reinforced:
AME light-nucleus binding is a poor observable to test a mechanism against.  This
probe removes the one quantity that looked like an exception.

mpmath at 50 dps from the vendored AME table; no float64 arithmetic.  `float()`
appears only in f-strings and in ratio reporting.
"""
import sys
from math import comb
from pathlib import Path

_R = Path(__file__).resolve().parents[1]
for _p in (str(_R), str(_R / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import mpmath as mp                                              # noqa: E402
from substrate.codata_constants import ame_binding_mev as AME    # noqa: E402

mp.mp.dps = 50
CHECKS = []


def check(name, got, want, note=""):
    ok = got == want
    CHECKS.append(ok)
    print(f"  [{'ok ' if ok else 'FAIL'}] {name}: {got}" + (f"  ({note})" if note else ""))
    return ok


def tower(Bs, kmax):
    f = lambda j: mp.mpf(0) if j < 2 else Bs[j]                  # noqa: E731
    return {k: sum((-1) ** (k - j) * comb(k, j) * f(j) for j in range(k + 1))
            for k in range(2, kmax + 1)}


def mirror_avg(A):
    """The corpus convention: N=Z nuclide at even A, mirror average at odd A."""
    if A % 2 == 0:
        return AME(A // 2, A)
    Z = (A - 1) // 2
    return (AME(Z, A) + AME(A - Z, A)) / 2


def most_bound(A):
    """A convention that never switches on the parity of A."""
    best = None
    for Z in range(1, A):
        try:
            v = AME(Z, A)
        except Exception:
            continue
        if best is None or v > best:
            best = v
    return best


print("=" * 78)
print("b_7/b_6 is a TRANSIENT — the tower does not stop at A = 7")
print("=" * 78)

Bs = {A: mirror_avg(A) for A in range(2, 17)}
mu = tower(Bs, 16)
rat = {k: mu[k] / mu[k - 1] for k in range(3, 17)}

print("\n1. The ratio sequence, extended past the A<=7 window")
print(f"   {'k':>2} {'mu_k':>16} {'ratio':>10}")
for k in range(2, 17):
    r = f"{float(rat[k]):>10.4f}" if k in rat else " " * 10
    mark = "   <- earlier window ends here" if k == 7 else ""
    print(f"   {k:>2} {mp.nstr(mu[k], 9):>16} {r}{mark}")

check("k=7 ratio reproduces the recorded 2.2468",
      abs(abs(float(rat[7])) - 2.2468) < 1e-3, True, f"{float(rat[7]):.4f}")
check("k=7 is NOT the limit — |ratio| falls below 2 by k=8",
      abs(float(rat[8])) < 2, True, f"{float(rat[8]):.4f}")
tail = [float(rat[k]) for k in range(10, 17)]
check("every ratio for k>=10 lies in (-2.0, -1.8)",
      all(-2.0 < r < -1.8 for r in tail), True,
      f"{min(tail):.4f} .. {max(tail):.4f}")
check("k=7 lies OUTSIDE that band", not (-2.0 < float(rat[7]) < -1.8), True,
      f"{float(rat[7]):.4f}")

print("\n2. Not an artifact — a convention with no parity switch agrees")
Bs2 = {}
for A in range(2, 17):
    v = most_bound(A)
    if v is not None:
        Bs2[A] = v
mu2 = tower(Bs2, max(Bs2))
rat2 = {k: mu2[k] / mu2[k - 1] for k in range(3, max(Bs2) + 1)}
m1 = sum(float(rat[k]) for k in range(10, 17)) / 7
m2 = sum(float(rat2[k]) for k in range(10, 17)) / 7
print(f"       mirror-average / N=Z   mean ratio k>=10 = {m1:.4f}")
print(f"       most-bound at each A   mean ratio k>=10 = {m2:.4f}")
check("both conventions land in (-2.0, -1.8)", -2.0 < m1 < -1.8 and -2.0 < m2 < -1.8,
      True, f"{m1:.4f} and {m2:.4f}")
check("they agree to within 0.05", abs(m1 - m2) < 0.05, True, f"{abs(m1 - m2):.4f}")

print("\n3. What -2 would mean — a candidate reading, not a result")
c = mp.mpf("1.7")
mus = tower({A: c * (-1) ** A for A in range(2, 17)}, 16)
rs = [float(mus[k] / mus[k - 1]) for k in range(8, 17)]
print(f"       pure c*(-1)^A staggering, ratios k=8..16:")
print(f"         {[round(r, 4) for r in rs]}")
check("pure staggering tends to -2 but is NOT exactly -2 at finite k",
      all(r < -2 for r in rs) and abs(rs[-1] + 2) < 1e-3, True,
      f"k=16 gives {rs[-1]:.6f}")
check("and it converges monotonically toward -2",
      all(rs[i] < rs[i + 1] for i in range(len(rs) - 1)), True)
print("       -> the observed tail near -1.9 is CONSISTENT with pairing dominating")
print("          the high-k coefficients.  Candidate, not established: -1.9 is not")
print("          -2, the data oscillate more, and no mechanism is derived here.")

ok = all(CHECKS)
print("\n" + "=" * 78)
print(f"{sum(CHECKS)}/{len(CHECKS)} checks pass")
print("=" * 78)
print("""
VERDICT (scope-(a); nothing refuted):

  b_7/b_6 = -2.2468 is the last point of a sequence still in transit, not a
  limit.  Extending the same construction to A = 16 gives ratios that settle
  near -1.9, and k = 7 lies outside the band every k >= 10 occupies.

  The earlier probe's measurement is correct: b_7/b_6 IS the most
  convention-robust quantity in the A <= 7 window.  Convention-robustness and
  convergence in k are different properties, and only the first was measured.

  Consequence: a closed form matched to -2.2468 would be matched to a
  transient.  The earlier probe's central conclusion -- that AME light-nucleus
  binding is the wrong observable to test a mechanism against -- is untouched
  and strengthened, since this removes the one quantity that looked like an
  exception.
""")
sys.exit(0 if ok else 1)
