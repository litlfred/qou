#!/usr/bin/env python3
"""
lever1_gevrey_order_pin.py — pin the Gevrey order of the binding period a_D^(n) (lever-1 / z2bn).

Context. An external AI dialog (2026-07-12 session) proposed an alien-calculus / resurgence
framing for the binding kernel, whose load-bearing technical claim is that the branch-point
Puiseux structure of the color cubic forces `a_D^(n) ∝ |(1/2)_n^fall|/R^n` — FACTORIAL
(Gevrey-1) growth — so that the standard (level-1) Borel transform tames the series and its
singularities ω carry alien derivatives Δ_ω. The corpus already measured that the naive
single-branch factorial rate OVERSHOOTS the true lw ratio ~2.6× at n=8
(lever1_sw_period_lw_rate_refine.py): lw tracks the involution-class ~√n ratio.

THIS PROBE pins the growth class precisely:
  1. q=1 (exact integers): a_D^(n) = I(n)/n with I(n) the involution/telephone numbers
     (A000085). Gevrey order s := lim log a_D^(n) / (n log n) = 1/2, NOT 1. Verified against
     the classical asymptote I(n) ~ (n/e)^{n/2} e^{√n−1/4}/√2 and by the two-sided
     integer sandwich  n! ≤ 4^n·I(n)²  and  I(n)² ≤ 2^n·n!  (Lean-proved sorry-free in
     QOU/Mass/BindingGevreyHalf.lean; asserted here numerically for n ≤ 60).
  2. Level-1 Borel is the WRONG plane: the level-1 Borel coefficients a_D^(n)/n! decay
     super-exponentially ⇒ B₁[a_D] is ENTIRE ⇒ no finite singularities ⇒ no alien
     derivatives in that plane. The dialog's Gevrey-1 picture fails as stated.
  3. q₀ (numerical): S(n) = Σ_{λ⊢n} dim_q(λ) at the substrate q₀ — the deformation dressing
     ln(S_q(n)/I(n))/n GROWS through n=28 (0.017 → 0.36), and the exact per-partition
     exponent bound (balanced convention) is dim_q ≤ [n]_q! ~ q^{n(n−1)/2}, with the
     staircase-class shapes attaining exponent n²/2 − Θ(n^{3/2}). So the q-deformation
     CHANGES the divergence class: classical Gevrey-1/2 at q=1 → q-GEVREY (Jackson q-Borel
     territory, a_n ≲ q^{n²/2}) at q₀, with the measured exponent ratio
     ln(S_q/I)/((n²/2)·ln q) rising 0.05 → 0.25 (n ≤ 28; n^{−1/2}-class corrections;
     asymptotic regime not reached). Canonical planes: level-1/2 Borel at q=1 (probed in
     lever1_borel_half_singularity_probe.py); the q₀ object sits between the classical and
     q-Borel scales — an Écalle acceleration chain, sharpening what "resurgence of the
     binding kernel" would even mean.

FINDING (scope-(a) + two Lean-proved integer inequalities): the binding period is
Gevrey-1/2 at q=1, not Gevrey-1 (refutes the external dialog's level-1 Borel framing);
at q₀ the class deforms toward q-Gevrey. Anti-fit: I(n) exact integers from the proved
telephone recurrence; dim_q categorical q-hook; nothing tuned, nothing wired. EXPLORATORY.

Audit: docs/audits/2026-07-12-alien-calculus-review-binding-gevrey-half.md
"""
from __future__ import annotations
import sys
from pathlib import Path

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

NMAX = 60          # exact q=1 range
NMAX_Q = 28        # q₀ symbolic-free numeric range (partitions of 28 = 3718)


def involution_numbers(nmax):
    I = [1, 1]
    for n in range(2, nmax + 1):
        I.append(I[n - 1] + (n - 1) * I[n - 2])
    return I


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


def S_q(n):
    return mp.fsum(dimq(l) for l in partitions(n))


