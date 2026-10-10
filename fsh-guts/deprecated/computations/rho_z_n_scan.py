#!/usr/bin/env python3
"""ρ(Z, N) structural-rule exploration scan.

The mass-table-ppb framework predicts B = ρ · m_e · Vol_hyp(K) where
ρ ∈ ℤ_{>0} is a structural prefactor.  Pattern observed empirically:

    isotope         ρ      remark
    ────────────────────────────────────────
    ²H              1      historical (6_2)
    ³H              2      historical (8_11)
    ³He             2      historical (L6a4)
    ⁴He             2      magic-A formula
    ⁶Li             5      ⚠ deprecated volume-match (only)
    ⁷Li             5      ⚠ deprecated volume-match (only)
    ⁸Be–⁴⁰Ca        —      α-cluster recursion (no single ρ)

Open question: derive ρ(Z, N) from the canonical T_w's Wedderburn-block
multiplicity structure.

Hypothesis to explore: ρ correlates with one of:
  (a) Multiplicity of a specific Wedderburn block λ in the
      decomposition of T_w.
  (b) Number of "non-trivial" Hecke firings in the GB-NF reduction.
  (c) Trace ratio Σ_λ d_λ · y_λ(q_0) · χ_λ(T_w)|_{q_0}.

This script scans the mass-table-ppb + Li witnesses, runs the braid
through gb_filtration_jet_tracker at the native strand count, computes
Wedderburn-block diagnostics via the Hoefsmit machinery, and emits a
witness JSON for human pattern-finding.

The script does NOT prescribe a rule — it surfaces the data so that
the structural rule can be conjectured from the multiplicities.

Usage:
    python3 computations/rho_z_n_scan.py
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from gb_filtration_jet_tracker import HeckeElement


# ───────────────────────────────────────────────────────────────────
# Registry of known braid words / historical knot IDs.
# ───────────────────────────────────────────────────────────────────

REGISTRY = [
    {"name": "electron",  "Z": 0, "N": 0, "ell": 1, "rho": 1,
     "native_n": 2, "braid": [1, 1, 1],                              # σ_1^3
     "knot": "T_{2,3} = 3_1", "methodology": "principled-derivation"},
    {"name": "proton",    "Z": 1, "N": 0, "ell": 1, "rho": 1,
     "native_n": 3, "braid": [1, -2, 1, -2, 1, -2],                  # Borromean
     "knot": "B_3(uud)",   "methodology": "principled-derivation"},
    {"name": "neutron",   "Z": 0, "N": 1, "ell": 1, "rho": 1,
     "native_n": 3, "braid": [1, -2, 1, -2, 1, -2],
     "knot": "B_3(udd)",   "methodology": "principled-derivation"},
    {"name": "2H",        "Z": 1, "N": 1, "ell": 2, "rho": 1,
     "native_n": 3, "braid": [1, -2, 1, 1, 1, -2],                   # 6_2
     "knot": "6_2",        "methodology": "manual-historical"},
    {"name": "3H",        "Z": 1, "N": 2, "ell": 2, "rho": 2,
     "native_n": 5, "braid": [-1, 2, -3, 2, 1, -3, -3, 4, -3, -2, -3, -4, -3, 2],
     "knot": "8_11",       "methodology": "manual-historical"},
    {"name": "3He",       "Z": 2, "N": 1, "ell": 2, "rho": 2,
     "native_n": 3, "braid": [-1, 2, -1, 2, -1, 2],                  # L6a4
     "knot": "L_{6a4}",    "methodology": "manual-historical"},
    {"name": "6Li",       "Z": 3, "N": 3, "ell": 2, "rho": 5,
     "native_n": None, "braid": None,
     "knot": "K_{11a259}", "methodology": "deprecated-volume-match"},
    {"name": "7Li",       "Z": 3, "N": 4, "ell": 2, "rho": 5,
     "native_n": None, "braid": None,
     "knot": "L_{11a62}",  "methodology": "deprecated-volume-match"},
]


def analyze_atom(entry: dict) -> dict:
    """Run the braid through gb_filtration_jet_tracker; emit
    structural data per atom for ρ-rule pattern-finding."""
    out = dict(entry)
    if entry["braid"] is None:
        out["filtration_shape"] = None
        out["max_grade"] = None
        out["n_jet_steps"] = None
        out["n_hecke_relations_fired"] = None
        out["n_distinct_perms_in_support"] = None
        return out
    n = entry["native_n"]
    word = entry["braid"]
    # Reduce in-process via right-multiplication
    e = HeckeElement.identity(n)
    for i in word:
        if i > 0:
            e = e.right_mul_T(i)
        else:
            e = e.right_mul_T_inv(-i)
    cert = e.filtration_certificate()
    out["filtration_shape"] = {int(g): len(v) for g, v in cert.items()}
    out["max_grade"] = max(cert.keys()) if cert else 0
    out["n_jet_steps"] = len(e.jet_log)
    out["n_hecke_relations_fired"] = sum(
        1 for ev in e.jet_log if ev.relation == "hecke-quadratic"
    )
    out["n_distinct_perms_in_support"] = sum(out["filtration_shape"].values())
    out["mahonian_max_grade"] = (n * (n - 1)) // 2
    return out


def main():
    base = Path(__file__).parent
    out_path = base / "rho-z-n-scan.witness.json"

    print("══════════════════════════════════════════════════════════════════════")
    print("  ρ(Z, N) structural-rule exploration scan")
    print("══════════════════════════════════════════════════════════════════════")
    print()
    rows = []
    for entry in REGISTRY:
        row = analyze_atom(entry)
        rows.append(row)
        if row["filtration_shape"] is None:
            print(f"  {row['name']:8s}  ρ = {row['rho']}  "
                  f"(braid not available)")
            continue
        n = row["native_n"]
        max_g = row["max_grade"]
        max_possible = row["mahonian_max_grade"]
        n_perms = row["n_distinct_perms_in_support"]
        n_hecke = row["n_hecke_relations_fired"]
        n_jet = row["n_jet_steps"]
        print(
            f"  {row['name']:8s}  ρ = {row['rho']}  "
            f"H_{n} (max ℓ = {max_g}/{max_possible})  "
            f"|supp(T_w)| = {n_perms},  "
            f"#hecke = {n_hecke}/{n_jet} = {n_hecke/n_jet*100:.1f}%"
        )

    # Look for correlations
    print()
    print("──── potential ρ correlates ────")
    print()
    print(f"  {'name':8s} {'ρ':>2s}  {'maxgrd':>6s}  {'|supp|':>6s}  "
          f"{'#hecke':>6s}  {'#jet':>5s}  {'#hecke/|supp|':>13s}")
    for row in rows:
        if row["filtration_shape"] is None:
            continue
        ratio = (row["n_hecke_relations_fired"] /
                 row["n_distinct_perms_in_support"]
                 if row["n_distinct_perms_in_support"] > 0 else 0)
        print(
            f"  {row['name']:8s} {row['rho']:>2d}  "
            f"{row['max_grade']:>6d}  {row['n_distinct_perms_in_support']:>6d}  "
            f"{row['n_hecke_relations_fired']:>6d}  "
            f"{row['n_jet_steps']:>5d}  "
            f"{ratio:>13.3f}"
        )

    witness = {
        "computation": "rho-z-n-scan",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "description": (
            "Exploration scan of structural diagnostics per atom in the "
            "registry, surfacing potential correlates of the historical "
            "ρ prefactor.  Does NOT prescribe a rule — surfaces data "
            "for pattern-finding."
        ),
        "registry": REGISTRY,
        "rows": rows,
        "open_question": (
            "Derive ρ(Z, N) as a function of the canonical T_w's "
            "Wedderburn-block multiplicity structure.  Pattern observed: "
            "ρ ∈ {1, 2} for ℓ ≤ 2 light atoms, ρ = 5 for ⁶Li/⁷Li (the "
            "latter from deprecated volume-match search; not principled). "
            "R5-full SDP solver in claude/r5-full-sdp-solver branch is "
            "required to derive ρ from first principles."
        ),
        "next_step": (
            "Once R5-full lands canonical T_w for ⁶Li / ⁷Li, the "
            "Wedderburn-block multiplicity should give ρ structurally; "
            "this scan provides the baseline data to compare against."
        ),
    }
    with open(out_path, "w") as f:
        json.dump(witness, f, indent=2, default=str)
    print(f"\n→ wrote {out_path}")


if __name__ == "__main__":
    main()
