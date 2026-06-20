#!/usr/bin/env python3
"""
Option E v8 — Hecke involution + isospin-mirror (Z↔N) symmetry probe.

Per user enumeration of missing symmetries:
  - #2 Hecke involution q ↔ −q⁻¹: preserves quadratic, swaps sym/antisym
    eigenspaces. Effect on characters: χ^λ_{q→−q⁻¹}(β) ∝ (-1)^|β| χ^{λᵀ}_q(β).
  - #3+#5 Braid inversion β↔β⁻¹ combined with Z↔N (proton↔neutron)
    flavor swap: the ³He braid IS the Z↔N image of the ³H braid at
    the structural level.

v8 tests:
  A. Isospin-mirror identity: for chiral pair (λ, λᵀ), check
     χ^λ(β_T) vs χ^{λᵀ}(β_³He). If ³He IS the Z↔N mirror of T at the
     Wedderburn level, these should be equal (or anti-equal) per partition.
  B. Cross-isotope bar-(anti)symmetric combinations:
     M_sym(λ)  := (χ^λ(β_T) + χ^{λᵀ}(β_³He)) / 2
     M_asym(λ) := (χ^λ(β_T) − χ^{λᵀ}(β_³He)) / 2
     These directly measure the isospin-mirror residual.
  C. Same scales as v7 (m_e, μ₀, m_π, ℏ_q combinations).

If A finds the isospin-mirror identity holds exactly, this REPLACES
the 1.58× residual from v7 with a STRUCTURAL substrate observable.

Output: option-e-v8-hecke-involution-isospin-mirror.witness.json
"""

import json
import math
import sys
from datetime import datetime, timezone
from pathlib import Path
from mpmath import mpf, mp, fabs, acos


M_E_MEV = mpf("0.51099895069")
M_PI_MEV = mpf("139.57039")  # standalone probe: no substrate import (intentional)
Q_0 = mpf("1.1097090249")

H_Q = 1 - 1 / Q_0
H = Q_0 - 1 / Q_0
MU_0 = M_E_MEV / (mpf(3) * H / mpf(2))

AME_MeV = {"T": mpf("8.481798"), "3He": mpf("7.71806")}


def dim_sn(lam):
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


def transpose(lam):
    if not lam:
        return tuple()
    max_part = max(lam)
    return tuple(sum(1 for p in lam if p > i) for i in range(max_part))


def load_chi(repo_root, atom_label):
    fn_map = {"T": "t", "3He": "3he"}
    fn = (repo_root / "folio-assistant" / "computations"
          / f"atom-chi-rust-{fn_map[atom_label]}.witness.json")
    with fn.open() as f:
        data = json.load(f)["data"]
    chi_free, chi_atom = {}, {}
    for cfg, target in [("free", chi_free), ("atom", chi_atom)]:
        for e in data[cfg]["by_partition"]:
            part = e["partition"]
            if isinstance(part, str):
                part = tuple(eval(part))
            else:
                part = tuple(part)
            target[part] = mpf(str(e["chi_lambda"]))
    return chi_free, chi_atom


def load_y(repo_root, atom_label):
    name_map = {"T": "tritium-h9", "3He": "helium-3-h9"}
    fn = (repo_root / "folio-assistant" / "computations"
          / f"chi-{name_map[atom_label]}-at-q0-50dps.witness.json")
    with fn.open() as f:
        data = json.load(f)
    y = {}
    for e in data["by_partition"]:
        part = e["partition"]
        if isinstance(part, str):
            part = tuple(eval(part))
        else:
            part = tuple(part)
        y[part] = mpf(e["y_lambda"])
    return y


