#!/usr/bin/env python3
"""
MASS FORMULA WITH CURVATURE-RANK STRATIFICATION.

Per prop:curvature-rank-gb-stratification, the six-term mass formula
decomposes by curvature-rank stratum r = 0, 1, 2, ...:

  M = Σ_r m_r · D(r)

where m_r = stratum contribution and D(r) is the GB damping at depth r.

For nucleon braids (proton uud, neutron udd) with our 11-knot
hyperbolic database, we can identify each knot ideal's GB position
(curvature-rank stratum) and Wedderburn channel (jet/sym/std/alt).

The improved mass prediction uses the q-factorial damping
D(r) = 1/[r+1]_q! at each stratum (natural Habiro/cyclotomic
convergence weight) AND the Wedderburn weight w_λ at each jet
channel.  Combined:

  Δ(K_r,λ) = m_e · Vol(K_r,λ) · 1/[r+1]_q! · w_λ

For each isotope, sum over all knot-ideals in the trajectory.

Combined with the strict-derived baseline (Z*m_p + N*m_n + Z*m_e
+ alpha*(Phi_1 - 2[3]_q*Phi_2 + H_A^2*Phi_3) + Wigner T=0 + T=1),
this should bridge the binding gap structurally.
"""
from __future__ import annotations
import sys, json, warnings
from pathlib import Path
from datetime import datetime, timezone

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

import mpmath as mp
mp.mp.dps = 30

from hecke_core import (h as H_A_F, z as Z_MARKOV, _step_chain_generic)
from q_parameter import Q as Q0_FLOAT, Q_MP, Q_INV_MP
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV

Q0 = Q_MP; QI = Q_INV_MP  # was f64 roundtrip
H_A = Q0 - QI
me = mp.mpf(str(M_E_MEV))
z_m = mp.mpf(str(float(Z_MARKOV)))
G = mp.catalan
alpha_bind = me * 8 * G
q3_q = Q0**2 + 1 + QI**2
q2_q = Q0 + QI
HA2 = H_A**2
Wigner_unit = me * q3_q * q2_q**2

