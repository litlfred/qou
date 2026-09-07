#!/usr/bin/env python3
"""An AFFINE count multiplicity is structurally excluded by AME2020 — the test is
parameter-free.

CONTEXT.  `QOU.Mass.AffineCountMultiplicityWindow` studies the ansatz that the
count multiplicity is affine, `mu(A) = alpha*A + beta`, and proves the exact
cumulant `b_3 = -(3 alpha + 2 beta)` with the A-dependence cancelling entirely.
That file establishes what the ansatz IMPLIES; it does not test it.

This probe tests it, and it fails.

THE INVARIANT.  Write the binding in the binomial (Mobius) basis,
`B(A) = sum_k mu_k C(A,k)` with the corpus convention `B(0) = B(1) = 0`
(`CoordinationWeightDifferences.b3`, `b4`).  Under the affine ansatz,

    mu_k = (-1)^k [ k (alpha + beta) - beta ]                        (closed form)

so `(-1)^k mu_k` is an AFFINE function of k, for EVERY (alpha, beta).  Hence its
second difference vanishes identically:

    Delta^2 [ (-1)^k mu_k ] = 0                                      (the invariant)

WHY THIS MATTERS METHODOLOGICALLY.  The second-difference test uses NO fitted
parameter.  alpha and beta drop out before any datum is touched, so there is
nothing to tune and nothing to select — this is the opposite of the
selection-against-the-target the NO-FITTING directive bans.  A calibrated
comparison is also reported below, but it is the weaker statement of the two and
is shown only because the sign pattern it exposes is informative.

DATA.  The binomial-basis body-order coefficients, measured exactly and
convention-invariantly (all 27 mirror conventions) from the vendored AME2020
table, as recorded in `QOU/Mass/JetFiltrationSignObstruction.lean`:

    mu_2 +2.22457   mu_3 +1.42622   mu_4 +9.24338
    mu_5 -55.77912  mu_6 +166.12507 mu_7 -373.24295

SCOPE.  (b) — a STRUCTURAL EXCLUSION of the affine class, with the proved
invariant named: `(-1)^k mu_k` affine in k, hence vanishing second difference.
The measured second differences are non-zero and monotonically growing, so no
(alpha, beta) whatsoever reproduces the data.  This is stronger than the usual
scope-(a), and it is legitimate (b) precisely because the invariant is proved
rather than searched for.

It excludes the AFFINE class ONLY.  It says nothing about count multiplicities
in general, nothing about the coordination picture (`z = A-1`), and nothing
about the binding gap's extensive term beyond removing one candidate shape.

Exact `Fraction` arithmetic end to end — no float64 anywhere (AGENTS.md binds
probes exactly as it binds producers).  `float()` appears only inside f-strings.
"""
import sys
from fractions import Fraction as F

# AME2020, convention-invariant across all 27 mirror conventions.
MU = {2: F("2.22457"), 3: F("1.42622"), 4: F("9.24338"),
      5: F("-55.77912"), 6: F("166.12507"), 7: F("-373.24295")}

CHECKS = []


def check(name, got, want, note=""):
    ok = got == want
    CHECKS.append(ok)
    print(f"  [{'ok ' if ok else 'FAIL'}] {name}: {got}" + (f"  ({note})" if note else ""))
    return ok


def affine_mu(k, alpha, beta):
    """The closed form: mu_k = (-1)^k [ k(alpha+beta) - beta ]."""
    return (-1) ** k * (k * (alpha + beta) - beta)


print("=" * 78)
print("An AFFINE count multiplicity is structurally excluded — parameter-free test")
print("=" * 78)

# ---------------------------------------------------------------- closed form
print("\n1. The closed form, verified against the corpus's own cumulant definitions")
# b_2 = bind(2); b_3 = bind(3) - 3 bind(2); b_4 = bind(4) - 4 bind(3) + 6 bind(2)
a, b = F(7), F(-3)          # arbitrary rationals; the identity is not numeric
bind = lambda A: a * A + b  # noqa: E731  -- the affine ansatz
check("mu_2 closed form", affine_mu(2, a, b), bind(2))
check("mu_3 closed form", affine_mu(3, a, b), bind(3) - 3 * bind(2))
check("mu_4 closed form", affine_mu(4, a, b), bind(4) - 4 * bind(3) + 6 * bind(2))
check("mu_5 closed form", affine_mu(5, a, b),
      bind(5) - 5 * bind(4) + 10 * bind(3) - 10 * bind(2))
# and it matches the corpus's own b3_affine_eq
check("agrees with b3_affine_eq = -(3a+2b)", affine_mu(3, a, b), -(3 * a + 2 * b))

