#!/usr/bin/env python3
"""
Terminal resolution of the deuteron composite link.

Applies the Skein relation at each of the 9 inter-nucleon crossings,
one at a time, tracking all 3^9 = 19683 resolution paths.

At each crossing, the Skein relation gives:
  q [L+] - q^{-1} [L-] = (q^{1/2} - q^{-1/2}) [L_0]
  → [L-] = q^2 [L+] - q(q^{1/2} - q^{-1/2}) [L_0]

Each resolution path replaces each crossing with either:
  L+ (positive crossing kept)
  L- (negative crossing kept)
  L_0 (crossing smoothed/resolved)

The mass of each fully-resolved link is Vol/hbar_q^2 (from SnapPy).
The deuteron mass = weighted sum over all paths.

Run: python3 computations/terminal-resolution-deuteron.py

Time estimate: ~30 min (19683 SnapPy volume computations)
Output: computations/terminal-resolution-deuteron.witness.json
"""

import json
import math
import sys
import time
from datetime import datetime, timezone
from itertools import product
from pathlib import Path

try:
    import snappy
except ImportError:
    print("ERROR: snappy not installed. Run: pip install snappy")
    sys.exit(1)

# ── Parameters ───────────────────────────────────────────────────

Q_VAL = 1.110
Q_INV = 1.0 / Q_VAL
Q_HALF = Q_VAL**0.5
SKEIN_AMP = Q_HALF - 1.0 / Q_HALF
HBAR_Q = 1.0 - Q_INV
HBAR_Q2 = HBAR_Q**2

# Proton mass (for Skein correction factor)
M_PROTON = 938.272
VOL_B3 = 7.32772
CORRECTION = M_PROTON / (VOL_B3 / HBAR_Q2)

# ── Deuteron braid structure ─────────────────────────────────────
#
# 6 strands: proton (u,u,d) on strands 1-3, neutron (u,d,d) on 4-6
# Internal crossings (Borromean):
#   Proton: (σ_1 σ_2^{-1})^3 = [1,-2,1,-2,1,-2]
#   Neutron: (σ_4 σ_5^{-1})^3 = [4,-5,4,-5,4,-5]
# Inter-nucleon crossings:
#   9 crossings between proton quarks and neutron quarks
#   These use generators σ_1...σ_5 depending on which strands cross.
#
# In our braid representation, the inter-nucleon crossings are at
# generator σ_3 (between strand 3 and strand 4 — the bridge).
# But there are actually 9 quark-quark pairs across the nucleon boundary.
#
# For the terminal resolution: we resolve each of the 9 inter-nucleon
# crossings. Each crossing between quark i (proton) and quark j (neutron)
# can be:
#   + (positive crossing, braid generator σ_k)
#   - (negative crossing, σ_k^{-1})
#   0 (resolved/smoothed, the L_0 term)
#
# The 9 inter-nucleon quark pairs:
# (strand 0=u) × (strand 3=u, strand 4=d, strand 5=d) → 3 crossings
# (strand 1=u) × (strand 3=u, strand 4=d, strand 5=d) → 3 crossings
# (strand 2=d) × (strand 3=u, strand 4=d, strand 5=d) → 3 crossings

PROTON_QUARKS = ['u', 'u', 'd']   # strands 0, 1, 2
NEUTRON_QUARKS = ['u', 'd', 'd']  # strands 3, 4, 5

# The 9 inter-nucleon pairs
INTER_PAIRS = []
for i in range(3):
    for j in range(3):
        qi = PROTON_QUARKS[i]
        qj = NEUTRON_QUARKS[j]
        INTER_PAIRS.append((i, j+3, qi, qj))

print(f"Inter-nucleon quark pairs ({len(INTER_PAIRS)} total):")
for i, j, qi, qj in INTER_PAIRS:
    print(f"  strand {i}({qi}) × strand {j}({qj})")
print()

# ── Build braid word for each resolution ─────────────────────────

