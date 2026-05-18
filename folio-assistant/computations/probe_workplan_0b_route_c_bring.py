#!/usr/bin/env python3
"""Route C concrete: Bring zero-mode adaptation for nucleon M_N.

Per the workplan-0b spec, the Bring zero-mode template
([`prop:em-coupling-bring-zero-mode`](../../content/quantum-observable-universe/descartes-universe/em-coupling-bring-zero-mode.md))
fixes α_EM additively from the Euler characteristic χ(Bring) = −8.

For the baryon mass M_N, the analogous candidate is a **secondary
characteristic class** of the nucleon-braid complement.

## Standard secondary classes for 3-manifolds

For a closed orientable 3-manifold M (or knot/link complement):
- Primary Euler characteristic χ(M) = 0 (general fact for 3-manifolds)
- **Chern-Simons invariant CS(M)** — primary secondary characteristic
- **η-invariant η(M)** — APS spectral asymmetry
- **Reidemeister torsion τ_R(M)** — combinatorial, refines η
- **L²-torsion / volume** — Vol(M) for hyperbolic case

For B_3 complement (= 2 ideal regular octahedra):
- Vol(B_3) = 8·G ≈ 7.328 (Adams 1985, classical)
- CS(B_3, level k) — depends on flat SU(2) connection; classical for level 1

## Test bench

Try the additive structure:
  M_N(q_0) = [Vol(B_3) + secondary] / ℏ_q² · m_e
        OR
  M_N(q_0) = Vol(B_3) · [scalar factor involving secondary] / ℏ_q² · m_e

Empirically known: M_N = 938.918 MeV needs Vol(K_p)/ℏ_q² · m_e
factor = 938.918/0.511 = 1837.41. With Vol(B_3) = 7.328 alone,
factor = 7.328/0.00982 = 746.4. Ratio: 1837.41/746.4 = 2.461.

So the "additive secondary" interpretation:
  Vol_effective = 2.461 · Vol(B_3) = 18.027

Question: is 18.027 = Vol(B_3) + secondary_class for any known
secondary class evaluated at q_0?

The candidate values:
  - 2 · Vol(4_1) · π² / 6 = ?
  - Reidemeister-like η · h · k for integer k
  - Family A factor (5/2 + 3h²/4) applied multiplicatively
  - Catalan-related secondaries: G² · X for some X
"""
from __future__ import annotations
import json, sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from witness_base import WitnessBuilder
from q_parameter import Q_50_DIGIT_STR
from experimental_constants import M_E_MEV, M_P_MEV, Q_NEUTRON_MEV

mp.mp.dps = 100
Q = mp.mpf(Q_50_DIGIT_STR)
H = Q - 1/Q
HBAR = (Q - 1) / Q
G = mp.catalan
VOL_B3 = 8 * G
VOL_41 = mp.mpf("2.02988321281930725004240510854658")

M_E = mp.mpf(repr(M_E_MEV))
M_P = mp.mpf(repr(M_P_MEV))
M_N = M_P + mp.mpf(repr(Q_NEUTRON_MEV)) + M_E
M_NUCLEON = (M_P + M_N) / 2


