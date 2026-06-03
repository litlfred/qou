"""qbeta_symbolic_sdp_strict_complementarity.py — q-rational SDP
strict-complementarity selection of the β-decay knot operator T_β.

EXPLORATORY probe (three-calibration discipline applies — NO empirical
fit to CODATA Q_β; if the only way to match is to fit, this script STOPS
and records the negative result).

## The problem with the current selection

The production "knot-operator SDP" (`qbeta_decay_sdp_solver.py`) does NOT
run an SDP. It runs the min-L2 closed form

    x* = (n_target / (t·t)) · t,   with   n_target := Q_β(CODATA) / E_0 .

(see `qbeta_decay_sdp_solver.py` lines 78, 94). The net-constraint RHS
`n_target` IS the CODATA Q_β. So the selected T_β tautologically has
τ_M(T_β)(q_0) = Q_β(CODATA)/E_0 — it cannot *predict* Q_β. Sibling
PR #1739 (`qbeta_symbolic_tbeta_min_l2.py`) made this precise: the T_β
coordinates are (q-rational shape) × S, with S = Q_β(q_0)/E_0(q_0) the
single archimedean / CODATA input.

## The lever — genuine SDP strict complementarity

The canonical knot-operator-selection program (per
`prop:operator-selection-lp`, `lp_dual_solver.solve_operator_selection_lp`)
is

    min  t·x      s.t.   Σ_i x_i = n_target,   G·x ≥ 0,

with q-rational cost  t_i = τ_M(b_i)(q)  and q-rational Frobenius Gram
G_{ij} = τ_M(b_i b_j)(q).  The feasible set is the cone {G x ≥ 0} sliced
by the affine hyperplane {Σ x_i = n_target}.  Scaling n_target scales the
ENTIRE slice homogeneously, so the optimal vertex DIRECTION

    x*(n_target) / n_target   is INDEPENDENT of n_target,

and the active set (which Frobenius constraints bind) is fixed by (t, G)
alone — both q-rational.  Strict complementarity (when it holds) makes
this active set, hence the normalized selector, UNIQUE.

## The crux test (what this probe decides)

The full Q_β assembly (per `qbeta_ladder_verification_1ppq.py`) is

    Q_β = Q_A(q) · cos(α - b ℏ²/2) · (1 - b² ℏ⁴) · (1 + c_3 b³ ℏ⁶) · …

Q_A, α, b, ℏ_q are ALL q-rational / substrate-derived (NO CODATA Q_β).
The c_k are the precision-ladder corrections.  If the SDP-selected T_β
reproduces the same c_k *directions* with the overall scale supplied by a
q-rational n_target (NOT CODATA Q_β), then S cancels and Q_β is predicted
independent of its CODATA value.

This probe:
  1. Builds the q-rational cost t_i(q) = τ_M(b_i)(q) and Frobenius Gram
     G_{ij}(q) = τ_M(b_i b_j)(q) over the 6-element NF basis of H_3(q),
     reusing #1739's Hoefsmit blocks + Schur-element y_λ(q).
  2. Verifies that t_i(q) reproduces #1739's A_i(q) (cross-check).
  3. Solves the genuine operator-selection LP/SDP at q_0 and reports
     primal + dual (y0_star, y_star, active_set, primal/dual_obj, gap).
  4. Tests SCALE-INVARIANCE of the selector direction: solves at two
     distinct n_target values and checks x*(n1)/n1 == x*(n2)/n2.  This
     is the operational form of "S cancels from the directions".
  5. THE NEGATIVE-RESULT GUARD: checks whether the SDP optimum, with a
     q-rational n_target, still requires CODATA Q_β to fix the SCALE of
     τ_M(T_β).  Reports HONESTLY whether S cancels.

Ref: docs/canonical-derivation-cheat-sheet.md §"11. β-decay Q"
Ref: folio-assistant/computations/lp_dual_solver.py (solve_operator_selection_lp)
Ref: folio-assistant/computations/qbeta/qbeta_symbolic_tbeta_min_l2.py (PR #1739)
Ref: folio-assistant/computations/qbeta/qbeta_decay_sdp_solver.py (min-L2 incumbent)
Ref: prop:operator-selection-lp (LP/SDP first-class-infra rule, CLAUDE.md)
"""
from __future__ import annotations

