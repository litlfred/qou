#!/usr/bin/env python3
"""qns_levi_lock_beta_exact_probe — the pair-channel Levi exponent is EXACTLY 1.

Bean qou-ohaz / conj:levi-degeneracy. Companion to
qns_levi_lock_scaling_probe.py, which records beta_fit = 0.99628 for this
channel, and to the Lean
QOU/FluidDynamics/levi_pair_channel_branch_b.lean.

WHY THIS PROBE EXISTS. conj:levi-degeneracy is a trichotomy on
beta = limsup_k log C_L(k)/log k: beta = 0 is branch A (blow-up), beta = 1 is
branch B (regular), and 0 < beta < 1 is the MARGINAL WINDOW C, in which the
regularity verdict is explicitly undetermined. A recorded value of 0.99628 is
numerically close to 1 but formally sits inside window C, so on its face the
pair channel reads as undetermined. It is not.

THE CLOSED FORM. The Levi lock is kappa^2 = pi*nu/Gamma and the quantum
viscosity is nu_q = (q-1)/(2q). Writing eps := q - 1,

    nu_q      = eps / (2*(1+eps))
    kappa^2   = pi*eps / (2*Gamma*(1+eps))
    C_L       = 1/kappa^2 = (2*Gamma/pi) * (1+eps)/eps

That is EXACT -- not an asymptotic expansion. So

    log C_L = log(2*Gamma/pi) + log(1+eps) - log(eps)

and beta = lim_{eps->0} log C_L / log(1/eps) = 1 exactly, because the additive
constant and log(1+eps) -> 0 are both o(log(1/eps)). The 0.99628 is a
least-squares slope over a FINITE eps window, dominated by its coarse end,
where log(1+eps) has not yet become negligible. This probe measures that
directly: the secant exponent over successive decades, and the same
least-squares fit the sibling probe runs, so the artifact is identified rather
than argued about.

PRECISION. mpmath end-to-end at 50 dps, per AGENTS.md "PROBES ARE NOT EXEMPT":
a probe conclusion becomes an argument that nothing re-derives, and the whole
point here is a discrepancy in the 3rd decimal place, which float64 slope
fitting is exactly the wrong instrument for. No float() arithmetic; mp.nstr for
display only.

SCOPE (a), per-channel, and CONDITIONAL. The lock formula C_L = Gamma/(pi*nu_q)
is a MODEL INPUT, not derived. This settles what the corpus's own formula
implies for ONE channel (the anti-parallel pair); it does not resolve
conj:levi-degeneracy, and says nothing about channels the lock does not cover.

Run: python3 -u computations/qns_levi_lock_beta_exact_probe.py 2>&1 | tee /tmp/qns_beta.log
"""
from __future__ import annotations

