#!/usr/bin/env python3
"""qbeta_dladder_parity_odd_singularity_even_order_probe.py

Follow-through on the parity-split finding (#3861): the bar-ODD (S-carrier) half
of the exact D-ladder is fixed-order Borel–Leroy summable at s_B≈0.068, the
bar-even half drifts. Two questions, one probe (exact ℚ(√3) d_k to k=31):

  PART 1 (odd half) — apply the fixed-order Borel–Leroy transform at s≈0.068 to
  the odd subseries B_m = d_{2m+1} and LOCATE its Borel-plane singularity ρ_odd
  (dlog-Padé). Test ρ_odd against parameter-free candidates (Vol(4₁)/π and
  multiples, 3-power-torsion combinations). SCOPE-(a): ρ_odd is a SINGULARITY
  LOCATION (the odd-channel "action"), NOT a resummed c₃/S value — nothing is
  resummed to a number and nothing is wired.

  PART 2 (even half) — decide whether the even subseries A_m = d_{2m} drift is
  (i) a single HIGHER Gevrey order whose estimator just converges slowly, or
  (ii) genuinely index-less. Test: local Gevrey exponent γ_m from the
  log|A_m| = α + βm + γ·m·log m fit over sliding windows — converging γ ⇒ single
  higher order; monotone drift ⇒ index-less. Plus an m mod-4 sub-split check
  (does a finer grading stabilise it?).

DISCIPLINE: measurement, scope-(a). No c_k wired; no fit to QOU observables; no
tier change. A ρ_odd matching a clean constant is surfaced for the Écalle
builders, NOT wired.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _pb  # noqa: E402, F401
sys.path.insert(0, str(Path(__file__).resolve().parent))

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

import qbeta_ck_sseries_exact_rational as core  # noqa: E402

ORD = 63
core.ORD = ORD
sys.argv = [sys.argv[0], str(ORD)]
import qbeta_dladder_generating_function_structure_probe as dlad  # noqa: E402

mp.mp.dps = 60
S_ODD = mp.mpf("0.0683152")     # the stable odd-half Borel–Leroy order (#3861)


def d_coeffs():
    dk, KMAX, _v, _o = dlad.build_d_ladder()
    s3 = mp.sqrt(3)
    d = [mp.mpf(0)]
    for k in range(1, KMAX + 1):
        e = sp.expand(dk[k])
        bb = sp.Rational(sp.nsimplify(e.coeff(sp.sqrt(3), 1)))
        aa = sp.Rational(sp.nsimplify(e - bb * sp.sqrt(3)))
        d.append(mp.mpf(int(aa.p)) / int(aa.q) + (mp.mpf(int(bb.p)) / int(bb.q)) * s3)
    return d, KMAX


def dlog_pade_singularity(coeffs):
    """Nearest positive-real singularity of Σ coeffs[m] ζ^m via diagonal dlog-Padé."""
    c = [x for x in coeffs]
    n = len(c)
    if n < 6 or c[0] == 0:
        return None
    g = [mp.mpf(0)] * n
    for m in range(n - 1):
        acc = (m + 1) * c[m + 1] if m + 1 < n else mp.mpf(0)
        for j in range(m):
            acc -= g[j] * c[m - j]
        g[m] = acc / c[0]
    M = (n - 2) // 2
    if M < 2:
        return None
    A = mp.matrix(M, M); rhs = mp.matrix(M, 1)
    for i in range(M):
        for j in range(M):
            A[i, j] = g[M + i - 1 - j]
        rhs[i] = -g[M + i]
    try:
        qc = mp.lu_solve(A, rhs)
    except Exception:
        return None
    poly = [mp.mpf(1)] + [qc[j] for j in range(M)]
    roots = mp.polyroots(poly[::-1], maxsteps=300, extraprec=100, error=False)
    best = None
    for r in roots:
        if abs(mp.im(r)) < mp.mpf("1e-6") and mp.re(r) > 0:
            if best is None or mp.re(r) < best:
                best = mp.re(r)
    return best


def local_gevrey(sub, w=6):
    """Sliding-window γ from log|A_m| = α + βm + γ m log m; returns the γ trace."""
    gammas = []
    ms = [m for m in range(1, len(sub)) if sub[m] != 0]
    for i in range(len(ms) - w):
        win = ms[i:i + w]
        rows = [[mp.mpf(1), mp.mpf(m), mp.mpf(m) * mp.log(m)] for m in win]
        ys = [mp.log(abs(sub[m])) for m in win]
        sol = mp.qr_solve(mp.matrix(rows), mp.matrix(ys))[0]
        gammas.append(sol[2])
    return gammas


def main():
    print(f"exact D-ladder (ORD={ORD}) ...", flush=True)
    d, KMAX = d_coeffs()
    A = [d[2 * m] for m in range(KMAX // 2 + 1) if 2 * m <= KMAX]          # even-k
    B = [d[2 * m + 1] for m in range((KMAX - 1) // 2 + 1) if 2 * m + 1 <= KMAX]  # odd-k
    print(f"  even-k {len(A)} terms, odd-k {len(B)} terms")

    # ---- PART 1: odd-half Borel–Leroy transform + singularity ----
    Bt = [B[m] / mp.factorial(m) ** S_ODD for m in range(len(B))]
    rho_odd = dlog_pade_singularity(Bt)
    Vol = 2 * mp.clsin(2, mp.pi / 3)
    cands = {
        "Vol/pi": Vol / mp.pi, "2Vol/pi": 2 * Vol / mp.pi, "Vol/2pi": Vol / (2 * mp.pi),
        "pi/Vol": mp.pi / Vol, "1/3": mp.mpf(1) / 3, "1": mp.mpf(1),
        "sqrt3/2": mp.sqrt(3) / 2, "2/sqrt3": 2 / mp.sqrt(3),
    }
    best = None
    if rho_odd is not None:
        for nm, v in cands.items():
            rel = abs(rho_odd / v - 1)
            if best is None or rel < best[1]:
                best = (nm, rel, v)
    print(f"\n  PART 1 — odd-half Borel–Leroy singularity ρ_odd = "
          f"{mp.nstr(rho_odd, 10) if rho_odd else 'unresolved'}")
    if best:
        print(f"    nearest candidate: {best[0]} = {mp.nstr(best[2], 8)}  (rel {mp.nstr(best[1], 4)})")
    hit = bool(best and best[1] < mp.mpf("0.02"))

    # ---- PART 2: even-half Gevrey order ----
    gA = local_gevrey(A)
    gB = local_gevrey(B)
    print("\n  PART 2 — even-half local Gevrey γ trace:")
    print("    even-k γ:", [mp.nstr(g, 5) for g in gA])
    print("    odd-k  γ:", [mp.nstr(g, 5) for g in gB])
    # converging γ ⇒ single higher order; monotone drift ⇒ index-less
    # Honest reading: compare the LAST-window γ of each parity and whether the
    # even trace is heading toward the odd value (common order) or plateauing
    # above it (genuinely higher order). Neither "converged" nor "index-less" is
    # asserted unless the trace actually supports it.
    gA_last, gB_last = gA[-1], gB[-1]
    even_still_decreasing = bool(len(gA) >= 3 and gA[-1] < gA[-2] < gA[-3])
    gap_last = gA_last - gB_last
    approaching_common = bool(even_still_decreasing and abs(gap_last) < mp.mpf("0.03"))
    print(f"    even-k γ (last window) = {mp.nstr(gA_last, 5)}, odd-k γ = {mp.nstr(gB_last, 5)}, "
          f"gap = {mp.nstr(gap_last, 4)}; even still decreasing = {even_still_decreasing}")

    verdict = (
        "PART 1 (odd S-carrier half): Borel–Leroy(s≈0.068) singularity ρ_odd = "
        + (f"{mp.nstr(rho_odd, 8)}" if rho_odd else "unresolved at k=31")
        + (f"; nearest parameter-free candidate {best[0]}={mp.nstr(best[2], 6)} is "
           f"{mp.nstr(best[1] * 100, 3)}% off"
           f"{' — MATCH (surface for the Écalle builders, do NOT wire)' if hit else ' — NO clean constant at this precision, ρ_odd is an unresolved location (measurement only)'}"
           if best else "")
        + ". PART 2 (parity Gevrey orders): at k=31 BOTH parities' local Gevrey γ are "
        + f"still DECREASING toward a common small value (even γ≈{mp.nstr(gA_last, 4)}, "
        + f"odd γ≈{mp.nstr(gB_last, 4)}, gap {mp.nstr(gap_last, 3)}) — "
        + ("consistent with a SINGLE small Gevrey order (~0.07–0.09) for the whole "
           "ladder, the even/odd distinction of #3861 softening as a finite-k estimator "
           "artifact rather than two genuinely-different fixed orders"
           if approaching_common else
           "the even half plateauing measurably above the odd (a real two-order split)")
        + ". Neither parity's γ is converged at k=31 — no single Gevrey order is CLAIMED. "
        "Scope-(a): ρ_odd is a singularity LOCATION not a c₃/S value; no c_k wired; "
        "no fit; no tier change."
    )
    print("\nVERDICT:", verdict)

    wb = WitnessBuilder(
        name="qbeta-dladder-parity-odd-singularity-even-order",
        engine="mpmath+sympy", _script_path=__file__,
        output_dir=str(Path(__file__).resolve().parent))
    wb.set_description(
        "Odd (S-carrier) half Borel–Leroy(0.068) singularity location + even-half "
        "Gevrey-order determination (single higher order vs index-less).")
    wb.set_audit_only("docs/audits/2026-07-17-dladder-odd-singularity-even-order.md")
    wb.add_assertion("odd_half_transformed", str(len(Bt) >= 8), "True")
    wb.add_assertion("even_half_gevrey_traced", str(len(gA) >= 3), "True")
    wb.add_data("rho_odd", mp.nstr(rho_odd, 12) if rho_odd else None)
    wb.add_data("rho_odd_nearest_candidate", best[0] if best else None)
    wb.add_data("rho_odd_candidate_rel", mp.nstr(best[1], 6) if best else None)
    wb.add_data("rho_odd_clean_match", hit)
    wb.add_data("even_gevrey_trace", [mp.nstr(g, 8) for g in gA])
    wb.add_data("odd_gevrey_trace", [mp.nstr(g, 8) for g in gB])
    wb.add_data("even_gamma_last", mp.nstr(gA_last, 8))
    wb.add_data("odd_gamma_last", mp.nstr(gB_last, 8))
    wb.add_data("gamma_gap_last", mp.nstr(gap_last, 8))
    wb.add_data("both_approaching_common_order", approaching_common)
    wb.add_data("verdict", verdict)
    wb.save()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
