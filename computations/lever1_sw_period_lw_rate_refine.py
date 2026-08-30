#!/usr/bin/env python3
"""
lever1_sw_period_lw_rate_refine.py — quantitative refinement of the SW-period ↔ lw fork
(lever-1 / bean z2bn). mpmath-only (runs where sympy is firewalled).

Context. `sw_period_growth_probe.py` (audit-only) resolved the depth-2/SL2 vs #1765/lw fork
for the prolonged SW periods `a_D^(n) = ∮_γ λ_SW^(n)` on the color cubic
`P = X³ + (z+1)X² + (z²+z+1)X + (z³+z²+z+1)`:
  (i)  depth-2:  a_D^(n+2) = τ·a_D^(n+1) − a_D^(n),  ratio → λ₊ ≈ 2.184  (SL2, τ=2.6424)
  (ii) #1765/lw: a_D^(n) = lw(n−1) = (1/n)·Σ_{λ⊢n} dim_q,  ratio GROWS  (super-exp)
and argued (ii) wins via the branch-point Puiseux estimate `a_D^(n) ∝ |(1/2)_n^fall|/R^n`.
The corpus (prop:sw-period-residue-sum, Lean `sw_period_eq_residue_sum`) gives the same period
as an algebraic residue sum = Σ_λ dim_q = lw. So the τ-recurrence is an n≤4 EFFECTIVE FIT
(also Lean-proved (b)-excluded in `Lever1Depth2Exclusion.lean`).

THIS PROBE adds two things the audit-only argument did not pin numerically:
  1. Reproduces the fork in-container (mpmath-only): the lw ratio grows (super-exp) while the
     depth-2 ratio → λ₊, and they SPLIT at n≥5 — confirms the resolution with the local tools.
  2. QUANTITATIVE rate check (new): the NAIVE single-branch estimate `(n−½)/R` (R = nearest of
     the 6 branch points) OVERSHOOTS the true lw ratio (~2.5× at n=8: 7.95 vs 3.10). The color
     cubic has SIX branch points in 3 pairs (|z| ≈ 0.943, 1.0, 1.061); the exact geometric rate
     is the FULL multi-branch residue sum, not the nearest point. The true lw ratio tracks the
     involution-class ~√n growth (q→1 limit of lw is the telephone/involution numbers).

FINDING (scope-(a)): the fork resolution STANDS (super-exp lw, not constant-λ₊ depth-2) — but
the geometric rate is QUANTITATIVELY the multi-branch-point sum, NOT the single-point falling
factorial; the naive rate overshoots ~2.5×. So the open geometric piece is sharper than
"derive τ": it is the exact super-exp a_D^(n) kernel (the q-Bessel-class / multi-branch residue
sum), the τ-recurrence being only the n≤4 shadow. Refines the z2bn "τ=tr B derivation" framing.

Anti-fit: lw is categorical (q-hook dim_q, no fit); the branch points are the cubic's geometry;
τ is the wired closed form. The overshoot is a reported quantitative mismatch, not a tuned match.
No wiring. EXPLORATORY, scope-(a).

Audit: docs/audits/2026-07-12-lever1-sw-period-lw-rate-refine.md
"""
from __future__ import annotations
import sys
from pathlib import Path
from math import sqrt

HERE = Path(__file__).resolve().parent
for p in (str(HERE / "substrate"), str(HERE)):
    if p not in sys.path:
        sys.path.insert(0, p)

import mpmath as mp  # noqa: E402
import _path_bridge  # noqa: F401, E402 — flat-namespace bridge
from _precision import set_compute_dps
set_compute_dps()
# Precision must be raised BEFORE the module-scope constants below: at
# import time mp.dps is still mpmath's default 15 (~binary64), and a
# literal rounded there cannot be recovered by raising dps afterwards.
# Idempotent. Gate: mpf_import_time_dps_audit.py (bean qou-j6gb).
set_compute_dps()

