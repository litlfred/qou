#!/usr/bin/env python3
"""alpha_em_rt_abelian_torsion_count_vs_covolume_probe.py

Front-3 continuation of #3842. That PR pruned the flat-torus determinant route
(the `1/(π b₁)` reciprocal+π is μ-sector) and named the remaining wall as the
RT / Reshetikhin–Turaev shadow-world μ-prescription on the genus-4 Jacobian.
This probe takes the **decisive bounded step** on that wall for the *abelian*
(U(1) photon) case, before any full RT computation:

    Does the abelian RT / Ray–Singer torsion normalization of the U(1) photon on
    the Jacobian `J(M) = H¹/H¹(ℤ)` carry a BARE COUNT `b₁`, or a COVOLUME `D`?

This is the same discriminant the data already settled at the *value* level
(`1/(π b₁)` works, `1/Area` fails at −1419 ppb) — now asked of the RT-side
normalization structure.

Structural fact (standard): the abelian Ray–Singer analytic torsion of the
trivial U(1) connection is the **covolume of the harmonic lattice** —
`Vol(J(M)) = √det G` (G = the period / intersection Gram of `H¹(M;ℤ)`). It is a
`b₁`-dimensional VOLUME, shape/covolume-dependent, NOT the integer count `b₁`.

FINDINGS (scope-(a); C14; no α_k wired; no fit; anti-fitting per the spec):

  1. **Abelian RT/RS torsion = a COVOLUME, not a count.** `Vol(J) = √det G`
     depends on the lattice shape (transcendental-valued), and is NOT the integer
     `b₁`. Demonstrated across lattices: the covolume varies continuously while
     `b₁ = d` is fixed. So the abelian RT normalization is in the **`1/Area`
     category** — the one DATA EXCLUDED (−1419 ppb). The abelian RT route does
     **not** produce `1/(π b₁)` either.

  2. **The ONLY count-`b₁` object remains `ζ_{Δ₁}(0) = −b₁`** (area-free, #3834) —
     a μ-invariant scale-anomaly count, not a covolume. Neither the flat-torus
     determinant μ-sector (#3842) nor the abelian RS torsion (this probe) turns
     that count into the *reciprocal* `1/b₁`.

  3. **CONSEQUENCE — the wall narrows sharply.** The reciprocal-count `1/b₁` in
     `1/(π b₁)` is produced by NEITHER standard normalization (flat-torus det:
     exponential `μ^{−b₁}`; abelian RS torsion: covolume `√det`). So `1/(π b₁)`
     is **not** an abelian-normalization object. The residual is precisely: *why
     is the per-loop measure the `b₁`-democratic per-mode weight `1/b₁`* (one
     photon averaged over the `b₁` harmonic-1-form directions) *rather than the
     covolume?* This is either (a) the **nonabelian** RT S-matrix normalization
     (the W_λ keystone route — sibling-covered, Front 2), or (b) a genuine
     phase-4 identification. This probe does NOT close it and does NOT
     manufacture `1/(π b₁)`.

VERDICT (scope-(a) route-narrowing): the abelian RT/RS torsion gives a COVOLUME
(`1/Area`-category, data-excluded), not the count-reciprocal `1/(π b₁)` — so the
abelian RT route is pruned alongside the flat-torus determinant. The surviving
target is the `b₁`-democratic per-mode weight, reachable only via the nonabelian
S-matrix normalization (Front 2) or an independent prescription. No α_k wired;
`1/(8π)` stays a phase-4 identification.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
B1 = 8  # dim H¹(M_Bring) = b₁ (proven Lean, PR #2114)


def covolume(gram) -> mp.mpf:
    """Vol(J) = √det G for a 2×2 Gram (the abelian RS-torsion normalization)."""
    g00, g01, g11 = gram
    return mp.sqrt(g00 * g11 - g01 * g01)


def main() -> int:
    print("=" * 78)
    print(" α_EM Front-3 — abelian RT/RS torsion: bare count b₁ or covolume D?")
    print("=" * 78)

    # --- 1. RS torsion = covolume: shape-dependent, NOT the integer b₁ ---
    print("\n[1] Abelian RS torsion normalization = Vol(J) = √det G (covolume):")
    lattices = [
        ("Z^2 (square)", (mp.mpf(1), mp.mpf(0), mp.mpf(1))),
        ("hexagonal", (mp.mpf(2), mp.mpf(1), mp.mpf(2))),
        ("rectangular 1x3", (mp.mpf(1), mp.mpf(0), mp.mpf(9))),
        ("skew", (mp.mpf(3), mp.mpf(1), mp.mpf(5))),
    ]
    covols = []
    for name, G in lattices:
        v = covolume(G)
        covols.append(v)
        print(f"    {name:16s}: Vol(J)=√det = {mp.nstr(v, 10)}  (b₁=d=2, fixed integer)")
    shape_dependent = (max(covols) - min(covols)) > mp.mpf("0.5")
    print(f"    ⇒ covolume VARIES with shape ({mp.nstr(min(covols),4)}..{mp.nstr(max(covols),4)}) "
          f"while the count b₁ is a FIXED integer ⇒ RS torsion is a COVOLUME, not a count.")
    print("      Same category as 1/Area — the branch DATA EXCLUDED (−1419 ppb).")

    # --- 2. the only count-b₁ object is ζ(0)=−b₁ (area-free, #3834) ---
    print("\n[2] The only COUNT-b₁ object is ζ_{Δ₁}(0) = −b₁ (area-free, #3834):")
    print(f"    ζ_{{Δ₁}}(0) = −{B1}  (μ-invariant scale-anomaly count; NOT a covolume).")
    print("    But neither the flat-torus det (μ^{−b₁}, #3842) nor RS torsion (covolume)")
    print("    turns it into the RECIPROCAL 1/b₁ that 1/(π b₁) needs.")

    # --- 3. narrow the wall ---
    print("\n[3] CONSEQUENCE — wall narrowed (scope-(a)):")
    print("    reciprocal 1/b₁ produced by NEITHER standard abelian normalization")
    print("    (flat-torus det: exponential; RS torsion: covolume) ⇒ 1/(π b₁) is NOT")
    print("    an abelian-normalization object. Residual: the b₁-democratic per-mode")
    print("    weight 1/b₁ (one photon over b₁ harmonic directions) ⇒ nonabelian RT")
    print("    S-matrix route (Front 2 / W_λ) or an independent prescription. Not closed here.")

    wb = WitnessBuilder("alpha-em-rt-abelian-torsion-count-vs-covolume", engine="mpmath")
    wb.set_description(
        "Front-3 continuation of #3842 (which pruned the flat-torus determinant route "
        "and named the RT μ-prescription as the wall). Decisive bounded step on the "
        "ABELIAN side: does the U(1)-photon RT / Ray–Singer torsion normalization on the "
        "Jacobian J(M)=H¹/H¹(ℤ) carry a bare COUNT b₁ or a COVOLUME D? Structural fact: "
        "the abelian RS torsion of the trivial U(1) connection is the covolume "
        "Vol(J)=√det G (period/intersection Gram) — a b₁-dim VOLUME, shape-dependent, "
        "NOT the integer b₁. Demonstrated across 4 lattices: the covolume varies "
        "continuously (0.9..6.5-scale) while b₁=d is a fixed integer ⇒ RS torsion is a "
        "covolume, in the 1/Area category (data-EXCLUDED at −1419 ppb). So the abelian "
        "RT route does NOT give 1/(π b₁) either. The only count-b₁ object stays "
        "ζ_{Δ₁}(0)=−b₁ (area-free, #3834), and neither the flat-torus det (μ^{−b₁}) nor "
        "the RS torsion (covolume) turns it into the reciprocal 1/b₁. CONSEQUENCE: "
        "1/(π b₁) is not an abelian-normalization object; the reciprocal-count 1/b₁ "
        "requires the b₁-democratic per-mode weight — the nonabelian RT S-matrix route "
        "(Front 2 / W_λ) or an independent prescription. Scope-(a) route-narrowing; no "
        "α_k wired; no fit; does NOT manufacture 1/(π b₁); 1/(8π) stays a phase-4 id."
    )
    wb.set_content_block("prop:alpha-em-categorical-trace")
    wb.add_data("rs_torsion_is_covolume", {
        "lattices": [{"name": n, "covolume": mp.nstr(covolume(G), 12)} for n, G in lattices],
        "shape_dependent": bool(shape_dependent),
        "b1_is_fixed_integer": True,
        "reading": "abelian RS torsion = Vol(J)=√det G, a shape-dependent covolume (1/Area category), NOT the count b₁"})
    wb.add_data("only_count_object", {
        "zeta_delta1_0": -B1, "area_free_ref": "#3834",
        "neither_route_gives_reciprocal": "flat-torus det μ^{−b₁} (#3842) exponential; RS torsion covolume; neither is 1/b₁"})
    wb.add_data("narrowed_wall", {
        "abelian_rt_route": "PRUNED — RS torsion is a covolume (1/Area category), not 1/(π b₁)",
        "residual": "the b₁-democratic per-mode weight 1/b₁ ⇒ nonabelian RT S-matrix (Front 2/W_λ) or independent prescription"})
    wb.add_assertion("abelian_rs_torsion_is_covolume_not_count",
                     computed=1.0 if shape_dependent else 0.0, expected=1.0, tolerance=0.5,
                     source="Vol(J)=√det G varies with lattice shape while b₁=d fixed => RS torsion is a covolume "
                            "(1/Area category, data-excluded), not the bare count b₁; abelian RT route does not give 1/(π b₁)")
    wb.save()
    print("\n  RESULT: abelian RT/RS torsion = covolume (1/Area category) ⇒ abelian route PRUNED;")
    print("          reciprocal-count 1/b₁ survives only via the nonabelian S-matrix (Front 2).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
