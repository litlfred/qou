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
z_sym = q**3 / (q**2 + 1)


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
    import mpmath as mp
    from _precision import set_compute_dps, fmt
    set_compute_dps()
    # Q_MP is the exact 50-digit mpf. It used to be downcast with `float()`
    # here, which threw away the substrate precision before any arithmetic and
    # put four raw float64 fields into the witness (bean qou-pdfx).
    q0 = Q_MP
    f = sp.lambdify(q, tr_M_simplified, modules=["mpmath"])
    val_at_q0 = f(q0)
    print(f"\n  Numerical at q_0 = {mp.nstr(q0, 12)}:")
    print(f"    tr_M(σ_1^7 σ_2^4)(q_0) = {mp.nstr(val_at_q0, 12)}")

    # HISTORICAL reference values, printed for orientation only — both
    # predate the convention-D migration and neither is asserted against.
    # See the cross-check block below for why (bean qou-pdfx).
    print(f"\n  Historical reference values (convention C, NOT asserted):")
    print(f"    char_fast Markov tr at q_0 ≈ 1.6334")
    print(f"    PR #546 Plancherel tr at q_0 ≈ 0.4331")

    # Anti-self-reciprocity check
    tr_M_at_inv_q = sp.cancel(tr_M_simplified.subs(q, 1 / q))
    f_inv = sp.lambdify(q, tr_M_at_inv_q, modules=["mpmath"])
    val_at_inv_q = f_inv(q0)
    print(f"\n  At 1/q_0:")
    print(f"    tr_M(1/q_0) = {mp.nstr(val_at_inv_q, 12)}")
    print(f"    ratio tr_M(1/q)/tr_M(q) = "
          f"{mp.nstr(val_at_inv_q / val_at_q0, 8)}")

    # Try to identify polynomial structure
    print(f"\n  Numerator polynomial structure (after simplification):")
    num, den = sp.fraction(sp.cancel(tr_M_simplified))
    print(f"    numerator   = {num}")
    print(f"    denominator = {den}")

    # Categorical mass anchor
    # WAS: `mp_me = 938.272 / 0.51099895`, a float64 division of two
    # TRUNCATED literals, then `mp.mpf(str(mp_me))` and `fmt(rho_p)` at 60
    # digits. Three defects in one line: `938.272` is short of the registry's
    # 938.27208943 and `0.51099895` short of 0.51099895069, so the ratio was
    # 1836.1525009 against the registry's 1836.1526734 — WRONG AT THE 7th
    # SIGNIFICANT DIGIT (94 ppb) — and the serializer then published ~45
    # manufactured digits on top of a float64 value. Read the registry and
    # carry mpf.
    from codata_constants import M_E_MEV, M_P_MEV_VALIDATION
    mp_me = mp.mpf(M_P_MEV_VALIDATION) / mp.mpf(M_E_MEV)
    rho_p = mp_me / val_at_q0
    print(f"\n  Categorical mass dimensional bridge:")
    print(f"    m_p / m_e (CODATA) = {mp_me:.6f}")
    print(f"    ρ_p^CODATA = (m_p/m_e) / |tr_M(σ_1^7σ_2^4)| = "
          f"{mp.nstr(rho_p, 10)}")

    # NO char_fast cross-check (bean qou-pdfx). This block compared the
    # computed value against a literal `char_fast_ref = 1.6334` and failed at
    # ratio 1.1536, which is what the bean recorded as a "15.4% divergence".
    #
    # 1.6334 is a hardcoded CONVENTION-C decimal. There is no `char_fast`
    # function anywhere in the live tree to call — the only implementations
    # are in `fsh-guts/deprecated/computations/` — so this was never a cross-check
    # against code, only against a transcribed number from a retired path.
    # Convention C was excised 2026-08-09 (owner ruling R1, 2026-08-15 makes
    # D canonical), and under D this word gives 1.8843…, which is what the
    # recursive reducer and `prop:markov-trace-recursive-reducer` both
    # publish. Three live paths agree; the frozen decimal was the outlier.
    #
    # `markov_trace_recursive.py` reached the same conclusion about the same
    # constant and states it best: "Checking a migrated value against a frozen
    # pre-migration decimal is worse than not checking it, because the
    # disagreement it reports is really agreement with the wrong thing."
    #
    # So the assertion is REMOVED rather than re-tuned, and its absence is
    # recorded in the witness. No independent convention-D reference for this
    # word exists yet; when one does, assert against it here.
    ratio_to_charfast = val_at_q0 / mp.mpf("1.6334")   # reported, never asserted
    print(f"\n  Ratio to the historical convention-C decimal = "
          f"{mp.nstr(ratio_to_charfast, 8)}  (reported, NOT a check — see comment)")

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
        "tr_M_proton_at_q0": fmt(val_at_q0),
        "tr_M_proton_at_inv_q0": fmt(val_at_inv_q),
        "ratio_at_inv_q": fmt(val_at_inv_q / val_at_q0),
        "rho_p_codata": fmt(rho_p),
        "cross_check": ("none — the only available reference was a frozen "
                        "convention-C decimal (1.6334); see bean qou-pdfx"),
        "ratio_to_historical_convention_c_decimal": f"{ratio_to_charfast:.6f}",
    }
    # A LIVE structural check replacing the retired convention-C comparison
    # (bean qou-pdfx). Under convention C this trace carried half-integer
    # powers of q — the stale 2026-07-05 witness still records
    # `2*q**(41/2) + …` — and under D it is a Laurent polynomial in q with
    # integer exponents only. That is the property the migration turns on, it
    # is checkable here with no external reference, and it fails loudly if
    # anything reintroduces a √q atom.
    half_powers = [
        a for a in sp.cancel(tr_M_simplified).atoms(sp.Pow)
        if a.exp.is_Rational and not a.exp.is_Integer and a.base == q
    ]
    out = (WitnessBuilder.wrap_legacy(
        "markov-trace-atomic-proton-full", witness,
        script_path=__file__, engine="sympy")
        .add_assertion(
            "convention_d_form_has_no_half_integer_q_powers",
            computed=str(len(half_powers)),
            expected="0",
            source=("convention D (owner ruling R1, 2026-08-15); the "
                    "superseded convention-C form carried q**(41/2) etc."),
        )
        .save())
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