def main() -> int:
    print("=== lever-1: Gevrey-order pin for the binding period a_D^(n) ===\n")
    I = involution_numbers(NMAX)

    # --- 1. two-sided integer sandwich (the Lean statements), n ≤ 60 exact ---
    fact = [1] * (NMAX + 1)
    for n in range(1, NMAX + 1):
        fact[n] = fact[n - 1] * n
    sandwich_ok = all(
        fact[n] <= 4 ** n * I[n] ** 2 and I[n] ** 2 <= 2 ** n * fact[n]
        for n in range(NMAX + 1))
    print(f"sandwich  n! ≤ 4ⁿ·I(n)²  and  I(n)² ≤ 2ⁿ·n!   (n ≤ {NMAX}): "
          f"{'HOLDS' if sandwich_ok else 'FAILS'}  [Lean: BindingGevreyHalf.lean]")

    # --- 2. Gevrey slope s_n = log a_D / (n log n) → 1/2, + asymptote check ---
    print(f"\n  {'n':>3} {'s_n=ln(aD)/(n ln n)':>20} {'ln I − asymptote':>17} {'(aD/n!)^(1/n)':>14}")
    slope = {}
    asym_err = {}
    level1 = {}
    for n in (10, 20, 30, 40, 50, 60):
        aD = mp.mpf(I[n]) / n
        s = mp.log(aD) / (n * mp.log(n))
        A = (n / mp.mpf(2)) * mp.log(n) - n / mp.mpf(2) + mp.sqrt(n) - mp.mpf('0.25') - mp.log(2) / 2
        err = mp.log(I[n]) - A
        b1 = (aD / mp.mpf(fact[n])) ** (mp.mpf(1) / n)
        slope[n], asym_err[n], level1[n] = float(s), float(err), float(b1)
        print(f"  {n:>3} {float(s):>20.5f} {float(err):>17.5f} {float(b1):>14.6f}")
    gevrey_half = abs(asym_err[60]) < 0.05 and 0.35 < slope[60] < 0.5
    # (a_D/n!)^(1/n) for a Gevrey-1/2 sequence decays like √(e/n) → 0; assert the scaling.
    lvl1_scaled = {n: level1[n] * mp.sqrt(n / mp.e) for n in level1}
    level1_entire = (level1[60] < level1[30] < level1[10]
                     and 0.8 < float(lvl1_scaled[60]) < 1.2)
    print(f"\n  ln I(n) matches the (n/e)^(n/2)·e^(√n−1/4)/√2 asymptote to "
          f"{asym_err[60]:+.4f} at n=60 ⇒ order 1/2 (slope s_60={slope[60]:.4f}, → 1/2 like 1/ln n)")
    print(f"  level-1 Borel coeff (a_D/n!)^(1/n) ↓ {level1[10]:.4f} → {level1[60]:.6f}, matching "
          f"√(e/n) (scaled: {float(lvl1_scaled[60]):.3f} ≈ 1) ⇒ B₁ ENTIRE "
          f"(no finite singularity, no Δ_ω in the level-1 plane)")

    # --- 3. q₀: the deformation CHANGES the class toward q-Gevrey ---
    lnq = mp.log(q)
    print(f"\n  {'n':>3} {'S_q(n)':>14} {'ln(S_q/I)/n':>12} {'lnS_q/((n²/2)lnq)':>18}")
    dress = {}
    qgev = {}
    envelope_ok = True
    for n in (7, 14, 21, NMAX_Q):
        Sq = S_q(n)
        d = mp.log(Sq / I[n]) / n
        g = mp.log(Sq / I[n]) / ((n ** 2 / mp.mpf(2)) * lnq)
        dress[n], qgev[n] = float(d), float(g)
        # exact q-Gevrey envelope: S_q ≤ p(n)·q^{n(n−1)/2} (dim_q ≤ [n]_q!)
        if mp.log(Sq) > (n * (n - 1) / mp.mpf(2)) * lnq + n:
            envelope_ok = False
        print(f"  {n:>3} {float(Sq):>14.5g} {float(d):>12.5f} {float(g):>18.4f}")
    dressing_grows = dress[NMAX_Q] > dress[14] > dress[7]
    print(f"\n  dressing ln(S_q/I)/n GROWS {dress[7]:.3f} → {dress[NMAX_Q]:.3f} (not exponential-"
          f"class); exponent ratio vs the q-Gevrey envelope q^(n²/2) rises "
          f"{qgev[7]:.3f} → {qgev[NMAX_Q]:.3f} (n^(-1/2)-class corrections; asymptote not "
          f"reached at n≤{NMAX_Q}).")
    print(f"  Exact bound dim_q ≤ [n]_q! ⇒ S_q ≤ p(n)·q^(n(n−1)/2): "
          f"{'HOLDS' if envelope_ok else 'VIOLATED'} ⇒ the q₀ class is q-GEVREY "
          f"(Jackson q-Borel territory), NOT classical Gevrey-1/2.")

    ok = sandwich_ok and gevrey_half and level1_entire and dressing_grows and envelope_ok
    print(f"\n### Verdict ({'ALL CHECKS PASS' if ok else 'CHECK FAILED'}):")
    print("    • q=1: binding period is Gevrey-1/2, NOT Gevrey-1 ⇒ canonical plane = level-1/2")
    print("      Borel (Écalle acceleration), see lever1_borel_half_singularity_probe.py")
    print("    • q₀: the deformation moves the class toward q-Gevrey (a_n ≲ q^(n²/2)) — the")
    print("      alien-calculus geometry at q₀ is an acceleration CHAIN, not one Borel plane.")

    try:
        from witness_base import WitnessBuilder
        wb = WitnessBuilder("lever1-gevrey-order-pin", engine="mpmath")
        wb.set_description(
            "Lever-1 (z2bn): Gevrey-order pin for the binding period a_D^(n)=S(n)/n. "
            "q=1 exact: a_D=I(n)/n (telephone numbers) satisfies the two-sided integer sandwich "
            "n! ≤ 4^n·I(n)^2 and I(n)^2 ≤ 2^n·n! (Lean-proved in QOU/Mass/BindingGevreyHalf.lean; "
            "asserted here to n=60) and matches the (n/e)^(n/2)e^(sqrt n-1/4)/sqrt2 asymptote ⇒ "
            "Gevrey-1/2, NOT Gevrey-1. The level-1 Borel coefficients a_D/n! decay like sqrt(e/n) "
            "⇒ B₁ entire ⇒ no alien derivatives in the level-1 plane (refutes the external "
            "dialog's Gevrey-1/standard-Borel framing, scope-(a)). At q₀ the dressing "
            "ln(S_q/I)/n GROWS (0.017→0.36, n≤28) under the exact envelope S_q ≤ p(n)q^(n(n−1)/2) "
            "⇒ the deformation CHANGES the class toward q-Gevrey (Jackson q-Borel territory) — "
            "an Écalle acceleration chain, not one Borel plane. Anti-fit: exact integers + "
            "categorical q-hook dim_q; nothing tuned; no wiring.")
        wb.add_data("sandwich_holds_to_n", NMAX)
        wb.add_data("gevrey_slope_s_n", slope)
        wb.add_data("asymptote_residual_ln", asym_err)
        wb.add_data("level1_borel_root_test", level1)
        wb.add_data("level1_root_test_scaled_sqrt_n_over_e", {k: float(v) for k, v in lvl1_scaled.items()})
        wb.add_data("q0_dressing_ln_ratio_per_n", dress)
        wb.add_data("q0_exponent_ratio_vs_qgevrey_envelope", qgev)
        wb.add_assertion(
            name="binding_period_gevrey_half_at_q1_qgevrey_deformed_at_q0",
            computed=str(int(ok)), expected="1", tolerance=0,
            source=("integer sandwich n!≤4^n I(n)^2 ≤ 8^n n! holds to n=60 (Lean-proved core); "
                    "ln I matches the order-1/2 asymptote to %+.4f at n=60; level-1 Borel root "
                    "test decays as sqrt(e/n) (scaled %.3f≈1 ⇒ B1 entire, level-1 plane "
                    "singularity-free); q0 dressing grows %.3f→%.3f under the exact q^(n(n−1)/2) "
                    "envelope ⇒ class deforms toward q-Gevrey at q0."
                    % (asym_err[60], float(lvl1_scaled[60]), dress[7], dress[NMAX_Q])))
        out = wb.save()
        print(f"\nWitness: {out}")
    except Exception as e:
        print(f"\n(witness skipped: {e})")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
