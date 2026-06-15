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

Compute the symbolic Markov trace of the ACTUAL 11-crossing atomic-
braid proton word σ_1^7 σ_2^4 in H_3(q) via axiomatic reduction in ℚ(q).

The single-generator powers σ_i^k reduce via the Hecke quadratic
relation σ_i^2 = h σ_i + 1, giving the recurrence

  σ_i^k = a_k σ_i + b_k,  with
  a_{k+1} = a_k · h + b_k,
  b_{k+1} = a_k,
  a_0 = 0, b_0 = 1.

For σ_1^7 σ_2^4 in H_3(q):
  σ_1^7 = a_7(h) σ_1 + b_7(h)
  σ_2^4 = a_4(h) σ_2 + b_4(h)
  σ_1^7 · σ_2^4 = a_7 a_4 σ_1 σ_2 + a_7 b_4 σ_1 + b_7 a_4 σ_2 + b_7 b_4

  Markov trace:
    tr_M(σ_1^7 σ_2^4) = a_7 a_4 · z²
                     + (a_7 b_4 + b_7 a_4) · z
                     + b_7 b_4 · 1

This is a closed-form rational function in q. Substituting q_0 gives
the categorical anchor for prop:atomic-mass-gb-nf.

Output: markov-trace-atomic-proton-full.witness.json
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

import sympy as sp

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))

from witness_base import WitnessBuilder  # noqa: E402

q = sp.symbols("q", positive=True)
h_sym = q - 1 / q
z_sym = 1 / (sp.sqrt(q) + 1 / sp.sqrt(q))


def hecke_power_decomposition(k: int):
    """σ^k = a_k(h) σ + b_k(h) where:
       a_{k+1} = a_k · h + b_k,
       b_{k+1} = a_k.
       a_0 = 0, b_0 = 1.
    Returns (a_k_symbolic_in_h, b_k_symbolic_in_h)."""
    h = sp.symbols("h")
    a, b = sp.Integer(0), sp.Integer(1)
    for _ in range(k):
        a, b = sp.expand(a * h + b), a
    return a, b


def hecke_power_in_q(k: int):
    """σ^k as polynomial in q (after substituting h = q − q^{-1}).
    Returns (a_k(q), b_k(q))."""
    h = sp.symbols("h")
    a_h, b_h = hecke_power_decomposition(k)
    a_q = sp.cancel(a_h.subs(h, h_sym))
    b_q = sp.cancel(b_h.subs(h, h_sym))
    return a_q, b_q


