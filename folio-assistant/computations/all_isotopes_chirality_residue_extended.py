#!/usr/bin/env python3
"""
EXTENDED CHIRALITY-RESIDUE FRAMEWORK — uses 56-knot B_3 hyperbolic
database (vs. original 11-knot inline list) to scan atomic braids for
std-channel knot sub-words and accumulate Σ Vol·|(q;q)_r|.

The extension targets atomic braids of length 13-21 (D through ⁴He,
⁶Li, ⁷Li), which were previously underrepresented because no 8- or
10-crossing std-channel knot ideals could match.

Imports EXTENDED_KNOTS from hyperbolic_knot_db_extended (4-7 crossing
hardcoded + 8/10-crossing via SnapPy with channel computed from
H_3(q_0) Hoefsmit characters).

Saves witness `all-isotopes-chirality-residue-extended.witness.json`.
"""
from __future__ import annotations
import sys, json, warnings
from pathlib import Path
from datetime import datetime, timezone

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

import mpmath as mp
mp.mp.dps = 30

from hecke_characters import partitions_of, dim_q
from q_parameter import Q as Q0_FLOAT
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV
from hyperbolic_knot_db_extended import get_extended_knots

# Re-use helper definitions from the original script
from all_isotopes_chirality_residue import (
    Q0, QI, me, q_int, q_pochhammer, frobenius_codim,
    b3_braid_word, atom_braid_word, cyclic_shifts, reversed_word,
    closure_class, find_knot_matches, chirality_residue,
)


