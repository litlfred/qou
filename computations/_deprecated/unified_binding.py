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
E_0_MeV = 938.272 / M_PROTON_TOWER  # tower-level calibration (non-magic path)

# Single-level β-decay calibration (per prop:categorical-mass-markov):
# E_0 = 0.782 MeV = free-neutron β-decay Q-value.
# This is the CANONICAL categorical calibration for single-level
# Markov trace mass identity: 𝔪|_SL = |tr_M|; B = E_0 · (|tr_M_free| - |tr_M_atom|).
from experimental_constants import Q_NEUTRON_MEV  # noqa: E402
E_0_BETA_MeV = Q_NEUTRON_MEV  # 0.78233341 MeV (CODATA-derived)


def unified_binding(Z, N, cache):
    """B_pred via magic-anchor (opt 7) or shorthand (opt 5)."""
    A = Z + N
    mtype = magic_type(Z, N)
    key = f"{Z}-{N}"

    if mtype != "non-magic":
        # OPT 7: magic-anchor with β-decay calibration (per
        # prop:categorical-mass-markov). 𝔪|_SL = |tr_M|. The traces
        # share the common rescaling within the same atom, so:
        #   B = E_0_β · (|tr_M_free| - |tr_M_atom|)
        # with E_0_β = 0.782 MeV (free-neutron β-decay Q).
        # No need to unroll exp(common_max_ln) — the DIFFERENCE of
        # rescaled traces times E_0_β gives binding directly.
        if key in cache["opt7_magic_anchors"]:
            d = cache["opt7_magic_anchors"][key]
            if "error" not in d:
                atom_abs = abs(d["atom_trM_signed"])
                free_abs = abs(d["free_trM_signed"])
                B = E_0_BETA_MeV * (free_abs - atom_abs)
                return {
                    "method": "opt7-β-calib",
                    "magic_type": mtype,
                    "m_free_MeV": E_0_BETA_MeV * free_abs,
                    "m_atom_MeV": E_0_BETA_MeV * atom_abs,
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
        # Light (A ≤ 20)
        ("D",    1,  1,    2.22),
        ("T",    1,  2,    8.48),
        ("3He",  2,  1,    7.72),
        ("4He",  2,  2,   28.30),
        ("6Li",  3,  3,   32.00),
        ("7Li",  3,  4,   39.24),
        ("9Be",  4,  5,   58.17),
        ("10B",  5,  5,   64.75),
        ("11B",  5,  6,   76.20),
        ("12C",  6,  6,   92.16),
        ("13C",  6,  7,   97.11),
        ("14C",  6,  8,  105.66),
        ("14N",  7,  7,  104.66),
        ("15N",  7,  8,  115.49),
        ("16O",  8,  8,  127.62),
        ("17O",  8,  9,  131.76),
        ("18O",  8, 10,  139.81),
        ("19F",  9, 10,  147.80),
        ("20Ne", 10, 10, 160.65),
        # Medium (A ~ 20-60)
        ("22Ne", 10, 12, 177.77),
        ("23Na", 11, 12, 186.56),
        ("24Mg", 12, 12, 198.26),
        ("27Al", 13, 14, 224.95),
        ("28Si", 14, 14, 236.54),
        ("32S",  16, 16, 271.78),
        ("40Ca", 20, 20, 342.05),
        ("48Ca", 20, 28, 416.00),  # double-magic
        ("56Fe", 26, 30, 492.25),  # peak of binding curve
        ("58Ni", 28, 30, 506.46),
        # Heavy (A > 60)
        ("90Zr", 40, 50, 783.90),
        ("120Sn", 50, 70, 1020.55),
        ("208Pb", 82, 126, 1636.45),  # heaviest stable double-magic
    ]

    # Warm cache
    cache = warm_all_caches([(a, Z, N) for a, Z, N, _ in ATOMS])

    print(f"  {'Atom':>6} {'Z':>3} {'N':>3} {'A':>3} {'type':>10} {'method':>14} "
          f"{'B_pred':>10} {'B_AME':>8} {'B_err':>8} {'|Δm/m|%':>9} "
          f"{'B/A_pred':>9} {'B/A_AME':>9}")
    print("  " + "-" * 115)

    results = []
    for atom, Z, N, B_AME in ATOMS:
        r = unified_binding(Z, N, cache)
        A = Z + N
        M_total = A * 938.272
        mtype = magic_type(Z, N)
        dm_m = abs(r["B_pred_MeV"] - B_AME) / M_total * 100
        B_err = r["B_pred_MeV"] - B_AME
        B_per_A_pred = r["B_pred_MeV"] / A
        B_per_A_AME = B_AME / A
        print(f"  {atom:>6} {Z:>3d} {N:>3d} {A:>3d} {mtype:>10} {r['method']:>14} "
              f"{r['B_pred_MeV']:>10.3f} {B_AME:>8.2f} {B_err:>+8.3f} "
              f"{dm_m:>8.4f}% {B_per_A_pred:>9.4f} {B_per_A_AME:>9.4f}")
        results.append({**r, "atom": atom, "Z": Z, "N": N, "A": A,
                        "magic_type_full": mtype,
                        "B_AME_MeV": B_AME, "M_atom_MeV": M_total,
                        "B_err_MeV": B_err,
                        "B_per_A_pred": B_per_A_pred,
                        "B_per_A_AME": B_per_A_AME,
                        "delta_m_over_m_pct": dm_m})

    # Summary stats
    print()
    by_method = {}
    for r in results:
        by_method.setdefault(r["method"], []).append(r["delta_m_over_m_pct"])
    print(f"  |Δm/m|% by method:")
    for m, vals in by_method.items():
        print(f"    {m:>18}: min={min(vals):.4f}%, max={max(vals):.4f}%, "
              f"mean={sum(vals)/len(vals):.4f}%, n={len(vals)}")

    # Trends by A
    print()
    print(f"  |Δm/m|% by A-bucket (non-magic shorthand):")
    buckets = {"A≤10": [], "A∈[11,20]": [], "A∈[21,50]": [], "A>50": []}
    for r in results:
        if r["method"] != "opt5-shorthand":
            continue
        A = r["A"]
        if A <= 10:
            buckets["A≤10"].append(r["delta_m_over_m_pct"])
        elif A <= 20:
            buckets["A∈[11,20]"].append(r["delta_m_over_m_pct"])
        elif A <= 50:
            buckets["A∈[21,50]"].append(r["delta_m_over_m_pct"])
        else:
            buckets["A>50"].append(r["delta_m_over_m_pct"])
    for bucket, vals in buckets.items():
        if vals:
            print(f"    {bucket:>12}: n={len(vals)}, mean={sum(vals)/len(vals):.4f}%, "
                  f"min={min(vals):.4f}%, max={max(vals):.4f}%")

    dms = [r["delta_m_over_m_pct"] for r in results]
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