# ------------------------------------------------- the parameter-free invariant
print("\n2. The invariant: (-1)^k mu_k is affine in k, so Delta^2 vanishes — for ANY (a,b)")
for (a2, b2) in [(F(7), F(-3)), (F(-1, 3), F(11, 5)), (F(0), F(1)), (F(1), F(0))]:
    s = {k: (-1) ** k * affine_mu(k, a2, b2) for k in range(2, 8)}
    d1 = {k: s[k + 1] - s[k] for k in range(2, 7)}
    d2 = [d1[k + 1] - d1[k] for k in range(2, 6)]
    check(f"Delta^2 == 0 at (a,b)=({a2},{b2})", d2, [F(0)] * 4)

# ------------------------------------------------------------- the measurement
print("\n3. The measured second differences — exact zero is required")
s = {k: (-1) ** k * MU[k] for k in MU}
d1 = {k: s[k + 1] - s[k] for k in range(2, 7)}
d2 = {k: d1[k + 1] - d1[k] for k in range(2, 6)}
print(f"    {'k':>2} {'(-1)^k mu_k':>14} {'Delta1':>13} {'Delta2':>13}")
for k in range(2, 8):
    c1 = f"{float(d1[k]):>13.5f}" if k in d1 else " " * 13
    c2 = f"{float(d2[k]):>13.5f}" if k in d2 else " " * 13
    print(f"    {k:>2} {float(s[k]):>14.5f} {c1} {c2}")
check("second differences computed", len(d2), 4)
check("non-zero count", sum(1 for v in d2.values() if v != 0), 4, "all four; zero required")
check("monotonically increasing", all(d2[k] < d2[k + 1] for k in range(2, 5)), True)
check("smallest |Delta2| exceeds 14", min(abs(v) for v in d2.values()) > 14, True,
      f"min = {float(min(abs(v) for v in d2.values())):.5f}")

# --------------------------------------------------- the calibrated comparison
print("\n4. Calibrated on mu_2, mu_3 only — every uncalibrated prediction is WRONG-SIGNED")
alpha = MU[3] + 2 * MU[2]
beta = MU[2] - 2 * alpha
check("calibration reproduces mu_2", affine_mu(2, alpha, beta), MU[2], "by construction")
check("calibration reproduces mu_3", affine_mu(3, alpha, beta), MU[3], "by construction")
print(f"    alpha = {float(alpha):.6f}   beta = {float(beta):.6f}")
print(f"    {'k':>2} {'predicted':>13} {'measured':>13} {'sign':>10} {'meas/pred':>10}")
opposite = 0
for k in range(2, 8):
    p, m = affine_mu(k, alpha, beta), MU[k]
    same = (p > 0) == (m > 0)
    if k >= 4 and not same:
        opposite += 1
    tag = "  <- calibrated" if k <= 3 else ""
    print(f"    {k:>2} {float(p):>13.5f} {float(m):>13.5f} "
          f"{'same' if same else 'OPPOSITE':>10} {float(m / p):>10.2f}{tag}")
check("uncalibrated predictions with OPPOSITE sign", opposite, 4, "k = 4,5,6,7 — all of them")

print("\n5. The two sign sequences are in ANTIPHASE, not merely different")
pred_sign = [1 if affine_mu(k, alpha, beta) > 0 else -1 for k in range(4, 8)]
meas_sign = [1 if MU[k] > 0 else -1 for k in range(4, 8)]
check("predicted signs k=4..7", pred_sign, [-1, 1, -1, 1])
check("measured  signs k=4..7", meas_sign, [1, -1, 1, -1])
check("exact antiphase", [-x for x in pred_sign], meas_sign)

ok = all(CHECKS)
print("\n" + "=" * 78)
print(f"{sum(CHECKS)}/{len(CHECKS)} checks pass")
print("=" * 78)
print("""
VERDICT (scope-(b), structural exclusion of the affine class):

  Under an affine count multiplicity mu(A) = alpha*A + beta, the quantity
  (-1)^k mu_k is an AFFINE function of k for every (alpha, beta), so its second
  difference vanishes identically.  The measured second differences are

      +14.32039   +35.86614   +63.81021   +96.77193

  non-zero and monotonically growing.  NO (alpha, beta) reproduces AME2020.

  The test is parameter-free: alpha and beta cancel before any datum is used, so
  nothing is fitted and nothing is selected.  The calibrated comparison is the
  weaker corollary and is reported only because its failure is systematic --
  every one of the four uncalibrated predictions carries the OPPOSITE sign, in
  exact antiphase, with the magnitude gap growing 1.82 -> 6.39 -> 13.42 -> 23.28.

  EXCLUDES: the affine class only.
  DOES NOT TOUCH: count multiplicities in general, the coordination picture
  z = A-1, or the binding gap's extensive term beyond removing one shape.
""")
sys.exit(0 if ok else 1)
