#!/usr/bin/env python3
"""qbeta_stage_c_per_block_chi_closed_form_probe.py — Stage C
DECISIVE: per-block χ^λ for the electron-knot trefoil are CLEAN
q-monomials, recovered symbolically with no float64 anywhere.

**Two structural findings closed in this probe:**

1. PR #1851 "validated" χ values were tr(σ_1), not tr(trefoil). The
   0-indexed word `[(1,0),(1,1),(1,0)]` caused chi_lambda_braid's
   `idx = gen-1 = -1` to silently skip out-of-range generators,
   leaving only the middle σ_1 contribution. The Hoefsmit/Stage B
   q-stability is still valid but for σ_1, not the trefoil.

2. With the correct 1-indexed word `σ_1·σ_2·σ_1 = [(1,1),(1,2),(1,1)]`,
   the per-block χ^λ are EXACT symbolic q-monomials:

       χ^(3)(q)     = q^3
       χ^(2,1)(q)   = 0   (the (2,1) block contributes ZERO)
       χ^(1,1,1)(q) = -q^(-3)

   These are derived symbolically via the Hoefsmit construction in
   mpmath/sympy (no float64), matching the pyhecke 1-indexed output
   exactly. The (2,1) = 0 is structural: σ_1·σ_2·σ_1 in the standard
   2×2 rep has trace q²·a + a'/q² = -q/(q²+1) + q/(q²+1) = 0 by
   exact algebraic cancellation.

**Stage C consequence:** the trefoil's contribution to the operator-
level ladder lives entirely in the (3,) and (1,1,1) blocks; the
(2,1) block is silent at this word. The Markov-trace aggregate is

    tr_M(trefoil) = y_(3)(q)·q^3 + y_(1,1,1)(q)·(-q^(-3))

(with y_(2,1)·0 = 0). With the standard bar-symmetric Wenzl weights
y_(1,1,1)(q) = y_(3)(q^(-1)), this is the structural form that
specializes to the Jones polynomial.

For c_k extraction: each per-block χ^λ(q) substituted with the
substrate ladder variable u = b(q)·ℏ_q² and Taylor-expanded around
q_0 gives the per-block operator-level N=k structure. The (2,1)
block contributes 0 to every c_k from THIS word — a clean
operational anchor.

**Precision note** (per Copilot review on PR #1873): the symbolic
derivation here uses exact sympy rationals end-to-end (no float64
in the algebra). The validation step against `pyhecke` necessarily
goes through `chi_lambda_braid(q_value=float(Q0))` — the existing
Python fallback API takes Python floats — so the validation
comparison itself is at ~16 dps (float64 ceiling on the pyhecke
side). The closed-form (q³, 0, −q⁻³) themselves are EXACT
q-monomials, anchored by the float64-level validation at q₀.
"""
from __future__ import annotations


import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import time
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "hecke"))

import os  # noqa: E402
os.environ.setdefault("QOU_COMPUTE_DPS", "65")
os.environ.setdefault("QOU_OUTPUT_DPS", "50")

from _precision import set_compute_dps  # noqa: E402
set_compute_dps(65)
import mpmath as mp  # noqa: E402
mp.mp.dps = 50
import sympy as sp  # noqa: E402

from hecke_characters import chi_lambda_braid  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402


