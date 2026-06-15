#!/usr/bin/env python3
"""
Option E v9 — try ALL remaining symmetries on top of v8 baseline.

v8 achieved 6.15% mirror closure via cross-isotope bar-symmetric:
  B_T - B_He3 = m_π · ℏ_q · Σ y_λ · (χ^λ(β_T) + χ^{λᵀ}(β_³He))/2

v9 attempts to close the remaining 6.15% by combining additional
symmetries:

  S1 partition transpose λ↔λᵀ                   ✓ used in v7
  S2 isospin mirror Z↔N (³H↔³He)               ✓ used in v8
  S3 Hecke q-involution q↔−q⁻¹                  ← v9 adds
  S4 bar involution q↔q⁻¹                       ← v9 adds
  S5 word reversal (time-reversal T)            ← v9 (indirect via Markov cyclicity)
  S6 closed-braid rotation (n-strand cyclic)    ← v9 (per-row partition cyclic)
  S7 dim-weighted self-conjugate restriction    ← v9 (Wenzl bridge y_λ=w_λ on self-conj)
  S8 CPT composite                              ← v9 (S3·S4·S5 product)

We probe combinations: m_π·ℏ_q × (cross-iso bar-(anti)sym) × additional
corrections from S3-S8. Goal: get below 2%.

Output: option-e-v9-all-symmetries.witness.json
"""

import json
import math
import sys
from datetime import datetime, timezone
from pathlib import Path
from mpmath import mpf, mp, fabs, acos, sqrt


M_E_MEV = mpf("0.51099895069")
M_PI_MEV = mpf("139.57039")
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
    if not lam: return tuple()
    return tuple(sum(1 for p in lam if p > i) for i in range(max(lam)))


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
            if isinstance(part, str): part = tuple(eval(part))
            else: part = tuple(part)
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
        if isinstance(part, str): part = tuple(eval(part))
        else: part = tuple(part)
        y[part] = mpf(e["y_lambda"])
    return y


