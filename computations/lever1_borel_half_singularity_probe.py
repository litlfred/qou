#!/usr/bin/env python3
"""
lever1_borel_half_singularity_probe.py — level-1/2 Borel–Padé singularity hunt for the
binding period a_D^(n) (lever-1 / z2bn).

Context. lever1_gevrey_order_pin.py pinned the growth class: at q=1 the binding period
a_D^(n)=I(n)/n is Gevrey-1/2 (Lean sandwich n! ≤ 4^n·I(n)² ≤ 8^n·n!), so the CANONICAL
Borel plane is level-1/2: B_{1/2}[a_D](ξ) = Σ a_D^(n)·ξⁿ/Γ(n/2+1). This is where the
external dialog's alien-derivative picture must live if it lives anywhere — the level-1
plane is entire (no singularities). This probe LOCATES the level-1/2 singularities.

Analytic expectation at q=1 (from I(n) ~ (n/e)^{n/2}e^{√n−1/4}/√2):
  b_n = a_D^(n)/Γ(n/2+1) ⇒ |b_n|^{1/n} → √2 ⇒ RADIUS ρ = 1/√2 ≈ 0.7071.
  All b_n > 0 ⇒ (Pringsheim) the dominant singularity is ON THE POSITIVE REAL AXIS at
  ξ = 1/√2. The residual e^{√n} factor is sub-geometric ⇒ the singularity is NOT a pole
  (essential / exponential-branch type — the signature of a mixed-level transseries);
  Padé poles should ACCUMULATE along the real axis beyond ρ rather than isolate.

Measurements:
  1. Root test |b_n|^{1/n} with Richardson-in-1/√n → √2 (q=1, n ≤ 60).
  2. Padé [L/L] pole map: nearest pole vs 1/√2; clustering of real poles > ρ.
  3. q₀ (n ≤ 28): the gevrey-pin probe showed the class deforms toward q-GevREY —
     here the level-1/2 root test at q₀ keeps RISING with n (no finite-radius plateau),
     the finite-n shadow of the radius → 0 collapse: at q₀ no single classical Borel
     level carries the period; the object needs the Jackson q-Borel / acceleration chain.
  4. Geometric comparison (REPORTED ONLY, numerology guard): the color-cubic branch
     moduli (|z| ≈ 0.943, 1.0, 1.061) live in the z-plane, NOT the Borel-ξ plane; no
     identification is claimed. The measured level-1/2 datum (ρ, axis, type) is the
     structural target any derived multi-branch kernel must reproduce.

FINDING (scope-(a)): the q=1 level-1/2 Borel plane has its dominant singularity at
ξ = 1/√2 on the positive real axis, non-polar (accumulating Padé poles); at q₀ the
level-1/2 radius does not stabilize (class change confirmed from the Borel side).
Anti-fit: I(n) exact; dim_q categorical; expectations derived from proved asymptotics
before measurement. No wiring. EXPLORATORY.

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
try:
    from _precision import set_compute_dps
    set_compute_dps()
except Exception:
    mp.mp.dps = 60
try:
    from q_parameter import Q_50_DIGIT_STR as Q0
    q = mp.mpf(Q0)
except Exception:
    q = mp.mpf('1.1099785955573347')

NMAX = 60
NMAX_Q = 28
SQRT2 = mp.sqrt(2)


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


def borel_half_coeffs(aD):
    """b_n = a_D^(n) / Γ(n/2+1), starting at n=1."""
    return [aD[n] / mp.gamma(mp.mpf(n) / 2 + 1) for n in range(1, len(aD))]


def pade_poles(b, L, M):
    """Poles of the [L/M] Padé approximant of Σ b_n ξ^{n} (b indexed from n=1)."""
    coeffs = [mp.mpf(0)] + list(b[:L + M])          # include the a_0 = 0 term
    p, qd = mp.pade(coeffs, L, M)
    roots = mp.polyroots([qd[len(qd) - 1 - k] for k in range(len(qd))],
                         maxsteps=200, extraprec=80)
    return sorted(roots, key=lambda z: abs(z))


def main() -> int:
    print("=== lever-1: level-1/2 Borel–Padé singularity probe for a_D^(n) ===\n")
    I = involution_numbers(NMAX)
    aD1 = [mp.mpf(0)] + [mp.mpf(I[n]) / n for n in range(1, NMAX + 1)]
    b1 = borel_half_coeffs(aD1)

    # --- 1. root test → √2 (radius 1/√2), Richardson in 1/√n ---
    rt = {n: float(b1[n - 1] ** (mp.mpf(1) / n)) for n in (20, 30, 40, 50, 60)}
    # model ln r_n = ln ρ⁻¹ + a/√n + c·(ln n)/n : 3-point solve at n = 30, 40, 60
    ns = [30, 40, 60]
    A = mp.matrix(3, 3)
    rhs = mp.matrix(3, 1)
    for i, n in enumerate(ns):
        A[i, 0], A[i, 1], A[i, 2] = 1, 1 / mp.sqrt(n), mp.log(n) / n
        rhs[i, 0] = mp.log(rt[n])
    sol = mp.lu_solve(A, rhs)
    r_extrap = float(mp.e ** sol[0, 0])
    print(f"root test |b_n|^(1/n) (q=1): " +
          ", ".join(f"n={n}: {v:.4f}" for n, v in rt.items()))
    print(f"  extrapolated (a/√n + c·ln n/n fit): {r_extrap:.4f}  vs  √2 = "
          f"{float(SQRT2):.4f}  (rel err {abs(r_extrap / float(SQRT2) - 1):.3f})")
    radius_ok = abs(r_extrap / float(SQRT2) - 1) < 0.10

    # --- 2. Padé pole map ---
    poles = pade_poles(b1, 28, 28)
    real_pos = [z for z in poles if abs(mp.im(z)) < 1e-6 and mp.re(z) > 0]
    nearest = poles[0]
    rho = 1 / SQRT2
    print(f"\nPadé [28/28] poles (nearest 6 by |ξ|):")
    for z in poles[:6]:
        print(f"  ξ = {mp.nstr(z, 6):>22}   |ξ| = {float(abs(z)):.4f}")
    n_real_band = sum(1 for z in real_pos if float(rho) * 0.9 < abs(z) < 3)
    print(f"nearest pole |ξ| = {float(abs(nearest)):.4f} vs ρ = 1/√2 = {float(rho):.4f}; "
          f"positive-real poles in [0.9ρ, 3): {n_real_band} (accumulation ⇒ non-polar, "
          f"branch/essential type)")
    pringsheim_ok = abs(mp.im(nearest)) < 1e-6 and mp.re(nearest) > 0
    nearest_ok = abs(float(abs(nearest)) - float(rho)) / float(rho) < 0.10
    accumulation = n_real_band >= 4

    # --- 3. q₀: level-1/2 root test does not stabilize (class change, Borel side) ---
    aDq = [mp.mpf(0)] + [mp.fsum(dimq(l) for l in partitions(n)) / n
                         for n in range(1, NMAX_Q + 1)]
    bq = borel_half_coeffs(aDq)
    rtq = {n: float(bq[n - 1] ** (mp.mpf(1) / n)) for n in (7, 14, 21, NMAX_Q)}
    print(f"\nroot test |b_n|^(1/n) (q₀): " +
          ", ".join(f"n={n}: {v:.4f}" for n, v in rtq.items()))
    # q=1 root test is FALLING toward √2 from above? (check direction) — at q₀ it must RISE
    q1_dir = rt[60] - rt[30]
    q0_dir = rtq[NMAX_Q] - rtq[14]
    print(f"  trend q=1: {q1_dir:+.4f} (settling); trend q₀: {q0_dir:+.4f} (RISING ⇒ no "
          f"finite-radius plateau — the level-1/2 plane collapses at q₀; q-Gevrey class)")
    q0_rises = q0_dir > 0.05

    # --- 4. geometric comparison (reported only) ---
    print(f"\ncolor-cubic branch moduli (z-plane, for reference only — NO identification "
          f"claimed): |z| ≈ 0.943, 1.000, 1.061")
    print(f"measured level-1/2 datum (ξ-plane): ρ = 1/√2 ≈ {float(rho):.4f}, positive real "
          f"axis, non-polar.")

    ok = radius_ok and pringsheim_ok and nearest_ok and accumulation and q0_rises
    print(f"\n### Verdict ({'ALL CHECKS PASS' if ok else 'CHECK FAILED'}):")
    print("    • q=1: dominant level-1/2 Borel singularity at ξ = 1/√2 (positive real axis,")
    print("      Pringsheim), non-polar (Padé poles accumulate) — the derived structural")
    print("      target for any multi-branch residue kernel.")
    print("    • q₀: level-1/2 root test rises without plateau ⇒ class change confirmed")
    print("      from the Borel side (q-Gevrey; acceleration chain needed).")

    try:
        from witness_base import WitnessBuilder
        wb = WitnessBuilder("lever1-borel-half-singularity-probe", engine="mpmath")
        wb.set_description(
            "Lever-1 (z2bn): level-1/2 Borel–Padé singularity hunt for the binding period "
            "a_D^(n). q=1 (exact I(n)/n, n≤60): root test extrapolates to sqrt2 (radius "
            "rho=1/sqrt2 ~ 0.7071); Padé [28/28] nearest pole on the positive real axis at "
            "|xi| ~ rho (Pringsheim) with real poles accumulating beyond rho ⇒ non-polar "
            "(branch/essential) singularity — the e^(sqrt n) subexponential signature of a "
            "mixed-level transseries. At q0 (n≤28) the level-1/2 root test rises without "
            "plateau ⇒ no classical Borel level carries the q0 period (q-Gevrey class; "
            "Jackson q-Borel / acceleration chain). The measured (rho, axis, type) datum is "
            "the structural target for the open multi-branch super-exp kernel. Anti-fit: "
            "expectations derived from proved asymptotics before measurement; exact/categorical "
            "inputs; no wiring. Scope-(a).")
        wb.add_data("q1_root_test", rt)
        wb.add_data("q1_root_test_extrapolated", r_extrap)
        wb.add_data("q1_expected_sqrt2", float(SQRT2))
        wb.add_data("q1_nearest_pole_abs", float(abs(nearest)))
        wb.add_data("q1_nearest_pole_re_im", [float(mp.re(nearest)), float(mp.im(nearest))])
        wb.add_data("q1_real_pole_accumulation_count", n_real_band)
        wb.add_data("q0_root_test", rtq)
        wb.add_data("q0_root_test_trend", float(q0_dir))
        wb.add_assertion(
            name="borel_half_singularity_at_inv_sqrt2_q1_and_q0_class_change",
            computed=str(int(ok)), expected="1", tolerance=0,
            source=("q=1 level-1/2 root test → %.4f (√2 to %.1f%%); nearest Padé pole "
                    "|ξ|=%.4f ≈ 1/√2 on the positive real axis with %d real poles "
                    "accumulating (non-polar); q₀ root test rises %+0.4f (no plateau ⇒ "
                    "q-Gevrey class change from the Borel side)."
                    % (r_extrap, 100 * abs(r_extrap / float(SQRT2) - 1),
                       float(abs(nearest)), n_real_band, q0_dir)))
        out = wb.save()
        print(f"\nWitness: {out}")
    except Exception as e:
        print(f"\n(witness skipped: {e})")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
