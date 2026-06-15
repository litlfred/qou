#!/usr/bin/env python3
"""
ATOM TOWER MASS (EXPLORATORY): extend mass_endomorphism.py to A-nucleon atoms.

STATUS: Preliminary — the inter-nucleon coupling structure used here
(one crossing per (k, k+1) pair) is too sparse.  It produces atom vs
free tower masses that differ only sub-percent, yielding binding
energies that are off by 10^2 compared to AME.

Per mass-endomorphism-conjecture.md, a proper tower extension to nuclei
requires detailed per-generator V̂_i^full for every inter-nucleon
crossing in the full atom braid — including ud quark-exchange
crossings across nucleon boundaries, not just bare σ/σ⁻¹ pair markers.
This script is kept as a reproducible stub for the tower-for-atoms
conjecture.

Computes the full tower mass formula
    𝔪(W) = |Π V̂_i| + Σ Φ_q(|V̂_i|) + z² · Σ_{adj} Φ_q(|V̂_i V̂_j|)
for atomic braids W_atom and the disconnected-tensor baseline W_free.

Per prop:mass-endomorphism-tower, an A-nucleon Borromean atom has
    n_strands = 3A          (3 strands per Borromean nucleon)
    n_gens    = 3A - 1      (one less generator than strands)

The 3A-1 generators decompose as:
  - 2 intra-nucleon generators per nucleon (gen indices 3k, 3k+1)
    carrying the Borromean baryon crossings for nucleon k.
  - A-1 inter-nucleon generators (gen indices 3k+2 for k=0..A-2)
    carrying pair-type crossings:
       σ              for pp pairs    (bare positive crossing)
       σ⁻¹ ~ (1,-h)   for nn pairs    (bare negative crossing)
       ½(σ+σ⁻¹)       for pn pairs    (symmetric)

Scope: this is the FULL-TOWER categorical mass per
prop:categorical-mass-markov — no prefactor tuning.  The ONLY
calibration is E_0, the fibre functor R → ℝ, fixed by matching one
reference experiment (neutron β-decay Q = 0.782 MeV).

Binding energy:
    B = E_0 · ( 𝔪(W_free) - 𝔪(W_atom) )

Relies on mass_endomorphism.py for Phi_q, additive_wedderburn_volumes,
mass_from_tower, z_mark, w_sym/std/alt, q0.
"""
import sys
import math
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from mass_endomorphism import (
    q0, qi0, z_mark, HA, w_sym, w_std, w_alt,
    Phi_q, additive_wedderburn_volumes, mass_from_tower,
    proton_cross, neutron_cross,
)

# ── Calibration ────────────────────────────────────────────────────
# The tower-level fibre functor τ: R → ℝ is fixed by ONE reference.
# Descended Markov trace is ~0.5% of total mass (per mass-endomorphism-
# conjecture.md), so the tower-level E_0 is ~200× smaller than the
# descended-level 0.782 MeV.  We calibrate directly from m_p by asking:
# what E_0 maps 𝔪_tower(proton) to 938.272 MeV?  This is a single
# archimedean input, equivalent in spirit to the neutron β-decay Q
# but applied at tower scale.
#
# 𝔪_tower(proton on 3 strands, 2 gen) ≈ 1.18e6 categorical units
# Per `prop:three-calibration-inputs` (CAL-3) E_0 must trace back to
# Q_β(n), not proton mass — proton-mass-anchoring is a forbidden
# second pinning of the hadronic scale. Use the canonical
# E_0_CALIBRATION_MEV from hecke_core (= experimental_constants.
# Q_NEUTRON_MEV = 0.78233341 MeV). The proton-tower mass is retained
# only as a per-block intermediate, not as an E_0 anchor.
_PROTON_VOLS = additive_wedderburn_volumes(3, proton_cross)
_, _, _, _M_PROTON_TOWER = mass_from_tower(_PROTON_VOLS)
from hecke_core import E_0_CALIBRATION_MEV  # noqa: E402, F401



# ── Atom builder ───────────────────────────────────────────────────

