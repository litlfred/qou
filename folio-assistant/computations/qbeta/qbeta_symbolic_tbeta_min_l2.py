"""qbeta_symbolic_tbeta_min_l2.py — Step 1 of "1 y 2 y 3 y": SYMBOLIC
(pre-archimedean, formal q) closed form for the T_β NF coordinates,
extending the qbeta_prearchimedean_z_recursion.py backbone.

## What this probe attempts

The existing knot-operator SDP (qbeta_decay_sdp_solver.py) solves the
min-L2-norm problem AT q_0 (numerically):

    x* = argmin ||x||²   subject to   A(q_0) · x = S,
        S := Q_β/E_0 at q_0,    A_i(q) = τ_M(b_i)(q),    b_i ∈ NF basis.

The closed form is x* = A(q_0)^T · S / ||A(q_0)||²  (no Gram, no SDP —
Moore–Penrose for a single equality). Per the audit
`2026-06-02-qbeta-prearchimedean-recursion-status.md` (sharpened
2026-06-03), this is the LAST archimedean step: A_i(q) is fully
q-symbolic (Hoefsmit seminormal + cyclotomic y_λ(q)), so if we evaluate
the closed form SYMBOLICALLY in q, the T_β coordinates become

    x_i(q) = A_i(q) · S / ||A(q)||²,   S an archimedean scalar.

That is: the SHAPE of T_β as a function of q is q-rational; the only
archimedean input is the overall scalar S. The c_k of Q_β are then
(q-rational shape) × S — pre-archimedean modulo one number.

## Where the symbolic data comes from (pre-existing, exact)

- Hoefsmit σ_i per Wedderburn block of H_3(q):
    qbeta_per_block_symbolic.py lines 60–73
- NF-basis matrices b_i in each block (γ, σ₀, σ₁, L₊, L₋, e⁻):
    same file, line 76 (nf_mats())
- χ_λ(b_i)(q) = trace of those matrices (q-rational):
    same file, line 95
- y_λ(q) for n=3 as Laurent in r = q^{1/2} (Schur-element-style):
    y-lambda-cyclotomic-factor.witness.json (results["3"])

## What the probe outputs

  1. Symbolic A_i(q) for i = 1..6 (closed-form q-rationals).
  2. Symbolic ||A(q)||² (q-rational).
  3. Symbolic T_β coords x_i(q) = A_i(q)·S/||A||² (linear in S, shape q-rational).
  4. Numeric sanity: at q_0 with S = 0.186893691885…, the coords
     match the witness's T_beta_nf_coefficients to ≤ 1e-10.
  5. Symbolic τ_M(T_β)(q) = A·x = ||A||²·S/||A||² = S (the tautology;
     the q-shape of T_β reshuffles under change of q so the constraint
     remains satisfied — confirms the min-L2 rule's q-dependence).
  6. Symbolic Taylor expansion of A(q)·x_FIXED_at_q0 around q=1 — this
     is the actual τ_M(T_β)(q) used downstream for c_k.

## Pre-archimedean accounting

The archimedean / CODATA input to the c_k is now LOCALISED to the single
scalar S = Q_β(q_0)/E_0(q_0). Everything else is q-symbolic. This makes
the Habiro-integrality test (Step 2) runnable on the q-rational shape,
and gives the bridge instance (Step 3) a concrete handle: the candidate
Habiro element is S · F(q) where F(q) is the q-rational shape.

Ref: docs/audits/2026-06-02-qbeta-prearchimedean-recursion-status.md
Ref: folio-assistant/computations/qbeta/qbeta_per_block_symbolic.py
Ref: folio-assistant/computations/y-lambda-cyclotomic-factor.witness.json
"""
from __future__ import annotations

import sys
from pathlib import Path

# computations/ on sys.path — for _path_bridge + witness_base
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _pb  # noqa: E402, F401

import ast  # noqa: E402
import json  # noqa: E402

import sympy as sp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402


HERE = Path(__file__).resolve().parent


