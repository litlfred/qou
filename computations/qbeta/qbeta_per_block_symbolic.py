"""qbeta_per_block_symbolic.py — symbolic per-Wedderburn-block
decomposition of χ_λ(T_β)(q) for the Q_β precision-ladder derivation.

Per the framework's `per-wedderburn-block-c5-c6.md` scaffolding:
the c_k coefficients of the Q_β precision ladder admit a per-Wedderburn-
block decomposition c_k = Σ_λ dim_q²(V_λ) · c_k^(λ). This script
computes the symbolic per-block characters χ_λ(T_β)(q) at each block:

  V_(3) (trivial 1D):     χ_(3)(T_β)(q) = polynomial in q
  V_(2,1) (standard 2D):  χ_(2,1)(T_β)(q) = LINEAR in h = q − 1/q
  V_(1,1,1) (sign 1D):    χ_(1,1,1)(T_β)(q) = polynomial in 1/q

The V_(2,1) result is structurally remarkable: the 2D rep's character
collapses to a linear function of the Hecke parameter h, independent
of the b² off-diagonal structure. The b² contribution from χ(σ_2)
cancels against χ(L_+) and χ(L_-).

This is the foundational data for per-block c_k^(λ) extraction via
Taylor expansion around q = 1.

Run:
    python3 folio-assistant/computations/qbeta_per_block_symbolic.py
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
from mpmath import mp, mpf  # noqa: E402
import sympy as sp  # noqa: E402
import json  # noqa: E402


def main() -> None:
    q = sp.Symbol("q", positive=True)
    h = q - 1 / q
    z = 1 / (sp.sqrt(q) + 1 / sp.sqrt(q))
    eps = sp.Symbol("eps")

    # Symbolic seminormal matrices for each Wedderburn block of H_3(q)
    sigma_0_V3 = sp.Matrix([[q]])
    sigma_1_V3 = sp.Matrix([[q]])

    sigma_0_V111 = sp.Matrix([[-1 / q]])
    sigma_1_V111 = sp.Matrix([[-1 / q]])

    # V_(2,1) Hoefsmit seminormal in {T_1 = [[1,2],[3]], T_2 = [[1,3],[2]]}
    b_sym = sp.sqrt(q ** 4 + q ** 2 + 1) / (q ** 2 + 1)
    sigma_0_V21 = sp.Matrix([[q, 0], [0, -1 / q]])
    sigma_1_V21 = sp.Matrix([
        [-1 / (q * (q ** 2 + 1)), b_sym],
        [b_sym, q ** 3 / (q ** 2 + 1)],
    ])

    # NF basis matrices
    def nf_mats(s0, s1):
        I = sp.eye(s0.rows)
        return [I, s0, s1, s0 * s1, s1 * s0, s0 * s1 * s0]

    blocks = {
        "(3)": (nf_mats(sigma_0_V3, sigma_1_V3), 1),
        "(2,1)": (nf_mats(sigma_0_V21, sigma_1_V21), q + 1 / q),
        "(1,1,1)": (nf_mats(sigma_0_V111, sigma_1_V111), 1),
    }

    nf_names = ["γ", "σ_0", "σ_1", "L_+", "L_-", "e_-"]

    # Symbolic per-block characters
    print("=" * 78)
    print("Symbolic χ_λ(b_i) per-Wedderburn-block at H_3(q)")
    print("=" * 78)
    print(f"{'i':<3} {'name':<6} {'(3)':<20} {'(2,1)':<35} {'(1,1,1)':<25}")
    chi = {}
    for label, (mats, dim_q) in blocks.items():
        chi[label] = [sp.simplify(sp.trace(m)) for m in mats]

    for i, name in enumerate(nf_names):
        print(f"{i:<3} {name:<6} {str(chi['(3)'][i]):<20} {str(chi['(2,1)'][i]):<35} {str(chi['(1,1,1)'][i]):<25}")
    print()

    # Load post-fix T_β NF coefficients (SDP-identified)
    sdp = json.load(open(_pb.witness_path("qbeta-decay-sdp-knot-operator.witness.json", HERE)))
    T_beta = sdp["data"]["T_beta_nf_coefficients"]
    keys = ["γ", "σ₀", "σ₁", "L₊", "L₋", "e⁻"]
    x_vec = [sp.Float(T_beta[k], 25) for k in keys]

    # χ_λ(T_β)(q) symbolic
    chi_T = {}
    for label, (_, dim_q) in blocks.items():
        chi_T[label] = sp.simplify(sum(x_vec[i] * chi[label][i] for i in range(6)))

    print("=" * 78)
    print("χ_λ(T_β)(q) symbolic")
    print("=" * 78)
    for label in blocks:
        expr = chi_T[label]
        print(f"  χ_{label}(T_β)(q) = {sp.simplify(expr)}")
    print()

    # Special simplification for V_(2,1): is it LINEAR in h?
    chi_V21 = chi_T["(2,1)"]
    # Collect in q and 1/q
    expanded = sp.expand(chi_V21)
    print(f"V_(2,1) expanded: {expanded}")
    # h = q - 1/q
    # If χ_(2,1)(T_β) = A + B·h for constants A, B:
    coeff_const = expanded.subs(q, 1)  # value at q=1, h=0
    # coeff of (q - 1/q): take derivative w.r.t. q at q=1 and divide by dh/dq|_{q=1} = 2
    dchi_dq = sp.diff(chi_V21, q).subs(q, 1)
    dh_dq_at_1 = sp.diff(h, q).subs(q, 1)  # = 2
    # If χ = A + B·h, then dχ/dq = B · dh/dq, so B = dχ/dq / dh/dq
    B_coef = dchi_dq / dh_dq_at_1
    print(f"χ_(2,1)(T_β)(q=1) = A = {coeff_const}")
    print(f"Coefficient of h in χ_(2,1)(T_β): B = {B_coef}")
    print(f"Predicted form: A + B·h = {coeff_const} + {B_coef}·h")
    print(f"Verify: A + B·h at q_0...")
    q_0_str = json.load(open(_pb.witness_path("q-pinning-50-digit.witness.json", HERE)))["derived_50_digit"]["q"]
    q_0_val = sp.Float(q_0_str, 50)
    h_at_q0 = q_0_val - 1 / q_0_val
    pred = coeff_const + B_coef * h_at_q0
    actual = chi_V21.subs(q, q_0_val)
    print(f"  Predicted: {float(pred):.10f}")
    print(f"  Actual:    {float(actual):.10f}")
    print(f"  Diff:      {float(pred - actual):.2e}")
    print()

    # Taylor expansions
    print("=" * 78)
    print("Taylor expansion of χ_λ(T_β)(q) around q = 1 (in ε = q - 1)")
    print("=" * 78)
    taylor_data = {}
    for label in blocks:
        series = sp.series(chi_T[label].subs(q, 1 + eps), eps, 0, 8).removeO()
        coeffs = [float(series.coeff(eps, k)) for k in range(8)]
        taylor_data[label] = coeffs
        print(f"  χ_{label}(T_β)(1+ε):")
        for k, c in enumerate(coeffs):
            if abs(c) > 1e-15:
                print(f"    ε^{k}: {c:>+18.10e}")
    print()

    # Verify the symbolic identity tr_M(T_β) = Σ y_λ χ_λ(T_β)
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
        y_lam[label] = sp.Float(entry["y_at_q0_50dps"], 50)

    tau_M_via_blocks = sum(
        y_lam[label] * chi_T[label].subs(q, q_0_val) for label in blocks
    )
    print("=" * 78)
    print("Verification at q_0: τ_M(T_β) = Σ y_λ · χ_λ(T_β)")
    print("=" * 78)
    print(f"Σ y_λ · χ_λ(T_β)(q_0) = {float(tau_M_via_blocks):.12f}")
    print(f"target (= Q_β/E_0)    = 0.186893691885...")
    print(f"diff:                   {float(tau_M_via_blocks - sp.Float('0.186893691885')):.2e}")

    # Emit witness
    w = WitnessBuilder("qbeta-per-block-symbolic-decomposition", engine="python")
    w.set_description(
        "Symbolic per-Wedderburn-block decomposition of χ_λ(T_β)(q) "
        "for the Q_β precision ladder. Establishes the per-block "
        "characters as exact rational functions of q, identifies the "
        "V_(2,1) standard 2D rep's character as linear in h = q-1/q, "
        "and provides Taylor coefficients around q=1 for per-block "
        "c_k^(λ) extraction. Foundational data for the c_4..c_7 "
        "categorical derivation via Path B (KLR canonical-basis trace)."
    )
    w.add_data("symbolic_chi_V3", str(sp.simplify(chi_T["(3)"])))
    w.add_data("symbolic_chi_V21", str(sp.simplify(chi_T["(2,1)"])))
    w.add_data("symbolic_chi_V111", str(sp.simplify(chi_T["(1,1,1)"])))
    w.add_data("V21_structural_form", {
        "type": "linear in h",
        "A_constant": float(coeff_const),
        "B_coefficient_of_h": float(B_coef),
        "formula": "χ_(2,1)(T_β)(q) = A + B·h(q)",
        "interpretation": (
            "The 2D V_(2,1) block's character is LINEAR in the Hecke "
            "parameter h = q - 1/q. The b² off-diagonal contributions "
            "from σ_1 and σ_0·σ_1 cancel exactly. This is a structurally "
            "clean form that suggests categorical underpinning."
        ),
    })
    w.add_data("taylor_coeffs_around_q1", taylor_data)
    w.add_assertion(
        "tau_M_via_blocks_matches_target",
        computed=float(abs(tau_M_via_blocks - sp.Float("0.18689369"))),
        expected=0,
        tolerance=1e-7,
        source="Σ y_λ · χ_λ(T_β) = τ_M(T_β) = Q_β/E_0 at q_0 (post-bug-fix)",
    )
    w.save()


if __name__ == "__main__":
    main()
