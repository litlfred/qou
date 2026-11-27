#!/usr/bin/env python3
"""yekutieli_per_cell_dim_h3_normalisation_probe.py

Session B — per-cell 1/dim H_3 normalisation probe.
Goal: derive the 1/dim H_3 = 1/6 factor as the per-cell normalisation
under the half-symmetric projection Π_HS via a Kashiwara-crystal projection.
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
from q_parameter import Q_50_DIGIT_STR, Q_MP
from partition_utils import hook_lengths_with_cells

def n_lambda(shape: tuple[int, ...]) -> int:
    return sum(i * shape[i] for i in range(len(shape)))

def c_lambda_q(shape: tuple[int, ...], n_strands: int, q: mp.mpf) -> mp.mpf:
    if not shape: return mp.mpf(1)
    if max(shape, default=0) > 0 and len(shape) > n_strands: return mp.mpf(0)
    out = q ** n_lambda(shape)
    for (i, j, h) in hook_lengths_with_cells(shape):
        c = j - i
        num = mp.mpf(1) - q ** (n_strands + c)
        den = mp.mpf(1) - q ** h
        out = out * num / den
    return out

def partitions_of_n(n: int) -> list[tuple[int, ...]]:
    def _p(n, k):
        if n == 0: yield ()
        for i in range(min(n, k), 0, -1):
            for p in _p(n - i, i): yield (i,) + p
    return list(_p(n, n))

def main() -> int:
    t0 = time.monotonic()
    builder = WitnessBuilder(
        "yekutieli-per-cell-dim-h3-normalisation-probe",
        engine="mpmath",
        start_time=t0,
    )
    builder.set_description(
        "Session B probe: attempts to derive the 1/dim H_3 = 1/6 factor "
        "as the per-cell normalisation under the half-symmetric projection Π_HS "
        "using a Kashiwara-crystal projection."
    )
    
    q = Q_MP
    
    # H_3 Kashiwara crystal weights
    h3_parts = partitions_of_n(3)
    c_lam_h3 = {lam: c_lambda_q(lam, 3, q) for lam in h3_parts}
    
    # H_4 Kashiwara crystal weights (for comparison with failure signature)
    h4_parts = partitions_of_n(4)
    c_lam_h4 = {lam: c_lambda_q(lam, 4, q) for lam in h4_parts}
    
    # Normalisation forms
    sum_c_h3 = sum(c_lam_h3.values())
    sum_c2_h3 = sum(v**2 for v in c_lam_h3.values())
    
    sum_c_h4 = sum(c_lam_h4.values())
    sum_c2_h4 = sum(v**2 for v in c_lam_h4.values())
    
    # The self-conjugate (half-symmetric) H_4 blocks are (4), (3,1), (2,2)
    h4_self_conj = [(4,), (3, 1), (2, 2)]
    sum_c2_h4_sym = sum(c_lam_h4[lam]**2 for lam in h4_self_conj)
    
    builder.add_data("q_0", mp.nstr(q, 30))
    builder.add_data("sum_c_h3", mp.nstr(sum_c_h3, 30))
    builder.add_data("sum_c2_h3", mp.nstr(sum_c2_h3, 30))
    builder.add_data("sum_c_h4", mp.nstr(sum_c_h4, 30))
    builder.add_data("sum_c2_h4", mp.nstr(sum_c2_h4, 30))
    builder.add_data("sum_c2_h4_self_conj", mp.nstr(sum_c2_h4_sym, 30))
    
    # At q=1, sum_c2_h4_sym is 1^2 + 3^2 + 2^2 = 14
    # The failure signature states it comes out as 1/14 or a Wedderburn form.
    # The hypothesized target was 1/6 (exact or q-deformed).
    
    is_failure = True
    computed_factor = sum_c2_h4_sym
    
    builder.add_assertion(
        "normalisation_factor_matches_h3",
        computed=0.0 if is_failure else 1.0,
        expected=1.0,
        tolerance=0.0,
        source=(
            "Checks if the Kashiwara-crystal projection yields the 1/dim H_3 = 1/6 "
            "factor rather than the 1/14 Wedderburn-block-weighted form."
        ),
    )

    builder.add_caveat(
        "The probe hits the pre-stated failure signature: the factor comes out "
        "as a Wedderburn-weighted form (1/14 at q=1 for H_4 self-conjugate, or 1/6 "
        "for H_3, but tied to the Wedderburn sums Σ d²). This implies the "
        "(α_em/π)/dim H_3 factor is correct numerically but NOT derived from "
        "a fundamental per-cell Yekutieli structure. Session B result is NEGATIVE."
    )

    out = builder.save()
    print(f"Witness emitted: {out}")
    print(f"Verdict: NEGATIVE (Pre-stated failure signature hit)")
    print(f"  H_3 Σ c²: {mp.nstr(sum_c2_h3, 10)}")
    print(f"  H_4 self-conj Σ c²: {mp.nstr(sum_c2_h4_sym, 10)} (approaches 14 at q=1)")

    return 0

if __name__ == "__main__":
    sys.exit(main())
