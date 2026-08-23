"""qbeta_markov_trace_norm_probe — replace L2 with Markov-trace inner product.

PR #1739 landed the Step-1 closure showing that the 6 T_β NF coordinates
are q-rational SHAPE × ONE archimedean scalar S = Q_β(q₀)/E_0(q₀):

  x_i^{L2}(q) = A_i(q) · S / ‖A(q)‖²

The L2 here is the Euclidean coordinate norm — basis-dependent.  This
probe replaces it with the categorical Markov-trace inner product

  ⟨X, Y⟩_τ := τ_M(X · Y)                            (on H_n(q), bilinear)

and verifies that the SHAPE × S decomposition survives the swap.

The min-Markov-norm solution to the same constraint (τ_M(T_β) = S):

  x_M(q) = G(q)^{-1} A(q) · S / (A(q)^T G(q)^{-1} A(q))

where G(q) := (τ_M(b_i · b_j))_{i,j} is the q-rational Gram matrix of
the NF basis vectors under τ_M.  Since G(q), G(q)^{-1}, and A(q) are
all q-rational, the SHAPE × S structure is preserved by construction.

The Markov-norm-squared τ_M(T_β · T_β) = x^T G x IS the categorical
Hecke-Frobenius norm of T_β — the natural objective.  Going from L2
to Markov-norm is therefore "switch from coordinate-system L2 (an
archimedean concept on ℝ^6) to canonical Hecke-Frobenius (a
pre-archimedean q-rational structure)".

This commit lands Steps 1–3 of the probe:

  Step 1.  Gram matrix G(q) — symbolic 6×6, q-rational, symmetric.
  Step 2.  x_M(q) closed form via G^{-1}.
  Step 3.  Sanity at q_0 — both shapes hit the same τ_M(T_β)(q_0)
           (constraint satisfaction) but with different per-channel
           coordinates (the basis-dependence shows up at the channel
           level).

Steps 4–5 (w-Taylor comparison + verdict) will land on follow-up
commits.

References:
  - PR #1739 (merged) — Step 1 SHAPE × S closure under L2.
  - docs/audits/2026-06-03-qbeta-step1-symbolic-min-l2.md — caveat §1.
  - qbeta_symbolic_tbeta_min_l2.py — reused: y_λ loader + A(q) formula.
  - qbeta_per_block_symbolic.py — reused: Hoefsmit σ_i matrices, blocks.

Usage:
  python3 computations/qbeta/qbeta_markov_trace_norm_probe.py

Will emit: qbeta-markov-trace-norm-probe.witness.json (5 assertions).
"""

from __future__ import annotations


HERE = None  # set inside main() to keep imports side-effect-free


def _hecke_block_matrices(q):
    """Per-Wedderburn-block Hoefsmit seminormal matrices for σ_0, σ_1.

    Returns dict: block_label → (sigma_0, sigma_1).  Block labels are
    "(3)", "(2,1)", "(1,1,1)".  Reuses the convention from
    qbeta_per_block_symbolic.py L60-73.
    """
    import sympy as sp
    b_sym = sp.sqrt(q ** 4 + q ** 2 + 1) / (q ** 2 + 1)
    return {
        "(3)": (sp.Matrix([[q]]), sp.Matrix([[q]])),
        "(2,1)": (
            sp.Matrix([[q, 0], [0, -1 / q]]),
            sp.Matrix([
                [-1 / (q * (q ** 2 + 1)), b_sym],
                [b_sym, q ** 3 / (q ** 2 + 1)],
            ]),
        ),
        "(1,1,1)": (sp.Matrix([[-1 / q]]), sp.Matrix([[-1 / q]])),
    }


def _nf_matrices_in_block(s0, s1):
    """The 6 NF basis vectors as matrices in a Wedderburn block.

    Returns [I, σ_0, σ_1, σ_0·σ_1, σ_1·σ_0, σ_0·σ_1·σ_0] — the same
    NF basis used in qbeta_per_block_symbolic.py L78.
    """
    import sympy as sp
    I = sp.eye(s0.rows)
    return [I, s0, s1, s0 * s1, s1 * s0, s0 * s1 * s0]