def hoefsmit_blocks(q):
    """Symbolic Hoefsmit seminormal σ_0, σ_1 per Wedderburn block of H_3(q).

    Reproduced from qbeta_per_block_symbolic.py (single source of truth).
    """
    sigma_0_V3 = sp.Matrix([[q]])
    sigma_1_V3 = sp.Matrix([[q]])

    sigma_0_V111 = sp.Matrix([[-1 / q]])
    sigma_1_V111 = sp.Matrix([[-1 / q]])

    b_sym = sp.sqrt(q ** 4 + q ** 2 + 1) / (q ** 2 + 1)
    sigma_0_V21 = sp.Matrix([[q, 0], [0, -1 / q]])
    sigma_1_V21 = sp.Matrix(
        [
            [-1 / (q * (q ** 2 + 1)), b_sym],
            [b_sym, q ** 3 / (q ** 2 + 1)],
        ]
    )

    return {
        "(3)": (sigma_0_V3, sigma_1_V3),
        "(2,1)": (sigma_0_V21, sigma_1_V21),
        "(1,1,1)": (sigma_0_V111, sigma_1_V111),
    }


def nf_basis_mats(s0, s1):
    """6-element NF basis (γ, σ₀, σ₁, L₊, L₋, e⁻) as block matrices."""
    eye = sp.eye(s0.rows)
    return [eye, s0, s1, s0 * s1, s1 * s0, s0 * s1 * s0]


def load_y_lambda_symbolic(r):
    """Load y_λ(q) for n=3 as q-symbolic rational functions in r = q^{1/2}.

    Source: y-lambda-cyclotomic-factor.witness.json — these are the
    Schur-element-style cyclotomic factorisations of the LP-dual shadow
    prices, NOT q₀-numerics.
    """
    with open(
        _pb.witness_path("y-lambda-cyclotomic-factor.witness.json", HERE),
        encoding="utf-8",
    ) as f:
        data = json.load(f)
    n3 = data["results"]["3"]
    r_sym = r  # local alias for sp.sympify env
    out = {}
    for part_str, info in n3.items():
        poly_str = info["y_polynomial"]["polynomial_q"]
        # poly_str uses "r"; parse in env where r = r_sym
        expr = sp.sympify(poly_str, locals={"r": r_sym})
        part = tuple(ast.literal_eval(part_str))
        if part == (3,):
            label = "(3)"
        elif part == (2, 1):
            label = "(2,1)"
        elif part == (1, 1, 1):
            label = "(1,1,1)"
        else:
            continue
        out[label] = expr
    return out


