#!/usr/bin/env python3
"""
HECKE KNOT-IDEAL TRACKER — track when ideals' leading words are
hyperbolic knot braids, distinguishing proton from neutron.

User direction: in the GB filtration of H_n(q), look for ideals
whose left part (leading word) matches a hyperbolic knot.  The
filtration level provides the dampening factor for that knot's
contribution.  See if the trajectory of knot-ideals separates
proton (uud) from neutron (udd).

This script:
  1. Loads canonical hyperbolic knot braid representatives.
  2. For each proton/neutron braid word, scans all SUB-WORDS (sliding
     windows of length 4..9) to find matches against the knot
     database (modulo cyclic + reversal + Markov destabilization
     equivalences for the closure).
  3. Tags each match with (start, length, knot, hyperbolic_volume).
  4. Reports the difference in knot trajectories between proton and
     neutron — does the neutron pass through specific hyperbolic
     knots that the proton doesn't?

Output: structural fingerprint of p vs n at the knot-ideal level.
"""
from __future__ import annotations
import sys, json, warnings
from pathlib import Path
from datetime import datetime, timezone

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

import mpmath as mp
mp.mp.dps = 25

from q_parameter import Q as Q0_FLOAT, Q_MP, Q_INV_MP
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV

Q0 = Q_MP; QI = Q_INV_MP  # was f64 roundtrip
H_A = Q0 - QI


# Hyperbolic knot braid representatives (B_3, signed integer notation).
HYPERBOLIC_KNOTS = [
    # name, braid_word, n_strands, hyperbolic_volume
    ("4_1",  (1, -2, 1, -2),                         3, 2.0298832),
    ("5_2",  (1, 1, 1, -2, 1, -2),                   3, 2.8281220),
    ("6_1",  (1, 1, -2, 1, -2, -2),                  3, 3.1639633),
    ("6_2",  (1, 1, 1, -2, 1, -2, -2),               3, 4.4015175),
    ("6_3",  (1, 1, -2, 1, -2, 1, -2),               3, 5.6927297),
    ("7_2",  (1, 1, 1, 1, 1, -2, 1, -2),             3, 3.3317442),
    ("7_3",  (1, 1, 1, 1, -2, 1, 1, -2),             3, 4.5921326),
    ("7_4",  (1, 1, -2, 1, -2, -2, -2),              3, 5.0136959),
    ("7_5",  (1, 1, 1, 1, -2, 1, 1, 1, -2),          3, 6.4439185),
    ("7_6",  (1, 1, 1, -2, 1, -2, -2, -2),           3, 7.0846178),
    ("7_7",  (1, 1, -2, 1, -2, 1, -2, -2),           3, 7.6433568),
]


def cyclic_shifts(word):
    """All cyclic shifts of a tuple."""
    n = len(word)
    return [tuple(word[i:] + word[:i]) for i in range(n)]


def reversed_word(word):
    """Reversed braid word (closure-equivalent)."""
    return tuple(reversed(word))


def conjugate_classes(word):
    """All braid words in the same closure-equivalence class
    (cyclic shifts + reversal)."""
    classes = set()
    for shift in cyclic_shifts(word):
        classes.add(shift)
        classes.add(reversed_word(shift))
    return classes


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


def find_knot_matches(word, knot_db, min_len=4):
    """Find all sub-words of `word` (any length ≥ min_len) that
    match a hyperbolic knot braid (modulo cyclic + reversal
    closure equivalence).

    Returns list of (start, length, knot_name, vol).
    """
    n = len(word)
    matches = []
    for start in range(n):
        for length in range(min_len, n - start + 1):
            sub = tuple(word[start:start + length])
            for knot_name, knot_word, _, vol in knot_db:
                if length != len(knot_word):
                    continue
                if sub in conjugate_classes(knot_word):
                    matches.append({
                        'start': start, 'length': length,
                        'subword': sub, 'knot': knot_name,
                        'volume': vol,
                    })
                    break
    return matches


def damping_at_position(start, length, n_total):
    """A knot at position `start` with length `length` in a total
    braid of length `n_total` is "dampened" by its position in the
    GB filtration.  Use level = start (depth at which the knot
    starts).  Damping = 1/[level+1]_q!"""
    def q_int(n):
        return float((Q0**n - QI**n) / (Q0 - QI))
    def q_fact(n):
        out = 1.0
        for k in range(2, n+1):
            out *= q_int(k)
        return out
    return 1.0 / q_fact(start + 1) if start >= 0 else 1.0


