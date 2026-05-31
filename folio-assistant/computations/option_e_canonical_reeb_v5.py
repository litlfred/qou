#!/usr/bin/env python3
"""
Option E v5 — canonical Reeb-phase BINDING via free-vs-atom difference.

Per docs/canonical-derivation-cheat-sheet.md §"Bind" + A≥3 binding
campaign (PR #1417) + binding_reeb_phase_decomposition.py:

The binding energy is carried by the per-rep DIFFERENCE between free
and atom configurations:

  For rotation channels (|χ/dim| ≤ 1):
    Δθ_λ = θ_atom_λ - θ_free_λ = arccos(χ_atom/d_λ) - arccos(χ_free/d_λ)

  For growth channels (|χ/dim| > 1, outer reps (n)/(1^n)):
    extensive contribution = some function of χ_atom - χ_free

Scale: μ₀ = m_e / (3(q-q⁻¹)/2) ≈ 1.63 MeV per the framework.

Candidate B(K) formulas (all probed):

  F1: B = μ₀ · Σ_rot y_λ |Δθ_λ|
  F2: B = μ₀ · Σ_rot y_λ Δθ_λ (signed)
  F3: B = μ₀ · Σ_rot d_λ |Δθ_λ|  (dim-weighted, no y)
  F4: B = μ₀ · Σ_all y_λ |Δθ_λ_clamped|  (clamp χ/dim to [-1,1] before arccos)

Output:
  option-e-canonical-reeb-v5.witness.json
"""

import json
import math
import sys
from datetime import datetime, timezone
from pathlib import Path
from mpmath import mpf, mp, fabs, acos


# Cheat-sheet derived μ₀ = m_e / (3(q-q⁻¹)/2)
# Compute symbolically from q_0
M_E_MEV = mpf("0.51099895069")
Q_0 = mpf("1.1097090249") # from substrate calibration

H_Q = Q_0 - 1 / Q_0           # ℏ_q at q_0
MU_0 = M_E_MEV / (mpf(3) * H_Q / mpf(2))  # ≈ 1.63 MeV

AME_MeV = {
    "D":     mpf("2.224566"),
    "T":     mpf("8.481798"),
    "3He":   mpf("7.71806"),
}


def dim_sn(lam):
    """Dimension of Specht module S^λ via hook-length formula."""
    lam = list(lam)
    n = sum(lam)
    num = math.factorial(n)
    den = 1
    for i in range(len(lam)):
        for j in range(lam[i]):
            arm = lam[i] - j - 1
            leg = sum(1 for r in range(i + 1, len(lam)) if lam[r] > j)
            den *= arm + leg + 1
    return num // den


def load_chi(repo_root, atom_label):
    """Load free+atom χ_λ from atom-chi-rust-{atom}.witness.json."""
    fn_map = {"D": "d", "T": "t", "3He": "3he"}
    fn = repo_root / "folio-assistant" / "computations" / f"atom-chi-rust-{fn_map[atom_label]}.witness.json"
    with fn.open() as f:
        data = json.load(f)["data"]
    result = {}
    for cfg in ["free", "atom"]:
        entries = []
        for e in data[cfg]["by_partition"]:
            part_str = e["partition"]
            if isinstance(part_str, str):
                part = tuple(eval(part_str))
            else:
                part = tuple(part_str)
            entries.append({
                "partition": part,
                "chi": mpf(str(e["chi_lambda"])),
                "dim": dim_sn(part),
            })
        result[cfg] = entries
    return result


def load_y_lambda(repo_root, atom_label, n_strands):
    """Load y_λ from chi-{atom}-h{n}-at-q0-50dps.witness.json."""
    name_map = {"D": "deuteron-h6", "T": "tritium-h9", "3He": "helium-3-h9"}
    fn = repo_root / "folio-assistant" / "computations" / f"chi-{name_map[atom_label]}-at-q0-50dps.witness.json"
    with fn.open() as f:
        data = json.load(f)
    y_by_partition = {}
    for e in data["by_partition"]:
        part = e["partition"]
        if isinstance(part, str):
            part = tuple(eval(part))
        else:
            part = tuple(part)
        y_by_partition[part] = mpf(e["y_lambda"])
    return y_by_partition