def main() -> int:
    Q0_STR = "1.1099785827513808075916690956107688798744991218736"
    Q0 = mp.mpf(Q0_STR)

    t0 = time.monotonic()
    builder = WitnessBuilder(
        "qbeta-stage-c-per-block-chi-closed-form-probe",
        engine="python+sympy+mpmath",
        start_time=t0,
    )
    builder.set_description(
        "Stage C closed form: per-block χ^λ(σ_1σ_2σ_1) at n=3 derived "
        "symbolically via the Hoefsmit construction. Yields exact "
        "q-monomial closed forms (q^3, 0, -q^(-3)) for (3), (2,1), "
        "(1,1,1) respectively. No float64. The (2,1) = 0 is structural "
        "(exact cancellation in the 2×2 rep trace). Closes the per-block "
        "χ^λ extraction for the operator-level N=k probe."
    )
    builder.set_content_block("prop:q-beta-c-k-recursion-from-habiro-q-difference")

    print("=" * 78)
    print(" Stage C — per-block χ^λ(trefoil) closed forms (symbolic, no float64)")
    print("=" * 78)
    print()

    # Symbolic Hoefsmit construction for n=3, partition (2,1).
    q = sp.Symbol("q", positive=True)
    h = q - 1 / q

    # Standard Young Tableaux of (2,1):
    # T1: (1,2 in row 1; 3 in row 2); contents = {1:0, 2:1, 3:-1}
    # T2: (1,3 in row 1; 2 in row 2); contents = {1:0, 2:-1, 3:1}
    #
    # σ_1 swaps entries 1,2:
    #   On T1: ρ = c(2)-c(1) = 1-0 = +1 ⇒ same-row block, eigenval q
    #   On T2: ρ = -1-0 = -1 ⇒ same-col block, eigenval -1/q
    # σ_1 is diagonal: diag(q, -1/q) in (T1, T2) basis.
    #
    # σ_2 swaps entries 2,3:
    #   On T1: ρ = c(3)-c(2) = -1-1 = -2 ⇒ 2x2 block, a = h/(1-q^(-2·(-2))) = h/(1-q^4)
    #   On T2: ρ = 1-(-1) = +2 ⇒ a' = h/(1-q^(-4))
    # σ_2 = [[a, b], [b, a']] with b² = a·a' + 1.
    a_top = h / (1 - q ** 4)           # T1 diagonal (ρ=-2)
    a_bot = h / (1 - q ** (-4))        # T2 diagonal (ρ=+2)
    # Trefoil = σ_1·σ_2·σ_1. σ_1 is diagonal in this rep, so the
    # trace of σ_1·σ_2·σ_1 depends ONLY on the diagonal of σ_2 (the
    # off-diagonal b drops out in the trace), giving an exact
    # algebraic expression with no sqrt branch ambiguity (per Copilot
    # review on PR #1873).
    chi_21_sym = sp.cancel(q ** 2 * a_top + a_bot / q ** 2)
    # For completeness, also build the full 2×2 σ_2 (b kept for
    # downstream non-trace uses); not used in the trace below.
    bsq = sp.simplify(a_top * a_bot + 1)
    sigma2_21 = sp.Matrix([[a_top, sp.sqrt(bsq)],
                            [sp.sqrt(bsq), a_bot]])  # noqa: F841

    # Closed forms for (3,) and (1,1,1) are immediate from 1-dim reps
    chi_3_sym = q ** 3                # (3,): σ_i = q ⇒ σ_1σ_2σ_1 = q^3
    chi_111_sym = -1 / q ** 3         # (1,1,1): σ_i = -1/q

    # Simplify (2,1) symbolic trace
    chi_21_simplified = sp.simplify(chi_21_sym)

    print(f"  Symbolic per-block χ^λ(σ_1·σ_2·σ_1):")
    print(f"    χ^(3)(q)     = {chi_3_sym}")
    print(f"    χ^(2,1)(q)   = {chi_21_simplified}")
    print(f"    χ^(1,1,1)(q) = {chi_111_sym}")
    print()

    # Validate against pyhecke (1-indexed word) at q_0
    word_1indexed = [(1, 1), (1, 2), (1, 1)]
    print(f"  Validation at q_0 vs pyhecke (1-indexed word):")
    print(f"  {'λ':<10} {'symbolic':>18} {'pyhecke':>18} {'match':>10}")
    print(f"  {'-'*10} {'-'*18} {'-'*18} {'-'*10}")

    per_block = []
    q0_sp = sp.Float(Q0_STR, 50)
    all_match = True
    for label, chi_sym in [
        ((3,),       chi_3_sym),
        ((2, 1),     chi_21_simplified),
        ((1, 1, 1),  chi_111_sym),
    ]:
        v_sym_mp = mp.mpf(str(sp.N(chi_sym.subs(q, q0_sp), 50)))
        v_pyh = mp.mpf(str(chi_lambda_braid(label, word_1indexed,
                                            q_value=float(Q0))))
        diff = mp.fabs(v_sym_mp - v_pyh)
        ok = diff < mp.mpf("1e-12")
        all_match = all_match and ok
        print(f"  {str(label):<10} {float(v_sym_mp):>+18.12f} "
              f"{float(v_pyh):>+18.12f} "
              f"{'✓' if ok else '✗':>10}")
        per_block.append({
            "lambda": list(label),
            "chi_symbolic_q": str(chi_sym),
            "chi_at_q_0_symbolic": mp.nstr(v_sym_mp, 25),
            "chi_at_q_0_pyhecke": mp.nstr(v_pyh, 25),
            "match_at_q_0": ok,
        })
    print()

    print("=" * 78)
    print(" Structural reading: trefoil χ^(2,1) = 0 (exact)")
    print("=" * 78)
    print()
    print(f"  The (2,1) block contributes ZERO to χ(trefoil) for the")
    print(f"  word σ_1·σ_2·σ_1. By symbolic algebra:")
    print(f"    χ^(2,1) = q²·a + a'/q² where a = h/(1-q^4), a' = h/(1-q^-4)")
    print(f"    Substitute a = -1/(q(q²+1)), a' = q^3/(q²+1):")
    print(f"      q²·a   = -q/(q²+1)")
    print(f"      a'/q²  = +q/(q²+1)")
    print(f"      sum    = 0  (exact)")
    print()
    print(f"  Consequence — Markov trace of trefoil decomposes as:")
    print(f"    tr_M(trefoil) = y_(3)(q)·q^3 + y_(1,1,1)(q)·(-q^(-3))")
    print(f"                  + y_(2,1)(q)·0")
    print(f"                  = y_(3)·q^3 - y_(1,1,1)·q^(-3)")
    print()
    print(f"  The c_k structure of the operator-level Q_β ladder from")
    print(f"  the electron knot lives ENTIRELY in the (3,) and (1,1,1)")
    print(f"  blocks. The (2,1) block is silent at this word.")
    print()

    print("=" * 78)
    print(" VERDICT — Stage C")
    print("=" * 78)
    print()
    if all_match:
        print(f"  ✓ Symbolic χ^λ derivation matches pyhecke at q_0 to 12 dps.")
        print(f"    Per-block χ^λ closed forms (q^3, 0, -q^(-3)) are EXACT.")
        print(f"    No float64; pure symbolic q-monomials.")
        print()
        print(f"  Stage C operator-level extraction is now READY for the")
        print(f"  substrate u = b(q)·ℏ_q² substitution + N=k Taylor")
        print(f"  expansion. With clean q-monomial χ^λ, the per-block N=k")
        print(f"  coefficients are direct binomial expansions, no precision")
        print(f"  loss anywhere.")
    else:
        print(f"  ✗ Symbolic χ^λ does NOT match pyhecke — convention bug")
        print(f"    in the Hoefsmit construction or word interpretation.")
    print()

    builder.add_data("word_used", {
        "format": "1-indexed (σ_i where i ≥ 1)",
        "word": [list(w) for w in word_1indexed],
        "math": "σ_1·σ_2·σ_1 = electron knot = trefoil",
        "correction_from_pr_1851": (
            "PR #1851 used 0-indexed input which caused idx=-1 to "
            "silently skip out-of-range; the validated values there "
            "were tr(σ_1), not tr(trefoil)."
        ),
    })
    builder.add_data("per_block_chi_closed_forms", per_block)
    builder.add_data("structural_finding", {
        "chi_2_1_trefoil_is_exactly_zero": True,
        "proof_sketch": ("In Hoefsmit (2,1), σ_1·σ_2·σ_1 trace = "
                         "q²·a + a'/q² with a = -1/(q(q²+1)), "
                         "a' = q^3/(q²+1) ⇒ -q/(q²+1) + q/(q²+1) = 0."),
        "markov_decomposition": ("tr_M(trefoil) = y_(3)·q^3 + "
                                  "y_(1,1,1)·(-q^(-3)); (2,1) silent."),
    })
    builder.add_data("verdict", {
        "stage_c_chi_closed_forms_ready": all_match,
        "next_step": ("Substitute u = b(q)·ℏ_q² and expand each "
                      "per-block χ^λ around q_0 to extract operator-"
                      "level N=k coefficients (a_k_λ). With pure "
                      "q-monomial χ^λ, this is binomial-expansion-easy."),
    })

    builder.add_assertion(
        "stage_c_per_block_chi_symbolic_matches_pyhecke",
        computed=1 if all_match else 0,
        expected=1,
        tolerance=0,
        source=("Stage C correctness gate: the symbolic Hoefsmit "
                "construction (sympy, exact q-rational) must reproduce "
                "the pyhecke 1-indexed χ^λ(σ_1·σ_2·σ_1) values at q_0 "
                "to ≥ 12 dps. PASS confirms the closed forms "
                "(q^3, 0, -q^(-3)) are correct, anchoring the no-float64 "
                "operator-level extraction toward c_4..c_8."),
    )

    builder.save()
    print(f"  Witness: qbeta-stage-c-per-block-chi-closed-form-probe.witness.json")
    return 0 if all_match else 1


if __name__ == "__main__":
    raise SystemExit(main())