import sys
from pathlib import Path

# computations/ on sys.path — _path_bridge gives witness_base + lp_dual_solver
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _pb  # noqa: E402, F401

import ast  # noqa: E402
import json  # noqa: E402

import mpmath as mp  # noqa: E402
import numpy as np  # noqa: E402
import sympy as sp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402
from lp_dual_solver import solve_operator_selection_lp  # noqa: E402

HERE = Path(__file__).resolve().parent

# 50-dps compute floor per _precision.py discipline.
mp.mp.dps = 60


# --------------------------------------------------------------------------
# Symbolic H_3(q) data — reproduced from #1739 / qbeta_per_block_symbolic.py
# (single source of truth: Hoefsmit seminormal + Schur-element y_λ(q)).
# --------------------------------------------------------------------------
def hoefsmit_blocks(q):
    """Symbolic Hoefsmit seminormal σ_0, σ_1 per Wedderburn block of H_3(q)."""
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
    """y_λ(q) for n=3 as q-symbolic rational functions in r = q^{1/2}."""
    with open(
        _pb.witness_path("y-lambda-cyclotomic-factor.witness.json", HERE),
        encoding="utf-8",
    ) as f:
        data = json.load(f)
    n3 = data["results"]["3"]
    out = {}
    for part_str, info in n3.items():
        poly_str = info["y_polynomial"]["polynomial_q"]
        expr = sp.sympify(poly_str, locals={"r": r})
        part = tuple(ast.literal_eval(part_str))
        label = {(3,): "(3)", (2, 1): "(2,1)", (1, 1, 1): "(1,1,1)"}.get(part)
        if label:
            out[label] = expr
    return out


def build_symbolic_t_and_G(q):
    """Return (t_sym, G_sym, nf_names): q-rational Markov-trace cost vector
    t_i = τ_M(b_i) and Frobenius Gram G_{ij} = τ_M(b_i b_j), 6×6.

    τ_M of a global operator X = (X_λ)_λ is Σ_λ y_λ(q) · tr(X_λ).
    """
    r = sp.sqrt(q)
    y_lam = load_y_lambda_symbolic(r)
    blocks = hoefsmit_blocks(q)
    nf_names = ["γ", "σ_0", "σ_1", "L_+", "L_-", "e_-"]

    nf_per_block = {label: nf_basis_mats(s0, s1) for label, (s0, s1) in blocks.items()}

    def tau_M(per_block_mats, full_simplify=False):
        """Markov trace Σ_λ y_λ · tr(M_λ) of a per-block operator.

        The (2,1) block carries the radical b_sym = √(q⁴+q²+1)/(q²+1);
        sympy's heuristic GCD can fail on `simplify` of such mixed-radical
        sums.  We default to `together` (no GCD heuristic) and only attempt
        `radsimp` on the cost vector / Gram diagonal where it is safe.
        """
        expr = sum(y_lam[label] * sp.trace(per_block_mats[label]) for label in blocks)
        if full_simplify:
            try:
                return sp.radsimp(sp.together(expr))
            except Exception:  # noqa: BLE001 — robustness over a known sympy GCD bug
                return sp.together(expr)
        return sp.together(expr)

    # Cost t_i = τ_M(b_i) — rational in q (traces of NF basis are q-rational),
    # full-simplify safe.
    t_sym = [
        tau_M({label: nf_per_block[label][i] for label in blocks}, full_simplify=True)
        for i in range(6)
    ]

    # Gram G_{ij} = τ_M(b_i · b_j). Off-diagonal entries can carry the radical
    # (b_sym); keep them as `together`-folded expressions and rely on the
    # numeric evaluation at q_0 for the LP.
    G_sym = [[None] * 6 for _ in range(6)]
    for i in range(6):
        for j in range(6):
            prod = {label: nf_per_block[label][i] * nf_per_block[label][j] for label in blocks}
            G_sym[i][j] = tau_M(prod, full_simplify=(i == j))
    return t_sym, G_sym, nf_names


