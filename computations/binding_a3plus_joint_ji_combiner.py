#!/usr/bin/env python3
# polynomial_q_not_applicable: operator-valued binding combiner probe.
#   Reads the documented per-block eigenvalue (rotation e^{iθ}, growth
#   e^{θ}) from binding-reeb-phase-decomposition.witness.json and the
#   canonical chi-*-at-q0 y_λ weights.  NO fits.
"""
A≥3 binding — joint J⊕I (rotation⊕growth) operator-valued combiner probe.

# Ref: docs/audits/2026-06-14-qbessel-joint-ji-binding-probe.md
# Ref: docs/audits/2026-06-02-binding-A3plus-full-theta-verdict.md
# Ref: binding_reeb_phase_decomposition.py  (docstring §WHY, lines 8-16,
#        documents the per-block eigenvalue structure this probe reads)

## What this script does (and why it is NOT a fit)

The full-θ assembly (binding_a3plus_full_theta_assembly.py) collapses
every Wedderburn block to the magnitude |Δθ_λ| and sums:

    S_baseline(K) = Σ_λ y_λ · dim_λ · |Δθ_λ|          (³He +17.4%, no fit)

This discards the rotation/growth (J/I) distinction.  The decomposition
script DOCUMENTS the per-block eigenvalue directly:

    rotation reps (|r_λ|=|χ_λ/dim_λ|≤1): eigenvalue e^{±iθ_λ},  r=cos θ
    growth   reps (|r_λ|>1)            : eigenvalue q^{±writhe}, |r|=cosh θ

The scalar Markov trace keeps only the real part (the character
dim·cos θ / dim·cosh θ).  The UN-collapsed per-block object — the one the
decomposition docstring (line 176) says to carry to the operator-valued
combiner — is the full eigenvalue (extensive branch):

    z_λ = e^{iθ_λ}   (rotation, unit modulus, carries phase)
        = e^{θ_λ}    (growth,   real >1, extensive q^{+writhe})

The joint binding combiner is the modulus of the Markov-weighted
difference of full eigenvalues, free → bound:

    S_joint(K) = | Σ_λ y_λ · dim_λ · (z_atom_λ − z_free_λ) |

Rotation channels add as phasors (Jacobi-Anger interference); growth
channels add as positive reals (extensive).  Channel-flip blocks
(rotation free → growth bound) are the J→I continuation made concrete.

NO tuned parameters: z_λ is the eigenvalue the decomposition documents,
y_λ from chi-*-at-q0-50dps, θ_λ/r_λ from the Reeb decomposition, ρ from
{m_e, μ₀, ×ℏ_q}, Vol from substrate/knot_volumes.

## Usage

    cd folio-assistant/computations
    python3 binding_a3plus_joint_ji_combiner.py

Emits: binding-a3plus-joint-ji-combiner.witness.json
"""
from __future__ import annotations
import json
import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).resolve().parent))
import _path_bridge  # noqa: F401, E402

import mpmath as mp  # noqa: E402

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

HERE = Path(__file__).resolve().parent

B_AME = {
    "D":   AME_B_DEUTERON_MEV_VALIDATION,
    "T":   AME_B_TRITIUM_MEV_VALIDATION,
    "3He": AME_B_HE3_MEV_VALIDATION,
    "4He": AME_B_HE4_MEV_VALIDATION,
}
M_E_MEV = mp.mpf(str(M_E_MEV_F))
Q_0_STR = Q_50_DIGIT_STR


def load_witness(name: str) -> dict:
    return json.loads((HERE / name).read_text())


# ── Per-atom per-λ θ_λ / r_λ / channel vectors ──────────────────────
w = load_witness("binding-reeb-phase-decomposition.witness.json")
per_atom = w["data"]["per_atom"]

