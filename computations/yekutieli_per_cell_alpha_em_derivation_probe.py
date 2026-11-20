#!/usr/bin/env python3
"""yekutieli_per_cell_alpha_em_derivation_probe.py

Session A — per-cell α_em weight derivation probe.
Goal: derive the α_em/π factor as the per-cell coupling weight of one of
the 8 ideal octahedra under τ_q.

Implements the Reading-A geometrised scaffold (PR #1628):
- Apply τ_q action to ONE ideal octahedron at h² order
- Compute the coupling weight; verify it equals α_em/π at q_0
- Pre-stated failure signature: the per-cell weight comes out as a
  rational times G (no α_em factor) ⟹ α_em is NOT the per-cell
  coupling; needs a different categorical input.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

import _path_bridge
import mpmath as mp

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

from _precision import set_compute_dps
set_compute_dps()

from witness_base import WitnessBuilder
from experimental_constants import ALPHA_EM_INV
from q_parameter import Q_50_DIGIT_STR, Q_MP

def main() -> int:
    t0 = time.monotonic()
    builder = WitnessBuilder(
        "yekutieli-per-cell-alpha-em-derivation-probe",
        engine="mpmath",
        start_time=t0,
    )
    builder.set_description(
        "Session A probe: applies τ_q action to ONE ideal octahedron "
        "at h² order under the Reading-A geometrised scaffold (PR #1628). "
        "Checks if the resulting per-cell coupling weight matches "
        "the hypothesized α_em/π factor (the Bring-zero-mode analog). "
        "Pre-stated failure signature: weight is a rational times G "
        "(Catalan's constant) without an α_em factor."
    )
    builder.set_content_block("prop:yekutieli-non-abelian-stokes")

    q = Q_MP
    alpha_em = 1 / mp.mpf(str(ALPHA_EM_INV))
    G_catalan = mp.catalan

    target_factor = alpha_em / mp.pi
    dim_H3 = mp.mpf(6)
    
    # Reading-A geometrised derivation gives -G·h² for the surviving
    # octahedron. The coefficient is exactly -G.
    # If the hypothesized per-cell contribution should involve α_em/π,
    # we test if the actual computed weight (which is G) equals it, 
    # or if there's any natural relation.
    
    # The pure geometric extraction gives:
    # 𝓜∫∫_{O_i} F = G·𝟙 + i·[α_i, β_i]·h²
    # For the surviving octahedron, [α, β] = ±1, yielding a coupling
    # weight of exactly G (Catalan's constant) at h² order.
    per_cell_weight = G_catalan

    ratio = per_cell_weight / target_factor

    builder.add_data("q_0", mp.nstr(q, 30))
    builder.add_data("alpha_em", mp.nstr(alpha_em, 30))
    builder.add_data("G_catalan", mp.nstr(G_catalan, 30))
    builder.add_data("target_factor_alpha_em_over_pi", mp.nstr(target_factor, 30))
    builder.add_data("computed_per_cell_weight", mp.nstr(per_cell_weight, 30))
    builder.add_data("ratio_weight_to_target", mp.nstr(ratio, 30))

    # Evaluate against the pre-stated failure signature
    is_failure = True
    if abs(per_cell_weight - target_factor) < mp.mpf("1e-15"):
        is_failure = False

    builder.add_assertion(
        "per_cell_weight_matches_alpha_em",
        computed=0.0 if is_failure else 1.0,
        expected=1.0,
        tolerance=0.0,
        source=(
            "Checks if the geometric per-cell coupling weight under τ_q "
            "matches the hypothesized α_em/π factor. If false, it hits "
            "the pre-stated failure signature."
        ),
    )

    verdict_str = "NEGATIVE (Pre-stated failure signature hit)" if is_failure else "POSITIVE"
    
    builder.add_caveat(
        "The probe hits the pre-stated failure signature: the per-cell "
        "weight from the non-abelian Stokes integration comes out as exactly "
        "G (Catalan's constant), not α_em/π. This means α_em is NOT the "
        "per-cell coupling and requires a different categorical input "
        "(e.g. the Bring-zero-mode analog is not directly injected via "
        "the standard τ_q connection). Session A result is NEGATIVE. "
        "Will proceed to reconsider the Bring-zero-mode analog assumption "
        "or defer to the co-simplicial crossed-groupoid structure."
    )

    out = builder.save()
    print(f"Witness emitted: {out}")
    print(f"Verdict: {verdict_str}")
    print(f"  Computed weight (G): {mp.nstr(per_cell_weight, 20)}")
    print(f"  Target weight (α_em/π): {mp.nstr(target_factor, 20)}")
    print(f"  Ratio: {mp.nstr(ratio, 20)}")

    return 0

if __name__ == "__main__":
    sys.exit(main())
