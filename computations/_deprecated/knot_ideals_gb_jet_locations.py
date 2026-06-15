#!/usr/bin/env python3
"""
GB filtration + jet order locations of the hyperbolic knot ideals
appearing in proton/neutron braid trajectories.

For each knot match in the trajectory:
  - GB depth = position in atomic braid (where it starts)
  - GB length = word length
  - Jet order = partition height where its Hecke character dominates
  - Hecke level = strand count (always 3 here)
  - Wedderburn channel = sym (height 0) / std (height 1) / alt (height 2)

The user's hypothesis: the np splitting comes from the EXTRA knot
ideals that the neutron has compared to the proton, and the
specific GB/jet location of those ideals determines their
contribution.

We already found three neutron-only knot ideals:
  pos=1 length=8: 7_7
  pos=2 length=7: 6_3
  pos=3 length=6: 6_1

Now: where do these live in the (GB, jet) structure?
"""
from __future__ import annotations
import sys, json, warnings
from pathlib import Path
from datetime import datetime, timezone

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

import numpy as np
from scipy import sparse as sp_sparse
import mpmath as mp
mp.mp.dps = 25

from q_parameter import Q as Q0_FLOAT, Q_MP, Q_INV_MP
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV
from hecke_characters import partitions_of, build_seminormal_matrices, dim_q

Q0 = Q_MP; QI = Q_INV_MP  # was f64 roundtrip
H_A = Q0 - QI
h_val = float(H_A)


