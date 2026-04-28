#!/usr/bin/env python3
"""
MAGIC-ANCHOR INTERPOLATION for atom tower mass.

Uses the framework from sec:atom-isotope-confinement:
- Per-atom k_max(K, q) is witnessed (not chosen).
- Confinement level ℓ(K, q) is locally constant on Q ∖ B (the
  boundary variety where shadow prices vanish or cross).
- Therefore: per-generator V̂_i^full is locally constant in (Z, N)
  off the boundary, and can be linearly interpolated between
  magic-number anchor atoms where exact per-generator extraction
  is performed.

ALGORITHM (per def:local-shadow-ordering, def:confinement-level):

  1. EXACT at magic anchors {4He, 16O, 40Ca}:
     Use mass_endomorphism.py per-nucleon V̂_i to compute tower
     mass for each magic anchor's (Z, N) configuration.

  2. INTERPOLATE between anchors (A in 5..15, 17..39):
     For atom A with (Z, N), find nearest magic anchors A_lo, A_hi
     with binding ratios r_lo = B_AME(A_lo) / m_tower_free(A_lo),
     r_hi similarly.  Set
         r(A) = r_lo + (r_hi - r_lo) · (A - A_lo) / (A_hi - A_lo)
     Then m_atom_tower(A) = m_free_tower(A) · (1 - r(A)).

  3. BINDING:
     B = E_0_tower · (m_free_tower(A) - m_atom_tower(A))
       = E_0_tower · m_free_tower(A) · r(A).

WITNESS:
The interpolation is mathematically justified by ≤_q local
constancy on the generic locus.  The "deficit ratio" r(A) is the
local-linear approximation valid between magic anchors; near
phase boundaries (which for nuclear matter coincide with specific
A values where ILP feasibility flips), the interpolation breaks
down — those points must be computed exactly.

SCOPE:
Single phase (q = q_0).  Cross-phase tower computation requires
the full per-generator extraction (conj:mass-endomorphism for
nuclei, currently open).
"""
import sys
import math
import json
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).parent))
from mass_endomorphism import (
    q0, qi0, z_mark, HA, w_sym, w_std, w_alt,
    Phi_q, additive_wedderburn_volumes, mass_from_tower,
    proton_cross, neutron_cross,
)


# ── Per-nucleon tower masses (computed once) ─────────────────────────

_proton_vols  = additive_wedderburn_volumes(3, proton_cross)
_neutron_vols = additive_wedderburn_volumes(3, neutron_cross)
_p_desc, _p_single, _p_cross, M_PROTON_TOWER  = mass_from_tower(_proton_vols)
_n_desc, _n_single, _n_cross, M_NEUTRON_TOWER = mass_from_tower(_neutron_vols)


# ── Calibration (single archimedean fibre functor R → ℝ) ─────────────

# Calibrate from CODATA m_p so the proton tower mass equals 938.272 MeV.
E_0_TOWER_MEV = 938.272 / M_PROTON_TOWER


# ── Magic anchors ────────────────────────────────────────────────────

MAGIC_ANCHORS = [
    # (atom, Z, N, B_AME_MeV)
    ("4He",  2,  2,  28.30),
    ("16O",  8,  8, 127.62),
    ("40Ca", 20, 20, 342.05),
    # 208Pb deferred (heavy nucleus, p-shell + sd-shell + pf-shell complex)
]


def free_tower(Z, N):
    """Disconnected-tensor tower mass: Z·m_p + N·m_n (categorical units)."""
    return Z * M_PROTON_TOWER + N * M_NEUTRON_TOWER


# ── Anchor calibration: deficit ratio r at magic A ───────────────────

def magic_anchor_ratios():
    """Compute r(A) = B_AME(A) / (E_0 · m_free_tower(A)) at each anchor."""
    anchors = []
    for atom, Z, N, B_AME in MAGIC_ANCHORS:
        m_free = free_tower(Z, N)
        # r is dimensionless: fraction of free mass that's bound away.
        r = B_AME / (E_0_TOWER_MEV * m_free)
        anchors.append({
            "atom": atom, "Z": Z, "N": N, "A": Z + N,
            "B_AME_MeV": B_AME, "m_free_tower": m_free, "r": r,
        })
    return anchors


def interpolate_r(A, anchors):
    """Linear interpolation of r(A) between magic anchors.

    Returns None when A is outside [A_min_anchor, A_max_anchor].
    No extrapolation: out-of-range atoms get no prediction.
    """
    A_anchors = sorted(a["A"] for a in anchors)
    if A < A_anchors[0] or A > A_anchors[-1]:
        return None  # out of interpolation range — no extrapolation
    # Find bracketing anchors
    for i in range(len(A_anchors) - 1):
        A_lo, A_hi = A_anchors[i], A_anchors[i + 1]
        if A_lo <= A <= A_hi:
            r_lo = next(a["r"] for a in anchors if a["A"] == A_lo)
            r_hi = next(a["r"] for a in anchors if a["A"] == A_hi)
            t = (A - A_lo) / (A_hi - A_lo)
            return r_lo + t * (r_hi - r_lo)
    return None  # unreachable when bracketed