import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
for _p in (_HERE, _HERE.parent / "tools" / "qou-substrate" / "python"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

from mpmath import mp, mpf, log  # noqa: E402

mp.dps = 50

GAMMA = mpf(1)  # circulation; every conclusion below is Gamma-independent


def kappa2_lock(eps: mpf) -> mpf:
    """kappa^2 = pi*nu_q/Gamma with nu_q = (q-1)/(2q), q = 1+eps."""
    q = 1 + eps
    nu_q = (q - 1) / (2 * q)
    return mp.pi * nu_q / GAMMA


def C_L(eps: mpf) -> mpf:
    return 1 / kappa2_lock(eps)


def C_L_closed(eps: mpf) -> mpf:
    """The claimed exact closed form (2*Gamma/pi)*(1+eps)/eps."""
    return (2 * GAMMA / mp.pi) * (1 + eps) / eps


def secant_beta(e1: mpf, e2: mpf) -> mpf:
    """Local exponent between two eps values: log(C2/C1)/log(e1/e2)."""
    return log(C_L(e2) / C_L(e1)) / log(e1 / e2)


def main() -> int:
    print("=" * 78)
    print("Pair-channel Levi exponent: EXACT, not fitted  (mpmath, 50 dps)")
    print("=" * 78)

    # ---- 1. the closed form is exact, not asymptotic -------------------------
    print("\n[1] C_L(eps) == (2*Gamma/pi)*(1+eps)/eps  -- exact identity?")
    worst = mpf(0)
    for k in range(1, 25):
        eps = mpf(10) ** (-k)
        rel = abs(C_L(eps) - C_L_closed(eps)) / C_L_closed(eps)
        worst = max(worst, rel)
    print(f"    worst relative deviation over eps=1e-1..1e-24: {mp.nstr(worst, 5)}")
    # The identity is ALGEBRAIC -- 1/(pi*((q-1)/(2q))/Gamma) = (2*Gamma/pi)*(1+eps)/eps
    # with q = 1+eps -- so this check corroborates, it does not prove. The residual is
    # mpmath rounding at 50 dps working precision, ~1e-28, not a modelling discrepancy.
    # Threshold set at 1e-25: three orders above the observed residual, twenty-five
    # digits below any quantity of interest.
    closed_form_exact = worst < mpf(10) ** (-25)
    print(f"    agrees to >25 digits (algebraic identity; this corroborates): "
          f"{closed_form_exact}")

    # ---- 2. the secant exponent converges to 1 ------------------------------
    print("\n[2] secant exponent over successive decades")
    rows = []
    for k in (1, 2, 4, 7, 11, 15, 19):
        e1, e2 = mpf(10) ** (-k), mpf(10) ** (-(k + 1))
        b = secant_beta(e1, e2)
        rows.append((k, b))
        print(f"    [1e-{k:<2} , 1e-{k+1:<2}]   beta = {mp.nstr(b, 15)}")
    beta_finest = rows[-1][1]
    converges_to_one = abs(beta_finest - 1) < mpf(10) ** (-15)

    # ---- 3. reproduce the sibling probe's fit, and locate the artifact ------
    print("\n[3] least-squares slope over the sibling probe's window (eps=1e-1..1e-8)")
    xs = [-log(mpf(10) ** (-k)) for k in range(1, 9)]
    ys = [log(C_L(mpf(10) ** (-k))) for k in range(1, 9)]
    n = len(xs)
    xb = sum(xs) / n
    yb = sum(ys) / n
    beta_fit = (sum((x - xb) * (y - yb) for x, y in zip(xs, ys))
                / sum((x - xb) ** 2 for x in xs))
    recorded = mpf("0.9962774355467895")
    delta = abs(beta_fit - recorded)
    print(f"    beta_fit = {mp.nstr(beta_fit, 15)}")
    print(f"    sibling witness records {mp.nstr(recorded, 16)}")
    print(f"    |difference| = {mp.nstr(delta, 5)}")
    # The sibling computes this fit in float64. Reproducing it in exact arithmetic
    # therefore should NOT agree to more than float64's reach: a least-squares slope
    # over 8 log-scaled points accumulates ~1e-10. The residual is the sibling's own
    # float64 error, which is a small illustration of why AGENTS.md requires mpmath in
    # probes. Threshold 1e-9 = the float64 accumulation scale for this fit.
    reproduces = delta < mpf("1e-9")
    print(f"    reproduces it to the float64 accumulation scale (1e-9): {reproduces}")

    print("\n    the SAME fit, moved to a finer window (eps=1e-13..1e-20):")
    xs2 = [-log(mpf(10) ** (-k)) for k in range(13, 21)]
    ys2 = [log(C_L(mpf(10) ** (-k))) for k in range(13, 21)]
    xb2, yb2 = sum(xs2) / len(xs2), sum(ys2) / len(ys2)
    beta_fit2 = (sum((x - xb2) * (y - yb2) for x, y in zip(xs2, ys2))
                 / sum((x - xb2) ** 2 for x in xs2))
    print(f"    beta_fit(fine) = {mp.nstr(beta_fit2, 15)}")
    fit_is_window_artifact = abs(beta_fit2 - 1) < abs(beta_fit - 1) / 1000

    # ---- 4. verdict ---------------------------------------------------------
    print("\n" + "=" * 78)
    checks = [
        ("closed form C_L = (2G/pi)(1+eps)/eps agrees to >25 digits", closed_form_exact),
        ("secant exponent -> 1 (|beta-1| < 1e-15 at eps=1e-19)", converges_to_one),
        ("the recorded 0.99628 is reproduced to float64 scale (1e-9)", reproduces),
        ("the same fit on a fine window is >1000x closer to 1", fit_is_window_artifact),
    ]
    for name, ok in checks:
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
    allok = all(ok for _, ok in checks)
    print("=" * 78)
    print(
        "\nVERDICT: beta = 1 EXACTLY for the anti-parallel-pair channel under the\n"
        "lock formula, so this channel is branch B and the marginal window C\n"
        "(0 < beta < 1) is EXCLUDED for it. The recorded 0.99628 is a\n"
        "finite-window least-squares artifact, not a marginal exponent.\n"
        "\nSCOPE: conditional on the lock formula C_L = Gamma/(pi*nu_q), which is a\n"
        "model input and is NOT derived. Per-channel, scope (a). conj:levi-degeneracy\n"
        "is NOT resolved: other channels are untouched, and branch B for one channel\n"
        "is not branch B for the flow.\n"
        "\nThe Lean side does not depend on any of these numbers:\n"
        "linear_condNumber_forces_beta_one DERIVES beta = 1 from linear growth, so\n"
        "no fit precision enters the argument at all."
    )
    return 0 if allok else 1


if __name__ == "__main__":
    raise SystemExit(main())
