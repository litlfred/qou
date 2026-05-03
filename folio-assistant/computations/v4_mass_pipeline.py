#!/usr/bin/env python3
"""v4 mass pipeline — Item 3 from the 4-parallel followup.

Closes the §3·A integration gap: take the depth-1 single-generator and
depth-2 adjacent-pair tower terms produced by `crt_markov_v4.total_mass_h3a`
and combine them with the v3 descended Markov trace (from
`hecke_characters.compute_mass_at_level`) into a UNIFIED mass prediction.
Compare per-isotope to PDG / AME and to v3-only.

Question: does the v4 tower contribution close v3's 0.05–0.32% mass
errors, or does it stay flat / get worse?

Strategy:
  - For each light isotope, get v3's M_pred (which already adds Z·m_p +
    N·m_n + Z·m_e plus binding from the descended Markov trace at H_{3A}).
  - Use crt_markov_v4.total_mass_h3a to get depth-1 + depth-2 tower
    contributions (in the dimensionless Markov-trace normalisation).
  - Compute v4 as: M_v4 = M_v3 + ALPHA · (markov_v4_total - markov_v3_desc) ·
    m_e — where ALPHA is the binding-scale calibration that hecke_core
    uses (8 · m_e · Catalan, per `prop:binding-scale-catalan`).

  This is the simplest faithful integration: keep v3's framework, add the
  tower-term DELTA scaled by the same binding constant.
"""
from __future__ import annotations
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import mpmath
mpmath.mp.dps = 50

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as Q0
from experimental_constants import M_E_MEV, CATALAN
from hecke_characters import compute_mass_at_level
import crt_markov_v4 as v4

# Catalan binding-scale per prop:binding-scale-catalan; ALPHA in the
# original hecke_core is m_e · 8·G with G = Catalan's constant.
# Both M_E_MEV (CAL-0) and CATALAN are imported from experimental_constants
# per Gemini review on PR #515 (centralized-constants rule).
ALPHA_BIND = M_E_MEV * 8 * CATALAN  # ≈ 3.7445 MeV per categorical unit


# Reference masses (PDG 2022 / AME)
REFERENCE_MASSES_MEV = {
    'proton':   (1, 0, 938.27208816),
    'deuteron': (1, 1, 1875.61294257),  # ²H atom
    'tritium':  (1, 2, 2808.92113298),
    'he3':      (2, 1, 2808.39160743),
}


def predict(Z: int, N: int) -> dict:
    """Return both v3 and v4 predictions side by side."""
    A = Z + N
    if A == 0:
        return {'A': 0, 'v3_M': 0, 'v4_M': 0, 'note': 'A=0 — vacuum'}
    k = 3 * A

    # v3: descended Markov trace via hecke_characters
    t0 = time.time()
    M_v3, details_v3 = compute_mass_at_level(Z, N, k=k)
    markov_v3 = float(details_v3.get('markov_trace', 1.0))
    binding_v3 = float(details_v3.get('binding', 0.0))
    elapsed_v3 = time.time() - t0

    # v4: depth-1 + depth-2 tower terms
    t0 = time.time()
    try:
        v4_data = v4.total_mass_h3a(Z, N)
        # Per Gemini high-priority review on PR #515: keys returned by
        # crt_markov_v4.total_mass_h3a are 'tower_total_dimless' and
        # 'depth0_markov_trace' — NOT 'markov_total_A' / 'markov_desc'.
        # The earlier wrong keys made both default to markov_v3 → tower
        # delta was always 0 (silent bug; no MeV correction).
        markov_total = float(v4_data.get('tower_total_dimless', markov_v3))
        markov_desc = float(v4_data.get('depth0_markov_trace', markov_v3))
        # Tower DELTA = total - desc (the "missing 99%" claim)
        tower_delta = markov_total - markov_desc
        # Apply same binding-scale calibration to the tower delta:
        v4_correction_MeV = ALPHA_BIND * tower_delta
    except Exception as e:
        v4_data = {'error': str(e)}
        markov_total = markov_v3
        markov_desc = markov_v3
        tower_delta = 0.0
        v4_correction_MeV = 0.0
    elapsed_v4 = time.time() - t0

    M_v4 = float(M_v3) + v4_correction_MeV

    return {
        'Z': Z, 'N': N, 'A': A, 'k': k,
        'M_v3_MeV': float(M_v3),
        'markov_v3': markov_v3,
        'binding_v3_dimless': binding_v3,
        'markov_v4_total': markov_total,
        'tower_delta_dimless': tower_delta,
        'v4_correction_MeV': v4_correction_MeV,
        'M_v4_MeV': M_v4,
        'elapsed_v3_s': elapsed_v3,
        'elapsed_v4_s': elapsed_v4,
    }


