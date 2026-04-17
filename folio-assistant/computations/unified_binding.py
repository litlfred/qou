#!/usr/bin/env python3
"""
Unified binding computation using heavy-atom-opts cache.

Combines optimizations:
  - OPT 2: per-nucleon characters (cached)
  - OPT 5: nucleon-shorthand for non-magic
  - OPT 7: exact joint H_{3A}(q) signed Markov trace for magic

Produces mass / B / |Δm/m|% table for all atoms.

For each atom:
  - Magic (single or double): B = E_0 · (free_trM - atom_trM) from opt-7 cache
  - Non-magic: B = E_0 · (pair-contrib) from opt-5 shorthand

|Δm/m|% = |B_pred - B_AME| / (A · 938.272 MeV)
"""
import sys
import math
import json
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).parent))
from heavy_atom_opts import (
    MAGIC, magic_type, warm_all_caches, load_cache,
    nucleon_shorthand_mass,
)
from mass_endomorphism import q0, mass_from_tower, additive_wedderburn_volumes, proton_cross


_p_vols = additive_wedderburn_volumes(3, proton_cross)
_, _, _, M_PROTON_TOWER = mass_from_tower(_p_vols)
E_0_MeV = 938.272 / M_PROTON_TOWER  # tower-level calibration

# Single-level calibration from |tr_M(proton)| — for opt-7 magic path.
# tr_M(proton) computed from atom_character_raw(1, 0) sum over partitions.
from hecke_core import atom_character_raw, _PARTITION_TABLE
import math as _math
_p_active = [e for e in _PARTITION_TABLE
             if e.get('has_ysn', False) and e.get('k', 0) <= 6]
_p_max_ln = 0.0
_p_data = []
for _e in _p_active:
    _c, _l, _d = atom_character_raw(1, 0, _e, include_inter=True)
    _p_data.append({'chi': _c, 'ln': _l, 'dim': _d,
                    'w': _e.get('wedderburn_weight', 0)})
    if _l > _p_max_ln:
        _p_max_ln = _l
_p_trM = 0.0
for pd in _p_data:
    _p_trM += pd['w'] * pd['chi'] * _math.exp(pd['ln'] - _p_max_ln) / pd['dim']
_abs_p_trM = abs(_p_trM) * _math.exp(_p_max_ln)
E_0_SINGLE_MeV = 938.272 / _abs_p_trM if _abs_p_trM > 0 else 0
print(f"# |tr_M(proton)| = {_abs_p_trM:.4e}, E_0_single = {E_0_SINGLE_MeV:.4e} MeV")


def unified_binding(Z, N, cache):
    """B_pred via magic-anchor (opt 7) or shorthand (opt 5)."""
    A = Z + N
    mtype = magic_type(Z, N)
    key = f"{Z}-{N}"

    if mtype != "non-magic":
        # OPT 7: use exact magic-anchor ABSOLUTE Markov traces.
        # Per prop:categorical-mass-markov, mass = |tr_M|, not signed.
        if key in cache["opt7_magic_anchors"]:
            d = cache["opt7_magic_anchors"][key]
            if "error" not in d:
                # Use |tr_M| (mass identity requires absolute value)
                atom_abs = abs(d["atom_trM_signed"])
                free_abs = abs(d["free_trM_signed"])
                # Mass scale via common rescaling exp(common_max_ln)
                # E_0_single calibrates |tr_M(proton)| → m_p = 938.272 MeV
                # For the atom, |tr_M(W_atom)| gives mass in same units
                scale = math.exp(d.get("common_max_ln", 0))
                m_atom_abs = atom_abs * scale
                m_free_abs = free_abs * scale
                # Binding from mass defect
                B = E_0_SINGLE_MeV * (m_free_abs - m_atom_abs)
                return {
                    "method": "opt7-magic",
                    "magic_type": mtype,
                    "m_free_MeV": E_0_SINGLE_MeV * m_free_abs,
                    "m_atom_MeV": E_0_SINGLE_MeV * m_atom_abs,
                    "B_pred_MeV": B,
                    "atom_trM_signed": d["atom_trM_signed"],
                    "free_trM_signed": d["free_trM_signed"],
                }
    # Non-magic: use shorthand
    d = nucleon_shorthand_mass(Z, N, cache)
    m_free_MeV = E_0_MeV * d["m_free"]
    m_atom_MeV = E_0_MeV * d["m_atom"]
    B = E_0_MeV * (d["m_free"] - d["m_atom"])
    return {
        "method": "opt5-shorthand",
        "magic_type": "non-magic",
        "m_free_MeV": m_free_MeV,
        "m_atom_MeV": m_atom_MeV,
        "B_pred_MeV": B,
        "pair_contrib": d["pair_contrib"],
    }


if __name__ == "__main__":
    print("UNIFIED BINDING TABLE (opts 2, 5, 7)")
    print("=" * 96)
    print(f"q₀ = {q0}")
    print(f"E_0 = {E_0_MeV:.4e} MeV/cat.unit (from m_p tower → CODATA 938.272 MeV)")
    print()

    ATOMS = [
        ("D",    1,  1,   2.22),
        ("T",    1,  2,   8.48),
        ("3He",  2,  1,   7.72),
        ("4He",  2,  2,  28.30),
        ("6Li",  3,  3,  32.00),
        ("12C",  6,  6,  92.16),
        ("14C",  6,  8, 105.66),
        ("16O",  8,  8, 127.62),
        ("20Ne", 10, 10, 160.65),
        ("40Ca", 20, 20, 342.05),
    ]

    # Warm cache
    cache = warm_all_caches([(a, Z, N) for a, Z, N, _ in ATOMS])

    print(f"  {'Atom':>6} {'A':>3} {'method':>14} {'m_free(MeV)':>13} "
          f"{'m_atom(MeV)':>13} {'B_pred':>10} {'B_AME':>8} {'|Δm/m|%':>9}")
    print("  " + "-" * 92)

    results = []
    for atom, Z, N, B_AME in ATOMS:
        r = unified_binding(Z, N, cache)
        A = Z + N
        M_total = A * 938.272
        dm_m = abs(r["B_pred_MeV"] - B_AME) / M_total * 100
        print(f"  {atom:>6} {A:>3d} {r['method']:>14} "
              f"{r['m_free_MeV']:>13.2f} {r['m_atom_MeV']:>13.2f} "
              f"{r['B_pred_MeV']:>10.4f} {B_AME:>8.2f} {dm_m:>8.4f}%")
        results.append({**r, "atom": atom, "Z": Z, "N": N, "A": A,
                        "B_AME_MeV": B_AME, "M_atom_MeV": M_total,
                        "delta_m_over_m_pct": dm_m})

    # Summary stats
    dms = [r["delta_m_over_m_pct"] for r in results]
    print()
    print(f"  |Δm/m|% summary:")
    print(f"    min   = {min(dms):.4f}%")
    print(f"    max   = {max(dms):.4f}%")
    print(f"    mean  = {sum(dms)/len(dms):.4f}%")

    witness = {
        "computation": "unified-binding",
        "description": (
            "Unified binding table using heavy-atom-opts cache: "
            "magic atoms via opt-7 exact joint H_{3A}(q) signed trace, "
            "non-magic via opt-5 nucleon-shorthand."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "q": q0, "E_0_MeV": E_0_MeV, "M_proton_tower": M_PROTON_TOWER,
        },
        "results": results,
        "summary": {
            "min_dm_m_pct": min(dms),
            "max_dm_m_pct": max(dms),
            "mean_dm_m_pct": sum(dms) / len(dms),
        },
    }
    out = Path(__file__).parent / "unified-binding.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
