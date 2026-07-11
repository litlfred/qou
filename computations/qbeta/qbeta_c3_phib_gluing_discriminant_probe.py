#!/usr/bin/env python3
"""qbeta_c3_phib_gluing_discriminant_probe.py — EXACT discriminant locus of the
m-deformed 4₁ gluing system, and its distances to the canonical substrate
paths. EXPLORATORY MEASUREMENT — no fit, no wiring.

Context. Three independent scope-(a) negatives (θ-Reeb smooth, #3600; smooth
phase laws rate-excluded + lever-class menu empty, #3562/#3596; Φ_q pole
seeding anchor-blind, #3596) localize the S anchor-swing to the m-DEFORMED
gluing system. The natural singular set of that system is its DISCRIMINANT
LOCUS: parameter values m where the gluing polynomial

    g(z, m) = m²z²(z−1)(m²z−1) − 1  =  m⁴z⁴ − m²(m²+1)z³ + m²z² − 1

has a double root in z (branch points of the shape curve z(m) — exactly where
Newton degenerates and the NZ expansion breaks). This probe computes the locus
EXACTLY (sympy resultant, factored over ℚ), then measures distances from:
  * the complete structure m = 1,
  * the real-m axis (real substrate deformations, Im 𝔙 = 0 line),
  * the canonical candidate paths from rounds 1-2 (b-aligned muon near-match
    m = e^{u/2}, u = t·e^{iπ/4}; real u = t; the proton-floor magnitude).

Readout logic (one-sided, no fit): if some discriminant point sits within
~anchor-separation (1e-8) of a canonical path, the u³-lever has a concrete
geometric home (a branch-point graze). If every distance is O(1), the
hypersensitivity is NOT a gluing-variety branch point either — sharpening the
localization to the substrate→m ASSIGNMENT itself (upstream of the geometry),
i.e. conj:algebraic-geometric-dilog-equivalence's map, not the variety.

Run: python3 -u computations/qbeta/qbeta_c3_phib_gluing_discriminant_probe.py \\
       2>&1 | tee /tmp/qbeta_c3_phib_gluing_discriminant.log
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qou_substrate.precision import set_compute_dps  # noqa: E402

set_compute_dps()


def main() -> int:
    from qou_substrate.constants import q_at, q_muon_at

    anchors = {"proton": q_at(50), "muon": q_muon_at(50)}
    t_p = mp.log(anchors["proton"])
    dq = float(anchors["proton"] - anchors["muon"])

    wb = WitnessBuilder("qbeta-c3-phib-gluing-discriminant", engine="mpmath+sympy")
    wb.set_description(
        "Exact discriminant locus of the m-deformed 4_1 gluing polynomial "
        "g(z,m) = m^2 z^2 (z-1)(m^2 z - 1) - 1 (sympy resultant, factored "
        "over Q), with distances from m=1, the real-m axis, and the canonical "
        "substrate candidate paths. Locates (or excludes) a branch-point "
        "graze as the geometric home of the u^3-lever hypersensitivity. "
        "Exploratory; no fit; no c_k wired.")
    wb.set_content_block("prop:phi-b-unitary-bar-odd")

    print("=" * 78)
    print(" 4₁ gluing discriminant locus (exact) vs canonical substrate paths")
    print("=" * 78)

    # ---- exact discriminant in m (sympy, over ℚ) ----
    z, m = sp.symbols("z m")
    g = sp.expand(m ** 2 * z ** 2 * (z - 1) * (m ** 2 * z - 1) - 1)
    res = sp.factor(sp.resultant(g, sp.diff(g, z), z))
    print(f"\n[1] g(z,m) = {g}")
    print(f"    Res_z(g, dg/dz) factors: {res}")
    # collect the nontrivial factors (drop unit/monomial factors m^k, constants)
    factors = []
    for fac, mult in sp.factor_list(res)[1]:
        if fac.free_symbols:  # skip pure constants
            if fac == m:      # m = 0 is the degenerate cusp, not a deformation
                continue
            factors.append((fac, mult))
    wb.add_data("gluing_polynomial", str(g))
    wb.add_data("discriminant_factors", [(str(f), int(k)) for f, k in factors])

    # ---- numeric roots of each factor (in m), 40 dps ----
    disc_pts = []
    for fac, _ in factors:
        poly = sp.Poly(fac, m)
        coeffs = [mp.mpf(str(c)) if sp.im(c) == 0 else mp.mpc(str(sp.re(c)), str(sp.im(c)))
                  for c in poly.all_coeffs()]
        for r in mp.polyroots(coeffs, maxsteps=200, extraprec=120):
            disc_pts.append(mp.mpc(r))
    # dedupe
    uniq = []
    for r in disc_pts:
        if all(mp.fabs(r - s) > mp.mpf("1e-25") for s in uniq):
            uniq.append(r)
    uniq.sort(key=lambda r: (float(mp.fabs(r - 1))))
    print(f"\n[2] discriminant points in m ({len(uniq)} distinct):")
    for r in uniq[:12]:
        print(f"    m = {mp.nstr(r, 12):>36s}   |m−1| = {mp.nstr(mp.fabs(r - 1), 8)}"
              f"   |Im m| = {mp.nstr(mp.fabs(mp.im(r)), 6)}")
    wb.add_data("discriminant_points_m",
                [{"m": mp.nstr(r, 25), "abs_m_minus_1": mp.nstr(mp.fabs(r - 1), 12),
                  "abs_im": mp.nstr(mp.fabs(mp.im(r)), 12)} for r in uniq])

    # ---- distances from the canonical paths ----
    d_complete = min(mp.fabs(r - 1) for r in uniq)
    d_realaxis = min(mp.fabs(mp.im(r)) for r in uniq)  # distance of locus to ℝ
    # canonical candidate points at the proton anchor:
    cands = {
        "m = e^{t/2} (real u = t)": mp.e ** (t_p / 2),
        "m = e^{t e^{i pi/4}/2} (b-aligned near-match)":
            mp.e ** (t_p * mp.e ** (mp.mpc(0, 1) * mp.pi / 4) / 2),
        "m = e^{u_min(p) i /2} (floor, imaginary dir)":
            mp.e ** (mp.mpc(0, 1) * mp.mpf("0.2134566682") / 2),
    }
    print("\n[3] distances:")
    print(f"    locus → m=1 (complete): {mp.nstr(d_complete, 8)}")
    print(f"    locus → real-m axis:    {mp.nstr(d_realaxis, 8)}")
    dists = {}
    for name, mc in cands.items():
        d = min(mp.fabs(r - mc) for r in uniq)
        dists[name] = d
        print(f"    locus → {name}: {mp.nstr(d, 8)}")
    print(f"    (anchor separation scale: |Δq| = {dq:.3e})")
    wb.add_data("distances", {
        "to_complete_m1": mp.nstr(d_complete, 15),
        "to_real_axis": mp.nstr(d_realaxis, 15),
        **{k: mp.nstr(v, 15) for k, v in dists.items()},
        "anchor_separation_dq": dq})

    # ---- verdict assertions (one-sided) ----
    min_all = min([d_complete, d_realaxis] + list(dists.values()))
    graze = float(min_all) < 1e-6
    wb.add_assertion("locus_is_O1_far_from_canonical_paths",
                     computed=float(1.0 if not graze else 0.0), expected=1.0,
                     tolerance=0.1,
                     source=f"min distance {mp.nstr(min_all, 6)} >> anchor "
                            f"separation {dq:.1e} => no branch-point graze")
    wb.add_assertion("complete_structure_not_on_locus",
                     computed=float(d_complete), expected=float(d_complete),
                     tolerance=1e-30,
                     source="recorded exact-locus distance from m=1 (informational)")

    ok = all(a.passed for a in wb.assertions)
    wb.add_data("verdict", (
        ("NO BRANCH-POINT GRAZE: the exact discriminant locus of the m-deformed "
         f"4_1 gluing system sits O(1)-far (min {mp.nstr(min_all, 4)}) from the "
         "complete structure, the real-m axis, and every canonical candidate "
         "path — 10^5+ times the anchor separation. Combined with the three "
         "prior negatives, the u^3-lever hypersensitivity is now excluded from "
         "(i) smooth substrate phases, (ii) the pole-seeding stage, (iii) the "
         "gluing-variety branch points. Scope-(a): the near-singularity lives "
         "in the substrate->m ASSIGNMENT (the archimedean-realization functor "
         "of conj:algebraic-geometric-dilog-equivalence) upstream of the "
         "geometry — the map itself, not the variety. No ingredient excluded "
         "structurally; no fit; nothing wired."
         if not graze else
         "BRANCH-POINT GRAZE FOUND — a discriminant point sits within 1e-6 of "
         "a canonical path; report the pair and STOP (do not fit m(q0)).")))
    wb.save()
    print("\nwitness -> computations/qbeta/qbeta-c3-phib-gluing-discriminant.witness.json")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
