#!/usr/bin/env python3
"""
EXTEND CHIRALITY-RESIDUE FRAMEWORK TO ALL ISOTOPES.

Per the np splitting derivation:
  Δm_{n-p} = m_e · Σ_3 + m_e · Σ_chir
where Σ_chir = Vol(6_1) · |(q;q)_3| from the SOLE std-channel
chirality knot in the neutron's curvature-rank-3 GB stratum.

Generalize to atom (Z, N):
  binding correction = m_e · Σ_3A + m_e · Σ_chir(Z,N)
where:
  Σ_3A   = Σ_{λ⊢3A} 1/dim_q V_λ        (atomic Frobenius co-Casimir)
  Σ_chir = Σ over std-channel knot ideals (k, r, λ) in the atomic
           GB trajectory of:  Vol(K) · |(q;q)_r| · indicator(λ=std)

For each atom: build 3A-strand braid (B_3 prefix on first nucleon
+ typed quark crossings + inter-nucleon couplings), scan for
hyperbolic-knot sub-words, identify std-channel residues, sum
contributions.

Compare to AME binding values for D, T, ³He, ⁴He, ⁶Li, ⁷Li.
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
from q_parameter import Q as Q0_FLOAT, Q_MP, Q_INV_MP
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV

Q0 = Q_MP; QI = Q_INV_MP  # was f64 roundtrip
me = mp.mpf(str(M_E_MEV))


def q_int(n):
    return (Q0**n - QI**n) / (Q0 - QI)


def q_pochhammer(n):
    out = mp.mpf(1)
    for k in range(1, n+1):
        out *= (1 - Q0**k)
    return out


def frobenius_codim(n_strands):
    return sum(1 / dim_q(tuple(lam)) for lam in partitions_of(n_strands))


HYPERBOLIC_KNOTS = [
    # name, word, vol, jet_channel (0=sym, 1=std, 2=alt)
    ("4_1",  (1, -2, 1, -2),                    2.0299, 0),
    ("5_2",  (1, 1, 1, -2, 1, -2),              2.8281, 0),
    ("6_1",  (1, 1, -2, 1, -2, -2),             3.1640, 1),
    ("6_2",  (1, 1, 1, -2, 1, -2, -2),          4.4015, 0),
    ("6_3",  (1, 1, -2, 1, -2, 1, -2),          5.6927, 0),
    ("7_2",  (1, 1, 1, 1, 1, -2, 1, -2),        3.3317, 0),
    ("7_3",  (1, 1, 1, 1, -2, 1, 1, -2),        4.5921, 1),
    ("7_4",  (1, 1, -2, 1, -2, -2, -2),         5.0137, 2),
    ("7_5",  (1, 1, 1, 1, -2, 1, 1, 1, -2),     6.4439, 0),
    ("7_6",  (1, 1, 1, -2, 1, -2, -2, -2),      7.0846, 0),
    ("7_7",  (1, 1, -2, 1, -2, 1, -2, -2),      7.6434, 0),
]


def b3_braid_word():
    return (1, -2, 1, -2, 1, -2)


def atom_braid_word(Z, N):
    """Build atomic braid: B_3 prefix + per-nucleon crossings +
    inter-nucleon couplings.  Generators: 1-indexed σ_1..σ_{3A-1}."""
    A = Z + N
    # Start with B_3 on first 3 strands
    word = list(b3_braid_word())
    # Per-nucleon quark crossings (within each nucleon's 3 strands)
    quark_types = ['u'] * (Z * 3) + ['d'] * (N * 3)
    # Re-arrange: each nucleon has its 3 quarks; proton uud, neutron udd
    quark_types = []
    for k in range(A):
        if k < Z:
            quark_types.extend(['u', 'u', 'd'])
        else:
            quark_types.extend(['u', 'd', 'd'])
    # Quark crossings (intra-nucleon, on σ_{3k+1}, σ_{3k+2})
    for k in range(A):
        offset = 3 * k
        # Crossing of quarks 0 and 1 (on generator σ_{offset+1})
        # Crossing of quarks 1 and 2 (on generator σ_{offset+2})
        # Crossing of quarks 0 and 2 (on σ_{offset+1})
        for i in range(3):
            for j in range(i+1, 3):
                gen = offset + min(i, j) + 1
                if gen >= 3 * A:
                    continue
                t_i = quark_types[offset + i]
                t_j = quark_types[offset + j]
                if t_i == t_j == 'u':
                    word.append(gen)
                elif t_i == t_j == 'd':
                    word.append(-gen)
                else:
                    word.append(gen)
    # Inter-nucleon crossings (on σ_{3k} for k=1..A-1)
    for k in range(1, A):
        gen = 3 * k
        # Couple nucleon k-1 and nucleon k via gen
        # Type: pp, nn, or pn based on nucleon types
        prev_nuc = 'p' if k - 1 < Z else 'n'
        curr_nuc = 'p' if k < Z else 'n'
        if prev_nuc == 'p' and curr_nuc == 'p':
            word.append(gen)
        elif prev_nuc == 'n' and curr_nuc == 'n':
            word.append(-gen)
        else:
            word.append(gen)
    return tuple(word)


def cyclic_shifts(word):
    n = len(word)
    return [tuple(word[i:] + word[:i]) for i in range(n)]


def reversed_word(word):
    return tuple(reversed(word))


def closure_class(word):
    classes = set()
    for shift in cyclic_shifts(word):
        classes.add(shift)
        classes.add(reversed_word(shift))
    return classes


def find_knot_matches(word, knot_db, min_len=4, max_len=9):
    n = len(word)
    matches = []
    for start in range(n):
        for length in range(min_len, min(n - start + 1, max_len + 1)):
            sub = tuple(word[start:start + length])
            for knot_name, knot_word, vol, channel in knot_db:
                if length != len(knot_word):
                    continue
                if sub in closure_class(knot_word):
                    matches.append({
                        'start': start, 'length': length,
                        'knot': knot_name, 'volume': vol,
                        'channel': channel,
                    })
                    break
    return matches


def chirality_residue(matches, channel_filter=1):
    """Sum m_e · Vol(K) · |(q;q)_r| over std-channel matches."""
    total = mp.mpf(0)
    breakdown = []
    for m in matches:
        if m['channel'] != channel_filter:
            continue
        r = m['start']
        qpr = q_pochhammer(r + 1)  # |(q;q)_{r+1}|; or use r as in np case
        # Use r itself per np-splitting derivation
        qpr = q_pochhammer(r) if r >= 1 else mp.mpf(1)
        val = me * mp.mpf(str(m['volume'])) * mp.fabs(qpr)
        total += val
        breakdown.append((r, m['knot'], float(val)))
    return float(total), breakdown


def main():
    print("=" * 100)
    print("CHIRALITY-RESIDUE FRAMEWORK EXTENDED TO ALL ISOTOPES")
    print("=" * 100)
    print(f"  q_0 = {Q0_FLOAT}")
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
    }
    M_H_ATOMIC = M_P_MEV + M_E_MEV
    isotopes = [
        ('p (1H)',  1, 0, M_H_ATOMIC, 0.0),
        ('n',       0, 1, M_N_MEV,    0.0),
        ('D',       1, 1, 1876.12393, AME_BIND['D']),
        ('T',       1, 2, 2809.43215, AME_BIND['T']),
        ('³He',     2, 1, 2809.41347, AME_BIND['³He']),
        ('⁴He',     2, 2, 3728.40133, AME_BIND['⁴He']),
    ]

    print(f"  {'iso':<8} {'#strands':>9} {'#std knots':>11} {'Σ_chir(MeV)':>14} "
          f"{'CODATA reference':>20}")
    rows = []
    for name, Z, N, M_ref, B_ame in isotopes:
        A = Z + N
        word = atom_braid_word(Z, N)
        matches = find_knot_matches(word, HYPERBOLIC_KNOTS)
        std_matches = [m for m in matches if m['channel'] == 1]
        chir_total, breakdown = chirality_residue(matches, channel_filter=1)
        print(f"  {name:<8} {len(word):>9} {len(std_matches):>11} "
              f"{chir_total:>14.6f} {B_ame if A>=2 else (M_N_MEV-M_P_MEV):>20.4f}")
        rows.append({
            'iso': name, 'Z': Z, 'N': N, 'A': A, 'word_length': len(word),
            'n_std_matches': len(std_matches),
            'chirality_residue_MeV': chir_total,
            'std_breakdown': breakdown,
            'ame_binding': B_ame,
        })

    # For p, n: just chirality residue gives np splitting.  For D+:
    # check if chirality residue + atomic Frobenius co-Casimir extension
    # gives bindings.
    print()
    print("=" * 100)
    print("  Comparison with binding data:")
    print("=" * 100)
    print(f"  {'iso':<8} {'Σ_chir':>10} {'m_e·Σ_3A':>10} {'sum':>10} "
          f"{'AME':>8} {'err %':>8}")
    for r in rows:
        if r['iso'] in ('p (1H)', 'n'):
            continue
        sigma_3A = float(me) * fc.get(r['A'], 0)
        chir = r['chirality_residue_MeV']
        total = chir + sigma_3A  # naive combination
        ame = r['ame_binding']
        if ame > 0:
            err = (total - ame) / ame * 100
            print(f"  {r['iso']:<8} {chir:>+10.4f} {sigma_3A:>+10.4f} "
                  f"{total:>+10.4f} {ame:>+8.4f} {err:>+7.2f}%")

    # np splitting check
    print()
    print(f"  np splitting check:")
    n_chir = next(r['chirality_residue_MeV'] for r in rows if r['iso'] == 'n')
    p_chir = next(r['chirality_residue_MeV'] for r in rows if r['iso'].startswith('p'))
    sigma_3 = float(me) * fc[1]
    delta_pred = sigma_3 + (n_chir - p_chir)  # only the diff for chir
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
        'computation': 'all-isotopes-chirality-residue',
        'description': (
            'Extension of np-splitting chirality-residue framework to '
            'D, T, 3He, 4He.  For each atom, scan atomic braid for '
            'hyperbolic-knot ideals; identify std-channel (chirality) '
            'residues; sum m_e·Vol·|(q;q)_r|.  Combined with atomic '
            'Frobenius co-Casimir Σ_{3A} for binding prediction.'
        ),
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'q_0': Q0_FLOAT,
        'isotopes': rows,
    }
    out = Path(__file__).parent / "all-isotopes-chirality-residue.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")


if __name__ == "__main__":
    main()