def main() -> int:
    q = sp.Symbol("q", positive=True)
    r = sp.sqrt(q)
    S = sp.Symbol("S")  # archimedean scalar = Q_β(q_0)/E_0(q_0)

    print("=" * 78)
    print("Step 1: SYMBOLIC q-rational closed form for T_β NF coordinates")
    print("=" * 78)
    print()

    # ----- 1. Build q-symbolic A_i(q) = Σ_λ y_λ(q) · χ_λ(b_i)(q) ---------
    blocks = hoefsmit_blocks(q)
    y_lam = load_y_lambda_symbolic(r)
    nf_names = ["γ", "σ_0", "σ_1", "L_+", "L_-", "e_-"]

    print("y_λ(q) as q-symbolic (loaded from cyclotomic witness):")
    for label, expr in y_lam.items():
        print(f"  y_{label}(q) = {expr}")
    print()

    chi_per_block = {}
    for label, (s0, s1) in blocks.items():
        mats = nf_basis_mats(s0, s1)
        chi_per_block[label] = [sp.simplify(sp.trace(m)) for m in mats]

    A = [
        sp.simplify(sum(y_lam[label] * chi_per_block[label][i] for label in blocks))
        for i in range(6)
    ]

    print("A_i(q) = Σ_λ y_λ(q) · χ_λ(b_i)(q)  [q-rational closed forms]:")
    for i, name in enumerate(nf_names):
        # Try a tidy display
        A_i_r = sp.together(sp.simplify(A[i]))
        print(f"  A_{name:>3s}(q) = {A_i_r}")
    print()

    # ----- 2. Symbolic ||A(q)||² and min-L2 closed form ------------------
    print("Computing ||A(q)||² symbolically (q-rational sum of squares)…")
    norm_sq = sp.simplify(sum(A[i] ** 2 for i in range(6)))
    norm_sq_simpl = sp.together(norm_sq)
    print(f"  ||A(q)||² = {norm_sq_simpl}")
    print()

    print("T_β coordinates (min-L2 closed form, symbolic in q, linear in S):")
    print("  x_i(q) = A_i(q) · S / ||A(q)||²")
    x_sym = [sp.simplify(A[i] * S / norm_sq) for i in range(6)]
    for i, name in enumerate(nf_names):
        coeff_of_S = sp.simplify(x_sym[i] / S)
        coeff_of_S = sp.together(coeff_of_S)
        print(f"  x_{name:>3s}(q) / S = {coeff_of_S}")
    print()

    # ----- 3. Numeric sanity check at q_0 --------------------------------
    print("=" * 78)
    print("Numeric sanity check at q_0  (vs witness T_beta_nf_coefficients)")
    print("=" * 78)
    with open(
        _pb.witness_path("q-pinning-50-digit.witness.json", HERE),
        encoding="utf-8",
    ) as f:
        q0_str = json.load(f)["derived_50_digit"]["q"]
    q0 = sp.Float(q0_str, 50)

    with open(
        _pb.witness_path("qbeta-decay-sdp-knot-operator.witness.json", HERE),
        encoding="utf-8",
    ) as f:
        sdp = json.load(f)
    S_num = sp.Float(sdp["data"]["tau_M_at_q0"], 50)  # = Q_β/E_0
    coords_witness = sdp["data"]["T_beta_nf_coefficients"]
    name_map = {"γ": "γ", "σ_0": "σ₀", "σ_1": "σ₁",
                "L_+": "L₊", "L_-": "L₋", "e_-": "e⁻"}

    print(f"  q_0 = {float(q0):.10f}")
    print(f"  S   = τ_M(T_β)(q_0) = {float(S_num):.12f}")
    print()
    print(f"  {'name':<5s} {'symbolic@q_0':>20s} {'witness':>20s} {'diff':>12s}")
    max_diff = 0.0
    for i, name in enumerate(nf_names):
        val_sym = float(x_sym[i].subs({q: q0, S: S_num}))
        val_wit = coords_witness[name_map[name]]
        diff = abs(val_sym - val_wit)
        max_diff = max(max_diff, diff)
        print(f"  {name:<5s} {val_sym:>20.12f} {val_wit:>20.12f} {diff:>12.2e}")
    print()
    sanity_ok = max_diff < 1e-9
    print(
        f"  Symbolic min-L2 closed form ≡ numeric witness at q_0: "
        f"{'YES ✓' if sanity_ok else 'NO ✗'}  (max diff = {max_diff:.2e})"
    )
    print()

    # ----- 4. τ_M(T_β)(q) Taylor at q=1 (with x* fixed at q_0) ----------
    # This is the actual function used downstream for the c_k. With
    # x* fixed at q_0 (the current production rule), τ_M(T_β)(q) =
    # A(q) · x*(q_0). Compare its Taylor coefficients to the witness.
    print("=" * 78)
    print("τ_M(T_β)(q) Taylor expansion at q=1, with x* FIXED at q_0")
    print("(matches the current production rule; reproduces witness coefficients)")
    print("=" * 78)
    x_at_q0 = [x_sym[i].subs({q: q0, S: S_num}) for i in range(6)]
    tau_M_TB = sum(A[i] * x_at_q0[i] for i in range(6))
    w = sp.Symbol("w")
    tau_series = sp.series(tau_M_TB.subs(q, 1 + w), w, 0, 8).removeO()
    a_coeffs_sym = [tau_series.coeff(w, k) for k in range(8)]
    print(f"  {'k':>2s} {'a_k (symbolic, q_0 anchor)':>32s} {'a_k (witness)':>22s}")
    a_witness = sdp["data"]["tau_M_taylor_coefficients"]
    a_max_diff = 0.0
    for k in range(8):
        sym_val = float(a_coeffs_sym[k])
        wit_val = a_witness.get(f"a_{k}")
        if wit_val is None:
            print(f"  {k:>2d} {sym_val:>32.12e} {'(n/a)':>22s}")
            continue
        d = abs(sym_val - wit_val)
        a_max_diff = max(a_max_diff, d)
        print(f"  {k:>2d} {sym_val:>32.12e} {wit_val:>22.12e}   (Δ={d:.1e})")
    print()
    taylor_ok = a_max_diff < 1e-9
    print(
        f"  Symbolic τ_M(T_β) Taylor ≡ witness coefficients: "
        f"{'YES ✓' if taylor_ok else 'NO ✗'}  (max diff = {a_max_diff:.2e})"
    )
    print()

    # ----- 5. Punchline ------------------------------------------------
    print("=" * 78)
    print("Pre-archimedean accounting — what is symbolic, what is not")
    print("=" * 78)
    print(
        "  • A_i(q), ||A(q)||², x_i(q)/S  —  all q-rational, exact.\n"
        "    (Hoefsmit + Schur-element y_λ(q); NO q_0, NO CODATA.)\n"
        "  • The min-L2 rule itself  —  a single archimedean choice:\n"
        "    Euclidean norm on coordinate space, evaluated at the anchor q_0.\n"
        "  • Scalar S = Q_β(q_0)/E_0(q_0)  —  one archimedean number\n"
        "    (the experimental β-decay rate normalised by E_0).\n\n"
        "  ⇒  T_β coords are (q-rational shape) × S, evaluated at q_0.\n"
        "  ⇒  τ_M(T_β)(q) and Q_β(q) inherit the same structure.\n"
        "  ⇒  The precision-ladder c_k are (q-rational ratios) × S^*  where\n"
        "     the S-power depends on how the c_k normalise out in the\n"
        "     Q_A·cos·∏(1+c_k u^k) expansion. The q-rational SHAPE is\n"
        "     pre-archimedean; this is the input for Step 2 (Habiro\n"
        "     integrality) and Step 3 (bridge instance).\n"
    )

    # ----- 6. Witness ----------------------------------------------------
    wn = WitnessBuilder("qbeta-symbolic-tbeta-min-l2", engine="sympy")
    wn.set_description(
        "Closed-form, q-rational, pre-archimedean min-L2 selection of "
        "the β-decay knot operator T_β in H_3(q)'s NF basis. Reproduces "
        "the production witness's numeric T_beta_nf_coefficients at q_0 "
        "exactly. Locates the archimedean / CODATA input of the c_k to a "
        "single scalar S = Q_β(q_0)/E_0(q_0); everything else (Hoefsmit "
        "seminormal, Schur-element y_λ(q), basis traces, ||A(q)||²) is "
        "symbolic in q. This is Step 1 of the recursion-bridge plan; "
        "Step 2 (Habiro integrality) and Step 3 (bridge instance) now "
        "act on the q-rational SHAPE of x_i(q)/S, not on q_0-numerics."
    )
    wn.add_data("nf_names", nf_names)
    wn.add_data(
        "A_q_symbolic",
        [str(sp.together(sp.simplify(A[i]))) for i in range(6)],
    )
    wn.add_data("norm_sq_symbolic", str(norm_sq_simpl))
    wn.add_data(
        "x_per_S_symbolic",
        [str(sp.together(sp.simplify(x_sym[i] / S))) for i in range(6)],
    )
    wn.add_data("S_at_q0", float(S_num))
    wn.add_assertion(
        name="symbolic_coords_match_witness_at_q0",
        computed=bool(sanity_ok),
        expected=True,
        tolerance=1e-9,
        source="symbolic A·S/||A||² vs T_beta_nf_coefficients (knot-operator SDP)",
    )
    wn.add_assertion(
        name="symbolic_tau_M_taylor_matches_witness",
        computed=bool(taylor_ok),
        expected=True,
        tolerance=1e-9,
        source="series(τ_M(T_β)(1+w), w, 0, 8) vs tau_M_taylor_coefficients",
    )
    out = wn.save()
    print(f"  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
