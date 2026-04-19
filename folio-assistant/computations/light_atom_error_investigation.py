#!/usr/bin/env python3
"""
Light-atom error investigation.

Audit showed:
  D    err 0.0420%
  T    err 0.0754%
  3He  err 0.0023%

These were computed via symbolic canonical Markov trace + brane-scaled
tower. Symbolic canonical is slow (~30s+ per atom at H_9, H_{12}+);
this script uses the fast Plancherel Markov trace with the same brane-
scaled tower and extends to 4He, 6Li, 7Li, 9Be to expose the error
pattern across the light-atom range.

Plancherel vs symbolic canonical give numerically different trace
values; so the errors will differ from the audit's symbolic numbers.
We're after the PATTERN — is error monotonic in A? Tied to magic
numbers (2, 8)? Correlated with Z even/odd or N even/odd?

Framework per atom:
  tr_M_atom  = Plancherel sum over H_{3A} partitions
  tr_M_free  = same with include_inter=False
  B_canon    = E_0 * (|tr_M_free| - |tr_M_atom|)
  tower_level_1 raw = m_free^(1) - m_atom^(1) via canonical_tower
  B_tower    = hbar_q^2 * tower_level_1
  B_total    = B_canon + B_tower
  err        = |B_total - B_AME| / (A * 938.272) * 100
"""
from __future__ import annotations

import sys
import json
import time
from pathlib import Path
from datetime import datetime, timezone

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))

from q_parameter import Q as Q0, HA as h
from canonical_plus_multibrane import (HBAR_Q, E_0_BETA_DECAY_MEV,
                                             per_gen_V_hat_aggregated,
                                             lift_V_markov,
                                             tower_mass_level,
                                             brane_scaling)
from hecke_characters import partitions_of, dim_q, qfac
from mass_at_3A_proper import _cached_seminormal, atom_braid_word_3A


def _trM_word(word, n_strands):
    from scipy.sparse import issparse, eye as speye
    nfac = qfac(n_strands)
    total = 0.0
    for shape in partitions_of(n_strands):
        sigmas, dim, _ = _cached_seminormal(shape)
        if dim == 0:
            continue
        dq = dim_q(shape)
        if dq == 0:
            continue
        sparse = bool(sigmas) and issparse(sigmas[0])
        if sparse:
            prod = speye(dim, format='csr'); I = speye(dim, format='csr')
        else:
            prod = np.eye(dim); I = np.eye(dim)
        for (c, d, g) in word:
            if g < len(sigmas):
                prod = prod @ (c * sigmas[g] + d * I)
        chi = float(prod.diagonal().sum()) if sparse else float(np.trace(prod))
        total += (dq * dq) / nfac * chi / dim
    return total


def light_atom_analysis(Z, N, B_AME):
    A = Z + N
    n = 3 * A

    # Canonical term via Plancherel Markov trace
    word_atom = list(atom_braid_word_3A(
        Z, N, include_inter=True, include_electrons=True))
    word_free = list(atom_braid_word_3A(
        Z, N, include_inter=False, include_electrons=True))
    trM_a = _trM_word(word_atom, n)
    trM_f = _trM_word(word_free, n)
    canon_term = abs(trM_f) - abs(trM_a)
    B_canon = E_0_BETA_DECAY_MEV * canon_term

    # Tower term (level 1 only, with brane_scaling)
    V_a_0 = per_gen_V_hat_aggregated(Z, N, include_inter=True)
    V_f_0 = per_gen_V_hat_aggregated(Z, N, include_inter=False)
    V_a_1 = lift_V_markov(V_a_0, 1)
    V_f_1 = lift_V_markov(V_f_0, 1)
    m_a_1 = tower_mass_level(V_a_1, pair_mode="full")
    m_f_1 = tower_mass_level(V_f_1, pair_mode="full")
    tower_raw = m_f_1 - m_a_1
    tower_scaled = brane_scaling(1) * tower_raw
    B_tower = E_0_BETA_DECAY_MEV * tower_scaled

    B_total = B_canon + B_tower
    Mtot = A * 938.272
    err = abs(B_total - B_AME) / Mtot * 100
    rel_err = abs(B_total - B_AME) / B_AME * 100 if B_AME else float('nan')

    return {
        "Z": Z, "N": N, "A": A,
        "B_AME": B_AME, "Mtot_MeV": Mtot,
        "tr_M_atom": trM_a, "tr_M_free": trM_f,
        "B_canon_MeV": B_canon,
        "tower_raw": tower_raw, "tower_scaled": tower_scaled,
        "B_tower_MeV": B_tower,
        "B_total_MeV": B_total,
        "B_gap_MeV": B_total - B_AME,
        "err_mass_pct": err,
        "err_binding_pct": rel_err,
        "magic_Z": Z in {2, 8, 20, 28, 50, 82, 126},
        "magic_N": N in {2, 8, 20, 28, 50, 82, 126},
    }


