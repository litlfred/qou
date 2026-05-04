#!/usr/bin/env python3
"""
GS-filtration E_2-page (level-3 stratum) probe.

Per `prop:gb-spectral-sequence`, the six mass terms map to spectral-
sequence pages:
  E_∞^(0,*) = descended Markov trace             (Term 1)
  E_∞^(1,*) = single-gen tower Σ Φ_q(|V_i|)      (Term 2 = "single")
  E_∞^(2,*) = pair-gen tower z² Σ Φ_q(|V_i V_j|) (Term 3 = "cross")
  E_∞^(ℓ ≥ 3, *) = HIGHER-STRATUM prefix corrections (Term 6 — OPEN)

The level-3+ stratum is exactly the missing binding-energy
contribution. This probe enumerates triples of adjacent
generators in the atomic braid and computes their Markov-trace
residues — a first concrete handle on Term 6.

Sub-braid trace at the triple stratum: for each ordered triple
(i, j, k) of generators in the atomic braid:
  tr^(3)_{ijk} = tr_M(σ_{g_i} σ_{g_j} σ_{g_k})

where g_i, g_j, g_k are the generator indices of the corresponding
sub-braids of the atom. Sum with the z^3 normalization (consistent
with single z^0 and pair z^2 prefactors at lower strata).

If this gives non-trivial contributions at 4He, 12C, 16O, 40Ca
(where Term 6 is needed), it confirms the GS-filtration story.
"""
from __future__ import annotations

import json
import sys
import time
from datetime import datetime, timezone
from itertools import combinations
from pathlib import Path

import mpmath

sys.path.insert(0, str(Path(__file__).parent))
from per_braid_tower_hybrid import (
    q0, qi0, z_mark, M_E_MEV, AME_MASS_MEV, _safe_phi
)
AME_MASS_MEV.setdefault("6Li", 5603.05182)
AME_MASS_MEV.setdefault("7Li", 6535.36573)
AME_MASS_MEV.setdefault("9Be", 8392.74912)

from schur_weyl_mpmath import markov_trace_mpmath