def main() -> int:
    mp.dps = 50
    repo_root = Path(__file__).resolve().parent.parent.parent

    print(f"=== Scales ===")
    print(f"  m_e   = {float(M_E_MEV):.6f}")
    print(f"  μ₀    = {float(MU_0):.6f}")
    print(f"  m_π   = {float(M_PI_MEV):.6f}")
    print(f"  ℏ_q   = {float(H_Q):.6f}")
    print(f"  q_0   = {float(Q_0):.6f}\n")

    cf_T, ca_T = load_chi(repo_root, "T")
    cf_He3, ca_He3 = load_chi(repo_root, "3He")
    y_T = load_y(repo_root, "T")
    y_He3 = load_y(repo_root, "3He")

    parts = list(cf_T.keys())
    assert set(parts) == set(cf_He3.keys()), "Same partitions for T and He3"

    # Test A: Isospin-mirror identity per chiral pair (λ, λᵀ)
    print("=== Test A: Isospin-mirror identity χ_λ(β_T) vs χ_λᵀ(β_³He) ===\n")
    pairs_data = []
    isomirror_residual_atom = mpf(0)
    isomirror_residual_free = mpf(0)
    seen = set()
    for p in parts:
        pt = transpose(p)
        if p in seen or pt in seen:
            continue
        seen.add(p); seen.add(pt)
        if pt == p:
            # self-conjugate; nothing to mirror
            continue
        chi_T_p = ca_T[p]
        chi_He3_pt = ca_He3[pt]
        diff_atom = chi_T_p - chi_He3_pt
        sum_atom = chi_T_p + chi_He3_pt
        # Also check free side
        chi_T_p_free = cf_T[p]
        chi_He3_pt_free = cf_He3[pt]
        diff_free = chi_T_p_free - chi_He3_pt_free
        pairs_data.append({
            "lambda": str(p),
            "lambda_T": str(pt),
            "dim": dim_sn(p),
            "chi_T_lambda_atom": str(chi_T_p),
            "chi_He3_lambdaT_atom": str(chi_He3_pt),
            "diff_atom": str(diff_atom),
            "sum_atom": str(sum_atom),
            "ratio_atom": str(chi_T_p / chi_He3_pt) if chi_He3_pt != 0 else "inf",
            "diff_free": str(diff_free),
        })
        isomirror_residual_atom += fabs(diff_atom)
        isomirror_residual_free += fabs(diff_free)

    print(f"Total isospin-mirror residual (atom-side): Σ |χ_T(λ) - χ_He3(λᵀ)| = {float(isomirror_residual_atom):.6f}")
    print(f"Total isospin-mirror residual (free-side): {float(isomirror_residual_free):.6f}\n")
    print(f"Per-pair examples (first 5):")
    for p in pairs_data[:5]:
        chi_T = float(mpf(p["chi_T_lambda_atom"]))
        chi_He3 = float(mpf(p["chi_He3_lambdaT_atom"]))
        diff = float(mpf(p["diff_atom"]))
        print(f"  λ={p['lambda']:20s} λᵀ={p['lambda_T']:20s}  χ_T(λ)={chi_T:+8.4f}  χ_He3(λᵀ)={chi_He3:+8.4f}  diff={diff:+8.4f}")
    print()

    # Test B: Cross-isotope bar combinations weighted by y_λ
    print("=== Test B: Cross-isotope bar-(anti)symmetric combinations ===\n")
    sum_y_M_sym = mpf(0)
    sum_y_M_asym = mpf(0)
    sum_y_M_sym_free = mpf(0)
    sum_y_M_asym_free = mpf(0)
    for p in parts:
        pt = transpose(p)
        if pt == p:
            continue
        # M_sym(λ)  = (χ^λ(β_T) + χ^{λᵀ}(β_³He)) / 2  (atom)
        # M_asym(λ) = (χ^λ(β_T) − χ^{λᵀ}(β_³He)) / 2
        M_sym_atom = (ca_T[p] + ca_He3[pt]) / 2
        M_asym_atom = (ca_T[p] - ca_He3[pt]) / 2
        M_sym_free = (cf_T[p] + cf_He3[pt]) / 2
        M_asym_free = (cf_T[p] - cf_He3[pt]) / 2
        # Weight by y (use y_T for now; y should be same per Wenzl symmetry)
        y_p = y_T.get(p, mpf(0))
        sum_y_M_sym += y_p * M_sym_atom
        sum_y_M_asym += y_p * M_asym_atom
        sum_y_M_sym_free += y_p * M_sym_free
        sum_y_M_asym_free += y_p * M_asym_free

    print(f"Σ y_λ · M_sym  (atom): {float(sum_y_M_sym):+.6f}")
    print(f"Σ y_λ · M_asym (atom): {float(sum_y_M_asym):+.6f}")
    print(f"Σ y_λ · M_sym  (free): {float(sum_y_M_sym_free):+.6f}")
    print(f"Σ y_λ · M_asym (free): {float(sum_y_M_asym_free):+.6f}")
    diff_sym = sum_y_M_sym - sum_y_M_sym_free
    diff_asym = sum_y_M_asym - sum_y_M_asym_free
    print(f"diff atom-free (sym):  {float(diff_sym):+.6f}")
    print(f"diff atom-free (asym): {float(diff_asym):+.6f}\n")

    # Test C: Try scale × combination → mirror pair target
    diff_target = AME_MeV["T"] - AME_MeV["3He"]  # +0.7637 MeV
    print(f"=== Test C: Mirror pair target = {float(diff_target):.4f} MeV ===\n")

    scales = [
        ("m_e", M_E_MEV),
        ("μ₀", MU_0),
        ("μ₀·ℏ_q", MU_0 * H_Q),
        ("m_π", M_PI_MEV),
        ("m_π·ℏ_q", M_PI_MEV * H_Q),
        ("m_π·ℏ_q²", M_PI_MEV * H_Q ** 2),
    ]
    inputs = {
        "Σ y M_sym atom": sum_y_M_sym,
        "Σ y M_asym atom": sum_y_M_asym,
        "Σ y M_sym diff": diff_sym,
        "Σ y M_asym diff": diff_asym,
        "isomirror_residual_atom": isomirror_residual_atom,
    }
    results = {}
    for sname, scale in scales:
        for ikey, ivalue in inputs.items():
            value = scale * ivalue
            err = float((value - diff_target) / diff_target * 100)
            results[f"{sname} · {ikey}"] = {
                "value_MeV": float(value),
                "rel_err_pct": err,
                "closes_2pct": abs(err) <= 2,
                "closes_10pct": abs(err) <= 10,
            }

    # Sort by abs(err)
    sorted_results = sorted(results.items(), key=lambda x: abs(x[1]["rel_err_pct"]))
    print(f"  {'Formula':45s}  value     err")
    for name, r in sorted_results[:10]:
        marker = "  ✓✓" if r["closes_2pct"] else "  ✓" if r["closes_10pct"] else "   "
        print(f"{marker} {name:45s}  {r['value_MeV']:+9.4f}  {r['rel_err_pct']:+8.2f}%")

    # Write witness
    witness = {
        "engine": "python",
        "engineVersion": f"python {sys.version_info.major}.{sys.version_info.minor}",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "computation": "option-e-v8-hecke-involution-isospin-mirror",
        "description": (
            "Option E v8: isospin-mirror identity test χ_λ(β_T) vs "
            "χ_λᵀ(β_³He) + cross-isotope bar-(anti)symmetric combinations. "
            "Probes whether Z↔N + λ↔λᵀ together produce the canonical "
            "isospin-mirror residual."
        ),
        "scriptFile": "option_e_v8_hecke_involution_isospin_mirror.py",
        "precisionMetadata": {"compute_dps": 50, "output_dps": 30},
        "mirror_target_MeV": str(diff_target),
        "test_A_isospin_mirror_identity": {
            "total_residual_atom": str(isomirror_residual_atom),
            "total_residual_free": str(isomirror_residual_free),
            "n_chiral_pairs": len(pairs_data),
            "pair_examples": pairs_data[:10],
        },
        "test_B_cross_isotope_bar_combinations": {
            "sum_y_M_sym_atom":  str(sum_y_M_sym),
            "sum_y_M_asym_atom": str(sum_y_M_asym),
            "sum_y_M_sym_free":  str(sum_y_M_sym_free),
            "sum_y_M_asym_free": str(sum_y_M_asym_free),
            "diff_sym":  str(diff_sym),
            "diff_asym": str(diff_asym),
        },
        "test_C_results_top10": [
            {"formula": name, **r}
            for name, r in sorted_results[:10]
        ],
        "best_mirror_formula": sorted_results[0][0],
        "best_mirror_err": sorted_results[0][1]["rel_err_pct"],
    }

    out_path = (
        repo_root / "folio-assistant" / "computations"
        / "option-e-v8-hecke-involution-isospin-mirror.witness.json"
    )
    with out_path.open("w") as f:
        json.dump(witness, f, indent=2)
    print(f"\nWrote {out_path}")
    print(f"\nBest mirror closure: {sorted_results[0][0]} (err {sorted_results[0][1]['rel_err_pct']:+.2f}%)")

    return 0


if __name__ == "__main__":
    sys.exit(main())
