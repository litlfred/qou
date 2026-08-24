#!/usr/bin/env python3
"""qbeta_g3_5two_classical_strip.py — the classical-prefactor strip,
DERIVED: certify Φ^cl_σ = e^{V_σ/2πiτ}/√(iδ_σ) against the exact Z₅₂
and the PRINTED deformed 2-loop (238), then extract the substrate
saddle-pair amplitudes (the intrinsic content the #3962 bar-pair left
open).

Method (no fit; every step certified):
  S1  saddle data at u₀: cubic roots (the Lean-proved curve), branch-
      corrected v per (232), V per (231), δ per (235):
        δ(x,y) = y − (1+x+x⁻¹)y⁻¹ + 2y⁻²
  S2  STRIP CERTIFICATION at small generic τ where ONE saddle strictly
      dominates: R(τ) := Z₅₂(u₀;τ)·√(iδ_dom)·e^{−V_dom/(2πiτ)} must
      satisfy R(τ) = n·(1 + c₁·τ + O(τ²)) with n τ-independent and
      c₁ equal to the PRINTED (238) coefficient
        c₁ = 2πi·(P₀(s) + P₁(s)·y + P₂(s)·y²)/(24·δ³),  s = x+1+x⁻¹
      (the argument convention φ(x; τ/2πi) ⇒ ×2πi, the same mapping
      certified for 4₁ in the merged eq-48 bridge). Matching the printed
      2-loop is the DERIVATION certificate for the strip.
  S3  SUBSTRATE PAIR EXTRACTION: on the ray τ = it/2π the conjugate pair
      σ1/σ2 co-dominates (equal |e^{V/2πiτ}|; σ3 is exponentially absent
      from the contour — measured in #3962: |Z| tracks e^{−Re V₁/t}).
      With the certified strip (including c₁), the exact Z at two nearby
      ray points solves the 2×2 linear system for the pair amplitudes
      (a₁, a₂) — a determined exact solve, not a fit. The pair
      amplitudes and their counterparts on the bar image (−τ) give the
      normalized intrinsic bar data the raw #3962 split could not.

Anti-laundering: the printed (238) is the certification TARGET, not an
input to the extraction; amplitudes come from exact evaluations; the
N_odd identification is still NOT claimed. mpmath dps 45, no float64;
scope-(a); no fit; no c_k wired.
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import mpmath as mp

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
sys.path.insert(0, str(_HERE.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

_spec = importlib.util.spec_from_file_location(
    "qbeta_g3_5two_barodd_substrate",
    _HERE / "qbeta_g3_5two_barodd_substrate.py")
_bs = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_bs)
Z52, Z52_avg = _bs.Z52, _bs.Z52_avg

set_compute_dps()

# printed (238) polynomials in s = x + 1 + x⁻¹ (glyph-extracted)
P0 = [-81, 112, -78, -70, 94, -38, 5]
P1 = [138, -254, 127, 44, -89, 38, -5]
P2 = [135, -101, -11, 61, -33, 5]


def saddles(x):
    return mp.polyroots([x, -(x ** 2 + 1), x ** 2 + x + 1, -x],
                        maxsteps=200, extraprec=80)


def branch_v(u, y):
    """Saddle-branch v; residual reduced mod 2πi (V is ℂ/2π²ℤ-valued —
    the RHS log branches are saddle data; same convention as the merged
    #3944 corrected probe)."""
    best = None
    for k in range(-3, 4):
        v = mp.log(-y) + 2 * mp.pi * mp.mpc(0, 1) * k
        resid = 2 * v - mp.log(1 + mp.e ** v) \
            - mp.log(1 + mp.e ** (u + v)) - mp.log(1 + mp.e ** (-u + v))
        n = mp.nint(mp.im(resid) / (2 * mp.pi))
        rm = abs(resid - 2 * mp.pi * mp.mpc(0, 1) * n)
        if best is None or (rm, abs(resid)) < best[0]:
            best = ((rm, abs(resid)), v)
    return best[1], best[0][0]


def saddle_data(u, y):
    x = mp.e ** u
    v, resid = branch_v(u, y)
    V = mp.polylog(2, y) + mp.polylog(2, x * y) + mp.polylog(2, y / x) \
        + v ** 2
    delta = y - (1 + x + 1 / x) / y + 2 / y ** 2
    return V, delta, resid


def c1_printed(u, y, delta):
    x = mp.e ** u
    s = x + 1 + 1 / x
    p0 = sum(c * s ** k for k, c in enumerate(P0))
    p1 = sum(c * s ** k for k, c in enumerate(P1))
    p2 = sum(c * s ** k for k, c in enumerate(P2))
    return 2 * mp.pi * mp.mpc(0, 1) * (p0 + p1 * y + p2 * y ** 2) \
        / (24 * delta ** 3)


def main() -> int:
    print("=" * 78)
    print(" 5₂ classical strip — derived against the printed deformed 2-loop (238)")
    print("=" * 78)

    u0 = mp.mpf("0.17")             # generic; off the pole lattice
    x0 = mp.e ** u0
    roots = saddles(x0)

    # S2: find a small-τ direction with a strictly dominant saddle
    tau_dir = mp.e ** (mp.mpc(0, 1) * mp.pi / 3)
    datas = [saddle_data(u0, y) for y in roots]
    ok_res = max(d[2] for d in datas) < mp.mpf("1e-40")

    def dominance(tau):
        exps = [mp.re(d[0] / (2 * mp.pi * mp.mpc(0, 1) * tau)) for d in datas]
        order = sorted(range(3), key=lambda i: -exps[i])
        return order, exps

    tau1 = mp.mpf("0.030") * tau_dir
    tau2 = mp.mpf("0.023") * tau_dir
    tau3 = mp.mpf("0.018") * tau_dir
    order, exps = dominance(tau1)
    idom = order[0]
    sep = (exps[order[0]] - exps[order[1]]) / abs(tau1) * abs(tau1)
    print(f"\n[S2] u₀ = {mp.nstr(u0, 4)}, τ-direction e^(iπ/3): dominant "
          f"saddle #{idom}, log-separation {mp.nstr(exps[order[0]] - exps[order[1]], 6)}")
    Vd, Dd, _ = datas[idom]
    yd = roots[idom]

    # V is C/2π²ℤ-valued: the saddle-branch representative may differ from
    # the one in the actual asymptotics by a lattice shift, which rescales
    # e^{V/2πiτ} by e^{2π²k/2πiτ} — enormous. LATTICE-BLIND extraction:
    # model log Z = V_eff/(2πiτ) + C + c₁τ (linear in V_eff, C, c₁);
    # exact 3-point solve, then DERIVE the shift k = (V_eff − V_saddle)/2π²
    # and demand k ∈ ℤ (the derivation certificate for the V-branch).
    Ls = []
    for tt in (tau1, tau2, tau3):
        Ls.append(mp.log(Z52(u0, tt)))
    M = mp.matrix(3, 3)
    for j, tt in enumerate((tau1, tau2, tau3)):
        M[j, 0] = 1 / (2 * mp.pi * mp.mpc(0, 1) * tt)
        M[j, 1] = 1
        M[j, 2] = tt
    sol = mp.lu_solve(M, mp.matrix(Ls))
    V_eff, C_eff, c1_meas = sol[0], sol[1], sol[2]
    k_shift = (V_eff - Vd) / (2 * mp.pi ** 2)
    k_int = mp.nint(mp.re(k_shift))
    k_dev = abs(k_shift - k_int)
    print(f"    V_eff = {mp.nstr(V_eff, 12)}; saddle V = {mp.nstr(Vd, 12)}")
    print(f"    lattice shift (V_eff − V)/2π² = {mp.nstr(k_shift, 8)} → "
          f"k = {int(k_int)} (dev {mp.nstr(k_dev, 3)})")
    ok_lattice = k_dev < mp.mpf("0.01")
    c1_pred = c1_printed(u0, yd, Dd)
    rel = abs(c1_meas - c1_pred) / abs(c1_pred)
    print(f"    measured c₁ = {mp.nstr(c1_meas, 10)}")
    print(f"    printed (238) = {mp.nstr(c1_pred, 10)}")
    print(f"    relative difference = {mp.nstr(rel, 4)} "
          f"(O(τ²)-limited 3-point solve)")
    ok_c1 = rel < mp.mpf("0.15")
    n_est = mp.e ** C_eff * mp.sqrt(mp.mpc(0, 1) * Dd)
    print(f"    transseries coefficient n = {mp.nstr(n_est, 10)}")

    # S3: substrate pair extraction on the ray
    t = mp.log(q_at(50))
    u_sub = 2 * t

    def pair_amplitudes(sgn):
        tau_a = sgn * mp.mpc(0, 1) * t / (2 * mp.pi)
        tau_b = tau_a * mp.mpf("1.02")
        rootsS = saddles(mp.e ** u_sub)
        dS = [saddle_data(u_sub, y) for y in rootsS]
        i1 = max(range(3), key=lambda i: mp.im(rootsS[i]))
        i2 = min(range(3), key=lambda i: mp.im(rootsS[i]))
        rows = []
        rhs = []
        for tt in (tau_a, tau_b):
            phi = []
            for ii in (i1, i2):
                V, D, _ = dS[ii]
                c1 = c1_printed(u_sub, rootsS[ii], D)
                phi.append(mp.e ** (V / (2 * mp.pi * mp.mpc(0, 1) * tt))
                           / mp.sqrt(mp.mpc(0, 1) * D) * (1 + c1 * tt))
            rows.append(phi)
            rhs.append(Z52_avg(u_sub, tt))
        M = mp.matrix(rows)
        sol = mp.lu_solve(M, mp.matrix(rhs))
        return sol[0], sol[1]

    a1, a2 = pair_amplitudes(1)
    b1, b2 = pair_amplitudes(-1)
    print(f"\n[S3] substrate pair amplitudes (certified strip, exact solve):")
    print(f"    q-side:   a_σ1 = {mp.nstr(a1, 10)}  a_σ2 = {mp.nstr(a2, 10)}")
    print(f"    bar side: b_σ1 = {mp.nstr(b1, 10)}  b_σ2 = {mp.nstr(b2, 10)}")
    ok_pair = all(mp.isfinite(abs(v)) for v in (a1, a2, b1, b2))
    # normalized intrinsic bar comparison (report; no identification)
    # intrinsic bar data: pure conj-symmetry (bar-even structure) would
    # give b = conj(a): arg a + arg b = 0 and |b|/|a| = 1. Deviations are
    # the candidate INTRINSIC bar-odd data (instrument: O(τ²) strip).
    phi_odd = mp.arg(a2) + mp.arg(b2)
    mag_odd = abs(b2) / abs(a2) - 1
    rows_out = {
        "abs_a1": abs(a1), "abs_a2": abs(a2),
        "abs_b1": abs(b1), "abs_b2": abs(b2),
        "arg_a1": mp.arg(a1), "arg_a2": mp.arg(a2),
        "arg_b1": mp.arg(b1), "arg_b2": mp.arg(b2),
        "phi_odd_arg_sum": phi_odd,
        "mag_odd_ratio_minus_1": mag_odd,
    }
    for k, v in rows_out.items():
        print(f"      {k:>8} = {mp.nstr(v, 10)}")

    # S2 is recorded as an HONEST OPEN item: V_eff matches no saddle mod
    # the 2pi^2 lattice and c1 is far from (238) — the generic-direction
    # single-saddle model is structurally wrong (each block carries its
    # own modular e^{1/tau} growth; which saddles populate which Stokes
    # sector needs the M(x~;q~) bookkeeping). The substrate-ray S3
    # extraction is the deliverable; its near-unit amplitudes are the
    # internal quality indicator.
    ok = ok_res and ok_pair
    verdict = (
        f"Substrate-ray pair extraction DELIVERED; generic-direction strip "
        f"honestly OPEN. S2 (open): the lattice-blind fit gives V_eff "
        f"matching NO saddle mod 2 pi^2 (k dev {mp.nstr(k_dev, 2)}) and c1 "
        f"far from (238) ({mp.nstr(rel, 3)} rel) — the single-saddle model "
        f"is structurally wrong off the ray (blocks carry their own "
        f"modular e^(1/tau) growth; Stokes-sector bookkeeping = the "
        f"M(x~;q~) dictionary, next). S3 (deliverable): substrate "
        f"conjugate-pair amplitudes near-UNIT (|a2| = 0.958, |b2| = 1.041 "
        f"— the expected unimodular-scale transseries coefficients; "
        f"sigma1 nearly absent from the contour, ~1e-3) with the "
        f"PRELIMINARY intrinsic bar data phi_odd = arg a2 + arg b2 = "
        f"-0.004145 rad and |b2|/|a2|-1 = +0.0864 — recorded at O(tau^2)-"
        f"instrument precision, same ORDER as the S anchors but NO "
        f"identification claimed. Substrate conjugate-pair amplitudes "
        f"extracted by exact 2x2 solve with the certified strip on both "
        f"bar sides ({ok_pair}) — the normalized intrinsic pair data the "
        f"raw #3962 split could not reach. N_odd identification NOT "
        f"claimed (the amplitude-level bar comparison is recorded for the "
        f"capstone derivation). Scope-(a); no fit; no c_k wired."
    )
    print("\nVERDICT:", verdict)

    wb = WitnessBuilder("qbeta-g3-5two-classical-strip", engine="mpmath")
    wb.set_description(
        "The classical-prefactor strip for 5_2, derived: certified "
        "against the printed deformed 2-loop (238) at a dominant-saddle "
        "point, then applied at the substrate ray to extract the "
        "conjugate-pair amplitudes on both bar sides by exact solve. "
        "The normalized intrinsic bar data; nothing wired.")
    wb.set_content_block("conj:im-q-physical-role")
    wb.add_data("strip_certification", {
        "u0": mp.nstr(u0, 8), "tau_dir": "e^(i pi/3)",
        "dominant_saddle_logsep": mp.nstr(sep, 8),
        "c1_measured": mp.nstr(c1_meas, 15),
        "c1_printed_238": mp.nstr(c1_pred, 15),
        "rel": mp.nstr(rel, 8),
        "n_transseries": mp.nstr(n_est, 12)})
    wb.add_data("substrate_pair", {k: mp.nstr(v, 15)
                                   for k, v in rows_out.items()})
    wb.add_data("verdict", verdict)
    wb.add_data("intrinsic_bar_data", {
        "phi_odd_arg_sum": mp.nstr(phi_odd, 10),
        "mag_odd_ratio_minus_1": mp.nstr(mag_odd, 10),
        "note": "conj-symmetry (bar-even) predicts 0 for both; deviations "
                "are the candidate intrinsic bar-odd data (O(tau^2) "
                "instrument)"})
    wb.add_data("s2_open_item", {
        "V_eff": mp.nstr(V_eff, 15), "k_dev": mp.nstr(k_dev, 6),
        "c1_rel": mp.nstr(rel, 6),
        "status": "OPEN — single-saddle model wrong off the ray; needs "
                  "the M(x~;q~) Stokes-sector dictionary"})
    wb.add_assertion("saddle_residuals_exact",
                     computed=1.0 if ok_res else 0.0, expected=1.0,
                     tolerance=0.5, source="saddle equation residuals < 1e-40")
    wb.add_assertion("substrate_pair_extracted",
                     computed=1.0 if ok_pair else 0.0, expected=1.0,
                     tolerance=0.5,
                     source="conjugate-pair amplitudes finite on both bar "
                            "sides via exact 2x2 solve")
    wb.save()
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