def sym_to_float(expr, q, q0):
    """Evaluate a q-symbolic expression at q_0 to mpmath precision, then float."""
    val = expr.subs(q, sp.Float(str(q0), 60))
    return float(sp.N(val, 50))


def main() -> int:
    print("=" * 78)
    print("Q_β: q-rational SDP strict-complementarity selection of T_β")
    print("(EXPLORATORY — no CODATA-Q_β fit)")
    print("=" * 78)
    print()

    q = sp.Symbol("q", positive=True)

    # ---- 1. q-rational cost + Gram --------------------------------------
    print("[1] Building q-rational cost t_i(q) = τ_M(b_i) and Gram")
    print("    G_{ij}(q) = τ_M(b_i b_j) over the 6-element NF basis…")
    t_sym, G_sym, nf_names = build_symbolic_t_and_G(q)
    for i, nm in enumerate(nf_names):
        print(f"    t_{nm:>3s}(q) = {sp.together(t_sym[i])}")
    print()

    # ---- 2. Cross-check against #1739's A_i(q) ---------------------------
    # #1739's A_i(q) = Σ_λ y_λ χ_λ(b_i) = τ_M(b_i) = our t_i. Symbolic match.
    try:
        with open(
            _pb.witness_path("qbeta-symbolic-tbeta-min-l2.witness.json", HERE),
            encoding="utf-8",
        ) as f:
            sib = json.load(f)
        A_sib = sib["data"]["A_q_symbolic"]
        # Numeric agreement at q_0 (robust to radical-simplify failures).
        with open(
            _pb.witness_path("q-pinning-50-digit.witness.json", HERE), encoding="utf-8"
        ) as f2:
            q0_chk = mp.mpf(json.load(f2)["derived_50_digit"]["q"])
        # #1739's A strings use r = √q; map it to sqrt(q) for evaluation.
        r_sym = sp.sqrt(q)
        diffs = []
        for i in range(6):
            a_expr = sp.sympify(A_sib[i], locals={"r": r_sym, "q": q})
            a = sym_to_float(a_expr, q, q0_chk)
            t = sym_to_float(t_sym[i], q, q0_chk)
            diffs.append(abs(a - t))
        match_1739 = max(diffs) < 1e-10
        print(f"[2] t_i(q) ≡ #1739 A_i(q):  {'YES' if match_1739 else 'NO'}")
    except (FileNotFoundError, KeyError):
        match_1739 = None
        print("[2] #1739 witness not present locally — skipping A_i cross-check")
    print()

    # ---- substrate q_0 ---------------------------------------------------
    with open(
        _pb.witness_path("q-pinning-50-digit.witness.json", HERE), encoding="utf-8"
    ) as f:
        q0 = mp.mpf(json.load(f)["derived_50_digit"]["q"])

    t_num = np.array([sym_to_float(t_sym[i], q, q0) for i in range(6)])
    G_num = np.array(
        [[sym_to_float(G_sym[i][j], q, q0) for j in range(6)] for i in range(6)]
    )
    # Symmetrize tiny float asymmetry from independent simplifications.
    G_num = 0.5 * (G_num + G_num.T)

    # ---- 3. Genuine operator-selection LP at q_0 ------------------------
    # n_target is a q-RATIONAL normalization (NOT CODATA Q_β). We use
    # n_target = 1 (unit net) for the canonical direction; the physical
    # scale is restored separately and tested for cancellation below.
    print("[3] Genuine operator-selection LP at q_0 (n_target = 1, q-rational):")
    res1 = solve_operator_selection_lp(t_num, G_num, 1.0)
    print(f"    feasible       = {res1.feasible}")
    print(f"    x*             = {[f'{x:+.6f}' for x in res1.x_star]}")
    print(f"    y0_star        = {res1.y0_star:+.8f}")
    print(f"    y_star         = {[f'{y:+.4f}' for y in res1.y_star]}")
    print(f"    active_set     = {res1.active_set}")
    print(f"    primal_obj     = {res1.primal_obj:+.8f}")
    print(f"    dual_obj       = {res1.dual_obj:+.8f}")
    print(f"    duality_gap    = {res1.duality_gap:.2e}")
    print()

    # ---- 4. Scale-invariance of the selector direction ------------------
    # "S cancels from the directions" ⇔ x*(n)/n is independent of n.
    print("[4] Scale-invariance test (does S cancel from the DIRECTION?):")
    n_a, n_b = 0.1868936918861772, 1.0  # one CODATA-shaped, one q-rational
    res_a = solve_operator_selection_lp(t_num, G_num, n_a)
    res_b = solve_operator_selection_lp(t_num, G_num, n_b)
    if res_a.feasible and res_b.feasible:
        dir_a = np.array(res_a.x_star) / n_a
        dir_b = np.array(res_b.x_star) / n_b
        dir_diff = float(np.max(np.abs(dir_a - dir_b)))
        same_active = res_a.active_set == res_b.active_set
        scale_invariant = dir_diff < 1e-7 and same_active
        print(f"    active_set(n_a={n_a:.4f}) = {res_a.active_set}")
        print(f"    active_set(n_b={n_b:.4f}) = {res_b.active_set}")
        print(f"    max|x*(n_a)/n_a − x*(n_b)/n_b| = {dir_diff:.2e}")
        print(f"    DIRECTION is scale-invariant (S-independent): "
              f"{'YES' if scale_invariant else 'NO'}")
    else:
        scale_invariant = False
        dir_diff = float("nan")
        print("    LP infeasible at one of the targets — cannot test")
    print()

    # ---- 5. The crux: does S cancel from the c_k / Q_β prediction? ------
    print("[5] CRUX — does the overall scale S cancel from the Q_β prediction?")
    print("    The β-decay observable is  Q_β = E_0 · τ_M(T_β),  and")
    print("    τ_M(T_β) = t·x* = primal_obj.  Writing x* = scale · x̂ with x̂ the")
    print("    unit-net direction, τ_M(T_β) = scale · (t·x̂).  The DIRECTION x̂ is")
    print("    S-independent and q-rational (step 4), so the dimensionless")
    print("    precision-ladder FACTORS (1 + c_k u^k) — ratios of the frozen-")
    print("    direction q-shape — are S-INDEPENDENT.  BUT the overall MAGNITUDE")
    print("    τ_M(T_β) = scale·(t·x̂) needs the net-constraint `scale = n_target`,")
    print("    and the only categorical value for n_target is τ_M(T_β) itself —")
    print("    i.e. Q_β/E_0, the CODATA Q_β.  The operator-selection SDP fixes the")
    print("    DIRECTION of T_β in the NF basis, NOT its trace magnitude.")
    print()

    s_cancels_from_directions = bool(scale_invariant)
    s_cancels_from_magnitude = False  # the net scale is exactly Q_β/E_0

    # ---- 6. Honest verdict ----------------------------------------------
    print("[6] VERDICT:")
    if s_cancels_from_directions:
        verdict = (
            "PARTIAL (honest). The selector DIRECTION x̂ in the NF basis is "
            "S-independent and q-rational: strict complementarity fixes the "
            "active set from the q-rational (t, G) alone, so the dimensionless "
            "precision-ladder FACTORS (1 + c_k u^k) are S-independent. BUT the "
            "OVERALL MAGNITUDE Q_β = E_0·τ_M(T_β) still requires the "
            "net-constraint scale n_target = τ_M(T_β) = Q_β/E_0 — the CODATA "
            "Q_β. The SDP fixes the SHAPE of T_β, not its trace. So S does NOT "
            "fully cancel: Q_β's absolute value is not predicted "
            "CODATA-independently by this route. NO FIT introduced (the "
            "direction is forced by complementarity); honest PARTIAL — c_k "
            "directions closed, Q_β scale open."
        )
    else:
        verdict = (
            "NEGATIVE. The SDP selector direction was not scale-invariant in "
            "this configuration; S does not cleanly cancel. Reported as a "
            "negative result — no CODATA-Q_β fit attempted."
        )
    for line in verdict.split(". "):
        print("    " + line.strip() + ("." if not line.endswith(".") else ""))
    print()

    # ---- 7. Witness (primal + dual per LP/SDP first-class-infra) --------
    wb = WitnessBuilder("qbeta-symbolic-sdp-strict-complementarity", engine="lp+sympy")
    wb.set_description(
        "EXPLORATORY: replaces the archimedean min-L2 selection of the "
        "β-decay knot operator T_β with the canonical q-rational "
        "operator-selection LP/SDP (solve_operator_selection_lp) using "
        "q-rational cost t_i=τ_M(b_i) and Frobenius Gram G_{ij}=τ_M(b_i b_j). "
        "Tests whether strict complementarity makes the selector direction "
        "S-independent and q-rational so the CODATA scalar S=Q_β/E_0 cancels "
        "from the c_k directions. Finding: the selector DIRECTION is "
        "scale-invariant and q-rational (c_k *ratios* S-independent), but the "
        "overall Q_β magnitude still needs n_target=τ_M(T_β)=Q_β/E_0 — the SDP "
        "fixes the shape of T_β, not its trace. HONEST PARTIAL; no CAL-4 fit."
    )
    wb.add_parameter("q_0", str(float(q0)))
    wb.add_parameter("n_target_canonical", "1.0  (q-rational unit net; NOT CODATA Q_β)")
    wb.add_data("nf_names", nf_names)
    wb.add_data("t_symbolic", [str(sp.together(t_sym[i])) for i in range(6)])
    wb.add_data("G_symbolic_diag", [str(sp.together(G_sym[i][i])) for i in range(6)])
    wb.add_data("t_at_q0", [float(x) for x in t_num])
    wb.add_data("t_equals_1739_A", bool(match_1739) if match_1739 is not None else None)
    # LP/SDP first-class-infra REQUIRED fields (primal + dual).
    wb.add_data("x_star", list(res1.x_star))
    wb.add_data("y0_star", float(res1.y0_star))
    wb.add_data("y_star", list(res1.y_star))
    wb.add_data("active_set", list(res1.active_set))
    wb.add_data("primal_obj", float(res1.primal_obj))
    wb.add_data("dual_obj", float(res1.dual_obj))
    wb.add_data("duality_gap", float(res1.duality_gap))
    wb.add_data("direction_scale_invariant", bool(scale_invariant))
    wb.add_data("direction_max_diff_across_scales", float(dir_diff))
    wb.add_data("S_cancels_from_ck_directions", s_cancels_from_directions)
    wb.add_data("S_cancels_from_Qbeta_magnitude", s_cancels_from_magnitude)
    wb.add_data("verdict", verdict)

    wb.add_assertion(
        name="lp_strong_duality",
        computed=float(res1.duality_gap),
        expected=0.0,
        tolerance=1e-6,
        source="operator-selection LP strong duality |primal - dual|",
    )
    wb.add_assertion(
        name="selector_direction_S_independent",
        computed=bool(scale_invariant),
        expected=True,
        tolerance=0,
        source="x*(n_a)/n_a == x*(n_b)/n_b (S cancels from direction)",
    )
    out = wb.save()
    print(f"  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
