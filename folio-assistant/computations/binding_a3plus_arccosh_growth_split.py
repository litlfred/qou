#!/usr/bin/env python3
# polynomial_q_not_applicable: derivation refinement — explicit
#   arccos(rotation) + arccosh(growth) split per cheat-sheet line
#   414.  Reads canonical witness data only.  NO fits.
"""
A≥3 binding — explicit arccos/arccosh channel split (commit 6).

# Ref: docs/audits/2026-06-02-binding-A3plus-full-theta-derivation-design.md
# Ref: docs/canonical-derivation-cheat-sheet.md §9.3 line 414
# Ref: binding_a3plus_full_theta_assembly.py (commits 2-5)

## What this script does

Commits 2-5 used |Δθ_λ| = |θ_atom − θ_free| with the witness's
pre-computed θ_λ_rad values (which use arccos for rotation
channels and arccosh for channel-flip cases).  The result:
³He +17.4 % with the volume-scaled assembly.

This commit refines the assembly by explicitly splitting EVERY
partition's contribution into:

  - **rotation piece**: arccos(r_atom) − arccos(r_free)  (clamp |r|≤1)
  - **growth piece**: arccosh(|r_atom|) − arccosh(|r_free|)  (clamp |r|≥1)

and tests three combinations:

  **V1** (sum of magnitudes — baseline match to commits 4-5):
    Δθ_λ_combined = |Δθ_rot| + |Δθ_growth|

  **V2** (sinh of growth = extensive exp-linearization):
    Δθ_λ_combined = |Δθ_rot| + sinh(|Δθ_growth|)

  Per cheat-sheet line 414 — recover exp(Vol) from linear Δtr.

  **V3** (cosh of growth − 1, even more extensive):
    Δθ_λ_combined = |Δθ_rot| + (cosh(|Δθ_growth|) − 1)

Then assembles via `B(K) = μ₀ · Vol(K_bind) · Σ y · dim · Δθ_combined`.

## Usage

    cd folio-assistant/computations
    python3 binding_a3plus_arccosh_growth_split.py
"""
from __future__ import annotations
import json
import sys
import warnings
from pathlib import Path
from datetime import datetime, timezone

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).resolve().parent))
import _path_bridge  # noqa: F401, E402

import mpmath as mp  # noqa: E402

mp.mp.dps = 50

B_AME = {
    "D":   mp.mpf("2.22456611"),
    "T":   mp.mpf("8.4817986"),
    "3He": mp.mpf("7.71804393"),
    "4He": mp.mpf("28.295674"),
}
M_E_MEV = mp.mpf("0.51099895069")
Q_0 = mp.mpf("1.10997858275138084620")
HBAR_Q = 1 - 1 / Q_0
MU_0 = M_E_MEV / (3 * (Q_0 - 1 / Q_0) / 2)

chi_for = {
    "D":   "chi-deuteron-h6-at-q0-50dps.witness.json",
    "T":   "chi-tritium-h9-at-q0-50dps.witness.json",
    "3He": "chi-helium-3-h9-at-q0-50dps.witness.json",
    "4He": "chi-helium-4-h12-at-q0-50dps.witness.json",
}

from substrate.knot_volumes import VOL_BORROMEAN_MPF, VOL_8_11_MPF
VOL_K = {
    "D":   VOL_BORROMEAN_MPF,
    "T":   VOL_8_11_MPF,
    "3He": VOL_BORROMEAN_MPF,
    "4He": 2 * VOL_BORROMEAN_MPF,
}


def load_witness(name: str) -> dict:
    return json.loads((Path(__file__).parent / name).read_text())


# ── Load per-atom θ_λ vectors + per-atom y_λ ────────────────────
w = load_witness("binding-reeb-phase-decomposition.witness.json")
per_atom_theta = w["data"]["per_atom"]

per_atom_y = {}
for atom, fname in chi_for.items():
    cw = load_witness(fname)
    y_map = {}
    for entry in cw.get("by_partition", []):
        key = "_".join(str(p) for p in entry["partition"])
        y_map[key] = mp.mpf(entry["y_lambda"])
    per_atom_y[atom] = y_map


def theta_rotation(r: mp.mpf) -> mp.mpf:
    """arccos(r) clamped to [-1, 1].  Returns 0 outside the rotation
    range (extensive growth handled separately)."""
    if r > 1:
        r = mp.mpf(1)
    elif r < -1:
        r = mp.mpf(-1)
    return mp.acos(r)