def atom_crossings(nucleon_types, include_inter=True):
    """Build the crossings_per_gen dict for an A-nucleon atom braid.

    Parameters
    ----------
    nucleon_types : list of 'p' or 'n', length A
    include_inter : bool
        If False, omits inter-nucleon crossings (free-nucleon baseline).

    Returns
    -------
    dict : gen_index -> list of (c, d) crossings
    """
    A = len(nucleon_types)
    crossings = {}

    # Intra-nucleon: each nucleon has 2 generators (gen 3k, 3k+1)
    # carrying the proton_cross or neutron_cross from mass_endomorphism.py.
    for k, nt in enumerate(nucleon_types):
        src = proton_cross if nt == 'p' else neutron_cross
        crossings[3 * k]     = list(src.get(0, []))
        crossings[3 * k + 1] = list(src.get(1, []))

    # Inter-nucleon: generator 3k+2 couples nucleon k with nucleon k+1.
    # Pair type determines the crossing parameters.
    if include_inter:
        for k in range(A - 1):
            pair = (nucleon_types[k], nucleon_types[k + 1])
            if pair == ('p', 'p'):
                pair_cross = [(1.0, 0.0)]        # σ
            elif pair == ('n', 'n'):
                pair_cross = [(1.0, -HA)]        # σ⁻¹ ~ (1, -h)
            else:
                pair_cross = [(1.0, -HA / 2)]    # ½(σ + σ⁻¹)
            crossings[3 * k + 2] = pair_cross
    # else: inter-nucleon generators get empty (identity) crossings —
    # the generator is then "absent" and V̂_i^full = 1 (z·a+b with a=0,b=1).

    # Ensure every generator index 0..3A-2 is present (empty if absent).
    for i in range(3 * A - 1):
        crossings.setdefault(i, [])

    return crossings


def atom_tower_mass(nucleon_types, include_inter=True, return_breakdown=False):
    """Compute the full tower mass 𝔪(W) for an atom braid.

    When include_inter=False (free baseline), we sum per-nucleon tower
    masses INDIVIDUALLY — the disconnected tensor H_3(q)^⊗A embeds the
    nucleon towers separately, with no inter-nucleon generators at all.
    """
    A = len(nucleon_types)
    if not include_inter:
        # Free baseline: disconnected tensor of A independent nucleon
        # towers.  Each nucleon has 2 intra-generators, no inter.
        total = 0.0
        desc_sum = 0.0
        single_sum = 0.0
        cross_sum = 0.0
        all_vols = []
        for nt in nucleon_types:
            src = proton_cross if nt == 'p' else neutron_cross
            n_cross = {0: list(src.get(0, [])), 1: list(src.get(1, []))}
            n_vols = additive_wedderburn_volumes(3, n_cross)
            d, s, c, t = mass_from_tower(n_vols)
            desc_sum += d
            single_sum += s
            cross_sum += c
            total += t
            all_vols.extend(n_vols)
        if return_breakdown:
            return {
                "vols": all_vols,
                "desc": desc_sum,
                "single": single_sum,
                "cross": cross_sum,
                "total": total,
            }
        return total

    # Atom: joint H_{3A}(q) tower with inter-nucleon crossings.
    n_strands = 3 * A
    cross = atom_crossings(nucleon_types, include_inter=True)
    vols = additive_wedderburn_volumes(n_strands, cross)
    desc, single, cross_term, total = mass_from_tower(vols)
    if return_breakdown:
        return {
            "vols": vols,
            "desc": desc,
            "single": single,
            "cross": cross_term,
            "total": total,
        }
    return total