def main():
    print("=" * 100)
    print("HECKE KNOT-IDEAL TRACKER — proton vs neutron knot trajectories")
    print("=" * 100)
    print(f"  q_0 = {Q0_FLOAT}")
    print()

    p_word = nucleon_braid_word(['u', 'u', 'd'])
    n_word = nucleon_braid_word(['u', 'd', 'd'])
    print(f"  Proton  braid: {list(p_word)}  (length {len(p_word)})")
    print(f"  Neutron braid: {list(n_word)}  (length {len(n_word)})")
    print()

    # Find knot matches in each
    for name, word in [("PROTON", p_word), ("NEUTRON", n_word)]:
        print(f"  {name} knot trajectory:")
        matches = find_knot_matches(word, HYPERBOLIC_KNOTS, min_len=4)
        if not matches:
            print(f"    (no hyperbolic knot sub-words found)")
        else:
            print(f"    {'pos':>4} {'len':>4} {'knot':>6} {'Vol':>10} "
                  f"{'damp 1/[pos+1]_q!':>20} {'sub-word':<30}")
            for m in matches:
                damp = damping_at_position(m['start'], m['length'], len(word))
                print(f"    {m['start']:>4} {m['length']:>4} {m['knot']:>6} "
                      f"{m['volume']:>10.4f} {damp:>20.6e} {str(list(m['subword'])):<30}")
            # Aggregate volume·damping
            total_v_damp = sum(
                m['volume'] * damping_at_position(m['start'], m['length'], len(word))
                for m in matches
            )
            print(f"    Σ Vol · damping = {total_v_damp:.6f}")
        print()

    # Compare neutron - proton
    p_matches = find_knot_matches(p_word, HYPERBOLIC_KNOTS, min_len=4)
    n_matches = find_knot_matches(n_word, HYPERBOLIC_KNOTS, min_len=4)
    p_signature = sorted([(m['start'], m['knot']) for m in p_matches])
    n_signature = sorted([(m['start'], m['knot']) for m in n_matches])

    print("=" * 100)
    print("  Difference: neutron knot trajectory MINUS proton")
    print("=" * 100)

    p_set = set(p_signature)
    n_set = set(n_signature)
    only_p = p_set - n_set
    only_n = n_set - p_set
    shared = p_set & n_set

    print(f"  Shared knot-ideals: {sorted(shared)}")
    print(f"  Only in proton:    {sorted(only_p)}")
    print(f"  Only in neutron:   {sorted(only_n)}")

    # Volume-difference contribution
    def sig_total_damp(matches):
        return sum(m['volume'] * damping_at_position(m['start'], m['length'], 9)
                   for m in matches)

    p_total = sig_total_damp(p_matches)
    n_total = sig_total_damp(n_matches)
    print()
    print(f"  Proton  Σ(Vol · damping) = {p_total:.6f}")
    print(f"  Neutron Σ(Vol · damping) = {n_total:.6f}")
    print(f"  Difference (n − p)        = {n_total - p_total:+.6f}")
    print(f"  Times m_e                 = {(n_total - p_total) * M_E_MEV:+.6f} MeV")
    print(f"  CODATA Δm_{{n−p}}           = {M_N_MEV - M_P_MEV:+.6f} MeV")

    # Save
    witness = {
        'computation': 'hecke-knot-ideal-tracker',
        'description': (
            'Track hyperbolic-knot braid words appearing as sub-words '
            'of proton and neutron atomic braids.  Each match is an '
            'ideal in the GB filtration whose left part is a known '
            'hyperbolic knot.  Compare trajectories between p and n '
            'to look for structural distinction.'
        ),
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'q_0': Q0_FLOAT,
        'proton_word': list(p_word),
        'neutron_word': list(n_word),
        'proton_matches': p_matches,
        'neutron_matches': n_matches,
        'proton_total_vol_damping': p_total,
        'neutron_total_vol_damping': n_total,
        'shared_knots': [list(s) for s in sorted(shared)],
        'only_proton': [list(s) for s in sorted(only_p)],
        'only_neutron': [list(s) for s in sorted(only_n)],
    }
    out = Path(__file__).parent / "hecke-knot-ideal-tracker.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")


if __name__ == "__main__":
    main()
