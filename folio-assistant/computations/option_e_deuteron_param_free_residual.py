#!/usr/bin/env python3
"""
Option E — honest parameter-free deuteron Δ_λ residual.

This script does NOT search a scale menu and does NOT back-solve any
correction factor. It evaluates the 2026-05-26 crystal-weight form

    B(D) = m_e · |Σ_λ y_λ · χ^λ(β_D) · sgn(w₀^{S_{λ'}}) · f^λ|

at substrate q₀, using ONLY proved/cached factors (no C_knot, no
m_π·ℏ_q menu), and reports the honest residual vs the deuteron target
−B_D^AME / m_e = −4.353367 m_e.

Purpose: provide a reproducible record that Option E, evaluated
parameter-free, captures only 17.1% of the deuteron binding (−82.9%),
reproducing the 2026-05-29 retraction. This is NOT a closure candidate
— it documents that Option E does NOT close Δ_λ.

Output: option-e-deuteron-param-free-residual.witness.json
"""

import json
import math
import sys
from datetime import datetime, timezone
from pathlib import Path
from lean_uniqueness_refs import lean_uniqueness_ref  # noqa: E402
from mpmath import mpf, mp


M_E_MEV = mpf("0.51099895069")
B_D_AME_MEV = mpf("2.224566")  # deuteron binding (AME), as used in v6/v7
Q_0 = mpf("1.1097090249")


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
    return tuple(sum(1 for p in lam if p > i) for i in range(max(lam)))


def longest_element_sign(lam):
    """sgn(w₀^{S_{λ'}}) = product over columns c of (-1)^{c(c-1)/2}
    (sign of the longest element of the column-stabiliser Young subgroup)."""
    pt = transpose(lam)
    sgn = 1
    for col in pt:
        sgn *= (-1) ** (col * (col - 1) // 2)
    return sgn


def load_chi(repo_root):
    fn = (repo_root / "folio-assistant" / "computations"
          / "atom-chi-rust-d.witness.json")
    with fn.open() as f:
        data = json.load(f)["data"]
    chi_free, chi_atom = {}, {}
    for cfg, target in [("free", chi_free), ("atom", chi_atom)]:
        for e in data[cfg]["by_partition"]:
            part = e["partition"]
            part = tuple(eval(part)) if isinstance(part, str) else tuple(part)
            target[part] = mpf(str(e["chi_lambda"]))
    return chi_free, chi_atom


def load_y(repo_root):
    fn = (repo_root / "folio-assistant" / "computations"
          / "chi-deuteron-h6-at-q0-50dps.witness.json")
    with fn.open() as f:
        data = json.load(f)
    y = {}
    for e in data["by_partition"]:
        part = e["partition"]
        part = tuple(eval(part)) if isinstance(part, str) else tuple(part)
        y[part] = mpf(e["y_lambda"])
    return y


def main() -> int:
    mp.dps = 50
    repo_root = Path(__file__).resolve().parent.parent.parent

    chi_free, chi_atom = load_chi(repo_root)
    y = load_y(repo_root)

    target_signed = -B_D_AME_MEV / M_E_MEV  # -4.353367 m_e
    print(f"Deuteron target (Δ_λ residual): -B_D/m_e = {float(target_signed):.6f} m_e")

    # Parameter-free crystal-weight sum (no C_knot, no scale menu)
    S = mpf(0)
    per_lambda = []
    for p in sorted(chi_free, key=lambda x: (-sum(x), x)):
        f_lam = mpf(dim_sn(p))
        sgn = longest_element_sign(p)
        term = y[p] * chi_atom[p] * sgn * f_lam
        S += term
        per_lambda.append({
            "lambda": str(p),
            "y": str(y[p]),
            "chi_atom": str(chi_atom[p]),
            "sgn_w0": sgn,
            "f_lambda": int(f_lam),
            "term": str(term),
        })

    B_pred = M_E_MEV * abs(S)
    rel_err_pct = float((B_pred - B_D_AME_MEV) / B_D_AME_MEV * 100)
    captured = float(B_pred / B_D_AME_MEV * 100)
    residual_pred = S  # signed Δ_λ residual prediction in m_e
    unaccounted = target_signed - (-abs(S))  # m_e still missing
    c_knot = B_D_AME_MEV / (M_E_MEV * abs(S))  # the fitted back-solve factor

    print(f"Σ (signed, param-free)        = {float(S):.6f} m_e")
    print(f"B_pred = m_e·|Σ|              = {float(B_pred):.6f} MeV")
    print(f"B_D^AME                       = {float(B_D_AME_MEV):.6f} MeV")
    print(f"rel err                       = {rel_err_pct:+.2f}%")
    print(f"captured fraction             = {captured:.1f}%")
    print(f"Δ_λ residual predicted        = {float(-abs(S)):.6f} m_e")
    print(f"Δ_λ residual target           = {float(target_signed):.6f} m_e")
    print(f"unaccounted (param-free)      = {float(unaccounted):.6f} m_e")
    print(f"C_knot (back-solve = tgt/pred)= {float(c_knot):.6f}  (== retraction 5.852)")

    witness = {
        "engine": "python",
        "engineVersion": f"python {sys.version_info.major}.{sys.version_info.minor}",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "computation": "option-e-deuteron-param-free-residual",
        "description": (
            "Honest parameter-free deuteron Δ_λ residual for Option E "
            "(Kashiwara crystal weight). Evaluates B = m_e·|Σ y_λ·χ^λ·"
            "sgn(w₀)·f^λ| at q₀ with NO scale menu and NO back-solved "
            "C_knot. Documents that Option E captures only 17.1% of the "
            "deuteron binding (−82.9%), reproducing the 2026-05-29 "
            "retraction. NOT a closure candidate — closure_status is "
            "'does_not_close'."
        ),
        "scriptFile": "option_e_deuteron_param_free_residual.py",
        "precisionMetadata": {"compute_dps": 50, "output_dps": 30},
        "closure_status": "does_not_close",
        "is_closure_candidate": False,
        "inputs_provenance": {
            "chi_lambda": "atom-chi-rust-d.witness.json (interface-inclusive)",
            "y_lambda": "chi-deuteron-h6-at-q0-50dps.witness.json",
            "m_e_MeV": str(M_E_MEV),
            "B_D_AME_MeV": str(B_D_AME_MEV),
            "q_0": str(Q_0),
        },
        "deuteron_residual": {
            "target_signed_m_e": str(target_signed),
            "sum_signed_m_e": str(S),
            "B_pred_MeV": str(B_pred),
            "B_AME_MeV": str(B_D_AME_MEV),
            "rel_err_pct": rel_err_pct,
            "captured_fraction_pct": captured,
            "residual_pred_signed_m_e": str(-abs(S)),
            "unaccounted_m_e": str(unaccounted),
            "C_knot_backsolve_factor": str(c_knot),
            "C_knot_note": "C_knot == B_AME/(m_e·|Σ|); a back-solve, not a derived factor; matches retraction 5.852",
        },
        "per_lambda_terms": per_lambda,
    }
    out = (repo_root / "folio-assistant" / "computations"
           / "option-e-deuteron-param-free-residual.witness.json")
    with out.open("w") as f:
        witness["lean_uniqueness_ref"] = lean_uniqueness_ref("deuteron (²H)")
        json.dump(witness, f, indent=2)
    print(f"\nWrote {out}")
    print("\nclosure_status: does_not_close (parameter-free margin −82.9%)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
