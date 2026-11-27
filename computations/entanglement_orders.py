#!/usr/bin/env python3
"""
Track entanglement energy at multiple orders (GB filtration levels):

Order 0: |Π V̂_i|                            — direct product, no entanglement
Order 1: Σ Φ_q(|V̂_i|)                       — single-gen self-entanglement
Order 2: z² · Σ_{|i-j|=1} Φ_q(|V̂_i V̂_j|)   — adjacent pair (current formula)
Order 2': z^(2d) · Σ_{|i-j|=d} (d≥2)        — distance-weighted non-adjacent
Order 3: z^? · Σ_triples Φ_q(|V̂_i V̂_j V̂_k|)  — triple entanglement
Order 4: z^? · Σ_quads                       — quadruple
…

Each order's contribution should be SUPPRESSED by ℏ_q^(2k) or z^(2k)
per GB filtration level k.

This script computes all orders up to n_gens for p, n, D, T, ³He and
reports per-order contributions.  Goal: see whether higher orders
carry enough entanglement energy to close the neutron-tower gap.
"""
from __future__ import annotations
import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys, json, warnings
from pathlib import Path
from datetime import datetime, timezone
from itertools import combinations

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

import mpmath as mp
from _precision import set_compute_dps, fmt  # noqa: E402
set_compute_dps()

from hecke_core import atom_per_generator_volumes, z as Z_MARKOV
from q_parameter import Q as Q0_FLOAT, Q_MP, Q_INV_MP
from experimental_constants import M_E_MEV

Q0 = Q_MP; QI = Q_INV_MP  # was f64 roundtrip
z_m = mp.mpf(str(float(Z_MARKOV)))
me = mp.mpf(str(M_E_MEV))


def Phi_q(v, max_it=3000):
    if not isinstance(v, mp.mpf):
        v = mp.mpf(str(float(v)))
    if v >= 1:
        return mp.mpf('inf')
    prod = mp.mpf(1); coef = mp.mpf(1)/Q0
    for _ in range(1, max_it+1):
        t = mp.mpf(1) - coef*v
        if abs(t) < mp.mpf('1e-40'):
            return mp.mpf('inf')
        prod /= t
        if abs(coef*v) < mp.mpf('1e-60'):
            break
        coef /= Q0
    return prod


def entanglement_orders(V_arr: list, max_order: int = None) -> dict:
    """Compute entanglement at each GB filtration order 0..max_order.

    Order 0: |ΠV̂_i| (base)
    Order k (k≥1): Σ over k-subsets (i_1 < i_2 < ... < i_k) of
                   Φ_q(|V̂_{i_1} · ... · V̂_{i_k}|) ·
                   z^(2·max_distance_in_subset)
    where max_distance_in_subset = max(i_j - i_{j-1}) over consecutive pairs.
    For adjacent orders (k=1 single-gen, k=2 adjacent pair) this reduces
    to the paper's tower.
    """
    abs_V = [mp.fabs(mp.mpf(str(float(v)))) for v in V_arr]
    n = len(abs_V)
    if max_order is None:
        max_order = n

    orders = {}
    # Order 0: direct product
    prod = mp.mpf(1)
    for v in abs_V: prod *= v
    orders[0] = {'contribution': float(prod), 'n_terms': 1,
                  'description': '|ΠV̂_i|'}

    # Orders 1..n: k-subsets with GB-filtration weighting
    for k in range(1, max_order + 1):
        if k > n: break
        level_sum = mp.mpf(0)
        n_terms = 0
        for subset in combinations(range(n), k):
            # Product of V̂ over subset
            pv = mp.mpf(1)
            for i in subset: pv *= abs_V[i]
            if pv >= 1:
                continue   # past pole
            phi = Phi_q(pv)
            # GB filtration level: span of subset
            if k >= 2:
                span = max(subset) - min(subset)
                z_weight = z_m ** (2 * span)
            else:
                z_weight = mp.mpf(1)
            level_sum += z_weight * phi
            n_terms += 1
        orders[k] = {
            'contribution': float(level_sum),
            'n_terms': n_terms,
            'description': f'Σ_{{k={k}-subset}} z^(2·span) · Φ_q(Π V̂_i)',
        }
    return orders


print("=" * 100)
print("ENTANGLEMENT ORDERS — track contributions by GB filtration level")
print("=" * 100)
print(f"  q_0 = {float(Q0):.8f}, z = {float(z_m):.6f}")
print(f"  ℏ_q² = {float(((Q0-1)/Q0)**2):.6e}, z² = {float(z_m*z_m):.6f}")
print()

particle_data = []
for name, Z, N in [('proton', 1, 0), ('neutron', 0, 1),
                       ('D', 1, 1), ('T', 1, 2), ('³He', 2, 1)]:
    V_arr = [d['full'] for d in atom_per_generator_volumes(Z, N)]
    n_gens = len(V_arr)
    print(f"  ── {name} (Z={Z}, N={N}, n_gens={n_gens}) ──")
    V_str = ", ".join(f"{float(v):.4f}" for v in V_arr)
    print(f"  V̂_i = [{V_str}]")
    orders = entanglement_orders(V_arr)
    total = mp.mpf(0)
    print(f"  {'order':<6} {'n_terms':>8} {'contribution':>18} {'cumsum':>18}")
    for k, info in orders.items():
        total += mp.mpf(info['contribution'])
        print(f"  {k:<6} {info['n_terms']:>8} {info['contribution']:>18.4f} "
              f"{float(total):>18.4f}")
    print()
    particle_data.append({
        'particle': name, 'Z': Z, 'N': N, 'n_gens': n_gens,
        'orders': orders,
        'total': float(total),
    })

# Convert cat to MeV using calibration
# Take proton total as baseline
m_p_cat = next(p['total'] for p in particle_data if p['particle']=='proton')
from experimental_constants import M_P_MEV, M_N_MEV
calib = M_P_MEV / m_p_cat
print(f"  Calibration: E_0 = m_p_CODATA / proton_total_cat = {float(calib):.6e} MeV/cat")
print()
print(f"  Predicted masses (all orders, MeV):")
for p in particle_data:
    name = p['particle']
    m_MeV = p['total'] * calib
    ref = M_P_MEV if name == 'proton' else M_N_MEV if name == 'neutron' else None
    if ref:
        err = (m_MeV - ref) / ref * 100
        print(f"    {name:<8}: {float(m_MeV):.4f} MeV  (CODATA {ref}, err {float(err):+.3f}%)")
    else:
        print(f"    {name:<8}: {float(m_MeV):.4f} MeV  (atomic, not direct comparison)")

# Save witness
witness = {
    "computation": "entanglement-orders",
    "description": (
        "Entanglement energy tracked at all GB filtration orders "
        "(k = 0, 1, 2, ..., n_gens).  Each k-subset contribution "
        "weighted by z^(2·span) where span = max(i) - min(i) of the "
        "subset, reflecting the total number of crossings the "
        "k-entanglement spans."
    ),
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "q_0": Q0_FLOAT,
    "z": float(z_m),
    "calibration_MeV_per_cat": calib,
    "particles": particle_data,
}
from witness_base import WitnessBuilder  # noqa: E402 — P30 staleness triple
WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__)  # scriptHash/scriptCommitSha
witness["scriptFile"] = Path(__file__).name
out = Path(__file__).parent / "entanglement-orders.witness.json"
out.write_text(json.dumps(witness, indent=2, default=str))
print(f"\n  Witness: {out}")