# ── y_λ per atom from chi-*-at-q0-50dps witnesses ───────────────────
chi_witness_for_atom = {
    "D":   "chi-deuteron-h6-at-q0-50dps.witness.json",
    "T":   "chi-tritium-h9-at-q0-50dps.witness.json",
    "3He": "chi-helium-3-h9-at-q0-50dps.witness.json",
    "4He": "chi-helium-4-h12-at-q0-50dps.witness.json",
}
# Canonical precomputed Markov weights y_λ(q_0) per H_n.  The chi witness
# no longer embeds y_lambda (format drift); the jones-markov table is the
# light json source (no symbolic stack).  tables_by_n[str(n)].weights[]
# carries {partition, y_lambda}.  The ³He-baseline validation assertion
# below catches any q-mismatch (must reproduce the full-θ 0.7587).
Y_JM = load_witness("y-lambda-jones-markov-witness.json")["tables_by_n"]
y_lambda_per_atom: dict[str, dict[str, mp.mpf]] = {}
PARTIAL_ATOMS: list[tuple[str, int, int]] = []
for atom_key, fname in chi_witness_for_atom.items():
    chi_w = load_witness(fname)
    if chi_w.get("partial", False):
        PARTIAL_ATOMS.append((atom_key, chi_w.get("n_partitions", 0),
                              chi_w.get("n_partitions_total", 0)))
        continue  # gated out of assembly; skip the by_partition deref (may be empty)
    n_strands = chi_w.get("n_strands") or sum(chi_w["by_partition"][0]["partition"])
    weights = Y_JM[str(int(n_strands))]["weights"]
    y_map = {"_".join(str(p) for p in e["partition"]): mp.mpf(str(e["y_lambda"]))
             for e in weights}
    y_lambda_per_atom[atom_key] = y_map

ATOMS_FOR_ASSEMBLY = [a for a in chi_witness_for_atom
                      if a not in {p[0] for p in PARTIAL_ATOMS}]
if PARTIAL_ATOMS:
    print("WARNING — partial chi witnesses (gated out):", file=sys.stderr)
    for atom_key, n, nt in PARTIAL_ATOMS:
        print(f"  {atom_key}: {n}/{nt} partitions → SKIPPED", file=sys.stderr)


def eigenvalue(theta: mp.mpf, channel: str) -> mp.mpc:
    """Documented per-block eigenvalue (extensive branch).

    rotation: e^{iθ}  (unit modulus, carries phase)
    growth:   e^{θ}   (real >1, extensive q^{+writhe})
    """
    if channel == "growth":
        return mp.mpc(mp.exp(theta), 0)
    return mp.exp(mp.mpc(0, theta))  # e^{iθ}


# ── Build baseline Σ|Δθ| (validation) and joint S_joint per atom ────
per_atom_combined = {}
for atom_key in ATOMS_FOR_ASSEMBLY:
    atom_data = per_atom.get(atom_key, {})
    bp = atom_data.get("by_partition", [])
    y_map = y_lambda_per_atom.get(atom_key, {})

    baseline_sum = mp.mpf(0)          # Σ y·dim·|Δθ|   (reproduce assembly)
    joint_complex = mp.mpc(0, 0)      # Σ y·dim·(z_atom − z_free)
    joint_rot_complex = mp.mpc(0, 0)  # rotation-channel-only partial
    joint_grow_complex = mp.mpc(0, 0)  # growth-channel-only partial
    rows = []
    for row in bp:
        dim = row["dim"]
        part_key = "_".join(str(p) for p in row["partition"])
        y_lam = y_map.get(part_key)
        if y_lam is None:
            raise KeyError(
                f"chi-{atom_key} missing y_λ for partition {part_key} "
                f"(θ_λ has it; chi witness does not) — regenerate chi or "
                f"check jet-order alignment."
            )
        weight = y_lam * dim

        ch_free = row.get("channel_free", "")
        ch_atom = row.get("channel_atom", "")
        th_f = mp.mpf(row["theta_free_rad"])
        th_a = mp.mpf(row["theta_atom_rad"])

        # baseline |Δθ| (same convention as the full-θ assembly)
        dtheta_raw = row.get("delta_theta_rad")
        if dtheta_raw is None:           # channel-flip: raw subtraction
            delta_theta = th_a - th_f
        else:
            delta_theta = mp.mpf(dtheta_raw)
        baseline_sum += weight * abs(delta_theta)

        # joint: difference of full eigenvalues (extensive branch)
        z_f = eigenvalue(th_f, ch_free)
        z_a = eigenvalue(th_a, ch_atom)
        contrib = weight * (z_a - z_f)
        joint_complex += contrib
        is_flip = bool(row.get("channel_flip", False))
        # attribute partials by the BOUND-state channel
        if ch_atom == "growth":
            joint_grow_complex += contrib
        else:
            joint_rot_complex += contrib

        rows.append({
            "partition": part_key,
            "dim": dim,
            "y_lambda": str(y_lam),
            "channel_free": ch_free,
            "channel_atom": ch_atom,
            "channel_flip": is_flip,
            "abs_delta_theta_rad": str(abs(delta_theta)),
            "z_free": [str(z_f.real), str(z_f.imag)],
            "z_atom": [str(z_a.real), str(z_a.imag)],
            "contrib_mod": str(abs(contrib)),
        })

    per_atom_combined[atom_key] = {
        "baseline_sum_y_dim_abs_dtheta": str(baseline_sum),
        "joint_S_complex": [str(joint_complex.real), str(joint_complex.imag)],
        "joint_S_mod": str(abs(joint_complex)),
        "joint_rot_mod": str(abs(joint_rot_complex)),
        "joint_grow_mod": str(abs(joint_grow_complex)),
        "by_partition": rows,
    }