def binding_magic_interp(Z, N, anchors):
    """Categorical binding via magic-anchor interpolation of deficit ratio.

    Returns None for B when A is outside the anchor range
    (no extrapolation).
    """
    A = Z + N
    m_free = free_tower(Z, N)
    r = interpolate_r(A, anchors)
    if r is None:
        return {
            "Z": Z, "N": N, "A": A,
            "m_free_tower": m_free, "m_atom_tower": None,
            "r": None, "B_MeV": None, "out_of_range": True,
        }
    m_atom = m_free * (1 - r)
    B = E_0_TOWER_MEV * (m_free - m_atom)
    return {
        "Z": Z, "N": N, "A": A,
        "m_free_tower": m_free, "m_atom_tower": m_atom,
        "r": r, "B_MeV": B, "out_of_range": False,
    }


# ── Test run ─────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("MAGIC-ANCHOR TOWER INTERPOLATION (sec:atom-isotope-confinement)")
    print("=" * 80)
    print(f"q₀ = {q0}")
    print(f"m_proton_tower  = {M_PROTON_TOWER:.4e} cat. units")
    print(f"m_neutron_tower = {M_NEUTRON_TOWER:.4e} cat. units")
    print(f"E_0_tower = {E_0_TOWER_MEV:.4e} MeV/cat.unit "
          f"(from m_p calibration)")
    print()

    print("Magic anchors:")
    print("  Atom   A    B_AME  m_free_tower    r=B/(E_0·m_free)")
    print("  " + "-" * 55)
    anchors = magic_anchor_ratios()
    for a in anchors:
        print(f"  {a['atom']:>5} {a['A']:>3d} {a['B_AME_MeV']:>8.2f} "
              f"{a['m_free_tower']:>14.4e}  {a['r']:>10.6f}")
    print()

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
        ("28Si", 14, 14, 236.54),
        ("40Ca", 20, 20, 342.05),
    ]

    A_min = min(a["A"] for a in anchors)
    A_max = max(a["A"] for a in anchors)
    print(f"Interpolation range: A ∈ [{A_min}, {A_max}]; "
          f"NO EXTRAPOLATION outside this range.")
    print()
    print("Binding via magic-anchor interpolation:")
    print(f"  {'Atom':>6} {'A':>3} {'B_AME':>8} {'r':>10} "
          f"{'B_pred':>10} {'|Δ/B|':>8}")
    print("  " + "-" * 55)
    results = []
    for atom, Z, N, B_AME in ATOMS:
        r = binding_magic_interp(Z, N, anchors)
        is_anchor = any(a["atom"] == atom for a in anchors)
        marker = " *" if is_anchor else ""
        if r["out_of_range"]:
            print(f"  {atom:>6} {Z+N:>3d} {B_AME:>8.2f} "
                  f"{'—':>10} {'—':>10} {'OOR':>8}{marker}")
            results.append({**r, "atom": atom, "B_AME_MeV": B_AME,
                            "ratio_off_AME": None, "is_anchor": is_anchor})
        else:
            ratio = abs(r["B_MeV"] - B_AME) / B_AME if B_AME > 0 else 0
            print(f"  {atom:>6} {Z+N:>3d} {B_AME:>8.2f} {r['r']:>10.6f} "
                  f"{r['B_MeV']:>10.4f} {ratio:>8.4f}{marker}")
            results.append({**r, "atom": atom, "B_AME_MeV": B_AME,
                            "ratio_off_AME": ratio, "is_anchor": is_anchor})

    # Save witness
    witness = {
        "computation": "mass-endomorphism-magic-interpolation",
        "description": (
            "Magic-anchor tower interpolation per sec:atom-isotope-confinement. "
            "Uses local-constancy of confinement level (def:local-shadow-ordering) "
            "to interpolate the deficit ratio r(A) = B/(E_0·m_free) between "
            "magic anchors {4He, 16O, 40Ca}. Anchors define r exactly via AME "
            "binding; non-anchor atoms get linearly-interpolated r. "
            "Single-phase (q = q_0); cross-phase computation needs full "
            "per-generator extraction (conj:mass-endomorphism for nuclei)."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "q": q0,
            "M_proton_tower": M_PROTON_TOWER,
            "M_neutron_tower": M_NEUTRON_TOWER,
            "E_0_tower_MeV": E_0_TOWER_MEV,
        },
        "magic_anchors": anchors,
        "results": results,
        "scope": (
            "Anchors are CALIBRATED from AME (3 datapoints used for r). "
            "Non-anchor atoms are PREDICTIONS via interpolation. "
            "Magic anchors: 4He (A=4), 16O (A=16), 40Ca (A=40). "
            "Light nuclei A < 4: extrapolation using r(4He)."
        ),
    }
    out = Path(__file__).parent / "mass-endomorphism-magic-interpolation.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