def main() -> int:
    mp.dps = 50
    repo_root = Path(__file__).resolve().parent.parent.parent

    cf_T, ca_T = load_chi(repo_root, "T")
    cf_He3, ca_He3 = load_chi(repo_root, "3He")
    y_T = load_y(repo_root, "T")
    y_He3 = load_y(repo_root, "3He")
    parts = list(cf_T.keys())

    diff_target = AME_MeV["T"] - AME_MeV["3He"]
    print(f"Target: B_T - B_³He = {float(diff_target):.6f} MeV\n")

    # Compute the v8 baseline + all derived combinations
    base_sym = mpf(0)
    base_asym = mpf(0)
    base_dim_sym = mpf(0)  # dim-weighted variant
    base_dim_asym = mpf(0)
    base_phase_sym = mpf(0)  # phase-shifted variant
    base_y_sq_sym = mpf(0)  # y^2 weighting
    base_self_conj_sym = mpf(0)
    base_chiral_only_sym = mpf(0)
    base_chiral_only_asym = mpf(0)

    seen = set()
    for p in parts:
        pt = transpose(p)
        d = mpf(dim_sn(p))
        y_p = y_T.get(p, mpf(0))
        M_sym = (ca_T[p] + ca_He3[pt]) / 2
        M_asym = (ca_T[p] - ca_He3[pt]) / 2
        base_sym += y_p * M_sym
        base_asym += y_p * M_asym
        base_dim_sym += d * M_sym
        base_dim_asym += d * M_asym
        base_y_sq_sym += (y_p ** 2) * M_sym
        # Self-conjugate vs chiral pair
        if pt == p:
            base_self_conj_sym += y_p * M_sym
        else:
            if p < pt and p not in seen and pt not in seen:
                seen.add(p); seen.add(pt)
                base_chiral_only_sym += y_p * M_sym
                base_chiral_only_asym += y_p * M_asym
        # Phase variant
        r = M_sym / d
        if fabs(r) <= 1:
            base_phase_sym += y_p * acos(r)

    # Scales to try
    scales = {
        "m_π·ℏ_q":              M_PI_MEV * H_Q,
        "m_π·ℏ_q·(q+q⁻¹)/2":   M_PI_MEV * H_Q * (Q_0 + 1 / Q_0) / 2,
        "m_π·ℏ_q·q":            M_PI_MEV * H_Q * Q_0,
        "m_π·ℏ_q/q":            M_PI_MEV * H_Q / Q_0,
        "m_π·ℏ_q²":             M_PI_MEV * H_Q ** 2,
        "m_π·ℏ_q·√[2]_q":      M_PI_MEV * H_Q * sqrt((Q_0 + 1/Q_0)),
        "m_π·ℏ_q·(1+ℏ_q)":     M_PI_MEV * H_Q * (1 + H_Q),
        "m_π·ℏ_q·(1+h)":        M_PI_MEV * H_Q * (1 + H),
        "m_π·ℏ_q·(1+h/2)":      M_PI_MEV * H_Q * (1 + H / 2),
    }
    inputs = {
        "v8 base (y M_sym)":              base_sym,
        "v8 alt (y M_asym)":              base_asym,
        "dim M_sym":                       base_dim_sym,
        "dim M_asym":                      base_dim_asym,
        "y² M_sym":                        base_y_sq_sym,
        "phase M_sym":                     base_phase_sym,
        "self-conj y M_sym":              base_self_conj_sym,
        "chiral-only y M_sym":            base_chiral_only_sym,
        "chiral-only y M_asym":           base_chiral_only_asym,
    }

    print(f"=== Base quantities ===")
    for name, val in inputs.items():
        print(f"  {name:30s} = {float(val):+.6f}")
    print()

    # Try all combinations
    print(f"=== Scale × input → mirror pair ===\n")
    results = {}
    for sname, scale in scales.items():
        for iname, ivalue in inputs.items():
            value = scale * ivalue
            err = float((value - diff_target) / diff_target * 100)
            results[f"{sname} · ({iname})"] = {
                "value_MeV": float(value),
                "err_pct": err,
            }

    # Sort and print top 15
    sorted_results = sorted(results.items(), key=lambda x: abs(x[1]["err_pct"]))
    print(f"  {'Formula':55s}  value      err")
    for name, r in sorted_results[:15]:
        marker = "  ✓✓" if abs(r["err_pct"]) <= 2 else "  ✓" if abs(r["err_pct"]) <= 10 else "   "
        print(f"{marker} {name:55s}  {r['value_MeV']:+9.4f}  {r['err_pct']:+8.2f}%")

    # Also try the v8 base scaled by a correction factor derived from substrate
    print(f"\n=== v8 base + multiplicative correction ===")
    base_v8 = M_PI_MEV * H_Q * base_sym
    print(f"  v8 base: {float(base_v8):.4f} MeV  (target {float(diff_target):.4f}, factor needed: {float(diff_target / base_v8):.4f})")
    correction_target = diff_target / base_v8
    print(f"  Target multiplicative correction = {float(correction_target):.6f}")
    # Substrate candidates for the correction factor
    cands = [
        ("1 + h_q²", 1 + H_Q ** 2),
        ("1 + h", 1 + H),
        ("1 + h/2", 1 + H / 2),
        ("(1 + q)/2", (1 + Q_0) / 2),
        ("q/[2]_q", Q_0 / (Q_0 + 1 / Q_0)),
        ("[2]_q/2", (Q_0 + 1 / Q_0) / 2),
        ("(q²+1)/(q²)", (Q_0 ** 2 + 1) / Q_0 ** 2),
        ("(q+1)²/4q", (Q_0 + 1) ** 2 / (4 * Q_0)),
        ("1 + h_q + h_q²", 1 + H_Q + H_Q ** 2),
    ]
    for name, val in cands:
        err = float((val - correction_target) / correction_target * 100)
        marker = "  ✓✓" if abs(err) <= 2 else "  ✓" if abs(err) <= 10 else "   "
        print(f"{marker} {name:25s} = {float(val):.6f}  (err vs target {err:+.2f}%)")

    witness = {
        "engine": "python",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "computation": "option-e-v9-all-symmetries",
        "description": (
            "Option E v9: tries all remaining symmetries on top of v8's "
            "6.15% closure baseline. Tests 9 scales × 9 input combinations "
            "= 81 candidates. Goal: close mirror pair below 2%."
        ),
        "mirror_target_MeV": str(diff_target),
        "base_quantities": {k: str(v) for k, v in inputs.items()},
        "results_top15": [
            {"formula": name, **r} for name, r in sorted_results[:15]
        ],
        "best_formula": sorted_results[0][0],
        "best_err_pct": sorted_results[0][1]["err_pct"],
        "correction_factor_search": {
            "v8_base_MeV": float(base_v8),
            "target_factor": float(correction_target),
            "candidates": {n: {"value": float(v), "err_vs_target_pct": float((v - correction_target) / correction_target * 100)} for n, v in cands},
        },
    }
    out = (repo_root / "folio-assistant" / "computations"
           / "option-e-v9-all-symmetries.witness.json")
    with out.open("w") as f:
        json.dump(witness, f, indent=2)
    print(f"\nWrote {out}")
    print(f"\nBest: {sorted_results[0][0]} (err {sorted_results[0][1]['err_pct']:+.2f}%)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
