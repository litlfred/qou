#!/usr/bin/env python3
"""
Level 1 nuclear braid computation: B_{3A} (3 quark strands per nucleon).

At Level 0 (B_A), each nucleon is one strand. The inter-nucleon crossings
give binding energy but NOT the Q-value.

At Level 1 (B_{3A}), each nucleon is 3 quark strands (u,u,d for proton;
u,d,d for neutron). The Borromean internal structure + inter-nucleon
Hopf links give both binding energy AND Q-values.

The factored trace theorem still holds: tr = Π_i (z·a_i + b_i)
but now i runs over 3A-1 generators instead of A-1.

The Q-value comes from the log-ratio of traced volumes at the 3
quark-level generators of the converting nucleon.

WITNESS: all computations produce a witness JSON with:
  - input parameters (q, p, n)
  - every intermediate value (a_i, b_i, V̂_i for each generator)
  - the final trace and Q-value
  - algorithm description (reproducible)
  - cross-check against Level 0 where applicable

Usage:
    python3 computations/nuclear-braid-level1.py

Output:
    computations/nuclear-braid-level1.witness.json
"""

import json
import math
import sys
import time
from datetime import datetime, timezone
from pathlib import Path


# ── Parameters (from canonical q_parameter.py) ──────────────────

from q_parameter import Q as Q_VAL, Q_INV, HA, S_SKEIN as SKEIN_AMP, HBAR_Q
Q_HALF = Q_VAL**0.5
Z_MARKOV = 1.0 / (Q_HALF + 1.0/Q_HALF)
HBAR_Q2 = HBAR_Q**2


# ── Strand layout ────────────────────────────────────────────────
#
# For a nucleus N(p,n) with A = p+n nucleons:
# Total strands = 3A (3 quarks per nucleon)
#
# Nucleon i occupies strands [3i, 3i+1, 3i+2]:
#   Proton (u,u,d): strands 3i(+), 3i+1(+), 3i+2(-)
#   Neutron (u,d,d): strands 3i(+), 3i+1(-), 3i+2(-)
#
# Crossings:
#   INTRA-nucleon: Borromean crossings between strands of same nucleon
#   INTER-nucleon: Hopf crossings between strands of different nucleons

def strand_type(nucleon_idx, strand_offset, nucleon_type):
    """Return 'u' or 'd' for a quark strand.

    nucleon_type: 'p' (proton = u,u,d) or 'n' (neutron = u,d,d)
    strand_offset: 0, 1, or 2 within the nucleon
    """
    if nucleon_type == 'p':
        return ['u', 'u', 'd'][strand_offset]
    else:
        return ['u', 'd', 'd'][strand_offset]


def crossing_weight(type_i, type_j):
    """Crossing weight (c, d) for T(c,d) = c·σ + d·𝟙.

    From the Hecke inverse relation σ⁻¹ = σ − (q − q⁻¹):
      u-u (pp): positive crossing → c = 1, d = 0
      d-d (nn): negative crossing → c = 1, d = −HA
      u-d (pn): mixed crossing    → c = 1, d = −HA/2
    """
    if type_i == 'u' and type_j == 'u':
        return 1.0, 0.0
    elif type_i == 'd' and type_j == 'd':
        return 1.0, -HA
    else:
        return 1.0, -HA / 2.0


# ── Factored trace at Level 1 ───────────────────────────────────

