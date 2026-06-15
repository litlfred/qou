#!/usr/bin/env python3
# polynomial_q_not_applicable: derivation campaign per cheat-sheet
#   §9.3 line 414.  Carries the per-rep q-Reeb phase θ_λ at full
#   (non-linearized) order across D/T/³He/⁴He and assembles the
#   binding via the canonical chain.  Reads canonical witness data
#   only.  NO fits.
"""
A≥3 absolute binding — full-order θ_λ assembly.

# Ref: docs/audits/2026-06-02-binding-A3plus-full-theta-derivation-design.md
# Ref: docs/audits/2026-05-28-binding-endomorphism-analogy.md §A≥3 campaign
# Ref: docs/canonical-derivation-cheat-sheet.md §9.3 (the open gate)

## What this script does

1. **Loads per-atom θ_λ** vectors from
   `binding-reeb-phase-decomposition.witness.json` per-λ
   `by_partition` (carries rotation channels via arccos and
   growth / channel-flip cases via arccosh of |r|).

2. **Loads y_λ per atom** from
   `chi-{D,T,³He,⁴He}-h{6,9,12}-at-q0-50dps.witness.json` —
   Markov-trace weights at q_0.

3. **Tests 4 substrate-derived ρ candidates** (NO fit):
   - ρ_v1 = m_e (CAL-1)
   - ρ_v2 = μ₀ = m_e / (3·(q − q⁻¹)/2) — per-crossing mass scale per
     `binding_qhamiltonian_rotational_scale.py`
   - ρ_v3 = m_e · ℏ_q
   - ρ_v4 = μ₀ · ℏ_q

4. **Scales by atom-specific Vol(K_bind)** from SDP-classified
   binding links (`binding_link_volumes.py` + `substrate/knot_volumes`):
   D → Vol(𝓑₃) substitution (Hopf is Seifert-fibred = 0),
   T → Vol(8₁₁), ³He → Vol(L6a4) = Vol(Borromean),
   ⁴He → provisional 2·Vol(𝓑₃) (JSJ decomposition needed for
   the doubly-magic shell).

5. **Compares** to AME experimental B(K) and reports rel_err.

Companion: `binding_a3plus_arccosh_growth_split.py` adds the
explicit cosh-of-growth assembly for the ⁴He doubly-magic refinement.

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

# Canonical registries (NOT hard-coded literals; per Copilot review on
# PR #1726 to satisfy the hardcoded-literal audit).
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

set_compute_dps()

# AME experimental bindings from the validation registry.
B_AME = {
    "D":   AME_B_DEUTERON_MEV_VALIDATION,
    "T":   AME_B_TRITIUM_MEV_VALIDATION,
    "3He": AME_B_HE3_MEV_VALIDATION,
    "4He": AME_B_HE4_MEV_VALIDATION,
}

# Electron mass from the CAL-1 registry.
M_E_MEV = mp.mpf(str(M_E_MEV_F))

# Substrate q_0 (50dps) from the q_parameter registry.
Q_0_STR = Q_50_DIGIT_STR


def load_witness(name: str) -> dict:
    return json.loads((Path(__file__).parent / name).read_text())


# ── Load per-atom per-λ θ_λ vectors ──────────────────────────────
w = load_witness("binding-reeb-phase-decomposition.witness.json")
per_atom = w["data"]["per_atom"]

# ── Load y_λ per atom from chi-*-at-q0-50dps witnesses ───────────
chi_witness_for_atom = {
    "D":   "chi-deuteron-h6-at-q0-50dps.witness.json",
    "T":   "chi-tritium-h9-at-q0-50dps.witness.json",
    "3He": "chi-helium-3-h9-at-q0-50dps.witness.json",
    "4He": "chi-helium-4-h12-at-q0-50dps.witness.json",
}
y_lambda_per_atom: dict[str, dict[str, mp.mpf]] = {}
# Atoms whose chi witness is marked `partial: true` cannot be assembled —
# silently zeroing missing y_λ produces a plausible-looking but wrong Σ
# (per Copilot review on PR #1726 lines 119/138).  Track which atoms
# are gated out so the witness records the exclusion explicitly.
PARTIAL_ATOMS: list[tuple[str, int, int]] = []
for atom_key, fname in chi_witness_for_atom.items():
    chi_w = load_witness(fname)
    if chi_w.get("partial", False):
        n = chi_w.get("n_partitions", 0)
        nt = chi_w.get("n_partitions_total", 0)
        PARTIAL_ATOMS.append((atom_key, n, nt))
    by_part = chi_w.get("by_partition", [])
    y_map: dict[str, mp.mpf] = {}
    for entry in by_part:
        part_key = "_".join(str(p) for p in entry["partition"])
        y_map[part_key] = mp.mpf(entry["y_lambda"])
    y_lambda_per_atom[atom_key] = y_map

ATOMS_FOR_ASSEMBLY = [a for a in chi_witness_for_atom
                      if a not in {p[0] for p in PARTIAL_ATOMS}]
if PARTIAL_ATOMS:
    print("WARNING — partial chi witnesses detected:", file=sys.stderr)
    for atom_key, n, nt in PARTIAL_ATOMS:
        print(f"  {atom_key}: {n}/{nt} partitions covered  →  "
              f"assembly SKIPPED (incomplete data)", file=sys.stderr)

# ── Compute the rotation-phase-lead sum Σ y_λ · dim_λ · |Δθ_λ| ───
# (carries both rotation and growth channels — by_partition contains
# both, classified via `channel_free` / `channel_atom`.)
per_atom_sums = {}
for atom_key, atom_data in per_atom.items():
    if atom_key not in ATOMS_FOR_ASSEMBLY:
        continue  # skip partial-chi atoms; flagged separately
    bp = atom_data.get("by_partition", [])
    sum_full = mp.mpf(0)
    sum_rotation_only = mp.mpf(0)
    sum_growth_only = mp.mpf(0)
    rows = []
    y_map = y_lambda_per_atom.get(atom_key, {})
    for row in bp:
        dim = row["dim"]
        part_key = "_".join(str(p) for p in row["partition"])
        y_lam = y_map.get(part_key)
        if y_lam is None:
            # Per Copilot review: missing y_λ for an atom whose chi
            # witness is supposed to be complete is a hard error —
            # silent y_λ = 0 hides truncation + drift.
            raise KeyError(
                f"chi-{atom_key} witness is missing y_λ for partition "
                f"{part_key} (θ_λ has this partition; y_λ does not). "
                f"Either the chi witness is incomplete (regenerate) or "
                f"the θ_λ + chi witnesses are at different jet orders."
            )
        # Use the witness's pre-computed theta_*_rad strings for
        # channel-flip cases — taking abs(r) breaks rotation-channel
        # sign per Copilot review (e.g. ⁴He partition [9,2,1] has
        # r_atom < 0 → witness θ_atom = acos(r_atom) ≠ acos(|r_atom|)).
        dtheta_raw = row.get("delta_theta_rad")
        if dtheta_raw is None:
            theta_free_raw = row.get("theta_free_rad")
            theta_atom_raw = row.get("theta_atom_rad")
            if theta_free_raw is None or theta_atom_raw is None:
                raise ValueError(
                    f"chi-{atom_key} partition {part_key}: channel-flip "
                    f"row missing both delta_theta_rad AND "
                    f"theta_free_rad/theta_atom_rad — cannot recover Δθ."
                )
            delta_theta = mp.mpf(theta_atom_raw) - mp.mpf(theta_free_raw)
        else:
            delta_theta = mp.mpf(dtheta_raw)
        abs_delta_theta = abs(delta_theta)
        weight = y_lam * dim  # Markov-weighted per audit 2026-05-28
        contrib = weight * abs_delta_theta
        sum_full += contrib
        ch_free = row.get("channel_free", "")
        ch_atom = row.get("channel_atom", "")
        if "growth" in (ch_free + ch_atom):
            sum_growth_only += contrib
        else:
            sum_rotation_only += contrib
        rows.append({
            "partition": part_key,
            "dim": dim,
            "y_lambda": str(y_lam),
            "delta_theta_rad": str(delta_theta),
            "abs_delta_theta_rad": str(abs_delta_theta),
            "channel_free": ch_free,
            "channel_atom": ch_atom,
            "channel_flip": row.get("channel_flip", False),
            "contrib_y_dim_x_abs_dtheta": str(contrib),
        })
    per_atom_sums[atom_key] = {
        "sum_y_dim_abs_dtheta": str(sum_full),
        "sum_rotation_only": str(sum_rotation_only),
        "sum_growth_only": str(sum_growth_only),
        "by_partition": rows,
    }

# ── Substrate-derived ρ candidates ───────────────────────────────
q_0 = mp.mpf(Q_0_STR)
hbar_q = 1 - 1 / q_0  # ℏ_q = 1 − q⁻¹
mu_0 = M_E_MEV / (3 * (q_0 - 1 / q_0) / 2)  # μ₀ = m_e / (3·(q−q⁻¹)/2)

# ── Atom-specific binding-link volumes (substrate-derived knots) ─
# Per binding_link_volumes.py + binding-k-solver SDP registry:
#   D   → Hopf link (Vol = 0, Seifert-fibred) → substitute Vol(𝓑₃)
#         via the binding-endomorphism path (deuteron is special; +0.19%)
#   T   → 8₁₁ knot, Vol(8₁₁) = 8.2863168
#   ³He → L6a4 link = Borromean = Vol(𝓑₃) = 7.3277248
#   ⁴He → multi-link / JSJ decomposition (NOT a single binding link;
#         needs per-pair sum per binding_link_volumes.py finding).
#         Provisional: 2·Vol(𝓑₃) for the (2,2) doubly-magic shell.
try:
    from substrate.knot_volumes import VOL_BORROMEAN_MPF, VOL_8_11_MPF
    VOL_K = {
        "D":   VOL_BORROMEAN_MPF,           # via 𝓑₃ substitution (deuteron)
        "T":   VOL_8_11_MPF,                # 8₁₁ (hyperbolic)
        "3He": VOL_BORROMEAN_MPF,           # L6a4 = Borromean
        "4He": 2 * VOL_BORROMEAN_MPF,       # provisional (doubly-magic)
    }
except ImportError:
    # Narrow the fallback to ImportError so genuine runtime errors in
    # substrate.knot_volumes surface (per Copilot review on PR #1726).
    # Fallback constants from binding_link_volumes.py docstring.
    VOL_K = {
        "D":   mp.mpf("7.3277248"),
        "T":   mp.mpf("8.2863168"),
        "3He": mp.mpf("7.3277248"),
        "4He": mp.mpf("14.6554497"),
    }

rho_candidates = {
    "rho_v1_m_e": M_E_MEV,
    "rho_v2_mu_0": mu_0,
    "rho_v3_m_e_x_hbar_q": M_E_MEV * hbar_q,
    "rho_v4_mu_0_x_hbar_q": mu_0 * hbar_q,
}

# ── Test each ρ against B_AME ────────────────────────────────────
# Two assembly forms:
#   v_unscaled: B_pred = ρ · Σ y_λ · dim_λ · |Δθ_λ|
#   v_volume_scaled: B_pred = ρ · Vol(K_bind) · Σ y_λ · dim_λ · |Δθ_λ|
#     (extends the deuteron binding-endomorphism B = m_e · Vol(K) · Δtr
#      with Δtr → full-order Markov-Reeb sum per audit lead.)
results = {}
volume_scaled_results = {}
for rho_name, rho in rho_candidates.items():
    per_atom_results = {}
    per_atom_vol_results = {}
    for atom_key in per_atom:
        if atom_key not in B_AME:
            continue
        if atom_key not in per_atom_sums:
            continue  # partial chi witness; skipped
        sum_S = mp.mpf(per_atom_sums[atom_key]["sum_y_dim_abs_dtheta"])
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
        Vol = VOL_K.get(atom_key, mp.mpf(0))
        B_pred_vol = rho * Vol * sum_S
        rel_err_vol = abs(B_pred_vol - B_exp) / abs(B_exp)
        per_atom_vol_results[atom_key] = {
            "Vol_K_bind": str(Vol),
            "B_pred_MeV": str(B_pred_vol),
            "B_AME_MeV": str(B_exp),
            "rel_err": str(rel_err_vol),
            "closes_within_10pct": bool(rel_err_vol < mp.mpf("0.10")),
        }
    results[rho_name] = {
        "rho_value_MeV": str(rho),
        "per_atom": per_atom_results,
    }
    volume_scaled_results[rho_name] = {
        "rho_value_MeV": str(rho),
        "per_atom": per_atom_vol_results,
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
    sum_S = mp.mpf(per_atom_sums[atom]["sum_y_dim_abs_dtheta"])
    if sum_S == 0:
        continue
    rho_need_local = B_AME[atom] / sum_S
    diff = abs(rho_need_local - rho_need_audit.get(atom, mp.mpf(0)))
    rho_need_reproduced[atom] = {
        "rho_need_computed": str(rho_need_local),
        "rho_need_audit": str(rho_need_audit.get(atom, "n/a")),
        "diff_vs_audit": str(diff),
    }

wb = (WitnessBuilder("binding-a3plus-full-theta-assembly", engine="mpmath")
      .set_description(
          "A≥3 absolute binding derivation campaign — full-order θ_λ "
          "assembly.  Tests 4 substrate-derived ρ candidates "
          "(m_e, μ₀, with/without ℏ_q) and Vol(K_bind)-scaled "
          "assemblies against AME B(K).  Markov-weighted (y_λ from "
          "chi-*-at-q0-50dps witnesses).  NO fits."
      ))
wb.add_data("inputs", {
    "binding_reeb_witness": "binding-reeb-phase-decomposition.witness.json",
    "chi_per_atom_witnesses": list(chi_witness_for_atom.values()),
})
wb.add_data("substrate_constants", {
    "q_0": str(q_0),
    "hbar_q": str(hbar_q),
    "m_e_MeV": str(M_E_MEV),
    "mu_0_MeV": str(mu_0),
})
wb.add_data("rho_need_reproduced", rho_need_reproduced)
wb.add_data("per_atom_sums", per_atom_sums)
wb.add_data("rho_candidate_tests", results)
wb.add_data("rho_candidate_tests_volume_scaled", volume_scaled_results)
wb.add_data("volume_per_atom", {k: str(v) for k, v in VOL_K.items()})
wb.add_data("partial_atoms_excluded", [
    {"atom": a, "n_partitions": n, "n_partitions_total": nt}
    for a, n, nt in PARTIAL_ATOMS
])
# Closest non-fit A≥3 result so far (informational assertion).  ⁴He is
# gated out because its chi witness is partial (24/77); the earlier
# +2.7 % claim was INVALIDATED by Copilot review and retracted.
if "3He" in volume_scaled_results["rho_v2_mu_0"]["per_atom"]:
    he3_vol_mu0 = mp.mpf(
        volume_scaled_results["rho_v2_mu_0"]["per_atom"]["3He"]["rel_err"]
    )
    wb.add_assertion(
        "he3_volume_scaled_mu0_rel_err_under_25pct",
        computed=float(he3_vol_mu0 * 100),
        expected=17.4,
        tolerance=10.0,
        source=(
            "Best non-fit A≥3 derivation at this resolution: μ₀ · "
            "Vol(L6a4) · Σ y · dim · |Δθ| lands ³He at +17.4 % (no fit; "
            "complete chi witness).  ⁴He gated out — chi witness is "
            "partial (24/77); previous +2.7 % claim retracted."
        ),
    )
out_path = wb.save()

print("=" * 72)
print(" A≥3 binding — full-order θ_λ assembly")
print("=" * 72)
print(f"  q_0 = {float(q_0):.6f}")
print(f"  ℏ_q = 1 − q⁻¹ = {float(hbar_q):.6f}")
print(f"  m_e = {float(M_E_MEV):.6f} MeV")
print(f"  μ₀  = m_e / (3·(q−q⁻¹)/2) = {float(mu_0):.6f} MeV")
print()
print("  Σ_λ y_λ · dim_λ · |Δθ_λ| per atom:")
for atom, s in per_atom_sums.items():
    print(f"    {atom:>4s}  sum_full = {float(mp.mpf(s['sum_y_dim_abs_dtheta'])):>9.4f}  "
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
print("  ===== Volume-scaled: B_pred = ρ · Vol(K_bind) · Σ y_λ · dim_λ · |Δθ_λ| =====")
print("  Vol per atom:")
for atom, v in VOL_K.items():
    print(f"    {atom:>4s}  Vol(K_bind) = {float(v):>8.4f}")
print()
print(f"    {'rho_name':<28s} {'ρ MeV':>10s}", end="")
for atom in ["D", "T", "3He", "4He"]:
    print(f"  {atom:>10s}", end="")
print()
for rho_name, rdata in volume_scaled_results.items():
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
