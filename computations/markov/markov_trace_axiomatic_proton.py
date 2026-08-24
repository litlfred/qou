#!/usr/bin/env python3
"""
CLASS-A acknowledged-anchor banner (per Workplan-0b, applies to
hardcoded CODATA-precision literals in this file as well — see
`docs/audits/2026-05-18-workplan-0b-m-n-substrate-derivation.md`).
The numeric mass / Q-value constants used here are validation-chain
anchors pending substrate derivation; until that lands, treat them
as CAL-3-ish acknowledged inputs, NOT independent calibrations.
The compute-integration-watcher I9 audit therefore classifies this
script as `ok_acknowledged_anchor` rather than as a registry-bypass
violation.

Compute the symbolic Markov trace of the proton atomic braid word via
direct Markov-axiom + Hecke-quadratic-relation reduction in ℚ(q).

This bypasses PR #546's IndexError on σ_2 in `q_character_on_braid_word`.

**Convention D** throughout: `z = q³/(q²+1)` (owner ruling 2026-08-15).
The module docstring said `z = 1/(q^{1/2}+q^{-1/2})` — convention C — until
2026-08-23, while the code had carried D since at least 2026-07-05: a label
outliving the value it described.
The Markov trace is determined ENTIRELY by:

  Hecke quadratic:   σ_i² = h σ_i + 1            (h = q − q⁻¹)
  Braid relation:    σ_1 σ_2 σ_1 = σ_2 σ_1 σ_2
  Far commutation:   σ_i σ_j = σ_j σ_i  for |i−j| ≥ 2
  Markov axiom 1:    tr_M(1) = 1
  Markov axiom 2:    tr_M(α · σ_n) = z · tr_M(α)  for α ∈ H_{n−1} ⊂ H_n
                     with z = q³/(q²+1)  (convention D)
  Cyclic:            tr_M(α β) = tr_M(β α)

Strategy: reduce the proton word to a ℚ(q)-linear combination of basis
elements 1, σ_1, σ_2, σ_1σ_2, σ_2σ_1, σ_1σ_2σ_1 via Hecke-quadratic,
then apply axiom-determined values to each basis element.

Output: markov-trace-axiomatic-proton.witness.json
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 4, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))

from _precision import fmt, set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from qou_substrate.constants import MASS_RATIO_P_E  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

q = sp.symbols("q", positive=True)
h = q - 1 / q
z = q**3 / (q**2 + 1)


# Direct Markov-trace values on H_3 basis (derived from axioms):
#   tr_M(1)            = 1
#   tr_M(σ_i)           = z
#   tr_M(σ_1σ_2)        = z²        (Markov axiom on α = σ_1 ∈ H_2)
#   tr_M(σ_2σ_1)        = z²        (cyclic)
#   tr_M(σ_1σ_2σ_1)     = h·z² + z  (cyclic + Hecke quadratic on σ_1)
#                       = z(1 + hz)
#   tr_M(σ_1²)          = h·z + 1   (Hecke quadratic)
#   tr_M(σ_2²)          = h·z + 1
#   tr_M(σ_1²σ_2)       = ?         (compute via reduction)
#                       Use σ_1² = h σ_1 + 1:
#                       tr_M(σ_1²σ_2) = h·tr_M(σ_1σ_2) + tr_M(σ_2)
#                                     = h·z² + z

# Symbolic Markov-trace values for any reduced word in S_3
TR_M_BASIS = {
    (): sp.Integer(1),                  # identity
    (1,): z,                             # σ_1
    (2,): z,                             # σ_2
    (1, 2): z ** 2,                      # σ_1 σ_2
    (2, 1): z ** 2,                      # σ_2 σ_1
    (1, 2, 1): sp.cancel(h * z ** 2 + z),  # σ_1 σ_2 σ_1 (= σ_2 σ_1 σ_2 = w_0)
}


def markov_axioms_table() -> dict:
    """Return the symbolic Markov-trace values as displayed."""
    return {str(w): str(sp.cancel(v)) for w, v in TR_M_BASIS.items()}


def hecke_power_coeffs(k: int):
    """`σ^k = a_k σ + b_k` from the Hecke quadratic `σ² = hσ + 1`.

    The recurrence the content block states: `a_{k+1} = h a_k + b_k`,
    `b_{k+1} = a_k`, `a_0 = 0`, `b_0 = 1`.
    """
    a, b = sp.Integer(0), sp.Integer(1)
    for _ in range(k):
        a, b = sp.expand(h * a + b), a
    return a, b


def tr_M_sigma1_pow_sigma2_pow(k1: int, k2: int):
    """`tr_M(σ_1^{k1} σ_2^{k2})`, the block's closed form.

    Expanding each power by `hecke_power_coeffs` and applying the
    axiom-determined basis values gives
    `a_1 a_2 z² + (a_1 b_2 + b_1 a_2) z + b_1 b_2`.
    """
    a1, b1 = hecke_power_coeffs(k1)
    a2, b2 = hecke_power_coeffs(k2)
    return sp.cancel(sp.together(a1 * a2 * z ** 2 + (a1 * b2 + b1 * a2) * z + b1 * b2))


def main() -> int:
    set_compute_dps()

    print("=" * 96)
    print("  Symbolic Markov trace via direct Markov-axiom reduction in Q(q)")
    print("  Convention D: z = q^3/(q^2+1)")
    print("=" * 96)

    print("\n  Markov-axiom-determined trace values on the H_3 basis:")
    for w, v in TR_M_BASIS.items():
        w_str = "*".join(f"s_{i}" for i in w) if w else "1"
        print(f"    tr_M({w_str:<14}) = {sp.cancel(v)}")

    # ── the word the CONTENT BLOCK states: sigma_1^7 sigma_2^4 ───────────
    K1, K2 = 7, 4
    tr_block = tr_M_sigma1_pow_sigma2_pow(K1, K2)
    num, den = sp.fraction(tr_block)
    den_factored = sp.factor(den)
    print(f"\n  Block word s_1^{K1} s_2^{K2}:")
    print(f"    denominator = {den_factored}")

    q0 = mp.mpf(Q_50_DIGIT_STR)
    f_block = sp.lambdify(q, tr_block, modules="mpmath")
    tr_block_at_q0 = f_block(q0)
    print(f"    tr_M(q_0)   = {mp.nstr(tr_block_at_q0, 15)}")

    # rho_p, the categorical-mass anchor the block quotes
    rho_p = MASS_RATIO_P_E / abs(tr_block_at_q0)
    print(f"    rho_p       = (m_p/m_e)/|tr_M| = {mp.nstr(rho_p, 10)}")

    # ── the longest element, kept as the demo word it always was ─────────
    tr_w0 = sp.cancel(TR_M_BASIS[(1, 2, 1)])
    f_w0 = sp.lambdify(q, tr_w0, modules="mpmath")
    tr_w0_at_q0 = f_w0(q0)
    tr_w0_at_inv = f_w0(1 / q0)
    print(f"\n  Longest element s_1 s_2 s_1 (= w_0):")
    print(f"    tr_M(q_0)   = {mp.nstr(tr_w0_at_q0, 15)}")
    print(f"    tr_M(1/q_0) = {mp.nstr(tr_w0_at_inv, 15)}")
    print(f"    ratio       = {mp.nstr(tr_w0_at_inv / tr_w0_at_q0, 12)}"
          "   (neither +1 nor -1: see the bar-behaviour note below)")

    witness = {
        "computation": "markov-trace-axiomatic-proton",
        "description": (
            "Symbolic Markov trace by direct Markov-axiom reduction in Q(q), "
            "convention D (z = q^3/(q^2+1)). Reports the content block's word "
            "sigma_1^7 sigma_2^4 -- its closed form, exact denominator, value "
            "at q_0 and the rho_p anchor -- plus the H_3 longest element "
            "sigma_1 sigma_2 sigma_1 as a demo. Pure Markov axioms + Hecke "
            "quadratic + cyclicity, no representation theory."
        ),
        "reference_blocks": [
            "prop:markov-trace-axiomatic-closed-form",
            "prop:categorical-mass-markov",
            "prop:atomic-mass-gb-nf",
            "prop:markov-trace-antipode-polynomial-symmetry",
        ],
        "convention": "D",
        "z_symbolic": str(sp.cancel(z)),
        "h_3_markov_basis_table": markov_axioms_table(),
        "block_word": f"sigma_1^{K1} sigma_2^{K2}",
        "tr_M_block_word_symbolic": str(tr_block),
        "tr_M_block_word_denominator": str(den_factored),
        "tr_M_block_word_at_q0": fmt(tr_block_at_q0),
        "rho_p_from_block_word": fmt(rho_p),
        "demo_word": "sigma_1 sigma_2 sigma_1",
        "tr_M_demo_at_q0": fmt(tr_w0_at_q0),
        "tr_M_demo_at_inv_q0": fmt(tr_w0_at_inv),
        "bar_behaviour_note": (
            "Under q -> 1/q the H_3 longest-element trace is NEITHER symmetric "
            "NOR anti-symmetric, in convention C or D. This witness asserted "
            "both `anti_self_reciprocal` and `symmetric_under_q_inv` with "
            "expected=1.0 until 2026-08-23. That pair is unsatisfiable by "
            "construction -- f(1/q)=f(q) together with f(1/q)=-f(q) forces "
            "f == 0 -- so the witness could never go green, and both cited "
            "sections of prop:markov-trace-axiomatic-closed-form that do not "
            "exist in that block. The ratio is reported here as data instead."
        ),
        "q0Anchor": "proton",
        "q0Value": str(q0),
    }

    out = (WitnessBuilder.wrap_legacy(
        "markov-trace-axiomatic-proton", witness,
        script_path=__file__, engine="sympy+mpmath")
        .add_assertion(
            "block_word_denominator_is_convention_D",
            computed="1" if den_factored == sp.factor(q**7 * (q**2 + 1)**2) else "0",
            expected="1",
            tolerance="0",
            source=("prop:markov-trace-axiomatic-closed-form: the denominator "
                    "factors as q^7(q^2+1)^2, one (q^2+1) per Markov peel -- "
                    "the convention-D signature, which C cannot produce"),
        )
        .add_assertion(
            "block_word_tr_M_at_q0",
            computed=fmt(tr_block_at_q0),
            expected="1.88432",
            tolerance="1e-5",
            source="prop:markov-trace-axiomatic-closed-form: numerical evaluation at q_0",
        )
        .add_assertion(
            "block_word_rho_p",
            computed=fmt(rho_p),
            expected="974.44",
            tolerance="1e-2",
            source="prop:markov-trace-axiomatic-closed-form: the categorical-mass anchor",
        )
        .save())
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