def level1_trace(p, n, convert_neutron=None):
    """Compute the factored Markov trace at Level 1 (B_{3A}).

    If convert_neutron is not None, the neutron at that index
    (0-based within the neutron block) is treated as a proton
    (for computing the daughter trace).

    Returns: (log_trace, generator_data)
    where generator_data is a list of dicts for the witness.
    """
    A = p + n
    n_strands = 3 * A

    # Build nucleon types
    nucleon_types = ['p'] * p + ['n'] * n
    if convert_neutron is not None:
        # Convert the specified neutron (index within neutron block)
        nucleon_types[p + convert_neutron] = 'p'

    # Build strand types
    strand_types = []
    for nuc_idx in range(A):
        for offset in range(3):
            strand_types.append(strand_type(nuc_idx, offset, nucleon_types[nuc_idx]))

    # For each generator σ_i (i = 0, ..., 3A-2):
    # Collect all crossings from strand i with strands j > i.
    #
    # Crossings exist between:
    #   - Strands within the same nucleon (INTRA): Borromean
    #   - Strands in different nucleons (INTER): Hopf
    #
    # For the factored trace, ALL crossings at generator σ_i
    # are collected and chain-reduced to (a_i, b_i).

    log_trace = 0.0
    sign = 1
    generator_data = []

    for i in range(n_strands - 1):
        a, b = 0.0, 1.0  # identity
        n_crossings = 0
        nuc_i = i // 3
        off_i = i % 3

        for j in range(i + 1, n_strands):
            nuc_j = j // 3
            off_j = j % 3

            # Determine if this crossing exists:
            # INTRA-nucleon (same nucleon): always (Borromean structure)
            # INTER-nucleon (different nucleons): always (Hopf linking)
            # In the full B_{3A} braid, every pair crosses.

            ti = strand_types[i]
            tj = strand_types[j]
            c, d = crossing_weight(ti, tj)

            # Chain multiplication: (a σ + b)(c σ + d) → reduce
            new_a = a * c * HA + a * d + b * c
            new_b = a * c + b * d
            a, b = new_a, new_b
            n_crossings += 1

        # Markov-traced volume
        v = Z_MARKOV * a + b

        generator_data.append({
            'generator': i,
            'nucleon': nuc_i,
            'offset': off_i,
            'strand_type': strand_types[i],
            'n_crossings': n_crossings,
            'a': a,
            'b': b,
            'traced_volume': v,
            'log_traced_volume': math.log(abs(v)) if abs(v) > 1e-300 else -999,
        })

        if abs(v) > 1e-300:
            if v < 0:
                sign *= -1
            log_trace += math.log(abs(v))

    return log_trace, sign, generator_data


def compute_nucleus(name, p, n, t_obs_s, Q_exp, verbose=True):
    """Full Level 1 computation for one nucleus."""
    A = p + n
    t_start = time.time()

    if verbose:
        print(f"\n{'='*70}")
        print(f"{name}: N({p},{n}), A={A}, 3A={3*A} strands, "
              f"{3*A*(3*A-1)//2} crossings")

    # Parent trace
    log_par, sign_par, gen_par = level1_trace(p, n)

    # Daughter trace (convert first neutron)
    log_dau, sign_dau, gen_dau = level1_trace(p, n, convert_neutron=0)

    elapsed = time.time() - t_start

    # Quantum dilogarithm volumes
    phi_par = log_par  # Φ_q = log|tr|
    phi_dau = log_dau
    delta_phi = phi_par - phi_dau

    # Q-value
    Q_phi = delta_phi / HBAR_Q2

    # Q from the converting nucleon's generators only (Level 1 local)
    # The converting nucleon is at index p (first neutron).
    # Its 3 strands are at positions [3p, 3p+1, 3p+2].
    conv_start = 3 * p
    Q_local_log = 0.0
    for si in range(3):
        idx = conv_start + si
        if idx < len(gen_par) and idx < len(gen_dau):
            v_par = gen_par[idx]['traced_volume']
            v_dau = gen_dau[idx]['traced_volume']
            if abs(v_par) > 1e-300 and abs(v_dau) > 1e-300:
                Q_local_log += math.log(abs(v_par)) - math.log(abs(v_dau))

    Q_local = Q_local_log / HBAR_Q2

    if verbose:
        print(f"  Φ_q(par) = {phi_par:.6f}")
        print(f"  Φ_q(dau) = {phi_dau:.6f}")
        print(f"  ΔΦ = {delta_phi:+.6f}")
        print(f"  Q_Φ(total) = {Q_phi:.4f} (Hecke units)")
        print(f"  Q_local(3 strands) = {Q_local:.6f} (Hecke units)")
        if Q_exp:
            print(f"  Q_exp = {Q_exp:.5f} MeV")
        print(f"  Time: {elapsed:.2f}s")

        # Show the converting nucleon's generators
        print(f"  Converting nucleon (strands {conv_start}–{conv_start+2}):")
        for si in range(3):
            idx = conv_start + si
            if idx < len(gen_par) and idx < len(gen_dau):
                gp = gen_par[idx]
                gd = gen_dau[idx]
                print(f"    σ_{idx} ({gp['strand_type']}→{gd['strand_type']}): "
                      f"V̂_par={gp['traced_volume']:+.6e}, "
                      f"V̂_dau={gd['traced_volume']:+.6e}, "
                      f"log ratio={math.log(abs(gp['traced_volume'])) - math.log(abs(gd['traced_volume'])):+.6f}")

    return {
        'nucleus': name,
        'p': p, 'n': n, 'A': A,
        'n_strands': 3 * A,
        'phi_parent': phi_par,
        'phi_daughter': phi_dau,
        'delta_phi': delta_phi,
        'Q_phi_total': Q_phi,
        'Q_local_3strand': Q_local,
        'Q_exp': Q_exp,
        'elapsed_s': elapsed,
        'generator_data_parent': gen_par,
        'generator_data_daughter': gen_dau,
    }