# Hyperbolic knots database (with channel from gb_hyperbolic_knot_levels.py)
HYPERBOLIC_KNOTS = [
    # (name, word, vol, jet_channel)  — jet_channel in {0=sym, 1=std, 2=alt}
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


def q_int(n):
    return (Q0**n - QI**n) / (Q0 - QI)


def q_factorial(n):
    out = mp.mpf(1)
    for k in range(2, n+1):
        out *= q_int(k)
    return out


def b3_braid_word():
    return (1, -2, 1, -2, 1, -2)


def nucleon_braid_word(quark_types):
    word = list(b3_braid_word())
    for i in range(3):
        for j in range(i + 1, 3):
            gen = min(i + 1, 2)
            t_i, t_j = quark_types[i], quark_types[j]
            if t_i == t_j == 'u':
                word.append(gen)
            elif t_i == t_j == 'd':
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


def find_knot_matches(word, knot_db, min_len=4):
    n = len(word)
    matches = []
    for start in range(n):
        for length in range(min_len, n - start + 1):
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


def stratum_contribution(matches, mode):
    """Sum knot contributions weighted by curvature-rank damping."""
    total = mp.mpf(0)
    breakdown = {}
    for m in matches:
        r = m['start']  # curvature-rank = GB position
        ch = m['channel']
        if mode == 'qfac':
            D_pos = 1 / q_factorial(r + 1)
        elif mode == 'qpoch':
            # (q;q)_r damping (decreasing)
            D_pos = mp.mpf(1)
            for k in range(1, r + 2):
                D_pos *= mp.fabs(1 - Q0**k)
        elif mode == 'qint':
            D_pos = 1 / q_int(r + 1)
        else:
            D_pos = mp.mpf(1)
        # Channel/jet damping: w_λ at q_0
        # sym (0): q²/D, std (1): (q²+1)²/D, alt (2): q²/D
        D_q4_4q2_1 = Q0**4 + 4*Q0**2 + 1
        if ch == 0:
            D_jet = Q0**2 / D_q4_4q2_1
        elif ch == 1:
            D_jet = (Q0**2 + 1)**2 / D_q4_4q2_1
        else:
            D_jet = Q0**2 / D_q4_4q2_1
        contrib = me * mp.mpf(str(m['volume'])) * D_pos * D_jet
        total += contrib
        key = (r, m['knot'])
        breakdown[key] = float(contrib)
    return float(total), breakdown


def main():
    print("=" * 100)
    print("CURVATURE-RANK STRATIFIED MASS FORMULA")
    print("=" * 100)
    print(f"  q_0 = {Q0_FLOAT}")
    print()

    # All isotopes
    AME_BIND = {'D': 2.22456612, 'T': 8.481798,
                 '³He': 7.718058, '⁴He': 28.29566,
                 '⁶Li': 31.99405, '⁷Li': 39.24454}
    M_H_ATOMIC = M_P_MEV + M_E_MEV
    isotopes = [
        ('p (1H)', ['u','u','d'],  1, 0, M_H_ATOMIC, 0.0),
        ('n',       ['u','d','d'], 0, 1, M_N_MEV, 0.0),
    ]

    # First: tabulate p, n curvature-rank knot-ideal trajectories
    print("  Curvature-rank trajectory of nucleon braids:")
    print(f"  {'iso':<8} {'r=':>2} {'pos':>4} {'knot':>6} {'Vol':>8} "
          f"{'channel':>8} {'1/[r+1]_q!':>12} {'w_λ':>8} {'contrib':>12}")
    for name, qtypes, Z, N, _, _ in isotopes:
        word = nucleon_braid_word(qtypes)
        matches = find_knot_matches(word, HYPERBOLIC_KNOTS)
        for m in matches:
            r = m['start']
            ch = m['channel']
            D_pos = float(1 / q_factorial(r + 1))
            ch_name = ['sym', 'std', 'alt'][ch]
            D_q4 = float(Q0**4 + 4*Q0**2 + 1)
            if ch == 0 or ch == 2:
                w_lam = float(Q0**2) / D_q4
            else:
                w_lam = float((Q0**2 + 1)**2) / D_q4
            contrib = float(me) * m['volume'] * D_pos * w_lam
            print(f"  {name:<8} {r:>2} {r:>4} {m['knot']:>6} {m['volume']:>8.3f} "
                  f"{ch_name:>8} {D_pos:>12.6e} {w_lam:>8.4f} {contrib:>12.6f}")
    print()

    # np splitting via curvature-rank stratification (only neutron-extra)
    print("=" * 100)
    print("  np splitting from neutron-only knot ideals (curvature-rank weighted)")
    print("=" * 100)
    p_word = nucleon_braid_word(['u','u','d'])
    n_word = nucleon_braid_word(['u','d','d'])
    p_matches = find_knot_matches(p_word, HYPERBOLIC_KNOTS)
    n_matches = find_knot_matches(n_word, HYPERBOLIC_KNOTS)
    p_set = set((m['start'], m['knot']) for m in p_matches)
    n_set = set((m['start'], m['knot']) for m in n_matches)
    only_n = n_set - p_set
    only_n_matches = [m for m in n_matches if (m['start'], m['knot']) in only_n]
    print(f"  Neutron-extra knot ideals: {[(m['start'], m['knot']) for m in only_n_matches]}")
    print()
    for mode in ['qfac', 'qpoch', 'qint']:
        total, breakdown = stratum_contribution(only_n_matches, mode)
        codata = M_N_MEV - M_P_MEV
        err = (total - codata) / codata * 100
        print(f"  Mode '{mode}': Σ m_e·Vol·D = {total:+.6f} MeV "
              f"(CODATA Δm = {codata:.4f}, err {err:+.2f}%)")
        for key, val in breakdown.items():
            print(f"    r={key[0]} {key[1]}: {val:+.6f} MeV")
    print()

    # Save witness
    witness = {
        'computation': 'curvature-rank-mass',
        'description': (
            'Apply curvature-rank stratification (prop:curvature-rank-'
            'gb-stratification) to mass prediction.  Each hyperbolic-'
            'knot ideal at curvature-rank r contributes m_e * Vol(K) * '
            '1/[r+1]_q! * w_lambda (Wedderburn weight at jet channel).'
        ),
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'q_0': Q0_FLOAT,
        'codata_np_splitting': M_N_MEV - M_P_MEV,
    }
    out = Path(__file__).parent / "curvature-rank-mass.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")


if __name__ == "__main__":
    main()