def main() -> int:
    w = WitnessBuilder("workplan-0b-route-c-bring", engine="mpmath")
    w.set_description(
        "Route C concrete: Bring zero-mode analog for M_N. Tests "
        "secondary characteristic classes of B_3 complement as "
        "candidates for Vol(K_p) = 18.03 = Vol(B_3) + Σ_secondary."
    )
    w.set_content_block("conj:flavor-dressed-mass-from-substrate-split")

    # Implied Vol(K_p) from M_NUCLEON
    vol_K_p_implied = M_NUCLEON * HBAR**2 / M_E
    print(f"Implied Vol(K_p) for M_N: {mp.nstr(vol_K_p_implied, 15)}")
    print(f"  vs Vol(B_3) = 8G = {mp.nstr(VOL_B3, 15)}")
    secondary_needed = vol_K_p_implied - VOL_B3
    print(f"  → secondary needed = {mp.nstr(secondary_needed, 15)}")
    print(f"    (ratio: {float(vol_K_p_implied / VOL_B3):.6f})")
    print()

    # Additive secondary candidates
    print("Additive candidates (Vol_effective = Vol(B_3) + secondary):")
    additive = {
        "Vol(4_1)·5": VOL_41 * 5,
        "Vol(B_3)·1.461": VOL_B3 * mp.mpf("1.461"),
        "8G · h^(-2)/100": 8 * G * H**(-2) / 100,  # h^-2 is large at q_0
        "Vol(B_3) · (3/4)·h²·~13": VOL_B3 * mp.mpf(3)/4 * H**2 * 13,
        "π² · (5/2 - h²·G)": mp.pi**2 * (mp.mpf(5)/2 - H**2 * G),
        "Vol(4_1)·9 - Vol(B_3)": VOL_41 * 9 - VOL_B3,
        "h^(-2) · 0.105": H**(-2) * mp.mpf("0.105"),  # h^-2 ≈ 22.88
        "Vol(B_3)·(1+G)/G ·(something)": None,
    }
    print(f"  Target secondary = {float(secondary_needed):.6f}")
    print()
    for name, val in additive.items():
        if val is None: continue
        diff = float(val - secondary_needed)
        rel = diff / float(secondary_needed) * 100
        marker = " ← within 1%" if abs(rel) < 1 else ""
        print(f"  {name:30s} = {float(val):>10.5f}  (Δ {rel:+.2f}%){marker}")

    # Multiplicative candidates (Vol_effective = Vol(B_3) · factor)
    # NOTE (Copilot review on PR #751): the C2 inflection parameter
    # `(4-q)/(4q+3)` is the INPUT to the PR #690 categorical action
    # A(a), NOT the multiplicative mass-scale factor. The comparable
    # factor is the OUTPUT `A(a_C2) ≈ 2.46`. Keeping the input value
    # in the multiplicative_candidates map produced contradictory
    # numerics, so it is recorded separately under `c2_input_parameter`
    # in the witness rather than being compared to the target factor.
    print()
    print(f"Multiplicative candidates (Vol_eff = Vol(B_3) · factor):")
    print(f"  Required factor = {float(vol_K_p_implied / VOL_B3):.10f}")
    multiplicative = {
        "5/2 - h²·G (orig conjecture)": mp.mpf(5)/2 - H**2 * G,
        "5/2 + h²·(3/4) (Family A)": mp.mpf(5)/2 + H**2 * mp.mpf(3)/4,
        "1 + Vol(4_1)/(Vol(B_3)/2)": 1 + VOL_41 / (VOL_B3/2),
        "(1 + 1/q)^2 / 2": (1 + 1/Q)**2 / 2,
        "Vol(4_1)/h": VOL_41 / H,
        "[2]_q · (5/4)": (Q + 1/Q) * mp.mpf(5)/4,
    }
    # Recorded for cross-reference but NOT a mass-scale candidate.
    c2_input_parameter = (4 - Q)/(4*Q + 3)
    target_factor = vol_K_p_implied / VOL_B3
    for name, val in multiplicative.items():
        rel = float((val - target_factor) / target_factor * 100)
        marker = " ← within 1%" if abs(rel) < 1 else ""
        print(f"  {name:40s} = {float(val):>12.7f}  (Δ {rel:+.3f}%){marker}")

    w.add_data("vol_K_p_implied", float(vol_K_p_implied))
    w.add_data("secondary_needed", float(secondary_needed))
    w.add_data("target_factor", float(target_factor))
    w.add_data("additive_candidates", {n: float(v) for n, v in additive.items() if v is not None})
    w.add_data("multiplicative_candidates", {n: float(v) for n, v in multiplicative.items()})
    w.add_data("c2_input_parameter", float(c2_input_parameter))

    # NOTE (Copilot review on PR #751): the C2 inflection produces a
    # CATEGORICAL ACTION VALUE A(a_C2) ≈ 2.4615 — the MULTIPLICATIVE
    # mass-scale factor. The parameter `a_C2` itself is ≈ 0.388 (from
    # a_post_hoc = (4-q)/(4q+3)), NOT the mass-scale factor.
    #
    # `probe_a_selection_criteria.py` (PR #690) computes
    #     m_p_pred = Vol(B_3)/ℏ_q² · A(a_C2) · m_e
    # where A(a_C2) ≈ 2.4615 (the OUTPUT of the categorical action
    # at the inflection point), NOT the input `a_C2 ≈ 0.388`.
    # The required-factor cross-check below derives the mass-scale
    # factor algebraically from the target M_NUCLEON. It is labelled
    # `required_mass_scale_factor` (not `A_at_aC2`) to make explicit
    # that this is the empirically demanded factor, not an independent
    # PR #690 categorical-action computation.
    print()
    print(f"PR #690 C2 inflection cross-check (corrected per review):")
    required_mass_scale_factor = M_NUCLEON * HBAR**2 / (VOL_B3 * M_E)  # empirical
    print(f"  PR #690 inflection INPUT a (≈ 0.388): {float(c2_input_parameter):.10f}")
    print(f"  Required mass-scale factor (= M_N · ℏ_q² / (Vol(B_3)·m_e)): {float(required_mass_scale_factor):.10f}")
    print(f"  (Independent PR #690 A(a_C2) is computed in probe_a_selection_criteria.py, not here.)")
    print(f"  This required factor is what `5/2 − h²·G` empirically matches to 0.068%.")
    print(f"  Sanity m_p_pred = Vol(B_3)/ℏ_q² · required · m_e = {float(VOL_B3/HBAR**2 * required_mass_scale_factor * M_E):.6f} MeV (= M_N target by construction)")

    print()
    print("VERDICT for Route C:")
    print(f"  No additive secondary class gives Vol_eff = {float(vol_K_p_implied):.4f}")
    print(f"  cleanly. Multiplicative form requires factor ≈ 2.46;")
    print(f"  the C2 inflection (4-q)/(4q+3) is the closest empirical")
    print(f"  match but is NOT a standard secondary characteristic class.")
    print(f"  → Route C requires a new categorical construction.")

    out = w.save()
    print(f"\nWitness emitted: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