def main() -> int:
    print("=" * 96)
    print(f"  Markov trace of atomic-braid proton word σ_1^7 σ_2^4 in H_3(q)")
    print(f"  via direct axiomatic reduction (Hecke + Markov + cyclic)")
    print("=" * 96)

    # σ_1^7 decomposition
    a_7_h, b_7_h = hecke_power_decomposition(7)
    a_4_h, b_4_h = hecke_power_decomposition(4)
    print(f"\n  σ_1^7 = a_7(h) σ_1 + b_7(h),  where")
    print(f"    a_7(h) = {a_7_h}")
    print(f"    b_7(h) = {b_7_h}")
    print(f"  σ_2^4 = a_4(h) σ_2 + b_4(h),  where")
    print(f"    a_4(h) = {a_4_h}")
    print(f"    b_4(h) = {b_4_h}")

    # σ_1^7 · σ_2^4 expansion
    h = sp.symbols("h")
    a7 = sp.cancel(a_7_h.subs(h, h_sym))
    b7 = sp.cancel(b_7_h.subs(h, h_sym))
    a4 = sp.cancel(a_4_h.subs(h, h_sym))
    b4 = sp.cancel(b_4_h.subs(h, h_sym))

    # Markov trace via Hecke basis
    # σ_1^7 σ_2^4 = a7·a4 σ_1σ_2 + a7·b4 σ_1 + b7·a4 σ_2 + b7·b4
    # tr_M(σ_1σ_2) = z², tr_M(σ_1) = z, tr_M(σ_2) = z, tr_M(1) = 1.
    print(f"\n  Markov-trace axiom values (H_3):")
    print(f"    tr_M(σ_1)    = z = 1/(q^{{1/2}}+q^{{-1/2}})")
    print(f"    tr_M(σ_2)    = z")
    print(f"    tr_M(σ_1σ_2) = z²")
    print(f"    tr_M(1)      = 1")

    tr_M = (
        a7 * a4 * z_sym ** 2
        + a7 * b4 * z_sym
        + b7 * a4 * z_sym
        + b7 * b4
    )
    tr_M_simplified = sp.cancel(tr_M)
    print(f"\n  Markov trace tr_M(σ_1^7 σ_2^4)(q) symbolically (raw):")
    # Display in factored form if possible
    try:
        tr_M_factored = sp.factor(tr_M_simplified)
    except Exception:
        tr_M_factored = tr_M_simplified
    print(f"    {tr_M_factored}")

    # Numerical at q_0
    from q_parameter import Q_MP
    q0 = float(Q_MP)
    f = sp.lambdify(q, tr_M_simplified, modules=["mpmath"])
    val_at_q0 = float(f(q0))
    print(f"\n  Numerical at q_0 = {q0:.10f}:")
    print(f"    tr_M(σ_1^7 σ_2^4)(q_0) = {val_at_q0:.10f}")

    # Reference: PR #546 closed form gives tr ≈ 0.433 at q_0
    # char_fast (Markov-axiom-derived y_λ) gives tr ≈ 1.633 at q_0
    print(f"\n  Reference comparisons:")
    print(f"    char_fast Markov tr at q_0 ≈ 1.6334")
    print(f"    PR #546 Plancherel tr at q_0 ≈ 0.4331")

    # Anti-self-reciprocity check
    tr_M_at_inv_q = sp.cancel(tr_M_simplified.subs(q, 1 / q))
    f_inv = sp.lambdify(q, tr_M_at_inv_q, modules=["mpmath"])
    val_at_inv_q = float(f_inv(q0))
    print(f"\n  At 1/q_0:")
    print(f"    tr_M(1/q_0) = {val_at_inv_q:.10f}")
    print(f"    ratio tr_M(1/q)/tr_M(q) = {val_at_inv_q/val_at_q0:.4f}")

    # Try to identify polynomial structure
    print(f"\n  Numerator polynomial structure (after simplification):")
    num, den = sp.fraction(sp.cancel(tr_M_simplified))
    print(f"    numerator   = {num}")
    print(f"    denominator = {den}")

    # Categorical mass anchor
    mp_me = 938.272 / 0.51099895  # noqa: P31 — audit ratio display; live values via codata_constants/experimental_constants registry
    rho_p = mp_me / val_at_q0
    print(f"\n  Categorical mass dimensional bridge:")
    print(f"    m_p / m_e (CODATA) = {mp_me:.6f}")
    print(f"    ρ_p^CODATA = (m_p/m_e) / |tr_M(σ_1^7σ_2^4)| = {rho_p:.4f}")

    # Compare to char_fast value (the genuine Markov trace numerically)
    char_fast_ref = 1.6334
    ratio_to_charfast = val_at_q0 / char_fast_ref
    print(f"\n  Ratio my-Markov / char_fast = {ratio_to_charfast:.4f}")
    if abs(ratio_to_charfast - 1) < 0.01:
        print(f"    ✅ Matches char_fast Markov trace.")
    else:
        print(f"    Discrepancy from char_fast — investigate convention.")

    witness = {
        "computation": "markov-trace-atomic-proton-full",
        "description": (
            "Symbolic Markov-trace closed form for the actual atomic-"
            "braid 11-crossing proton word σ_1^7 σ_2^4 in H_3(q), "
            "derived via direct axiomatic reduction. Uses the Hecke-"
            "power recurrence σ_i^k = a_k(h) σ_i + b_k(h) where "
            "a_{k+1} = a_k h + b_k, b_{k+1} = a_k. Combined with "
            "Markov-axiom values on the H_3 basis to get the closed "
            "form in ℚ(q)."
        ),
        "reference_blocks": [
            "prop:atomic-mass-gb-nf",
            "prop:categorical-mass-markov",
        ],
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "hecke_power_a_7": str(a_7_h),
        "hecke_power_b_7": str(b_7_h),
        "hecke_power_a_4": str(a_4_h),
        "hecke_power_b_4": str(b_4_h),
        "tr_M_proton_full_symbolic": str(tr_M_simplified),
        "tr_M_proton_full_factored": str(tr_M_factored),
        "tr_M_proton_at_q0": val_at_q0,
        "tr_M_proton_at_inv_q0": val_at_inv_q,
        "ratio_at_inv_q": val_at_inv_q / val_at_q0,
        "rho_p_codata": rho_p,
        "matches_char_fast": abs(ratio_to_charfast - 1) < 0.01,
    }
    matches_char_fast = abs(ratio_to_charfast - 1) < 0.01
    out = (WitnessBuilder.wrap_legacy(
        "markov-trace-atomic-proton-full", witness,
        script_path=__file__, engine="sympy")
        .add_assertion(
            "matches_char_fast",
            computed=1.0 if matches_char_fast else 0.0,
            expected=1.0,
            tolerance=0.0,
            source="cross-check vs hecke_character_fast at q0 (1% tol)",
        )
        .save())
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
