#!/usr/bin/env python3
"""
Distance-weighted brane tower — non-adjacent pair contributions
with GB-filtration-level suppression.

Per user's structural insight (2026-04-24): "non-adjacent go up GB
filtration b/c more crossing".  A pair of generators separated by
distance d in the braid carries d intermediate crossings that must
be traversed.  This places the pair at jet level d (not level 1),
so the suppression is ℏ_q^(2d) → equivalently z^(2d) in the
Jones-Ocneanu Markov normalisation.

Original paper's brane tower formula (prop:mass-endomorphism-tower)
has:
  tower_pair = z² · Σ_{|i-j|=1} Φ_q(|V̂_i V̂_j|)

Extended (distance-weighted):
  tower_pair_ext = Σ_{d=1}^{n-1} z^(2d) · Σ_{|i-j|=d} Φ_q(|V̂_i V̂_j|)

This script computes both and reports the additional contribution
from non-adjacent pairs.  KEPT FOR FUTURE ACCURACY IMPROVEMENTS —
not currently used in authoritative mass predictions because
(a) the contributions are small relative to the neutron-tower gap,
(b) paper's canonical brane tower formula still restricts to
    adjacent pairs.

Once the neutron tower's factor-2 structural gap is resolved,
this non-adjacent correction becomes relevant for sub-ppm accuracy
on isotope bindings.
"""
from __future__ import annotations
import sys, json, warnings
from pathlib import Path
from datetime import datetime, timezone

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

import mpmath as mp
mp.mp.dps = 50

from hecke_core import atom_per_generator_volumes, z as Z_MARKOV
from q_parameter import Q as Q0_FLOAT, Q_MP, Q_INV_MP
from experimental_constants import M_E_MEV

Q0 = Q_MP; QI = Q_INV_MP  # was f64 roundtrip
z_m = mp.mpf(str(float(Z_MARKOV)))
me = mp.mpf(str(M_E_MEV))


def Phi_q(v, max_iter=3000):
    if not isinstance(v, mp.mpf):
        v = mp.mpf(str(float(v)))
    prod = mp.mpf(1)
    coef = mp.mpf(1) / Q0
    for _ in range(1, max_iter + 1):
        term = mp.mpf(1) - coef * v
        if abs(term) < mp.mpf("1e-40"):
            return mp.mpc("inf")
        prod /= term
        if abs(coef * v) < mp.mpf("1e-60"):
            break
        coef /= Q0
    return prod


def distance_weighted_brane_pair_tower(V_arr: list) -> dict:
    """Compute Σ_d z^(2d) · Σ_{|i-j|=d} Φ_q(|V̂_i V̂_j|) decomposed by d."""
    abs_V = [mp.fabs(mp.mpf(str(float(v)))) for v in V_arr]
    n = len(abs_V)
    per_d = {}
    total_weighted = mp.mpf(0)
    for d in range(1, n):
        pair_sum = mp.mpf(0)
        count = 0
        for i in range(n - d):
            j = i + d
            prod_ij = abs_V[i] * abs_V[j]
            if prod_ij < 1:
                pair_sum += Phi_q(prod_ij)
                count += 1
        w = z_m ** (2 * d)
        weighted = w * pair_sum
        per_d[d] = {
            'distance': d,
            'pair_count': count,
            'z_power_2d': float(w),
            'raw_sum': float(pair_sum),
            'weighted': float(weighted),
        }
        total_weighted += weighted
    return {
        'per_distance': per_d,
        'adj_only': per_d.get(1, {}).get('weighted', 0),
        'extended_total': float(total_weighted),
        'extra_from_non_adjacent': float(total_weighted - per_d.get(1, {}).get('weighted', 0)),
    }


def main() -> int:
    print("=" * 100)
    print("DISTANCE-WEIGHTED NON-ADJACENT BRANE TOWER")
    print("=" * 100)
    print(f"  q_0 = {Q0_FLOAT}")
    print(f"  z  = {float(z_m):.6f}")
    print(f"  (z^(2d) suppression at distance d — GB filtration level)")
    print()

    results = []
    for name, Z, N in [('proton', 1, 0), ('neutron', 0, 1),
                        ('D', 1, 1), ('T', 1, 2), ('³He', 2, 1)]:
        V = [d['full'] for d in atom_per_generator_volumes(Z, N)]
        ext = distance_weighted_brane_pair_tower(V)
        print(f"  ── {name} (Z={Z}, N={N}, n_gens={len(V)}) ──")
        print(f"  {'d':<3} {'#pairs':>6} {'z^(2d)':>14} {'raw sum':>14} {'weighted':>14}")
        for d, info in ext['per_distance'].items():
            print(f"  {d:<3} {info['pair_count']:>6} {info['z_power_2d']:>14.4e} "
                  f"{info['raw_sum']:>14.2f} {info['weighted']:>14.4f}")
        print(f"  Total distance-weighted: {ext['extended_total']:.4f}")
        print(f"  Adjacent-only (original):{ext['adj_only']:.4f}")
        print(f"  Extra from non-adj:     {ext['extra_from_non_adjacent']:+.4f}")
        print()
        results.append({'particle': name, 'Z': Z, 'N': N, 'n_gens': len(V),
                         'extended': ext})

    witness = {
        'computation': 'brane-tower-distance-weighted',
        'description': (
            "Distance-weighted non-adjacent brane tower pair "
            "contributions.  Each pair at distance d gets z^(2d) "
            "suppression reflecting the GB filtration level (d "
            "intermediate crossings between the two generators).  "
            "Preserved for future accuracy improvement; small "
            "contribution relative to the neutron-tower structural "
            "gap in current framework."
        ),
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'q_0': Q0_FLOAT,
        'z_markov': float(z_m),
        'results': results,
        'status': 'preserved — not used in authoritative predictions '
                   'pending neutron-tower gap resolution',
    }
    out = Path(__file__).parent / "brane-tower-distance-weighted.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
