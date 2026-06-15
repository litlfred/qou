"""qbeta_per_block_paper_closed_forms.py — verify paper's per-Wedderburn-
block closed forms for χ_λ(β_n - β_p) and extract per-block contributions
to the Q_β precision-ladder coefficients.

The paper's content block
`content/quantum-observable-universe/braids-and-knots/chi-per-irrep-cyclotomic-closed-forms.md`
states:

  χ_(3)(β_n) - χ_(3)(β_p)     = -(q²+1)²(q²-1)/(4q)
  χ_(2,1)(β_n) - χ_(2,1)(β_p)  = -(q⁴+1)(q²-1)/(4q³)
  χ_(1,1,1)(β_n) - χ_(1,1,1)(β_p) = -(q²+1)²(q²-1)/(4q⁵)

Each factors cleanly through (q²-1) = ℏ_q · q(q+1), giving:

  χ_(3) diff     = -(q²+1)²(q+1) · ℏ_q / 4
  χ_(2,1) diff   = -(q⁴+1)(q+1) · ℏ_q / (4q²)
  χ_(1,1,1) diff = -(q²+1)²(q+1) · ℏ_q / (4q⁴)

ALL THREE are LINEAR in ℏ_q at leading order — a structurally clean
form that explains the framework's ε^(2k) precision-ladder structure
via products of these per-block linear factors.

Verifies the paper's closed forms numerically + emits witness with
per-block Taylor coefficients ready for c_k^(λ) extraction.

Run:
    python3 folio-assistant/computations/qbeta_per_block_paper_closed_forms.py
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 5, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps()
import sympy as sp  # noqa: E402
from mpmath import mp, mpf  # noqa: E402
import json  # noqa: E402


def main() -> None:
    q = sp.Symbol("q", positive=True)
    h = q - 1 / q
    hbar = (q - 1) / q

    # Paper's closed forms
    chi_diff_paper = {
        "(3)":     -(q**2 + 1)**2 * (q**2 - 1) / (4 * q),
        "(2,1)":   -(q**4 + 1) * (q**2 - 1) / (4 * q**3),
        "(1,1,1)": -(q**2 + 1)**2 * (q**2 - 1) / (4 * q**5),
    }

    # Cleaner form factoring ℏ_q out
    chi_diff_clean = {
        "(3)":     -(q**2 + 1)**2 * (q + 1) * hbar / 4,
        "(2,1)":   -(q**4 + 1) * (q + 1) * hbar / (4 * q**2),
        "(1,1,1)": -(q**2 + 1)**2 * (q + 1) * hbar / (4 * q**4),
    }

    # Verify the two forms are symbolically equal
    print("=" * 78)
    print("Verify cleaner ℏ_q form matches paper's (q²-1) form")
    print("=" * 78)
    for shape in chi_diff_paper:
        diff = sp.simplify(chi_diff_paper[shape] - chi_diff_clean[shape])
        print(f"  {shape}: paper - clean = {diff}  ({'EQUAL' if diff == 0 else 'MISMATCH'})")
    print()

    # Numerical at q_0
    q_0_str = json.load(open(_pb.witness_path("q-pinning-50-digit.witness.json", HERE)))["derived_50_digit"]["q"]
    q_0 = sp.Float(q_0_str, 30)

    print("Per-block χ_λ(β_n - β_p) at q_0:")
    chi_at_q0 = {}
    for shape, expr in chi_diff_paper.items():
        val = float(expr.subs(q, q_0))
        chi_at_q0[shape] = val
        print(f"  χ_{shape} = {val:.10f}")
    print()

    # Verify Σ y_λ · χ_λ = τ_M(β_n - β_p) = -0.14207
    y_data = json.load(open(_pb.witness_path("y-lambda-at-q0.witness.json", HERE)))
    y_lam = {}
    for entry in y_data["data"]["by_n"]["3"]:
        partition_tuple = tuple(entry["partition"])
        if partition_tuple == (3,):
            label = "(3)"
        elif partition_tuple == (2, 1):
            label = "(2,1)"
        elif partition_tuple == (1, 1, 1):
            label = "(1,1,1)"
        else:
            continue
        y_lam[label] = float(entry["y_at_q0_50dps"])

    tau_diff = sum(y_lam[s] * chi_at_q0[s] for s in chi_at_q0)
    print(f"τ_M(β_n - β_p) via Σ y_λ · χ_λ = {tau_diff:.10f}")
    print(f"Direct compute (independent): -0.1420729314")
    print(f"Diff: {tau_diff - (-0.14207293):.2e}")
    print()

    # Taylor expansion in (q-1) = ε around q=1
    eps = sp.Symbol("eps")
    print("=" * 78)
    print("Taylor expansion of χ_λ(β_n - β_p) around q=1 (in ε = q-1)")
    print("=" * 78)
    taylor_coeffs = {}
    for shape, expr in chi_diff_paper.items():
        series = sp.series(expr.subs(q, 1 + eps), eps, 0, 7).removeO()
        coefs = [sp.simplify(series.coeff(eps, k)) for k in range(7)]
        taylor_coeffs[shape] = coefs
        print(f"  χ_{shape}(β_n - β_p) = {series}")
    print()

    # Map ε^k coefficients to ℏ_q² powers
    # ℏ_q = (q-1)/q, ℏ_q² ≈ ε² to leading order
    # χ_λ is linear in ℏ_q at leading order ⟹ ε^1 dominates
    print("LEADING-ORDER (ε^1) coefficients per block:")
    for shape, coefs in taylor_coeffs.items():
        print(f"  {shape}: ε^1 coeff = {coefs[1]}")
    print()

    # Compute per-block ℏ_q^k coefficients
    print("=" * 78)
    print("Per-block χ_λ(β_n - β_p) / ℏ_q at q_0 (LO coefficient)")
    print("=" * 78)
    hbar_at_q0 = float(hbar.subs(q, q_0))
    for shape, val in chi_at_q0.items():
        ratio = val / hbar_at_q0
        # Symbolic form
        sym_ratio = sp.simplify(chi_diff_paper[shape] / hbar)
        sym_at_q0 = float(sym_ratio.subs(q, q_0))
        print(f"  χ_{shape}/ℏ_q = {ratio:.6f} (at q_0); symbolic: {sym_ratio}")
    print()

    # Emit witness
    w = WitnessBuilder("qbeta-per-block-paper-closed-forms", engine="python")
    w.set_description(
        "Verifies the paper's per-Wedderburn-block closed forms for "
        "χ_λ(β_n - β_p) at H_3(q) and identifies the cleaner "
        "factored form: each block's character difference is LINEAR "
        "in ℏ_q = (q-1)/q at leading order. This provides the "
        "structural foundation for per-block c_k^(λ) extraction in "
        "the Q_β precision ladder."
    )
    w.add_data("paper_closed_forms", {
        s: str(chi_diff_paper[s]) for s in chi_diff_paper
    })
    w.add_data("cleaner_hbar_q_forms", {
        s: str(chi_diff_clean[s]) for s in chi_diff_clean
    })
    w.add_data("chi_at_q_0", chi_at_q0)
    w.add_data("y_lambda_at_q_0", y_lam)
    w.add_data("tau_M_diff_at_q_0", tau_diff)
    w.add_data("taylor_coefficients_per_block_ε_order", {
        s: [str(c) for c in taylor_coeffs[s]] for s in taylor_coeffs
    })
    w.add_data("leading_order_ℏ_q_coefficient", {
        s: str(sp.simplify(chi_diff_paper[s] / hbar)) for s in chi_diff_paper
    })
    w.add_assertion(
        "paper_and_clean_forms_agree",
        computed=sum(float(sp.simplify(chi_diff_paper[s] - chi_diff_clean[s])
                            .subs(q, 1.1)) for s in chi_diff_paper),
        expected=0,
        tolerance=1e-30,
        source="Paper's (q²-1) form and clean (q+1)·ℏ_q form are symbolically equal",
    )
    w.add_assertion(
        "sum_y_lambda_chi_lambda_diff_matches_tau_M",
        computed=float(abs(tau_diff - (-0.14207293))),
        expected=0,
        tolerance=1e-7,
        source="Σ y_λ · χ_λ(β_n - β_p) = τ_M(β_n - β_p) at q_0",
    )
    w.save()


if __name__ == "__main__":
    main()