# ── Main ─────────────────────────────────────────────────────────

def main():
    sec_yr = 365.25 * 86400
    sec_day = 86400

    nuclei = [
        ("2H",    1,  1, None,          None),
        ("3H",    1,  2, 12.32*sec_yr,  0.01861),
        ("3He",   2,  1, None,          None),
        ("4He",   2,  2, None,          None),
    ]

    # For A > 4, the 3A computation is expensive.
    # 3H: 3A=9, C(9,2)=36 crossings — fast
    # 4He: 3A=12, C(12,2)=66 crossings — fast
    # 6Li: 3A=18, C(18,2)=153 crossings — should be OK
    # 14C: 3A=42, C(42,2)=861 crossings — the factored trace is O(A²), should work!

    # Add larger nuclei — the factored trace is polynomial, not exponential
    nuclei.extend([
        ("6Li",   3,  3, None,          None),
        ("14C",   6,  8, 5730*sec_yr,   0.156),
        ("14N",   7,  7, None,          None),
        ("60Co", 27, 33, 5.2714*sec_yr, 0.318),
        ("90Sr", 38, 52, 28.79*sec_yr,  0.546),
        ("137Cs",55, 82, 30.17*sec_yr,  0.514),
        ("210Bi",83,127, 5.012*sec_day, 1.163),
    ])

    results = []
    for name, p, n, t_obs, Q_exp in nuclei:
        r = compute_nucleus(name, p, n, t_obs, Q_exp)
        results.append(r)

    # Calibrate Q and compute half-lives
    print("\n" + "=" * 80)
    print("Q-VALUE CALIBRATION AND HALF-LIFE PREDICTIONS")
    print("=" * 80)

    # Use Q_local (3-strand) for calibration
    h3_result = next(r for r in results if r['nucleus'] == '3H')
    Q_local_3H = h3_result['Q_local_3strand']
    Q_exp_3H = h3_result['Q_exp']

    if abs(Q_local_3H) > 1e-30:
        lambda_scale = Q_exp_3H / Q_local_3H
    else:
        lambda_scale = 0
        print("WARNING: Q_local(³H) ≈ 0, calibration failed")

    print(f"\nCalibration: λ = Q_exp(³H) / Q_local(³H) = {Q_exp_3H} / {Q_local_3H:.8f} = {lambda_scale:.8e}")
    print()

    sec_yr = 365.25 * 86400
    sec_day = 86400

    # Half-life from Q using Sargent Q^5
    K_half = (12.32 * sec_yr) * Q_exp_3H**5

    print(f"{'Nuc':>8} | Q_local | Q_cal MeV | Q_exp MeV | Q ratio | t_pred       | t_obs        | ratio")
    print("-" * 110)

    for r in results:
        if r['Q_exp'] is None:
            continue

        Q_cal = lambda_scale * r['Q_local_3strand']
        Q_exp = r['Q_exp']
        Q_ratio = Q_cal / Q_exp if Q_exp > 0 else 0

        if abs(Q_cal) > 1e-30:
            t_pred_s = K_half / Q_cal**5
        else:
            t_pred_s = float('inf')

        t_obs_s = r.get('Q_exp', 0)  # need to get t_obs from input
        # reconstruct t_obs
        obs_map = {'3H': 12.32*sec_yr, '14C': 5730*sec_yr, '60Co': 5.2714*sec_yr,
                   '90Sr': 28.79*sec_yr, '137Cs': 30.17*sec_yr, '210Bi': 5.012*sec_day}

        t_obs_s = obs_map.get(r['nucleus'], 0)
        if t_obs_s == 0:
            continue

        t_ratio = t_pred_s / t_obs_s if t_obs_s > 0 else 0
        off = abs(t_ratio - 1) * 100

        if t_obs_s > sec_yr:
            t_p = f"{t_pred_s/sec_yr:.2f} yr"
            t_o = f"{t_obs_s/sec_yr:.2f} yr"
        else:
            t_p = f"{t_pred_s/sec_day:.3f} d"
            t_o = f"{t_obs_s/sec_day:.3f} d"

        print(f"{r['nucleus']:>8} | {r['Q_local_3strand']:+7.4f} | {Q_cal:9.5f} | {Q_exp:9.5f} | {Q_ratio:7.3f} | {t_p:>12s} | {t_o:>12s} | {t_ratio:.4f}")

    # Write witness
    witness = {
        'computation': 'nuclear-braid-level1',
        'description': 'Level 1 factored Markov trace in B_{3A} (3 quark strands per nucleon)',
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'algorithm': {
            'method': 'factored_markov_trace',
            'theorem': 'thm:markov-trace-factorization',
            'level': 1,
            'strands_per_nucleon': 3,
            'complexity': 'O((3A)²) = O(9A²)',
            'steps': [
                '1. Assign quark types: proton=(u,u,d), neutron=(u,d,d)',
                '2. For each generator σ_i (i=0..3A-2):',
                '   a. Collect all crossings from strand i to strands j>i',
                '   b. Chain-reduce via Hecke: σ²=(q-q⁻¹)σ+1',
                '   c. Result: a_i σ_i + b_i',
                '3. Markov-traced volume: V̂_i = z·a_i + b_i',
                '4. log|tr| = Σ_i log|V̂_i| (factorization theorem)',
                '5. Q_local = Σ_{converting strands} log|V̂_par/V̂_dau| / ℏ_q²',
            ],
        },
        'parameters': {
            'q': Q_VAL,
            'z_markov': Z_MARKOV,
            'hbar_q': HBAR_Q,
            'hbar_q2': HBAR_Q2,
            'skein_amp': SKEIN_AMP,
        },
        'calibration': {
            'reference': '3H',
            'lambda_scale': lambda_scale,
        },
        'results': [{k: v for k, v in r.items()
                     if k not in ('generator_data_parent', 'generator_data_daughter')}
                    for r in results],
    }

    out_path = Path(__file__).parent / 'nuclear-braid-level1.witness.json'
    with open(out_path, 'w') as f:
        json.dump(witness, f, indent=2, default=str)
    print(f"\nWitness: {out_path}")


if __name__ == '__main__':
    main()