def main():
    print("=" * 90)
    print("v4 mass pipeline — does the depth-1 + depth-2 tower close §3·A?")
    print("=" * 90)
    print(f"q_0 = {Q0}")
    print(f"binding-scale ALPHA = m_e · 8G ≈ {ALPHA_BIND:.6f} MeV")
    print()
    print(f"{'name':>10} {'Z,N':>6} {'PDG MeV':>14} {'v3 MeV':>14} {'v3 err%':>10} "
          f"{'v4 MeV':>14} {'v4 err%':>10} {'Δv4-v3':>12} {'verdict':>16}")
    print("-" * 130)
    rows = []
    v3_better = 0; v4_better = 0; tied = 0
    for name, (Z, N, M_pdg) in REFERENCE_MASSES_MEV.items():
        r = predict(Z, N)
        if 'error' in r:
            print(f"{name:>10}  ERROR: {r['error']}")
            continue
        M_v3 = r['M_v3_MeV']
        M_v4 = r['M_v4_MeV']
        err_v3 = (M_v3 / M_pdg - 1) * 100
        err_v4 = (M_v4 / M_pdg - 1) * 100
        delta = M_v4 - M_v3
        if abs(err_v4) < abs(err_v3) - 0.001:
            verdict = '✓ v4 better'; v4_better += 1
        elif abs(err_v4) > abs(err_v3) + 0.001:
            verdict = '✗ v4 worse'; v3_better += 1
        else:
            verdict = '~ same'; tied += 1
        print(f"{name:>10} ({Z},{N}) {M_pdg:>14.4f} "
              f"{M_v3:>14.4f} {err_v3:>+9.4f}% "
              f"{M_v4:>14.4f} {err_v4:>+9.4f}% "
              f"{delta:>+12.4f} {verdict:>16}")
        rows.append({**r, 'name': name, 'M_pdg': M_pdg,
                     'err_v3_pct': err_v3, 'err_v4_pct': err_v4,
                     'delta_v4_v3': delta, 'verdict': verdict})

    print()
    print(f"Summary: v4 closer for {v4_better} atoms, v3 closer for {v3_better}, "
          f"tied for {tied}.")
    print()

    # Q-value comparisons under both
    print("Q-value comparisons (β-decay):")
    print(f"{'decay':>14} {'Q_PDG MeV':>14} {'Q_v3':>14} {'Q_v4':>14}")
    decays = [
        ('³H→³He', 'tritium', 'he3'),
        # ('⁶He→⁶Li', not in registry — would need ⁶He which isn't in REFERENCE_MASSES)
    ]
    Q_rows = []
    for label, parent_name, daughter_name in decays:
        parent = next((r for r in rows if r['name'] == parent_name), None)
        daughter = next((r for r in rows if r['name'] == daughter_name), None)
        if parent and daughter:
            Q_pdg_parent = REFERENCE_MASSES_MEV[parent_name][2]
            Q_pdg_daughter = REFERENCE_MASSES_MEV[daughter_name][2]
            Q_pdg = Q_pdg_parent - Q_pdg_daughter - M_E_MEV  # rough Q
            Q_v3 = parent['M_v3_MeV'] - daughter['M_v3_MeV'] - M_E_MEV
            Q_v4 = parent['M_v4_MeV'] - daughter['M_v4_MeV'] - M_E_MEV
            print(f"{label:>14} {Q_pdg:>14.4f} {Q_v3:>14.4f} {Q_v4:>14.4f}")
            Q_rows.append({'decay': label, 'Q_pdg': Q_pdg, 'Q_v3': Q_v3, 'Q_v4': Q_v4})

    print()
    print("VERDICT:")
    if v4_better > v3_better:
        print(f"  → v4 tower terms PARTIALLY close §3·A: {v4_better}/{v4_better+v3_better+tied} atoms improve.")
    elif v4_better == v3_better:
        print(f"  → v4 tower terms ~neutral: same number of improvements as regressions.")
    else:
        print(f"  → v4 tower terms make it WORSE by {v3_better - v4_better} atoms.")
        print(f"    The naïve scaling ALPHA · (markov_total - markov_desc) is NOT the right")
        print(f"    integration; the tower terms need a DIFFERENT calibration constant.")

    out = {
        'computation': 'v4-mass-pipeline',
        'computedAt': datetime.now(timezone.utc).isoformat(),
        'description': (
            "v4 mass pipeline integration test — wires crt_markov_v4 "
            "depth-1 + depth-2 tower terms into the v3 mass prediction "
            "via simple ALPHA-binding-scale rescaling. Reports per-atom "
            "v3 vs v4 error against PDG, plus Q-value comparisons."
        ),
        'binding_scale_alpha_MeV': ALPHA_BIND,
        'reference_masses_pdg': {n: m for n, (_, _, m) in REFERENCE_MASSES_MEV.items()},
        'predictions': rows,
        'q_values': Q_rows,
        'summary': {
            'v3_closer_count': v3_better,
            'v4_closer_count': v4_better,
            'tied_count': tied,
            'verdict': (
                'v4 closes §3·A' if v4_better > v3_better
                else 'v4 ~neutral' if v4_better == v3_better
                else 'v4 makes it worse — wrong calibration'
            ),
        },
    }
    out_path = Path(__file__).parent / 'v4-mass-pipeline.witness.json'
    with open(out_path, 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False, default=str)
    print(f"→ wrote {out_path}")


if __name__ == '__main__':
    main()