# ── Substrate-derived ρ + Vol(K) (mirror the full-θ assembly) ───────
q_0 = mp.mpf(Q_0_STR)
hbar_q = 1 - 1 / q_0
mu_0 = M_E_MEV / (3 * (q_0 - 1 / q_0) / 2)
try:
    from substrate.knot_volumes import VOL_BORROMEAN_MPF, VOL_8_11_MPF
    VOL_K = {"D": VOL_BORROMEAN_MPF, "T": VOL_8_11_MPF,
             "3He": VOL_BORROMEAN_MPF, "4He": 2 * VOL_BORROMEAN_MPF}
except ImportError:
    VOL_K = {"D": mp.mpf("7.3277248"), "T": mp.mpf("8.2863168"),
             "3He": mp.mpf("7.3277248"), "4He": mp.mpf("14.6554497")}

rho_candidates = {
    "rho_v1_m_e": M_E_MEV,
    "rho_v2_mu_0": mu_0,
    "rho_v3_m_e_x_hbar_q": M_E_MEV * hbar_q,
    "rho_v4_mu_0_x_hbar_q": mu_0 * hbar_q,
}


def rel_err(B_pred: mp.mpf, atom: str) -> mp.mpf:
    return abs(B_pred - B_AME[atom]) / abs(B_AME[atom])


# ── Volume-scaled comparison: baseline vs joint, per ρ per atom ─────
comparison = {}
for rho_name, rho in rho_candidates.items():
    per_atom_cmp = {}
    for atom in ATOMS_FOR_ASSEMBLY:
        if atom not in B_AME:
            continue
        c = per_atom_combined[atom]
        Vol = VOL_K.get(atom, mp.mpf(0))
        base_S = mp.mpf(c["baseline_sum_y_dim_abs_dtheta"])
        joint_S = mp.mpf(c["joint_S_mod"])
        B_base = rho * Vol * base_S
        B_joint = rho * Vol * joint_S
        per_atom_cmp[atom] = {
            "Vol_K_bind": str(Vol),
            "baseline_S": str(base_S),
            "baseline_B_pred_MeV": str(B_base),
            "baseline_rel_err": str(rel_err(B_base, atom)),
            "joint_S": str(joint_S),
            "joint_B_pred_MeV": str(B_joint),
            "joint_rel_err": str(rel_err(B_joint, atom)),
            "B_AME_MeV": str(B_AME[atom]),
            "joint_closer": bool(rel_err(B_joint, atom)
                                 < rel_err(B_base, atom)),
        }
    comparison[rho_name] = {"rho_value_MeV": str(rho),
                            "per_atom": per_atom_cmp}

# ── Witness ─────────────────────────────────────────────────────────
wb = (WitnessBuilder("binding-a3plus-joint-ji-combiner", engine="mpmath")
      .set_description(
          "A≥3 binding joint J⊕I (rotation⊕growth) operator-valued "
          "combiner probe.  Tests whether the documented per-block "
          "eigenvalue (rotation e^{iθ}, growth e^{θ}) combined as "
          "|Σ y_λ dim_λ (z_atom − z_free)| moves ³He/T toward closure "
          "vs the Σ|Δθ| baseline (³He +17.4%).  NO fits — reads the "
          "eigenvalue documented in binding_reeb_phase_decomposition.py."
      ))