def theta_growth(r: mp.mpf) -> mp.mpf:
    """arccosh(|r|) for |r| ≥ 1; 0 otherwise."""
    abs_r = abs(r)
    if abs_r <= 1:
        return mp.mpf(0)
    return mp.acosh(abs_r)


def channel_sum(by_partition: list, y_map: dict, combine_fn) -> mp.mpf:
    """Σ_λ y_λ · dim_λ · combine_fn(|Δθ_rot|, |Δθ_growth|)."""
    s = mp.mpf(0)
    for row in by_partition:
        key = "_".join(str(p) for p in row["partition"])
        y = y_map.get(key, mp.mpf(0))
        dim = row["dim"]
        r_free = mp.mpf(repr(row.get("r_free", 0)))
        r_atom = mp.mpf(repr(row.get("r_atom", 0)))
        d_rot = abs(theta_rotation(r_atom) - theta_rotation(r_free))
        d_growth = abs(theta_growth(r_atom) - theta_growth(r_free))
        s += y * dim * combine_fn(d_rot, d_growth)
    return s


def combine_v1(d_rot, d_growth):
    """Baseline — sum of magnitudes."""
    return d_rot + d_growth


def combine_v2(d_rot, d_growth):
    """sinh of growth — exp-linearization correction."""
    return d_rot + mp.sinh(d_growth)


def combine_v3(d_rot, d_growth):
    """cosh of growth − 1 — fully extensive piece."""
    return d_rot + (mp.cosh(d_growth) - 1)


# ── Compute per-atom Σ values for each combination + assemble ───
combos = {"V1_rot_plus_growth": combine_v1,
          "V2_sinh_growth": combine_v2,
          "V3_cosh_growth_m1": combine_v3}

results = {}
for combo_name, combo_fn in combos.items():
    atom_results = {}
    for atom_key in per_atom_theta:
        bp = per_atom_theta[atom_key].get("by_partition", [])
        y_map = per_atom_y.get(atom_key, {})
        sigma = channel_sum(bp, y_map, combo_fn)
        Vol = VOL_K.get(atom_key, mp.mpf(0))
        B_pred = MU_0 * Vol * sigma
        B_exp = B_AME.get(atom_key, mp.mpf(0))
        rel_err = abs(B_pred - B_exp) / abs(B_exp) if B_exp != 0 else mp.mpf("inf")
        atom_results[atom_key] = {
            "sigma": str(sigma),
            "Vol_K_bind": str(Vol),
            "B_pred_MeV": str(B_pred),
            "B_AME_MeV": str(B_exp),
            "rel_err": str(rel_err),
            "closes_within_10pct": bool(rel_err < mp.mpf("0.10")),
        }
    results[combo_name] = atom_results

out = {
    "computation": "binding-a3plus-arccosh-growth-split",
    "auditOnly": True,
    "description": (
        "A≥3 binding — explicit arccos(rotation) + arccosh(growth) "
        "split + 3 combination forms (sum, sinh, cosh−1) tested against "
        "B_AME.  Substrate-derived: ρ = μ₀, Vol from substrate/knot_volumes, "
        "y_λ from chi-*-at-q0-50dps witnesses, θ from arccos/arccosh of r."
    ),
    "timestamp_utc": datetime.now(timezone.utc).isoformat(),
    "substrate_constants": {
        "q_0": str(Q_0), "hbar_q": str(HBAR_Q),
        "m_e_MeV": str(M_E_MEV), "mu_0_MeV": str(MU_0),
    },
    "Vol_per_atom": {k: str(v) for k, v in VOL_K.items()},
    "combination_variants": results,
}

out_path = Path(__file__).parent / "binding-a3plus-arccosh-growth-split.witness.json"
with open(out_path, "w") as fp:
    json.dump(out, fp, indent=2)

print("=" * 72)
print(" A≥3 binding — explicit arccos/arccosh growth split (commit 6)")
print("=" * 72)
print(f"  ρ = μ₀ = {float(MU_0):.4f} MeV  (substrate-derived)")
print()
print(f"  {'combination':<24s}", end="")
for atom in ["D", "T", "3He", "4He"]:
    print(f"  {atom:>10s}", end="")
print()
for combo_name, atom_results in results.items():
    print(f"  {combo_name:<24s}", end="")
    for atom in ["D", "T", "3He", "4He"]:
        r = atom_results.get(atom)
        if r:
            rel_err = float(mp.mpf(r["rel_err"]))
            print(f"  {rel_err*100:>+8.1f}%", end="")
        else:
            print(f"  {'n/a':>10s}", end="")
    print()
print()
print(f"  Witness: {out_path}")
