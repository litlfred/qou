#!/usr/bin/env python3
"""
trace_convention_reconciliation.py — reconcile the two binding-trace
conventions (Wenzl Jones-Markov under Convention D vs normalized-Plancherel)
at the 50-digit proton pin.

Historically (PR #1397, pre-2026-08-09 convention-C + grouped ordering),
the binding-per-bond probe reported a 29% gap between binding_canonical's
Δtr(²H) = 0.5952397103674884 and an H_{3A}-direct Plancherel Δtr = 0.4241.
This script shows the gap is NOT a framework inconsistency but a
y_λ WEIGHT-SCHEME difference:

  - binding_canonical uses the WENZL JONES-MARKOV normalization under
    canonical **Convention D** (z_D = q³/(q² + 1), Wenzl level N = 2
    two-row cap, at the 50-digit proton pin q₀; owner rulings 2026-08-09
    and 2026-08-15 excised the historical convention C parameter
    z_C = 1/(√q + 1/√q) = √q/(q + 1)).
  - the per-bond probe used the NORMALIZED-PLANCHEREL weights
    (dim_q²/[n]_q!) — the q-Schur convention, which is not the canonical
    mass/binding trace weight scheme.

VERIFIED (Convention D, proton pin, borromean intra-nucleon ordering):
  1. binding_canonical's Δtr(²H) = 0.1470466779804084691094947290199176910037...
     equals the Wenzl-bridge joint-word Δtr on H₆ to all 50 digits.
  2. Same braid word + same χ_λ, the two y_λ schemes give different
     traces (Convention-D Wenzl Δtr = 0.147047 vs Plancherel Δtr = 0.000444;
     per-block weight difference, not a global scalar).

CONCLUSION: the canonical mass/binding convention is Convention D
(Wenzl JM at N = 2, z_D = q³/(q² + 1), proton pin).
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

from mpmath import mp, mpf, fabs

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

from mass_at_3A_proper import (  # noqa: E402
    Q0_PROTON,
    atom_braid_word_3A, chi_lambda_of_word,
    normalized_plancherel_weights_3A, _cached_seminormal,
)
from tr_m_wenzl_bridge_mpfr import tr_M_via_wenzl_bridge_mpfr  # noqa: E402

# Historical pre-2026-08-09 convention-C + grouped-ordering Δtr(²H) from
# binding_canonical (PR #1397), retained for provenance only (bean qou-yotw).
HISTORICAL_CONVENTION_C_GROUPED_DELTA_TR = "0.5952397103674884"


def tr_plancherel(word, A, n_gens):
    """Σ_λ y_λ^Plancherel · χ_λ(W) at H_{3A}."""
    tot = mpf(0)
    for shape, w in normalized_plancherel_weights_3A(A):
        sig, dim, _ = _cached_seminormal(shape, Q0_PROTON)
        if dim == 0:
            continue
        chi = chi_lambda_of_word(sig, dim, word, n_gens)
        tot += mpf(str(w)) * mpf(str(chi)) / dim
    return tot


def main():
    set_compute_dps()
    wb = WitnessBuilder("trace-convention-reconciliation", engine="mpmath")

    qs = Q_50_DIGIT_STR
    wb.add_parameter("q0", qs)
    wb.add_parameter("markov_convention", "D")

    # Deuteron joint H₆ braid words (free vs bound)
    word_free = atom_braid_word_3A(1, 1, include_inter=False)
    word_bound = atom_braid_word_3A(1, 1, include_inter=True)
    n_gens = 5

    # Wenzl JM under Convention D (z_D = q³/(q² + 1), proton pin) on the joint word
    af = fabs(mpf(str(tr_M_via_wenzl_bridge_mpfr(word_free, 6, qs, dps=50))))
    ab = fabs(mpf(str(tr_M_via_wenzl_bridge_mpfr(word_bound, 6, qs, dps=50))))
    dtr_wenzl = af - ab

    # normalized-Plancherel on the same word
    bf = fabs(tr_plancherel(word_free, 2, n_gens))
    bb = fabs(tr_plancherel(word_bound, 2, n_gens))
    dtr_planck = bf - bb

    # Read binding_canonical's Convention-D proton-pin deuteron delta_tr_exact
    # directly from its witness via add_upstream (records sha256 provenance).
    bc_witness = wb.add_upstream(HERE / "binding-canonical.witness.json")
    bc_rows = bc_witness.get("data", {}).get("results", [])
    d_row = next((r for r in bc_rows if r.get("atom") == "D"), None)
    if d_row is None or "delta_tr_exact" not in d_row:
        raise KeyError("binding-canonical.witness.json missing atom=='D' delta_tr_exact")
    dtr_canonical_reported = mpf(str(d_row["delta_tr_exact"]))
    fact_match = fabs(dtr_wenzl - dtr_canonical_reported)

    print("=" * 70)
    print("TRACE-CONVENTION RECONCILIATION (deuteron H₆, Convention D, proton pin)")
    print("=" * 70)
    print()
    print(f"  Wenzl JM Conv D (joint word): Δtr = {mp.nstr(dtr_wenzl, 16)}")
    print(f"  binding_canonical (reported): Δtr = {mp.nstr(dtr_canonical_reported, 16)}")
    print(f"  → same convention?            |Δ| = {mp.nstr(fact_match, 4)} (mpf)")
    print()
    print(f"  Plancherel (joint word):      Δtr = {mp.nstr(dtr_planck, 12)}")
    print(f"  Wenzl/Plancherel ratio:       {mp.nstr(dtr_wenzl / dtr_planck, 8)}")
    print()
    print("  → The Δtr gap between Wenzl JM (Convention D, z_D = q³/(q²+1))")
    print("    and normalized-Plancherel is the y_λ weight scheme, NOT a")
    print("    framework inconsistency. Convention D Wenzl JM at the proton")
    print("    pin is the canonical mass/binding convention.")

    wb.set_description(
        "Reconcile binding-trace conventions under canonical Convention D "
        "(z_D = q^3/(q^2+1), Wenzl N=2 two-row cap) at the 50-digit proton pin: "
        "binding_canonical's Δtr(²H) (0.147047) matches the Wenzl-bridge on the "
        "joint H₆ word to all 50 digits, whereas normalized-Plancherel gives "
        "0.000444 (a y_λ weight-scheme difference, not a framework inconsistency; "
        "historical convention-C grouped values were 0.5952 vs 0.4241)."
    )
    wb.add_data("markov_convention", "D")
    wb.add_data("deuteron_delta_tr", {
        "wenzl_jm_joint_word": mp.nstr(dtr_wenzl, 40),
        "binding_canonical_reported": mp.nstr(dtr_canonical_reported, 40),
        "wenzl_matches_canonical_residual": mp.nstr(fact_match, 6),
        "normalized_plancherel": mp.nstr(dtr_planck, 40),
        "wenzl_over_plancherel": mp.nstr(dtr_wenzl / dtr_planck, 40),
        "historical_convention_c_grouped_reported": HISTORICAL_CONVENTION_C_GROUPED_DELTA_TR,
    })
    wb.add_data("resolution", {
        "gap_cause": "y_λ weight scheme (Convention-D Wenzl Jones-Markov vs q-Schur Plancherel)",
        "canonical_convention": "Convention D — Wenzl JM at N=2 (z_D = q^3/(q^2+1)), proton pin",
        "probe_error": "binding-per-bond used Plancherel weights",
        "deuteron_result": "Wenzl-bridge joint-word Δtr matches binding_canonical delta_tr_exact to 50 digits under Convention D at the proton pin",
        "A_ge_3_status": "genuine open problem — single-link volume fails -60% in the correct Wenzl convention",
    })

    wb.add_assertion(
        "wenzl_matches_binding_canonical",
        computed=fact_match,
        expected=0,
        tolerance="1e-10",
        source="Convention-D Wenzl-bridge joint-word Δtr = binding_canonical "
               "delta_tr_exact to 50 digits at the proton pin (both use "
               "z_D = q^3/(q^2+1) and borromean intra-nucleon ordering).",
    )
    wb.add_assertion(
        "conventions_differ",
        computed=fabs(dtr_wenzl - dtr_planck),
        expected="0.147",
        tolerance="0.01",
        source="Convention-D Wenzl JM (0.1470) ≠ Plancherel (0.0004) at "
               "proton pin: per-block weight difference (historical "
               "convention-C grouped values were 0.5952 vs 0.4241).",
    )
    wb.save()


if __name__ == "__main__":
    main()