def compute_binding_candidates(atom_label, free_atom_chi, y_lambda):
    """Compute B(K) under 4 candidate formulas."""
    rotation_terms_F1 = mpf(0)
    rotation_terms_F2 = mpf(0)
    rotation_terms_F3 = mpf(0)
    all_terms_F4 = mpf(0)
    rot_count = 0
    growth_count = 0
    rot_summary = []

    chi_free_map = {e["partition"]: e["chi"] for e in free_atom_chi["free"]}
    chi_atom_map = {e["partition"]: e["chi"] for e in free_atom_chi["atom"]}
    dim_map = {e["partition"]: e["dim"] for e in free_atom_chi["free"]}

    for part in chi_free_map:
        chi_f = chi_free_map[part]
        chi_a = chi_atom_map[part]
        d = mpf(dim_map[part])
        y = y_lambda.get(part, mpf(0))
        r_f = chi_f / d
        r_a = chi_a / d
        is_rot_f = fabs(r_f) <= 1
        is_rot_a = fabs(r_a) <= 1

        if is_rot_f and is_rot_a:
            th_f = acos(r_f)
            th_a = acos(r_a)
            delta = th_a - th_f
            rotation_terms_F1 += y * fabs(delta)
            rotation_terms_F2 += y * delta
            rotation_terms_F3 += d * fabs(delta)
            rot_count += 1
            rot_summary.append({
                "partition": str(part),
                "dim": int(d),
                "r_free": str(r_f),
                "r_atom": str(r_a),
                "delta_theta": str(delta),
            })
        else:
            growth_count += 1

        # F4: clamp + arccos always
        def clamp(x):
            if x > 1: return mpf(1)
            if x < -1: return mpf(-1)
            return x
        th_f_clamped = acos(clamp(r_f))
        th_a_clamped = acos(clamp(r_a))
        all_terms_F4 += y * fabs(th_a_clamped - th_f_clamped)

    B_target = AME_MeV[atom_label]
    candidates = {
        "F1_mu0_y_lambda_abs_delta_theta_rot": MU_0 * rotation_terms_F1,
        "F2_mu0_y_lambda_signed_delta_theta_rot": MU_0 * rotation_terms_F2,
        "F3_mu0_dim_abs_delta_theta_rot": MU_0 * rotation_terms_F3,
        "F4_mu0_y_lambda_abs_delta_theta_all_clamped": MU_0 * all_terms_F4,
    }

    out = {
        "atom": atom_label,
        "rot_count": rot_count,
        "growth_count": growth_count,
        "B_target_MeV": str(B_target),
        "candidates": {
            name: {
                "B_pred_MeV": str(value),
                "rel_err_pct": str(100 * fabs(value - B_target) / B_target),
                "closes_2pct": bool(fabs(value - B_target) <= mpf("0.02") * B_target),
                "closes_10pct": bool(fabs(value - B_target) <= mpf("0.10") * B_target),
            }
            for name, value in candidates.items()
        },
        "rotation_blocks_sample": rot_summary[:3],
    }
    return out


def main() -> int:
    mp.dps = 50
    repo_root = Path(__file__).resolve().parent.parent.parent

    atom_n = {"D": 6, "T": 9, "3He": 9}

    print(f"μ₀ = {float(MU_0):.4f} MeV (cheat-sheet derived from m_e, q_0)")
    print(f"ℏ_q = {float(H_Q):.4f}")
    print(f"q_0 = {float(Q_0):.4f}\n")

    results = {}
    for atom_label in ["D", "T", "3He"]:
        free_atom = load_chi(repo_root, atom_label)
        y_lambda = load_y_lambda(repo_root, atom_label, atom_n[atom_label])
        results[atom_label] = compute_binding_candidates(atom_label, free_atom, y_lambda)

    witness = {
        "engine": "python",
        "engineVersion": f"python {sys.version_info.major}.{sys.version_info.minor}",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "computation": "option-e-canonical-reeb-v5",
        "description": (
            "Option E v5: canonical q-Reeb phase Δθ_λ = θ_atom - θ_free "
            "(per-rep, rotation channels only) with μ₀ scale, 4 formula "
            "variants. Uses atom-chi-rust caches for free+atom χ_λ DIFFERENCE."
        ),
        "scriptFile": "option_e_canonical_reeb_v5.py",
        "precisionMetadata": {"compute_dps": 50, "output_dps": 30},
        "scale": {"mu_0_MeV": str(MU_0), "h_q": str(H_Q), "q_0": str(Q_0)},
        "results": results,
    }

    # Print summary
    print("=== q-Reeb phase difference Δθ_λ = arccos(χ_atom/d) - arccos(χ_free/d) ===")
    print(f"Scale: μ₀ = {float(MU_0):.4f} MeV\n")
    for atom_label in ["D", "T", "3He"]:
        r = results[atom_label]
        print(f"--- {atom_label} ({r['rot_count']} rotation, {r['growth_count']} growth) ---")
        print(f"  B_target = {float(mpf(r['B_target_MeV'])):.5f} MeV")
        for name, c in r["candidates"].items():
            err = float(mpf(c["rel_err_pct"]))
            marker = "  ✓✓" if c["closes_2pct"] else "  ✓" if c["closes_10pct"] else "   "
            print(f"{marker} {name:48s} B_pred={float(mpf(c['B_pred_MeV'])):+8.4f}  err={err:6.2f}%")
        print()

    # Find best formula across all atoms
    formula_max_errs = {}
    for fname in ["F1_mu0_y_lambda_abs_delta_theta_rot",
                   "F2_mu0_y_lambda_signed_delta_theta_rot",
                   "F3_mu0_dim_abs_delta_theta_rot",
                   "F4_mu0_y_lambda_abs_delta_theta_all_clamped"]:
        errs = [float(mpf(results[a]["candidates"][fname]["rel_err_pct"]))
                for a in ["D", "T", "3He"]]
        formula_max_errs[fname] = max(errs)

    best_formula = min(formula_max_errs, key=formula_max_errs.get)
    print(f"\nBest formula (smallest max err across D/T/³He): {best_formula}")
    print(f"  Max rel err: {formula_max_errs[best_formula]:.2f}%")

    witness["best_formula"] = {
        "name": best_formula,
        "max_rel_err_pct": formula_max_errs[best_formula],
        "closes_uniformly_10pct": formula_max_errs[best_formula] <= 10.0,
        "closes_uniformly_2pct": formula_max_errs[best_formula] <= 2.0,
    }

    out_path = (
        repo_root / "folio-assistant" / "computations"
        / "option-e-canonical-reeb-v5.witness.json"
    )
    with out_path.open("w") as f:
        json.dump(witness, f, indent=2)
    print(f"\nWrote {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