try:
    from q_parameter import Q_50_DIGIT_STR as Q0
    q = mp.mpf(Q0)
except Exception:
    q = mp.mpf('1.1099785955573347')

TAU = mp.mpf('2.6423863133015')   # wired closed form 3(3q⁴+8q²+3)/(4q(q+1)²) at q₀


def qint(k):
    return (q ** k - q ** (-k)) / (q - 1 / q)

def qfac(n):
    r = mp.mpf(1)
    for k in range(1, n + 1):
        r *= qint(k)
    return r

def partitions(n, m=None):
    if m is None:
        m = n
    if n == 0:
        yield ()
        return
    for k in range(min(n, m), 0, -1):
        for r in partitions(n - k, k):
            yield (k,) + r

def hooks(lam):
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])]
    return [(row - j - 1) + (conj[j] - i - 1) + 1
            for i, row in enumerate(lam) for j in range(row)]

def dimq(lam):
    d = qfac(sum(lam))
    for h in hooks(lam):
        d /= qint(h)
    return d

def lw(c):
    return mp.fsum(dimq(l) for l in partitions(c + 1)) / (c + 1)


def branch_points():
    """The 6 branch points (disc_X = 0) of the color cubic, via deg-6 interpolation (no sympy)."""
    def bcd(z):
        return (z + 1, z ** 2 + z + 1, z ** 3 + z ** 2 + z + 1)

    def disc(z):
        b, c, d = bcd(z)
        a = mp.mpf(1)
        return 18 * a * b * c * d - 4 * b ** 3 * d + b ** 2 * c ** 2 - 4 * a * c ** 3 - 27 * a ** 2 * d ** 2

    nodes = [mp.mpf(k) - 3 for k in range(7)]
    V = mp.matrix(7, 7)
    rhs = mp.matrix(7, 1)
    for i, zn in enumerate(nodes):
        for j in range(7):
            V[i, j] = zn ** j
        rhs[i, 0] = disc(zn)
    coef = mp.lu_solve(V, rhs)
    return mp.polyroots([coef[6 - k, 0] for k in range(7)])