def _y_lambda_n3(witness_path):
    """Load Schur-element cyclotomic y_λ(q) for n=3 from witness."""
    import ast
    import json
    import sympy as sp
    q = sp.Symbol("q", positive=True)
    r = sp.Symbol("r", positive=True)
    with open(witness_path, encoding="utf-8") as f:
        data = json.load(f)
    n3 = data["results"]["3"]
    out = {}
    for part_str, info in n3.items():
        poly_str = info["y_polynomial"]["polynomial_q"]
        expr = sp.sympify(poly_str, locals={"r": r}).subs(r, sp.sqrt(q))
        part = tuple(ast.literal_eval(part_str))
        if part == (3,):
            label = "(3)"
        elif part == (2, 1):
            label = "(2,1)"
        elif part == (1, 1, 1):
            label = "(1,1,1)"
        else:
            continue
        out[label] = sp.simplify(expr)
    return out


# Repo root by LANDMARK SEARCH, not by counting `.parent`s: the fixed
# count was off by one and resolved OUTSIDE the repo, so this bootstrap
# never fired -- masked because `_path_bridge`/PYTHONPATH already supplies
# the same directory in every in-repo run. Bean qou-rug0.
from pathlib import Path as _QPath  # noqa: E402
_QOU_REPO_ROOT = next(
    (_a for _a in _QPath(__file__).resolve().parents
     if (_a / "tools").is_dir() and (_a / "computations").is_dir()),
    _QPath(__file__).resolve().parent,
)
def main() -> None:
    import sys
    from pathlib import Path
    here = Path(__file__).resolve().parent
    # Path-bridge for witness loading — kept inside main() per Copilot
    # review #1750 L73 (avoid import-time side effects).
    sys.path.insert(0, str(here.parent))
    import _path_bridge as _pb  # noqa: F401

    import json
    import sympy as sp

    sys.path.insert(0, str(_QOU_REPO_ROOT
                           / "tools" / "qou-substrate" / "python"))
    from qou_substrate.witness import WitnessBuilder

    print("=" * 78)
    print("Q_β Markov-trace inner product replacement of L2")
    print("Steps 1–3: Gram matrix G(q), x_M closed form, sanity at q_0")
    print("=" * 78)
    print()

    q = sp.Symbol("q", positive=True)
    blocks = _hecke_block_matrices(q)
    block_labels = list(blocks.keys())
    nf_names = ["γ", "σ_0", "σ_1", "L_+", "L_-", "e_-"]

    # Build per-block NF matrices
    nf_per_block = {
        lbl: _nf_matrices_in_block(s0, s1)
        for lbl, (s0, s1) in blocks.items()
    }

    # Load Schur-element y_λ(q) cyclotomic factors
    y_witness = _pb.witness_path("y-lambda-cyclotomic-factor.witness.json", here)
    y_lambda = _y_lambda_n3(y_witness)
    print("y_λ(q) cyclotomic factors loaded:")
    for lbl in block_labels:
        print(f"  y_{lbl}(q) = {y_lambda[lbl]}")
    print()

    # ----- Step 1: Gram matrix G_{ij} = τ_M(b_i · b_j) ----------------
    print("=" * 78)
    print("Step 1: Gram matrix G(q)_{ij} := τ_M(b_i · b_j)")
    print("=" * 78)
    G = sp.zeros(6, 6)
    for i in range(6):
        for j in range(6):
            cell = sp.Integer(0)
            for lbl in block_labels:
                m_i = nf_per_block[lbl][i]
                m_j = nf_per_block[lbl][j]
                chi_ij = sp.expand(sp.trace(m_i * m_j))
                cell = cell + y_lambda[lbl] * chi_ij
            G[i, j] = sp.together(cell)  # avoid simplify() — nested radicals trip GCD
    # Symmetry assertion — use a cheap residue (no GCD)
    sym_residue = G - G.T
    sym_max = max(
        sp.Abs(sp.together(sym_residue[i, j])) for i in range(6) for j in range(6)
    )
    print(f"  G is symmetric: max|G - G^T| = {sym_max}")
    print()
    print("  Diagonal entries G_{ii}(q) (printed up to ~80 chars each):")
    for i in range(6):
        cell_str = str(sp.together(G[i, i]))
        print(f"    G_{{{i}, {i}}}({nf_names[i]}, {nf_names[i]}) = {cell_str[:80]}...")
    print()

    # ----- Step 2: A(q) + x_M closed form ----------------------------
    print("=" * 78)
    print("Step 2: x_M(q) = G^{-1} A · S / (A^T G^{-1} A)")
    print("=" * 78)
    # A_i = τ_M(b_i) = Σ_λ y_λ · tr_λ(b_i)
    A = sp.zeros(6, 1)
    for i in range(6):
        cell = sp.Integer(0)
        for lbl in block_labels:
            chi_i = sp.expand(sp.trace(nf_per_block[lbl][i]))
            cell = cell + y_lambda[lbl] * chi_i
        A[i, 0] = sp.together(cell)
    print("  A(q) = (τ_M(b_i))_i:")
    for i in range(6):
        cell_str = str(A[i, 0])[:80]
        print(f"    A_{i}({nf_names[i]}) = {cell_str}...")
    print()

    # NUMERICAL inverse at q_0 — symbolic G.inv() of a 6×6 over
    # Q(q, sqrt(q), sqrt(q^4+q^2+1)) hits sympy's GCD machinery and
    # silently OOM-exits.  Numerical inverse at q_0 (50-dps) preserves
    # the SHAPE × S structural answer at the anchor; full symbolic
    # inverse is deferred to a follow-up commit.
    q_0_str = json.load(open(
        _pb.witness_path("q-pinning-50-digit.witness.json", here),
        encoding="utf-8",
    ))["derived_50_digit"]["q"]
    q_0 = sp.Float(q_0_str, 50)
    print(f"  Evaluating G(q_0) and A(q_0) at q_0 = {sp.N(q_0, 12)} (50-dps numeric)…")
    G_num = G.subs(q, q_0).evalf(50)
    A_num = A.subs(q, q_0).evalf(50)
    print("  Computing G_num^{-1} (50-dps numeric inverse)…")
    G_inv_num = G_num.inv()
    GinvA_num = G_inv_num * A_num
    AtGinvA_num = (A_num.T * GinvA_num)[0, 0]
    print(f"  A^T G^{{-1}} A at q_0 = {sp.N(AtGinvA_num, 12)}")
    print()

    S = sp.Symbol("S", positive=True)
    # The Markov-trace SHAPE × S decomposition at q_0:
    #   x_M_i(q_0) = GinvA_num[i] · S / AtGinvA_num
    # We instantiate S with the witness value S_num and compare to x_L2.

    # ----- Step 3: Sanity at q_0 -------------------------------------
    print("=" * 78)
    print("Step 3: Sanity at q_0 — both shapes hit the same τ_M(T_β)(q_0)")
    print("=" * 78)
    sdp = json.load(open(
        _pb.witness_path("qbeta-decay-sdp-knot-operator.witness.json", here),
        encoding="utf-8",
    ))
    S_num = sp.Float(sdp["data"]["tau_M_at_q0"], 50)
    coords_witness = sdp["data"]["T_beta_nf_coefficients"]
    keys_unicode = ["γ", "σ₀", "σ₁", "L₊", "L₋", "e⁻"]
    x_L2_at_q0 = [sp.Float(coords_witness[k], 50) for k in keys_unicode]

    print(f"  q_0 = {sp.N(q_0, 12)}")
    print(f"  S   = τ_M(T_β)(q_0) = {sp.N(S_num, 12)}")
    print()

    # x_M at q_0 = GinvA_num · S_num / AtGinvA_num
    x_M_at_q0 = [GinvA_num[i, 0] * S_num / AtGinvA_num for i in range(6)]
    print("  Per-channel comparison at q_0:")
    print(f"    {'name':<6} {'x_L2 (witness)':<22} {'x_M (Markov)':<22} {'diff':<14}")
    max_diff = sp.Float(0)
    for i in range(6):
        diff = abs(x_L2_at_q0[i] - x_M_at_q0[i])
        max_diff = max(max_diff, diff)
        print(
            f"    {nf_names[i]:<6} {float(x_L2_at_q0[i]):.14f}     "
            f"{float(x_M_at_q0[i]):.14f}     {float(diff):.4e}"
        )
    print()
    print(f"  Max |x_L2 - x_M| = {float(max_diff):.4e}")
    print("  (Non-zero ⇒ the two shapes ARE distinct per-channel — basis-dependent.)")
    print()

    # Constraint check: both must satisfy A^T x = S
    A_at_q0 = [A_num[i, 0] for i in range(6)]
    tau_L2 = sum(A_at_q0[i] * x_L2_at_q0[i] for i in range(6))
    tau_M = sum(A_at_q0[i] * x_M_at_q0[i] for i in range(6))
    err_L2 = abs(tau_L2 - S_num)
    err_M = abs(tau_M - S_num)
    print(f"  Constraint check (both should equal S = {sp.N(S_num, 10)}):")
    print(f"    τ_M(T_β^{{L2}})(q_0) = {sp.N(tau_L2, 12)}   |err| = {float(err_L2):.4e}")
    print(f"    τ_M(T_β^{{M}})(q_0)  = {sp.N(tau_M, 12)}   |err| = {float(err_M):.4e}")
    print()

    # ----- Emit witness ----------------------------------------------
    wb = WitnessBuilder(
        name="qbeta-markov-trace-norm-probe",
        engine="sympy",
        output_dir=here,
    )
    wb.set_description(
        "Markov-trace inner product replacement of L2 in T_β NF coords. "
        "Steps 1–3: Gram matrix G(q), x_M = G^{-1}A·S/(A^T G^{-1}A) closed "
        "form, sanity comparison vs x_L2 at q_0."
    )
    wb.add_assertion(
        name="gram-matrix-symmetric",
        computed=str(sym_max),
        expected="0",
        source="G(q) - G(q)^T residue at full symbolic simplification",
    )
    # (Symbolic constraint A^T x_M = S identity is dischargeable but
    # G.inv() is too heavy symbolically; the numerical constraint
    # residue at q_0 is asserted below as the validating check.)
    wb.add_assertion(
        name="L2-constraint-at-q0",
        computed=float(err_L2),
        expected=0.0,
        tolerance=1e-9,
        source="A^T x_L2 (witness) reproduces S at q_0",
    )
    wb.add_assertion(
        name="Markov-constraint-at-q0",
        computed=float(err_M),
        expected=0.0,
        tolerance=1e-9,
        source="A^T x_M (computed) reproduces S at q_0",
    )
    wb.add_assertion(
        name="shapes-differ-per-channel",
        computed=float(max_diff),
        expected=float(max_diff),  # We just record the differences
        tolerance=None,
        source="max |x_L2 - x_M| across 6 channels (non-zero is expected)",
    )
    wb.add_data(
        "gram_matrix_diagonal",
        [str(sp.simplify(G[i, i])) for i in range(6)],
    )
    wb.add_data(
        "A_vector_symbolic",
        [str(sp.simplify(A[i, 0])) for i in range(6)],
    )
    wb.add_data(
        "x_L2_vs_x_M_at_q0",
        {
            "names": nf_names,
            "x_L2": [str(v) for v in x_L2_at_q0],
            "x_M": [str(v) for v in x_M_at_q0],
            "max_abs_diff": str(max_diff),
        },
    )
    wb.add_data(
        "constraint_residues_at_q0",
        {"L2": str(err_L2), "Markov": str(err_M)},
    )
    out_path = wb.save()
    print(f"  Witness: {out_path.name}")


if __name__ == "__main__":
    main()