if __name__ == "__main__":
    ATOMS = [
        # (name, Z, N, B_AME_MeV)
        ("D",     1,  1,   2.22452),
        ("T",     1,  2,   8.481821),
        ("3He",   2,  1,   7.71804),
        ("4He",   2,  2,  28.295674),
        ("6Li",   3,  3,  32.00),
        ("7Li",   3,  4,  39.244529),
        ("9Be",   4,  5,  58.1650),
    ]

    print("=" * 115)
    print("LIGHT-ATOM ERROR INVESTIGATION  (Plancherel canonical + ℏ_q² tower)")
    print(f"q0 = {Q0}, ℏ_q = {HBAR_Q:.6f}, ℏ_q² = {HBAR_Q**2:.6f}")
    print(f"E_0 = {E_0_BETA_DECAY_MEV} MeV")
    print("=" * 115)

    print(f"\n  {'atom':>6} {'Z':>2} {'N':>2} {'A':>2} {'magic':>6} "
          f"{'B_canon':>10} {'B_tower':>10} {'B_tot':>10} {'B_AME':>10} "
          f"{'gap':>10} {'err_m%':>9} {'err_B%':>9}")
    print("  " + "-" * 110)

    all_results = []
    for name, Z, N, B_AME in ATOMS:
        t0 = time.time()
        try:
            r = light_atom_analysis(Z, N, B_AME)
            r["atom"] = name
            r["time_sec"] = time.time() - t0
            magic_tag = ""
            if r["magic_Z"]:
                magic_tag += "Z"
            if r["magic_N"]:
                magic_tag += "N"
            print(f"  {name:>6} {Z:>2} {N:>2} {Z+N:>2} {magic_tag:>6} "
                  f"{r['B_canon_MeV']:>+10.4f} {r['B_tower_MeV']:>+10.4f} "
                  f"{r['B_total_MeV']:>+10.4f} {B_AME:>+10.4f} "
                  f"{r['B_gap_MeV']:>+10.4f} "
                  f"{r['err_mass_pct']:>8.4f}% "
                  f"{r['err_binding_pct']:>8.3f}%")
            all_results.append(r)
        except Exception as e:
            import traceback
            print(f"  {name:>6}  ERR: {type(e).__name__}: {e}")
            traceback.print_exc()

    # Pattern analysis
    print("\n" + "=" * 115)
    print("PATTERN ANALYSIS")
    print("=" * 115)
    print(f"\n  A-dependence:")
    for r in sorted(all_results, key=lambda x: x["A"]):
        print(f"    A={r['A']:>2}  err={r['err_mass_pct']:.4f}%  "
              f"err_B={r['err_binding_pct']:.3f}%  gap={r['B_gap_MeV']:+.3f} MeV  "
              f"atom={r['atom']}")

    print(f"\n  Magic-number behavior:")
    for r in all_results:
        tag = ""
        if r["magic_Z"]: tag += " (Z=2 magic)"
        if r["magic_N"]: tag += " (N=2 magic)"
        if tag:
            print(f"    {r['atom']:>6}{tag}:  err={r['err_mass_pct']:.4f}%")

    print(f"\n  even/odd Z, even/odd N:")
    for r in all_results:
        zp = "even" if r["Z"] % 2 == 0 else "odd"
        np_ = "even" if r["N"] % 2 == 0 else "odd"
        print(f"    {r['atom']:>6} (Z {zp}, N {np_}):  "
              f"err={r['err_mass_pct']:.4f}%  gap={r['B_gap_MeV']:+.3f}")

    # Save witness
    out = Path(__file__).parent / "light-atom-error-investigation.witness.json"
    out.write_text(json.dumps({
        "computation": "light-atom-error-investigation",
        "description": (
            "Light-atom mass prediction error (D to 9Be) using "
            "Plancherel-level canonical Markov trace + brane-scaled "
            "level-1 tower. Expose error pattern vs A, magic numbers, "
            "Z/N parity."),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {"q0": Q0, "hbar_q": HBAR_Q,
                          "hbar_q_squared": HBAR_Q**2,
                          "E_0_MeV": E_0_BETA_DECAY_MEV},
        "results": all_results,
    }, indent=2, default=str))
    print(f"\nWitness: {out}")