def triple_stratum_term(Z: int, N: int) -> dict:
    """Sum over ordered triples of adjacent generators in atom braid.

    For atom with Z protons + N neutrons, the atomic braid has
    n_strands = 3A. We consider 3-strand sub-braids = single
    nucleons (the 3 generators within one nucleon) and triple
    products spanning multiple nucleons.

    Triple stratum elements:
      - intra-nucleon triple: σ_0 σ_1 σ_0 of one nucleon = trefoil
      - inter-nucleon triple: σ_a σ_b σ_c spanning 2 or 3 nucleons

    For tractability, this probe sums over the BB-saturated
    triples — those that fit within the canonical atomic braid
    structure. Enumerating all triples is O(A^3); we count distinct
    types and weight by combinatorial multiplicity.
    """
    A = Z + N
    if A == 0:
        return {"Z": Z, "N": N, "A": 0, "term6": 0.0}

    # Three trace types at the triple stratum:
    #   tr_p3 = trace of one proton (3-strand trefoil)
    #   tr_n3 = trace of one neutron (3-strand trefoil)
    #   tr_pp_pair = trace of 2-proton-pair from level-2 (cross), retained
    #                for cross-correlation
    # Plus inter-nucleon triples — first-order: 3 generators σ_{3k}, σ_{3k+1}, σ_{3k+2}
    # in a single nucleon, second-order: σ_{3k+1}, σ_{3k+2}, σ_{3(k+1)} crossing
    # nucleon boundary.

    # Per-nucleon trefoil traces
    if Z > 0:
        tr_p3, _, _ = markov_trace_mpmath(1, 0, q_val=q0, include_inter=False)
        tr_p3 = abs(tr_p3)
    else:
        tr_p3 = mpmath.mpf(0)
    if N > 0:
        tr_n3, _, _ = markov_trace_mpmath(0, 1, q_val=q0, include_inter=False)
        tr_n3 = abs(tr_n3)
    else:
        tr_n3 = mpmath.mpf(0)

    # Per-nucleon-pair traces (2 nucleons in series, 6 strands)
    tr_pp6 = mpmath.mpf(0)
    tr_nn6 = mpmath.mpf(0)
    tr_pn6 = mpmath.mpf(0)
    if Z >= 2:
        v, _, _ = markov_trace_mpmath(2, 0, q_val=q0, include_inter=True)
        tr_pp6 = abs(v)
    if N >= 2:
        v, _, _ = markov_trace_mpmath(0, 2, q_val=q0, include_inter=True)
        tr_nn6 = abs(v)
    if Z >= 1 and N >= 1:
        v, _, _ = markov_trace_mpmath(1, 1, q_val=q0, include_inter=True)
        tr_pn6 = abs(v)

    # Per-nucleon-triple trace (3 nucleons in series, 9 strands)
    # Captures the level-3 stratum's intra-nucleon contribution.
    tr_ppp9 = mpmath.mpf(0)
    tr_nnn9 = mpmath.mpf(0)
    tr_ppn9 = mpmath.mpf(0)
    tr_pnn9 = mpmath.mpf(0)
    if Z >= 3:
        v, _, _ = markov_trace_mpmath(3, 0, q_val=q0, include_inter=True)
        tr_ppp9 = abs(v)
    if N >= 3:
        v, _, _ = markov_trace_mpmath(0, 3, q_val=q0, include_inter=True)
        tr_nnn9 = abs(v)
    if Z >= 2 and N >= 1:
        v, _, _ = markov_trace_mpmath(2, 1, q_val=q0, include_inter=True)
        tr_ppn9 = abs(v)
    if Z >= 1 and N >= 2:
        v, _, _ = markov_trace_mpmath(1, 2, q_val=q0, include_inter=True)
        tr_pnn9 = abs(v)

    # Triple stratum contribution: z^3 · Σ Φ_q(|tr_triple|) over triples
    # Combinatorial multiplicities (binomial coefficients):
    n_ppp = Z * (Z - 1) * (Z - 2) // 6 if Z >= 3 else 0
    n_nnn = N * (N - 1) * (N - 2) // 6 if N >= 3 else 0
    n_ppn = (Z * (Z - 1) // 2) * N if Z >= 2 and N >= 1 else 0
    n_pnn = Z * (N * (N - 1) // 2) if Z >= 1 and N >= 2 else 0

    triple_sum = mpmath.mpf(0)
    contributors = []
    for label, count, tr_val in [
        ("ppp", n_ppp, tr_ppp9),
        ("nnn", n_nnn, tr_nnn9),
        ("ppn", n_ppn, tr_ppn9),
        ("pnn", n_pnn, tr_pnn9),
    ]:
        if count > 0 and tr_val > 0:
            phi = _safe_phi(tr_val)
            c = count * phi
            triple_sum += c
            contributors.append({
                "type": label,
                "count": count,
                "trace_abs": float(tr_val),
                "phi_q": float(phi) if not mpmath.isinf(phi) else "inf",
                "contribution": float(c) if not mpmath.isinf(c) else "inf",
            })
    triple_sum *= z_mark ** 3  # E_∞^(3,*) prefactor

    return {
        "Z": Z, "N": N, "A": A,
        "z3_factor": float(z_mark ** 3),
        "tr_p3": float(tr_p3),
        "tr_n3": float(tr_n3),
        "tr_pp6": float(tr_pp6),
        "tr_nn6": float(tr_nn6),
        "tr_pn6": float(tr_pn6),
        "tr_ppp9": float(tr_ppp9),
        "tr_nnn9": float(tr_nnn9),
        "tr_ppn9": float(tr_ppn9),
        "tr_pnn9": float(tr_pnn9),
        "n_triples": {"ppp": n_ppp, "nnn": n_nnn, "ppn": n_ppn, "pnn": n_pnn},
        "term6_z3_sum_PhiQ": (float(triple_sum)
                                if not mpmath.isinf(triple_sum) else "inf"),
        "contributors": contributors,
    }


if __name__ == "__main__":
    print("=" * 88)
    print("GS-filtration level-3 stratum probe (Term 6 — OPEN per gb-spectral-sequence)")
    print("=" * 88)
    print(f"q_0 = {q0}")
    print(f"z   = {float(z_mark):.6f}    z^3 = {float(z_mark ** 3):.6f}")
    print()

    ATOMS = [
        ("D", 1, 1), ("3He", 2, 1), ("3H", 1, 2), ("4He", 2, 2),
        ("6Li", 3, 3), ("9Be", 4, 5), ("12C", 6, 6), ("16O", 8, 8),
    ]

    print(f"  {'atom':>5} {'A':>3} {'#triples':>14} {'|tr_ppp9|':>11} "
          f"{'|tr_pnn9|':>11} {'Term6':>14} {'B/A (MeV)':>12}")
    print("  " + "-" * 86)
    rows = []
    for name, Z, N in ATOMS:
        t0 = time.time()
        try:
            r = triple_stratum_term(Z, N)
        except Exception as exc:
            r = {"Z": Z, "N": N, "A": Z + N, "error": str(exc)[:80],
                 "term6_z3_sum_PhiQ": float("nan")}
        elapsed = time.time() - t0
        bn = (938.272 - AME_MASS_MEV[name] / r["A"])
        nt = r.get("n_triples", {})
        n_total = sum(nt.values()) if isinstance(nt, dict) else 0
        t6 = r.get("term6_z3_sum_PhiQ", float("nan"))
        if isinstance(t6, str):  # "inf"
            t6_str = "inf"
        elif isinstance(t6, float):
            t6_str = f"{t6:>14.4e}"
        else:
            t6_str = str(t6)
        print(f"  {name:>5} {r['A']:>3} {n_total:>14} "
              f"{r.get('tr_ppp9', 0):>11.4e} {r.get('tr_pnn9', 0):>11.4e} "
              f"{t6_str:>14} {bn:>12.4f}  ({elapsed:.0f}s)")
        rows.append({**r, "atom": name, "binding_per_nucleon": bn})

    # Correlation
    import numpy as np
    valid = [r for r in rows
             if isinstance(r.get("term6_z3_sum_PhiQ"), float)
             and not np.isnan(r["term6_z3_sum_PhiQ"])
             and r["term6_z3_sum_PhiQ"] > 0]
    if len(valid) > 1:
        t6 = np.array([r["term6_z3_sum_PhiQ"] for r in valid])
        bn = np.array([r["binding_per_nucleon"] for r in valid])
        corr = np.corrcoef(t6, bn)[0, 1]
        print()
        print(f"  Correlation Term6 vs binding/nucleon (valid={len(valid)}): {corr:+.4f}")

    out = {
        "computation": "gs-filtration-E2-page-probe",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "q0": float(q0),
        "atoms": rows,
        "interpretation": (
            "Probes the E_∞^(3,*) page of the GS spectral sequence "
            "per prop:gb-spectral-sequence's identification with the "
            "missing Term 6. Sums z^3·Φ_q over per-triple-nucleon "
            "Markov traces (ppp / nnn / ppn / pnn). Tests whether this "
            "stratum gives non-trivial binding-correlated values where "
            "the lower strata cannot."
        ),
    }
    out_path = (Path(__file__).parent.parent.parent
                / "docs/audits/2026-05-02-gs-filtration-E2-probe.witness.json")
    out_path.write_text(json.dumps(out, indent=2, default=str))
    print()
    print(f"Witness: {out_path.relative_to(Path(__file__).parent.parent.parent)}")