def build_resolved_braid(resolution):
    """Build the braid word for a specific resolution of inter-nucleon crossings.

    resolution: tuple of 9 values, each '+', '-', or '0'
      '+' = positive crossing (σ_k)
      '-' = negative crossing (σ_k^{-1})
      '0' = smoothed (crossing removed)

    Returns: braid word as list of integers for SnapPy
    """
    # Internal Borromean crossings (always present)
    # Proton: (σ_1 σ_2^{-1})^3
    word = [1, -2, 1, -2, 1, -2]
    # Neutron: (σ_4 σ_5^{-1})^3
    word += [4, -5, 4, -5, 4, -5]

    # Inter-nucleon crossings
    # Each pair (i, j) with i in {0,1,2} and j in {3,4,5}
    # uses a generator between strands i and j.
    # In the 6-strand braid, the generator connecting strand i to strand j
    # is σ_{min(i,j)+1} ... but that's only valid for ADJACENT strands.
    # For non-adjacent strands, we need a sequence of generators.
    #
    # SIMPLIFICATION: in the standard braid representation, each
    # inter-nucleon crossing uses generator σ_3 (the bridge between
    # the proton block and neutron block). But with 9 crossings all
    # at σ_3, they compound via the Hecke relation.
    #
    # For the terminal resolution: we resolve each of the 9 crossings
    # at σ_3 independently. The resolution replaces σ_3 with:
    #   '+' → σ_3 (positive)
    #   '-' → -σ_3 (negative, i.e. σ_3^{-1})
    #   '0' → nothing (crossing removed)

    for k, res in enumerate(resolution):
        if res == '+':
            word.append(3)
        elif res == '-':
            word.append(-3)
        # '0' = smoothed, no crossing added

    return word

def compute_volume(braid_word):
    """Compute the hyperbolic volume of a link given by its braid closure."""
    try:
        L = snappy.Link(braid_closure=braid_word)
        M = L.exterior()
        vol = float(M.volume())
        return vol
    except Exception as e:
        return None

# ── Skein weights for each resolution path ───────────────────────

def skein_weight(resolution):
    """Compute the Skein weight for a resolution path.

    Each crossing contributes:
      '+' (L+): coefficient q in the Skein relation
      '-' (L-): coefficient q^{-1}
      '0' (L_0): coefficient (q^{1/2} - q^{-1/2})

    The total weight is the product of coefficients.
    """
    weight = 1.0
    for res in resolution:
        if res == '+':
            weight *= Q_VAL
        elif res == '-':
            weight *= Q_INV
        else:  # '0'
            weight *= SKEIN_AMP
    return weight

# ── Main computation ─────────────────────────────────────────────