def binding_tower(Z, N):
    """Categorical binding energy from the full tower formula.

    B = E_0 · ( 𝔪(W_free) - 𝔪(W_atom) )

    W_free: disconnected tensor (no inter-nucleon crossings).
    W_atom: full braid with pp, nn, pn inter-nucleon crossings.
    """
    # Convention: arrange as Z protons then N neutrons.
    nucleon_types = ['p'] * Z + ['n'] * N
    m_atom = atom_tower_mass(nucleon_types, include_inter=True,
                             return_breakdown=True)
    m_free = atom_tower_mass(nucleon_types, include_inter=False,
                             return_breakdown=True)
    B = E_0_CALIBRATION_MEV * (m_free['total'] - m_atom['total'])
    return {
        "Z": Z, "N": N, "A": Z + N,
        "m_atom": m_atom['total'],
        "m_atom_desc": m_atom['desc'],
        "m_atom_single": m_atom['single'],
        "m_atom_cross": m_atom['cross'],
        "m_free": m_free['total'],
        "m_free_desc": m_free['desc'],
        "m_free_single": m_free['single'],
        "m_free_cross": m_free['cross'],
        "B_MeV": B,
    }


# ── Test run ────────────────────────────────────────────────────────

if __name__ == "__main__":
    ATOMS = [
        ("D",    1,  1,   2.22),
        ("T",    1,  2,   8.48),
        ("3He",  2,  1,   7.72),
        ("4He",  2,  2,  28.30),
        ("6Li",  3,  3,  32.00),
        ("7Li",  3,  4,  39.24),
        ("9Be",  4,  5,  58.17),
        ("11B",  5,  6,  76.20),
        ("12C",  6,  6,  92.16),
        ("14C",  6,  8, 105.66),
        ("14N",  7,  7, 104.66),
        ("16O",  8,  8, 127.62),
        ("20Ne", 10, 10, 160.65),
    ]

    print("FULL TOWER MASS (mass-endomorphism-tower)")
    print("=" * 88)
    print(f"q₀ = {q0}, E_0 = {E_0_CALIBRATION_MEV} MeV")
    print(f"Wedderburn weights: w_sym={w_sym:.4f}, w_std={w_std:.4f}, w_alt={w_alt:.4f}")
    print(f"z_mark = {z_mark:.6f}, z² = {z_mark**2:.6f}")
    print()
    print(f"  {'Atom':>6} {'A':>3} {'B_AME':>8} {'𝔪_atom':>12} {'𝔪_free':>12} "
          f"{'B_tower':>10} {'|Δ/B|':>8}")
    print("-" * 88)

    results = []
    for atom, Z, N, B_AME in ATOMS:
        try:
            r = binding_tower(Z, N)
            B = r['B_MeV']
            ratio = abs(B - B_AME) / B_AME if B_AME > 0 else float('nan')
            print(f"  {atom:>6} {Z+N:>3d} {B_AME:>8.2f} "
                  f"{r['m_atom']:>12.4g} {r['m_free']:>12.4g} "
                  f"{B:>10.4f} {ratio:>8.4f}")
            results.append({
                "atom": atom, "Z": Z, "N": N, "A": Z + N,
                "B_AME_MeV": B_AME, "B_tower_MeV": B,
                "m_atom": r['m_atom'], "m_free": r['m_free'],
                "m_atom_desc": r['m_atom_desc'],
                "m_atom_single": r['m_atom_single'],
                "m_atom_cross": r['m_atom_cross'],
                "m_free_desc": r['m_free_desc'],
                "m_free_single": r['m_free_single'],
                "m_free_cross": r['m_free_cross'],
                "ratio_off_AME": ratio,
            })
        except Exception as exc:
            print(f"  {atom:>6}  ERROR: {exc}")
            results.append({"atom": atom, "error": str(exc)})

    # Save witness
    import json
    from datetime import datetime, timezone
    witness = {
        "computation": "mass-endomorphism-atom-tower",
        "description": (
            "Full tower mass formula applied to atom braids. "
            "B = E_0·(𝔪(W_free) - 𝔪(W_atom)) with "
            "𝔪 = |Π V̂| + Σ Φ_q(|V̂|) + z²·Σ_{adj} Φ_q(|V̂V̂|)."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "q": q0, "E_0_MeV": E_0_CALIBRATION_MEV,
            "z_mark": z_mark, "z_squared": z_mark**2,
            "w_sym": w_sym, "w_std": w_std, "w_alt": w_alt,
        },
        "results": results,
    }
    out = Path(__file__).parent / "mass-endomorphism-atom-tower.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
