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

    cd computations
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

# Canonical registries (NOT hard-coded literals; per Copilot review on
# PR #1726).
from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from experimental_constants import M_E_MEV as M_E_MEV_F  # noqa: E402
from codata_constants import (  # noqa: E402
    AME_B_DEUTERON_MEV_VALIDATION,
    AME_B_TRITIUM_MEV_VALIDATION,
    AME_B_HE3_MEV_VALIDATION,
    AME_B_HE4_MEV_VALIDATION,
)
from witness_base import WitnessBuilder  # noqa: E402
from substrate.knot_volumes import VOL_BORROMEAN_MPF, VOL_8_11_MPF  # noqa: E402

set_compute_dps()

B_AME = {
    "D":   AME_B_DEUTERON_MEV_VALIDATION,
    "T":   AME_B_TRITIUM_MEV_VALIDATION,
    "3He": AME_B_HE3_MEV_VALIDATION,
    "4He": AME_B_HE4_MEV_VALIDATION,
}
M_E_MEV = mp.mpf(str(M_E_MEV_F))
Q_0 = mp.mpf(Q_50_DIGIT_STR)
HBAR_Q = 1 - 1 / Q_0
MU_0 = M_E_MEV / (3 * (Q_0 - 1 / Q_0) / 2)

chi_for = {
    "D":   "chi-deuteron-h6-at-q0-50dps.witness.json",
    "T":   "chi-tritium-h9-at-q0-50dps.witness.json",
    "3He": "chi-helium-3-h9-at-q0-50dps.witness.json",
    "4He": "chi-helium-4-h12-at-q0-50dps.witness.json",
}

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
# Gate out atoms whose chi witness is `partial: true` — silently zeroing
# missing y_λ produces a plausible-looking but wrong Σ (per Copilot
# review on PR #1726 lines 115/142).
PARTIAL_ATOMS: list[tuple[str, int, int]] = []
for atom, fname in chi_for.items():
    cw = load_witness(fname)
    if cw.get("partial", False):
        n = cw.get("n_partitions", 0)
        nt = cw.get("n_partitions_total", 0)
        PARTIAL_ATOMS.append((atom, n, nt))
    y_map = {}
    for entry in cw.get("by_partition", []):
        key = "_".join(str(p) for p in entry["partition"])
        y_map[key] = mp.mpf(entry["y_lambda"])
    per_atom_y[atom] = y_map

ATOMS_FOR_ASSEMBLY = [a for a in chi_for
                      if a not in {p[0] for p in PARTIAL_ATOMS}]
if PARTIAL_ATOMS:
    print("WARNING — partial chi witnesses detected:", file=sys.stderr)
    for atom, n, nt in PARTIAL_ATOMS:
        print(f"  {atom}: {n}/{nt} partitions covered  →  "
              f"assembly SKIPPED (incomplete data)", file=sys.stderr)


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


def channel_sum(by_partition: list, y_map: dict, combine_fn,
                atom_label: str) -> mp.mpf:
    """Σ_λ y_λ · dim_λ · combine_fn(|Δθ_rot|, |Δθ_growth|).

    Raises KeyError if any partition in by_partition lacks a y_λ entry
    — silent y_λ = 0 fallbacks hide truncation + drift (per Copilot
    review on PR #1726).
    """
    s = mp.mpf(0)
    for row in by_partition:
        key = "_".join(str(p) for p in row["partition"])
        if key not in y_map:
            raise KeyError(
                f"chi-{atom_label} witness is missing y_λ for partition "
                f"{key} (θ_λ has this partition; y_λ does not). "
                f"Regenerate the chi witness or align jet orders."
            )
        y = y_map[key]
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
        if atom_key not in ATOMS_FOR_ASSEMBLY:
            continue  # skip partial-chi atoms; flagged separately
        bp = per_atom_theta[atom_key].get("by_partition", [])
        y_map = per_atom_y.get(atom_key, {})
        sigma = channel_sum(bp, y_map, combo_fn, atom_key)
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

wb = (WitnessBuilder("binding-a3plus-arccosh-growth-split", engine="mpmath")
      .set_description(
          "A≥3 binding — explicit arccos(rotation) + arccosh(growth) "
          "split + 3 combination forms (sum, sinh, cosh−1) tested against "
          "B_AME.  Substrate-derived: ρ = μ₀, Vol from substrate/knot_volumes, "
          "y_λ from chi-*-at-q0-50dps witnesses, θ from arccos/arccosh of r."
      ))
wb.add_data("substrate_constants", {
    "q_0": str(Q_0), "hbar_q": str(HBAR_Q),
    "m_e_MeV": str(M_E_MEV), "mu_0_MeV": str(MU_0),
})
wb.add_data("Vol_per_atom", {k: str(v) for k, v in VOL_K.items()})
wb.add_data("combination_variants", results)
# Headline assertion: cosh-growth assembly does NOT close T or ³He at
# A=3 — the earlier ⁴He +2.7 % claim was INVALIDATED by Copilot review
# on PR #1726 (⁴He chi witness is partial: true, 24/77 partitions, so
# y_λ = 0 was silently substituted for 53 partitions).  ⁴He is now
# gated out of the assembly until the chi witness is regenerated full.
# The remaining valid result on this assembly is T/³He = +99/+121 %
# under V1 — still refuted.
if "3He" in results["V1_rot_plus_growth"]:
    he3_v1_rel_err = mp.mpf(results["V1_rot_plus_growth"]["3He"]["rel_err"])
    wb.add_assertion(
        "he3_v1_rotation_plus_growth_does_not_close",
        computed=float(he3_v1_rel_err * 100),
        expected=120.6,
        tolerance=10.0,
        source=(
            "³He sum-of-rotation-plus-growth under μ₀·Vol(Borromean)·"
            "Σ y·dim·(|Δθ_rot|+|Δθ_growth|) lands at +121 % "
            "(refuted; full witness, no fit).  Open: explore non-trivial "
            "combinations + revisit ⁴He once chi-helium-4-h12 is full."
        ),
    )
out_path = wb.save()

print("=" * 72)
print(" A≥3 binding — explicit arccos/arccosh growth split")
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