HYPERBOLIC_KNOTS = [
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


def chi_lambda(shape, word):
    sigmas, dim, _ = build_seminormal_matrices(shape)
    if dim == 0:
        return 0.0
    is_sparse = sp_sparse.issparse(sigmas[0]) if sigmas else False
    if is_sparse:
        product = sp_sparse.eye(dim, format='csr')
        I = sp_sparse.eye(dim, format='csr')
    else:
        product = np.eye(dim)
        I = np.eye(dim)
    for w in word:
        idx = abs(w) - 1
        if idx >= len(sigmas):
            continue
        if w > 0:
            M = sigmas[idx]
        else:
            M = sigmas[idx] - h_val * I
        product = product @ M
    return (float(product.diagonal().sum()) if is_sparse
             else float(np.trace(product)))


def jet_order(knot_word):
    """Determine the Wedderburn channel where this knot's character
    is dominant. height(λ) - 1 ∈ {0=sym, 1=std, 2=alt}."""
    best_chi = 0.0
    best_shape = None
    for shape in partitions_of(3):
        chi = chi_lambda(tuple(shape), list(knot_word))
        if abs(chi) > abs(best_chi):
            best_chi = chi
            best_shape = tuple(shape)
    h = len(best_shape) - 1 if best_shape else -1
    channel = {0: "sym", 1: "std", 2: "alt"}.get(h, "?")
    return h, channel, best_chi, best_shape


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
            for knot_name, knot_word, _, vol in knot_db:
                if length != len(knot_word):
                    continue
                if sub in closure_class(knot_word):
                    matches.append({
                        'start': start, 'length': length,
                        'subword': sub, 'knot': knot_name,
                        'volume': vol,
                    })
                    break
    return matches


def main():
    print("=" * 100)
    print("GB filtration / jet order locations of knot ideals (p, n)")
    print("=" * 100)
    print()

    # Pre-compute jet order for each knot in the database
    print(f"  Jet order (Wedderburn channel) for each hyperbolic knot:")
    print(f"  {'knot':<6} {'word':<32} {'Vol':>8} {'height':>7} {'channel':>9} "
          f"{'dim_q dom':>10} {'|χ_max|':>10}")
    knot_jet = {}
    for name, word, n_str, vol in HYPERBOLIC_KNOTS:
        h, ch, chi, shape = jet_order(word)
        dq = float(dim_q(shape)) if shape else 0
        print(f"  {name:<6} {str(list(word)):<32} {vol:>8.3f} {h:>7} {ch:>9} "
              f"{dq:>10.4f} {abs(chi):>10.4f}")
        knot_jet[name] = {
            'jet_height': h,
            'channel': ch,
            'dominant_partition': shape,
            'dominant_dim_q': dq,
        }
    print()

    # Find matches in p and n
    p_word = nucleon_braid_word(['u', 'u', 'd'])
    n_word = nucleon_braid_word(['u', 'd', 'd'])

    p_matches = find_knot_matches(p_word, HYPERBOLIC_KNOTS, min_len=4)
    n_matches = find_knot_matches(n_word, HYPERBOLIC_KNOTS, min_len=4)

    p_set = set((m['start'], m['knot']) for m in p_matches)
    n_set = set((m['start'], m['knot']) for m in n_matches)
    only_n = n_set - p_set
    only_p = p_set - n_set
    shared = p_set & n_set

    print("=" * 100)
    print("  STRUCTURAL FINGERPRINT (GB filtration × jet order × Hecke level)")
    print("=" * 100)
    print()

    def render(label, matches_set, source_matches):
        print(f"  {label}:")
        if not matches_set:
            print(f"    (none)")
            return
        # Map back to full match info
        match_lookup = {(m['start'], m['knot']): m for m in source_matches}
        print(f"    {'GB pos':>7} {'len':>4} {'knot':>6} {'Vol':>8} "
              f"{'jet':>4} {'channel':>9} {'dim_q':>8}")
        for (pos, knot) in sorted(matches_set):
            m = match_lookup.get((pos, knot), {})
            jet = knot_jet.get(knot, {})
            print(f"    {pos:>7} {m.get('length',0):>4} {knot:>6} "
                  f"{m.get('volume',0):>8.3f} "
                  f"{jet.get('jet_height',-1):>4} "
                  f"{jet.get('channel','?'):>9} "
                  f"{jet.get('dominant_dim_q',0):>8.4f}")
        print()

    all_matches = p_matches + n_matches
    render("Shared (both p and n)",  shared, all_matches)
    render("ONLY in NEUTRON",        only_n, n_matches)
    render("ONLY in PROTON",         only_p, p_matches)

    # Now: for the np splitting, look only at the "only in neutron" set
    # and tabulate damping factors by jet × position
    print("=" * 100)
    print("  Neutron-extra knot ideals: (jet × GB-position) damping product")
    print("=" * 100)

    def q_int(n): return float((Q0**n - QI**n) / (Q0 - QI))
    def q_fact(n):
        out = 1.0
        for k in range(2, n+1): out *= q_int(k)
        return out

    print(f"  {'GB pos':>7} {'knot':>6} {'jet':>4} {'channel':>9} "
          f"{'D_pos = 1/[pos+1]_q!':>22} {'D_jet = 1/dim_q':>16} "
          f"{'D_total':>12} {'Vol*D_total':>14}")
    sum_vd = 0.0
    only_n_matches = [m for m in n_matches if (m['start'], m['knot']) in only_n]
    for m in only_n_matches:
        knot = m['knot']
        pos = m['start']
        jet = knot_jet.get(knot, {})
        D_pos = 1.0 / q_fact(pos + 1)
        D_jet = 1.0 / max(jet.get('dominant_dim_q', 1.0), 1e-12)
        D_total = D_pos * D_jet
        vd = m['volume'] * D_total
        sum_vd += vd
        print(f"  {pos:>7} {knot:>6} {jet.get('jet_height',-1):>4} "
              f"{jet.get('channel','?'):>9} "
              f"{D_pos:>22.6e} {D_jet:>16.6f} {D_total:>12.6e} {vd:>14.6f}")
    print()
    print(f"  Σ (Vol · D_total) over neutron-extra knots = {sum_vd:.6f}")
    print(f"  Times m_e = {sum_vd * M_E_MEV:.6f} MeV")
    print(f"  CODATA Δm_{{n−p}} = {M_N_MEV - M_P_MEV:.6f} MeV")
    if sum_vd > 0:
        print(f"  ratio = {(sum_vd * M_E_MEV)/(M_N_MEV - M_P_MEV):.4f}")

    # Save witness
    witness = {
        'computation': 'knot-ideals-gb-jet-locations',
        'description': (
            'For each hyperbolic knot ideal in proton/neutron braid '
            'trajectories, locate it in the (GB filtration position, '
            'jet order = partition height, Wedderburn channel) '
            'structural triple.  Reveal the structural fingerprint of '
            'np splitting via neutron-extra knot ideals.'
        ),
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'q_0': Q0_FLOAT,
        'knot_jet_table': knot_jet,
        'shared_knots': [list(s) for s in sorted(shared)],
        'only_neutron_knots': [list(s) for s in sorted(only_n)],
        'only_proton_knots': [list(s) for s in sorted(only_p)],
        'neutron_extra_sum_vol_damping': sum_vd,
        'codata_np_splitting_MeV': M_N_MEV - M_P_MEV,
    }
    out = Path(__file__).parent / "knot-ideals-gb-jet-locations.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")


if __name__ == "__main__":
    main()
