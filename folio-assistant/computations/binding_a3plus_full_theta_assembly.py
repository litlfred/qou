#!/usr/bin/env python3
# polynomial_q_not_applicable: derivation campaign per cheat-sheet
#   §9.3 line 414.  Carries the per-rep q-Reeb phase θ_λ at full
#   (non-linearized) order across D/T/³He/⁴He and assembles the
#   binding via the canonical chain.  Reads canonical witness data
#   only.  NO fits.
"""
A≥3 absolute binding — full-order θ_λ assembly (commit 2 of design plan).

# Ref: docs/audits/2026-06-02-binding-A3plus-full-theta-derivation-design.md
# Ref: docs/audits/2026-05-28-binding-endomorphism-analogy.md §A≥3 campaign
# Ref: docs/canonical-derivation-cheat-sheet.md §9.3 (the open gate)

## The lead

Per `2026-05-28-binding-endomorphism-analogy.md` §"The rotation-phase
lead", the Markov-weighted Reeb-phase sum

  Σ_λ y_λ · dim_λ · |Δθ_λ|

is the **first extensive observable** that doesn't collapse per atom
A.  The phenomenological scale `ρ_need = B_AME / Σ` is

  | atom | ρ_need (MeV/rad) |
  |------|------------------|
  |  D   | 14.7             |
  |  T   | 18.3             |
  | ³He  | 18.7             |
  | ⁴He  | 54.8             |

The **A=3 mirror pair agrees to 2 % with no fit** — strongest derived
binding observable to date.  Open: derive ρ from the substrate.

## What this script does

1. **Reproduce** the ρ_need values from
   `binding-reeb-phase-decomposition.witness.json` per-λ `by_partition`
   vectors + the AME experimental binding energies.

2. **Decompose by channel**: split the Σ into rotation channels
   (|r_λ| ≤ 1, contribute via arccos(r_λ)) vs growth channels
   (|r_λ| > 1, contribute via arccosh(|r_λ|)).  The audit's
   "extensive observable" finding is driven by growth-channel
   content per `binding-reeb-phase-decomposition.witness.json::
   growth_mass_*` (free grows 16.5 → 93 → 153 → 1504 D → ⁴He).

3. **Test two substrate-derived ρ candidates** (NO fit):
   - **ρ_v1 = m_e** = 0.510998... MeV (electron mass calibration).
     The "binding endomorphism" path B = m_e · Vol(K) · Δtr uses
     m_e directly as the per-crossing mass scale.
   - **ρ_v2 = μ₀ = m_e / (3·(q − q⁻¹)/2)** ≈ 1.6295 MeV.
     The "q-Hamiltonian rotational" path
     B = μ₀ · ℏ_q · J_q²(j=n/2) uses μ₀ derived per-crossing.

   For each candidate ρ, compute B_pred(K) = ρ · Σ y_λ dim_λ |Δθ_λ|
   and compare to B_AME.

This is a DIAGNOSTIC, derivation-campaign starting point.  If
neither ρ_v1 nor ρ_v2 closes, the next commit (commit 3 per design
plan) adds the growth-channel arccosh contribution to the sum.
NO fits at any step.

## Usage

    cd folio-assistant/computations
    python3 binding_a3plus_full_theta_assembly.py

Emits: binding-a3plus-full-theta-assembly.witness.json
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

# Constants — from the canonical chain ----------------------------------
try:
    from substrate._precision import set_compute_dps
    set_compute_dps()
except Exception:
    mp.mp.dps = 50

# Experimental AME bindings (CODATA / AME2020)
B_AME = {
    "D":   mp.mpf("2.22456611"),
    "T":   mp.mpf("8.4817986"),
    "3He": mp.mpf("7.71804393"),
    "4He": mp.mpf("28.295674"),
}

M_E_MEV = mp.mpf("0.51099895069")  # electron mass (CAL-1)

# Substrate-derived q_0 (50dps, proton-pin)
Q_0_STR = "1.10997858275138084620"  # truncated; will load from witness


def load_witness(name: str) -> dict:
    return json.loads((Path(__file__).parent / name).read_text())


# ── Load per-atom per-λ θ_λ vectors ──────────────────────────────
w = load_witness("binding-reeb-phase-decomposition.witness.json")
per_atom = w["data"]["per_atom"]

# ── Compute the rotation-phase-lead sum Σ y_λ · dim_λ · |Δθ_λ| ───
# (carries both rotation and growth channels — by_partition contains
# both, classified via `channel_free` / `channel_atom`.)
per_atom_sums = {}
for atom_key, atom_data in per_atom.items():
    bp = atom_data.get("by_partition", [])
    sum_full = mp.mpf(0)
    sum_rotation_only = mp.mpf(0)
    sum_growth_only = mp.mpf(0)
    rows = []
    for row in bp:
        dim = row["dim"]
        # Handle channel_flip cases where delta_theta_rad is None.
        dtheta_raw = row.get("delta_theta_rad")
        if dtheta_raw is None:
            # Channel-flip: rotation ↔ growth. For full-order θ_λ,
            # combine arccos (rotation side) with arccosh (growth
            # side) into a complex/magnitude form. Conservative: use
            # |Δθ| = |θ_atom − θ_free| where the missing piece is
            # taken from `r_free` / `r_atom` magnitudes directly.
            r_free = abs(mp.mpf(repr(row.get("r_free", 0))))
            r_atom = abs(mp.mpf(repr(row.get("r_atom", 0))))
            # Free / atom phases via |r| → arccos for |r|≤1 else arccosh.
            def theta_of(r: mp.mpf) -> mp.mpf:
                if r <= 1:
                    return mp.acos(r)
                return mp.acosh(r)  # imaginary part magnitude
            theta_free = theta_of(r_free)
            theta_atom = theta_of(r_atom)
            delta_theta = theta_atom - theta_free
        else:
            delta_theta = mp.mpf(dtheta_raw)
        abs_delta_theta = abs(delta_theta)
        weight = dim  # placeholder until y_λ added
        contrib = weight * abs_delta_theta
        sum_full += contrib
        ch_free = row.get("channel_free", "")
        ch_atom = row.get("channel_atom", "")
        if "growth" in (ch_free + ch_atom):
            sum_growth_only += contrib
        else:
            sum_rotation_only += contrib
        rows.append({
            "partition": "_".join(str(p) for p in row["partition"]),
            "dim": dim,
            "delta_theta_rad": str(delta_theta),
            "abs_delta_theta_rad": str(abs_delta_theta),
            "channel_free": ch_free,
            "channel_atom": ch_atom,
            "channel_flip": row.get("channel_flip", False),
            "contrib_dim_x_abs_dtheta": str(contrib),
        })
    per_atom_sums[atom_key] = {
        "sum_dim_abs_dtheta": str(sum_full),
        "sum_rotation_only": str(sum_rotation_only),
        "sum_growth_only": str(sum_growth_only),
        "by_partition": rows,
    }

# ── Substrate-derived ρ candidates ───────────────────────────────
q_0 = mp.mpf(Q_0_STR)
hbar_q = 1 - 1 / q_0  # ℏ_q = 1 − q⁻¹
mu_0 = M_E_MEV / (3 * (q_0 - 1 / q_0) / 2)  # μ₀ = m_e / (3·(q−q⁻¹)/2)

rho_candidates = {
    "rho_v1_m_e": M_E_MEV,
    "rho_v2_mu_0": mu_0,
    "rho_v3_m_e_x_hbar_q": M_E_MEV * hbar_q,
    "rho_v4_mu_0_x_hbar_q": mu_0 * hbar_q,
}

# ── Test each ρ against B_AME ────────────────────────────────────
results = {}
for rho_name, rho in rho_candidates.items():
    per_atom_results = {}
    for atom_key in per_atom:
        if atom_key not in B_AME:
            continue
        sum_S = mp.mpf(per_atom_sums[atom_key]["sum_dim_abs_dtheta"])
        B_pred = rho * sum_S
        B_exp = B_AME[atom_key]
        rel_err = abs(B_pred - B_exp) / abs(B_exp)
        per_atom_results[atom_key] = {
            "sum_S": str(sum_S),
            "B_pred_MeV": str(B_pred),
            "B_AME_MeV": str(B_exp),
            "rel_err": str(rel_err),
            "closes_within_10pct": bool(rel_err < mp.mpf("0.10")),
        }
    results[rho_name] = {
        "rho_value_MeV": str(rho),
        "per_atom": per_atom_results,
    }

# ── Reference: empirical ρ_need from audit (proves scaffold reads right) ──
rho_need_audit = {
    "D":   mp.mpf("14.7"),
    "T":   mp.mpf("18.3"),
    "3He": mp.mpf("18.7"),
    "4He": mp.mpf("54.8"),
}

rho_need_reproduced = {}
for atom in B_AME:
    if atom not in per_atom_sums:
        continue
    sum_S = mp.mpf(per_atom_sums[atom]["sum_dim_abs_dtheta"])
    if sum_S == 0:
        continue
    rho_need_local = B_AME[atom] / sum_S
    diff = abs(rho_need_local - rho_need_audit.get(atom, mp.mpf(0)))
    rho_need_reproduced[atom] = {
        "rho_need_computed": str(rho_need_local),
        "rho_need_audit": str(rho_need_audit.get(atom, "n/a")),
        "diff_vs_audit": str(diff),
    }

out = {
    "computation": "binding-a3plus-full-theta-assembly",
    "auditOnly": True,
    "description": (
        "A≥3 absolute binding derivation campaign — full-order θ_λ "
        "assembly (commit 2 of design plan).  Reproduces ρ_need lead "
        "from audit 2026-05-28 §A≥3 + tests 4 substrate-derived "
        "ρ candidates (m_e, μ₀, with/without ℏ_q).  NO fits.  Uses "
        "placeholder y_λ = dim_λ until y_λ-per-atom cross-witness "
        "lookup lands in commit 3."
    ),
    "timestamp_utc": datetime.now(timezone.utc).isoformat(),
    "inputs": {
        "binding_reeb_witness": "binding-reeb-phase-decomposition.witness.json",
    },
    "substrate_constants": {
        "q_0": str(q_0),
        "hbar_q": str(hbar_q),
        "m_e_MeV": str(M_E_MEV),
        "mu_0_MeV": str(mu_0),
    },
    "rho_need_reproduced": rho_need_reproduced,
    "per_atom_sums": per_atom_sums,
    "rho_candidate_tests": results,
}

out_path = Path(__file__).parent / "binding-a3plus-full-theta-assembly.witness.json"
with open(out_path, "w") as fp:
    json.dump(out, fp, indent=2)

print("=" * 72)
print(" A≥3 binding — full-order θ_λ assembly (commit 2)")
print("=" * 72)
print(f"  q_0 = {float(q_0):.6f}")
print(f"  ℏ_q = 1 − q⁻¹ = {float(hbar_q):.6f}")
print(f"  m_e = {float(M_E_MEV):.6f} MeV")
print(f"  μ₀  = m_e / (3·(q−q⁻¹)/2) = {float(mu_0):.6f} MeV")
print()
print("  Σ_λ dim_λ · |Δθ_λ| per atom  (placeholder — y_λ pending commit 3):")
for atom, s in per_atom_sums.items():
    print(f"    {atom:>4s}  sum_full = {float(mp.mpf(s['sum_dim_abs_dtheta'])):>9.4f}  "
          f"rot = {float(mp.mpf(s['sum_rotation_only'])):>9.4f}  "
          f"growth = {float(mp.mpf(s['sum_growth_only'])):>9.4f}")
print()
print("  ρ_need (audit doc / 2026-05-28) vs computed at this commit:")
for atom, rep in rho_need_reproduced.items():
    print(f"    {atom:>4s}  audit = {rep['rho_need_audit']:>6s}  "
          f"computed = {float(mp.mpf(rep['rho_need_computed'])):>9.4f}  "
          f"(diff {float(mp.mpf(rep['diff_vs_audit'])):>+8.4f})")
print()
print("  Substrate-derived ρ candidates vs B_AME:")
print(f"    {'rho_name':<28s} {'ρ MeV':>10s}", end="")
for atom in ["D", "T", "3He", "4He"]:
    print(f"  {atom:>10s}", end="")
print()
for rho_name, rdata in results.items():
    rho = float(mp.mpf(rdata["rho_value_MeV"]))
    print(f"    {rho_name:<28s} {rho:>10.4f}", end="")
    for atom in ["D", "T", "3He", "4He"]:
        atom_data = rdata["per_atom"].get(atom)
        if atom_data:
            rel_err = float(mp.mpf(atom_data["rel_err"]))
            print(f"  {rel_err*100:>+8.1f}%", end="")
        else:
            print(f"  {'n/a':>10s}", end="")
    print()
print()
print(f"  Witness: {out_path}")