wb.add_data("substrate_constants", {
    "q_0": str(q_0), "hbar_q": str(hbar_q),
    "m_e_MeV": str(M_E_MEV), "mu_0_MeV": str(mu_0),
})
wb.add_data("per_atom_combined", per_atom_combined)
wb.add_data("volume_per_atom", {k: str(v) for k, v in VOL_K.items()})
wb.add_data("baseline_vs_joint", comparison)
wb.add_data("partial_atoms_excluded", [
    {"atom": a, "n_partitions": n, "n_partitions_total": nt}
    for a, n, nt in PARTIAL_ATOMS])

# Validation assertion: baseline ³He Σ|Δθ| must reproduce the
# full-θ-assembly value (0.7587) — proves the witness read is correct.
if "3He" in per_atom_combined:
    he3_base = mp.mpf(per_atom_combined["3He"]["baseline_sum_y_dim_abs_dtheta"])
    wb.add_assertion(
        "he3_baseline_sum_reproduces_full_theta_assembly",
        computed=float(he3_base),
        expected=0.7587,
        tolerance=0.01,
        source="baseline Σ y·dim·|Δθ| for ³He must match "
               "binding-a3plus-full-theta-assembly (0.7587) — read check.",
    )
# Headline: does the joint combiner beat the +17.4% ³He baseline?
if "3He" in comparison["rho_v2_mu_0"]["per_atom"]:
    he3 = comparison["rho_v2_mu_0"]["per_atom"]["3He"]
    wb.add_assertion(
        "he3_joint_vs_baseline_recorded",
        computed=float(mp.mpf(he3["joint_rel_err"]) * 100),
        expected=float(mp.mpf(he3["baseline_rel_err"]) * 100),
        tolerance=1e9,  # informational: record both, never gate
        source=(f"³He μ₀·Vol joint rel_err = "
                f"{float(mp.mpf(he3['joint_rel_err']))*100:.1f}% vs baseline "
                f"{float(mp.mpf(he3['baseline_rel_err']))*100:.1f}%; "
                f"joint_closer={he3['joint_closer']}."),
    )
out_path = wb.save()

# ── Report ──────────────────────────────────────────────────────────
print("=" * 74)
print(" A≥3 binding — joint J⊕I (rotation⊕growth) combiner probe")
print("=" * 74)
print(f"  q_0={float(q_0):.6f}  ℏ_q={float(hbar_q):.6f}  "
      f"m_e={float(M_E_MEV):.6f}  μ₀={float(mu_0):.6f} MeV\n")
print("  Per-atom S (baseline Σ|Δθ| vs joint |Σ(z_a−z_f)|, "
      "rot/growth partial mods):")
for atom in ATOMS_FOR_ASSEMBLY:
    c = per_atom_combined[atom]
    print(f"    {atom:>4s}  baseline={float(mp.mpf(c['baseline_sum_y_dim_abs_dtheta'])):>10.4f}"
          f"  joint={float(mp.mpf(c['joint_S_mod'])):>12.4f}"
          f"  (rot={float(mp.mpf(c['joint_rot_mod'])):>9.4f}"
          f"  grow={float(mp.mpf(c['joint_grow_mod'])):>12.4f})")
print()
print("  Volume-scaled rel_err — baseline vs joint (ρ = μ₀):")
print(f"    {'atom':>4s}  {'baseline':>12s}  {'joint':>12s}  closer?")
for atom in ATOMS_FOR_ASSEMBLY:
    pa = comparison["rho_v2_mu_0"]["per_atom"].get(atom)
    if pa:
        print(f"    {atom:>4s}  {float(mp.mpf(pa['baseline_rel_err']))*100:>+11.1f}%"
              f"  {float(mp.mpf(pa['joint_rel_err']))*100:>+11.1f}%"
              f"  {'YES' if pa['joint_closer'] else 'no'}")
print(f"\n  Witness: {out_path}")