def main():
    print("=" * 100)
    print("CHIRALITY-RESIDUE FRAMEWORK — EXTENDED DATABASE (56 B_3 hyperbolic knots)")
    print("=" * 100)
    print(f"  q_0 = {Q0_FLOAT}")

    EXTENDED_KNOTS = get_extended_knots()
    n_std_db = sum(1 for _, _, _, ch in EXTENDED_KNOTS if ch == 1)
    print(f"  EXTENDED_KNOTS: {len(EXTENDED_KNOTS)} total, "
          f"{n_std_db} std-channel (chirality)")

    # Lengths covered
    lens = sorted({len(w) for _, w, _, _ in EXTENDED_KNOTS})
    print(f"  Braid-word lengths in DB: {lens}")
    print()

    # Pre-compute Frobenius co-Casimir per A
    print(f"  Atomic Frobenius co-Casimir Σ_{{3A}} = Σ_{{λ⊢3A}} 1/dim_q V_λ:")
    fc = {}
    for A in range(1, 5):
        n = 3 * A
        s = float(frobenius_codim(n))
        fc[A] = s
        print(f"    A = {A}, 3A = {n}:  Σ = {s:.6f}, m_e·Σ = {float(me)*s:.6f} MeV")
    print()

    AME_BIND = {
        'D':   2.22456612, 'T':   8.481798,
        '³He': 7.718058,   '⁴He': 28.29566,
        '⁶Li': 31.99405,   '⁷Li': 39.24454,
    }
    M_H_ATOMIC = M_P_MEV + M_E_MEV
    isotopes = [
        ('p (1H)',  1, 0, M_H_ATOMIC, 0.0),
        ('n',       0, 1, M_N_MEV,    0.0),
        ('D',       1, 1, 1876.12393, AME_BIND['D']),
        ('T',       1, 2, 2809.43215, AME_BIND['T']),
        ('³He',     2, 1, 2809.41347, AME_BIND['³He']),
        ('⁴He',     2, 2, 3728.40133, AME_BIND['⁴He']),
        ('⁶Li',     3, 3, 5603.05129, AME_BIND['⁶Li']),
        ('⁷Li',     3, 4, 6535.36573, AME_BIND['⁷Li']),
    ]

    # find_knot_matches default max_len=9; extend to 10 for the new DB
    max_knot_len = max(lens)

    print(f"  {'iso':<8} {'#strands':>9} {'#sym':>5} {'#std':>5} {'#alt':>5} "
          f"{'Σ_chir(MeV)':>14} {'CODATA ref':>15}")
    rows = []
    for name, Z, N, M_ref, B_ame in isotopes:
        A = Z + N
        word = atom_braid_word(Z, N)
        matches = find_knot_matches(word, EXTENDED_KNOTS,
                                    min_len=4, max_len=max_knot_len)
        std_matches = [m for m in matches if m['channel'] == 1]
        sym_matches = [m for m in matches if m['channel'] == 0]
        alt_matches = [m for m in matches if m['channel'] == 2]
        chir_total, breakdown = chirality_residue(matches, channel_filter=1)
        ref_label = (B_ame if A >= 2 else float(mp.mpf(str(M_N_MEV)) -
                                                  mp.mpf(str(M_P_MEV))))
        print(f"  {name:<8} {len(word):>9} {len(sym_matches):>5} "
              f"{len(std_matches):>5} {len(alt_matches):>5} "
              f"{chir_total:>14.6f} {ref_label:>15.4f}")
        rows.append({
            'iso': name, 'Z': Z, 'N': N, 'A': A, 'word_length': len(word),
            'n_total_matches': len(matches),
            'n_sym_matches': len(sym_matches),
            'n_std_matches': len(std_matches),
            'n_alt_matches': len(alt_matches),
            'chirality_residue_MeV': chir_total,
            'std_breakdown': breakdown,
            'all_matches': [
                {'start': m['start'], 'length': m['length'], 'knot': m['knot'],
                 'volume': float(m['volume']), 'channel': m['channel']}
                for m in matches
            ],
            'ame_binding': B_ame,
        })

    print()
    print("=" * 100)
    print("  Comparison with binding data:")
    print("=" * 100)
    print(f"  {'iso':<8} {'Σ_chir':>12} {'m_e·Σ_3A':>12} {'sum':>12} "
          f"{'AME':>10} {'gap (sum-AME)':>15} {'err %':>8}")
    for r in rows:
        if r['iso'] in ('p (1H)', 'n'):
            continue
        sigma_3A = float(me) * fc.get(r['A'], 0)
        chir = r['chirality_residue_MeV']
        total = chir + sigma_3A
        ame = r['ame_binding']
        gap = total - ame
        if ame > 0:
            err = (total - ame) / ame * 100
            print(f"  {r['iso']:<8} {chir:>+12.6f} {sigma_3A:>+12.6f} "
                  f"{total:>+12.6f} {ame:>+10.4f} {gap:>+15.6f} "
                  f"{err:>+7.2f}%")

    # np splitting check
    print()
    print(f"  np splitting check:")
    n_chir = next(r['chirality_residue_MeV'] for r in rows if r['iso'] == 'n')
    p_chir = next(r['chirality_residue_MeV'] for r in rows
                  if r['iso'].startswith('p'))
    sigma_3 = float(me) * fc[1]
    delta_pred = sigma_3 + (n_chir - p_chir)
    delta_codata = M_N_MEV - M_P_MEV
    print(f"    proton chirality residue:   {p_chir:+.6f}")
    print(f"    neutron chirality residue:  {n_chir:+.6f}")
    print(f"    n-p chirality diff:         {n_chir - p_chir:+.6f}")
    print(f"    m_e · Σ_3:                  {sigma_3:+.6f}")
    print(f"    predicted Δm_{{n-p}}:         {delta_pred:+.6f} MeV")
    print(f"    CODATA Δm_{{n-p}}:            {delta_codata:+.6f} MeV")
    print(f"    err = {(delta_pred-delta_codata)/delta_codata*100:+.3f}%")

    # Save witness
    witness = {
        'computation': 'all-isotopes-chirality-residue-extended',
        'description': (
            'Chirality-residue framework re-run with extended 56-knot '
            'B_3 hyperbolic database (4-10 crossing, channel annotation '
            'via Hoefsmit characters at q_0).  Compared to the original '
            '11-knot run, this scans 8- and 10-crossing knot ideals as '
            'well, including all 19 std-channel knots in the database.'
        ),
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'q_0': Q0_FLOAT,
        'database': {
            'count': len(EXTENDED_KNOTS),
            'std_channel_count': n_std_db,
            'word_lengths': lens,
        },
        'isotopes': rows,
    }
    out = Path(__file__).parent / "all-isotopes-chirality-residue-extended.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")


if __name__ == "__main__":
    main()