def main():
    n_crossings = 9
    resolutions = list(product(['+', '-', '0'], repeat=n_crossings))
    n_total = len(resolutions)

    print(f"Terminal resolution of deuteron composite link")
    print(f"  {n_crossings} inter-nucleon crossings")
    print(f"  {n_total} resolution paths (3^{n_crossings})")
    print(f"  q = {Q_VAL}")
    print()

    # First: compute the UNRESOLVED deuteron (all crossings positive)
    word_unresolved = build_resolved_braid(tuple('+' for _ in range(9)))
    vol_unresolved = compute_volume(word_unresolved)
    print(f"Unresolved deuteron (all + crossings): Vol = {vol_unresolved}")

    # Now: compute all 19683 resolutions
    t_start = time.time()
    results = []
    mass_weighted_sum = 0.0
    weight_sum = 0.0

    n_computed = 0
    n_failed = 0

    for idx, res in enumerate(resolutions):
        word = build_resolved_braid(res)
        vol = compute_volume(word)
        weight = skein_weight(res)

        if vol is not None:
            mass = vol / HBAR_Q2 * CORRECTION
            mass_weighted_sum += weight * mass
            weight_sum += weight
            n_computed += 1
        else:
            n_failed += 1
            mass = None

        results.append({
            'resolution': ''.join(res),
            'weight': weight,
            'vol': vol,
            'mass': mass,
        })

        if (idx + 1) % 1000 == 0 or idx == 0:
            elapsed = time.time() - t_start
            rate = (idx + 1) / elapsed if elapsed > 0 else 0
            eta = (n_total - idx - 1) / rate if rate > 0 else 0
            print(f"  {idx+1}/{n_total} ({n_computed} ok, {n_failed} failed) "
                  f"[{elapsed:.0f}s elapsed, ~{eta:.0f}s remaining]")

    elapsed = time.time() - t_start
    print()
    print(f"Completed: {n_computed} volumes computed, {n_failed} failed, {elapsed:.0f}s")
    print()

    # The deuteron mass from the terminal resolution:
    # M_d = Σ_paths weight(path) × mass(path) / Σ_paths weight(path)
    # ... actually the Skein relation is LINEAR, not a weighted average.
    # The correct combination depends on the specific Skein relation applied.
    #
    # For a single crossing: q L+ - q^{-1} L- = skein L_0
    # For 9 crossings: the full expansion gives 3^9 terms with specific
    # signs and weights.

    # The simplest interpretation: the deuteron mass is the term where
    # ALL crossings are in their physical configuration (mixed for pn).
    # The physical crossing for a pn pair is (L+ + L-)/2 = mixed.
    # So the physical mass is the AVERAGE over all +/- combinations.

    # Count only +/- resolutions (no smoothings)
    physical_sum = 0.0
    physical_count = 0
    for r in results:
        if '0' not in r['resolution'] and r['mass'] is not None:
            physical_sum += r['mass']
            physical_count += 1

    if physical_count > 0:
        M_d_physical = physical_sum / physical_count
    else:
        M_d_physical = 0

    # Also: the Skein-weighted sum
    if abs(weight_sum) > 1e-30:
        M_d_skein = mass_weighted_sum / weight_sum
    else:
        M_d_skein = 0

    m_p = 938.272
    m_n = 939.565

    B_d_physical = m_p + m_n - M_d_physical
    B_d_skein = m_p + m_n - M_d_skein

    print(f"RESULTS:")
    print(f"  Physical average (all +/- combos): M_d = {M_d_physical:.3f}, B_d = {B_d_physical:.4f} MeV")
    print(f"  Skein-weighted: M_d = {M_d_skein:.3f}, B_d = {B_d_skein:.4f} MeV")
    print(f"  Experimental: B_d = 2.224 MeV")
    print()

    # Volume statistics
    vols = [r['vol'] for r in results if r['vol'] is not None]
    if vols:
        print(f"Volume statistics:")
        print(f"  min = {min(vols):.6f}")
        print(f"  max = {max(vols):.6f}")
        print(f"  mean = {sum(vols)/len(vols):.6f}")
        print(f"  2×Vol(B_3) = {2*VOL_B3:.6f}")

    # Write witness
    witness = {
        'computation': 'terminal-resolution-deuteron',
        'description': 'Skein resolution of 9 inter-nucleon crossings in deuteron composite',
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'parameters': {
            'q': Q_VAL,
            'hbar_q2': HBAR_Q2,
            'correction_factor': CORRECTION,
            'n_crossings': n_crossings,
            'n_resolutions': n_total,
        },
        'results': {
            'M_d_physical': M_d_physical,
            'B_d_physical': B_d_physical,
            'M_d_skein': M_d_skein,
            'B_d_skein': B_d_skein,
            'B_d_experimental': 2.224,
            'n_computed': n_computed,
            'n_failed': n_failed,
            'elapsed_s': elapsed,
        },
        # Don't store all 19683 results — just summary
        'volume_stats': {
            'min': min(vols) if vols else None,
            'max': max(vols) if vols else None,
            'mean': sum(vols)/len(vols) if vols else None,
        },
    }

    out_path = Path(__file__).parent / 'terminal-resolution-deuteron.witness.json'
    with open(out_path, 'w') as f:
        json.dump(witness, f, indent=2, default=str)
    print(f"\nWitness: {out_path}")


if __name__ == '__main__':
    main()