def main() -> int:
    bps = branch_points()
    R = min(abs(b) for b in bps)
    abs_bps = sorted(float(abs(b)) for b in bps)
    print("=== lever-1: SW-period ↔ lw fork — quantitative rate refinement (mpmath) ===\n")
    print(f"color-cubic branch points |z| (6 = 3 pairs): "
          f"{['%.4f' % v for v in abs_bps]}")
    print(f"R (nearest to 0) = {float(R):.5f}\n")

    # depth-2/SL2 tower
    aD = {2: mp.mpf(1), 3: lw(2), 4: lw(3)}
    for n in range(5, 9):
        aD[n] = TAU * aD[n - 1] - aD[n - 2]

    print(f"  {'n':>2} {'lw(n-1)':>10} {'lw-ratio':>9} {'(n-½)/R':>9} {'√n':>6} {'depth2-ratio':>13}")
    prev = None
    lw_ratios, d2_ratios, naive, sqrtn = [], [], [], []
    for n in range(2, 9):
        l = lw(n - 1)
        rl = float(l / prev) if prev else float('nan')
        st = float((n - mp.mpf('0.5')) / R)
        rd = float(aD[n] / aD[n - 1]) if n > 2 else float('nan')
        if n > 2:
            lw_ratios.append(rl)
            d2_ratios.append(rd)
            naive.append(st)
            sqrtn.append(sqrt(n))
        print(f"  {n:>2} {float(l):>10.4f} {rl:>9.3f} {st:>9.3f} {sqrt(n):>6.3f} {rd:>13.3f}")
        prev = l

    # --- the three structural facts ---
    lw_grows = all(lw_ratios[i] < lw_ratios[i + 1] for i in range(len(lw_ratios) - 1))  # super-exp
    d2_converges = abs(d2_ratios[-1] - d2_ratios[-2]) < 0.01                            # → λ₊ const
    fork_splits = lw_ratios[-1] - d2_ratios[-1] > 0.5                                   # split at large n
    naive_overshoots = naive[-1] / lw_ratios[-1] > 2.0                                  # ~2.5× at n=8

    print(f"\n### Findings (scope-(a))")
    print(f"  • FORK RESOLVED (reproduced in-container): lw ratio grows "
          f"{lw_ratios[0]:.2f}→{lw_ratios[-1]:.2f} (super-exp) while depth-2 → "
          f"λ₊≈{d2_ratios[-1]:.3f} (constant); they split at n≥5. ⇒ lw/#1765 is the true "
          f"prolongation, τ-recurrence is the n≤4 effective fit.")
    print(f"  • NAIVE single-branch rate OVERSHOOTS: (n−½)/R = {naive[-1]:.2f} at n=8 vs true lw "
          f"ratio {lw_ratios[-1]:.2f} ({naive[-1]/lw_ratios[-1]:.1f}×). The color cubic has 6 "
          f"branch points (3 pairs); the exact rate is the FULL multi-branch residue sum, not the")
    print(f"    nearest point. The lw ratio tracks the involution-class ~√n ({sqrtn[-1]:.2f} at n=8),")
    print(f"    consistent with the q→1 telephone-number limit of lw.")
    print(f"  ⇒ the open geometric piece is sharper than 'derive τ': the exact super-exp a_D^(n)")
    print(f"    kernel (q-Bessel-class / multi-branch residue sum); τ is only its n≤4 shadow.")

    ok = lw_grows and d2_converges and fork_splits and naive_overshoots

    try:
        from witness_base import WitnessBuilder
        wb = WitnessBuilder("lever1-sw-period-lw-rate-refine", engine="mpmath")
        wb.set_description(
            "Lever-1 (z2bn): quantitative refinement of the SW-period↔lw fork, mpmath-only. "
            "Reproduces the fork resolution in-container (lw ratio grows 1.34→3.10 super-exp; "
            "depth-2 → λ₊≈2.18 constant; split at n≥5 ⇒ lw/#1765 is the true prolongation, "
            "τ-recurrence the n≤4 fit). NEW: the naive single-branch rate (n−½)/R overshoots the "
            "true lw ratio ~2.5× at n=8 (color cubic has 6 branch points in 3 pairs; exact rate = "
            "full multi-branch residue sum, not nearest point). lw tracks the involution-class ~√n "
            "(q→1 telephone limit). Sharpens the open piece to the exact super-exp a_D^(n) kernel "
            "(q-Bessel-class), τ being its n≤4 shadow. Anti-fit: lw categorical, branch points "
            "geometric, overshoot reported not tuned. Scope-(a), no wiring.")
        wb.add_data("branch_points_abs", abs_bps)
        wb.add_data("R_nearest", float(R))
        wb.add_data("lw_ratios", lw_ratios)
        wb.add_data("depth2_ratios", d2_ratios)
        wb.add_data("naive_single_branch_rate", naive)
        wb.add_data("naive_overshoot_factor_n8", float(naive[-1] / lw_ratios[-1]))
        wb.add_assertion(
            name="fork_resolved_naive_rate_overshoots",
            computed=str(int(ok)), expected="1", tolerance=0,
            source=("lw ratio grows super-exp (%.2f→%.2f) vs depth-2 → λ₊≈%.3f constant (split at "
                    "n≥5 ⇒ lw is the true prolongation, τ the n≤4 fit); the naive single-branch "
                    "(n−½)/R overshoots the true lw ratio %.1f× at n=8 ⇒ the exact geometric rate "
                    "is the full 6-branch-point residue sum, not the nearest point."
                    % (lw_ratios[0], lw_ratios[-1], d2_ratios[-1], naive[-1] / lw_ratios[-1])))
        out = wb.save()
        print(f"\nWitness: {out}")
    except Exception as e:
        print(f"\n(witness skipped: {e})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
