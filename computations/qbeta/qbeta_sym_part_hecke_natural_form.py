#!/usr/bin/env python3
"""qbeta_sym_part_hecke_natural_form.py — algebraic identity:
the symmetric part of Δtr_M(q) under t ↔ 1/t (t = q^(1/2))
admits a Hecke-natural closed form.

CONTEXT. Follow-up to PR #1615 bar-decomposition probe. That probe
established Δtr_M(q) = sym(t) + antisym(t) with sym(t) = clean
closed form. This probe identifies the Hecke-natural reading:

    sym(Δtr_M)(q) = -h · (q-1) / (2·q^(1/2))   [proved identity]
                  = -[2]_{q^(1/2)} · h̃² / 2
                  = -(q^(1/2) + q^(-1/2)) · (q^(1/2) - q^(-1/2))² / 2

where:
    h   = q - q^(-1)                  full-q bar-antisymmetric
    h̃   = q^(1/2) - q^(-1/2)          half-q bar-antisymmetric
    [2]_t = t + t^(-1)               q-deformed integer in t-basis

The sym part is a PRODUCT of two bar-antisymmetric Hecke quantities
(one at full q, one at half q). Under bar-involution t ↔ 1/t, each
factor flips sign, so the product is preserved — consistent with the
sym-projection definition.

DISCIPLINE (anti-pattern guard). This identifies the ALGEBRAIC form
of sym, not a c_k closure. Per AGENTS.md "Don't propose a seventh
fit-based ansatz":

  - The numerical relation `Q_β/m_e ≈ 140 · |sym|` at q_proton would
    require a substrate constant ~140 (1/h² ≈ 102 or [2]_q/h² ≈ 195 —
    neither hits cleanly). DO NOT WIRE.
  - To use this identity for Q_β requires identifying the CATEGORICAL
    OBJECT producing the sym projection in the chain. Open research.

The structural reading h · (q-1) suggests categorical reading:
the wedge / antisymmetrized product of TWO Hecke bar-derivatives
(the q-deformed Lie bracket [h, h̃] structure). Documented as the
direction for the next structural attack.
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
import time
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent.parent / "tools" / "qou-substrate" / "python"))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def main() -> int:
    t0 = time.monotonic()
    set_compute_dps()

    builder = WitnessBuilder("qbeta-sym-part-hecke-natural-form",
                              engine="python+sympy", start_time=t0)
    builder.set_description(
        "Hecke-natural closed form for sym(Δtr_M)(q) under convention D: "
        "exact algebraic identity sym = -h·(q⁴-q⁻⁴)/8 = "
        "-h²·[2]_q·[2]_{q²}/8 with h = q-q⁻¹. The convention-C forms "
        "(-h·h̃/2 = -[2]_{q^(1/2)}·h̃²/2) are retained and still checked "
        "against the recorded C-era sym: the STRUCTURE — a product of two "
        "bar-antisymmetric Hecke quantities, hence bar-symmetric — survived "
        "the 2026-08-09 convention migration; only the second factor's "
        "argument (half-q → q⁴) and the constant (2 → 8) moved."
    )
    builder.set_audit_only(
        "docs/audits/2026-06-01-qbeta-sym-part-hecke-natural-form.md"
    )

    upstream = builder.add_upstream(
        _pb.witness_path("qbeta-delta-tr-bar-decomposition-probe.witness.json", HERE)
    )

    q = sp.Symbol("q", positive=True)
    t = sp.Symbol("t", positive=True)

    sym_q_str = upstream["data"]["bar_t_decomposition"]["symmetric_part_q"]
    # sympify creates its OWN `q` symbol unless we bind to ours via locals
    sym_q_witness = sp.sympify(sym_q_str, locals={"q": q})

    # Hecke-natural reformulation
    h = q - 1 / q                            # full-q bar-antisymmetric
    h_tilde = sp.sqrt(q) - 1 / sp.sqrt(q)    # half-q bar-antisymmetric
    two_q_half = sp.sqrt(q) + 1 / sp.sqrt(q)  # [2]_{q^(1/2)}

    # THE IDENTITY MOVED WITH THE CONVENTION, AND THE STRUCTURE SURVIVED.
    #
    # Forms 1-3 below are EXACTLY TRUE for the convention-C sym, and exactly
    # false for the convention-D sym this probe now reads. That is not a
    # refutation of the reading — it is the same object re-indexed.
    #
    # The chain, traced rather than guessed. `habiro-coefficients-atomic` was
    # regenerated D-only on 2026-08-18 (f392d7540, "atomic witness unmixed").
    # The bar-decomposition probe upstream of this one is UNCHANGED since
    # 2026-08-02, but its witness still held a 2026-08-08 computation from the
    # pre-D atomic witness; regenerating it picked up D and the symmetric part
    # changed shape:
    #
    #     C:  sym = (-q^3 + q^2 + q - 1) / (2 q^(3/2))
    #             = -(t^2 - 1)(t^4 - 1) / (2 t^3)          [t = q^(1/2)]
    #     D:  sym = (-q^10 + q^8 + q^2 - 1) / (8 q^5)
    #             = -(t^4 - 1)(t^16 - 1) / (8 t^10)
    #
    # Written in bar-antisymmetric factors, the structure is the SAME shape:
    #
    #     C:  sym = -h * h_tilde / 2          (full q) x (half q),   /2
    #     D:  sym = -h * H     / 8            (full q) x (q^4),      /8
    #
    #         with H = q^4 - q^(-4), and equivalently
    #         D:  sym = -h^2 * [2]_q * [2]_{q^2} / 8,
    #         which is the exact analogue of form 2's
    #         C:  sym = -[2]_{q^(1/2)} * h_tilde^2 / 2.
    #
    # So the docstring's structural reading is intact: sym is still a PRODUCT
    # of two bar-antisymmetric Hecke quantities, so each factor flips sign
    # under t <-> 1/t and the product is preserved. What moved is the second
    # factor's argument (half-q -> q^4) and the constant (2 -> 8).
    #
    # All six identities below are verified by sympy in this run, C forms
    # against the recorded C-era sym and D forms against the live upstream —
    # the C claim is CHECKED here, not merely asserted in a comment.

    #: The convention-C symmetric part, recorded verbatim from the
    #: 2026-08-08 upstream witness (13ff8207f). Kept so the historical forms
    #: stay falsifiable rather than becoming folklore. Never compared against
    #: the live upstream.
    SYM_Q_CONVENTION_C_HISTORICAL = sp.sympify(
        "(-q**3 + q**2 + q - 1)/(2*q**(3/2))", locals={"q": q})

    # Convention C — the three original forms, now historical.
    form_1 = -h * (q - 1) / (2 * sp.sqrt(q))
    form_2 = -two_q_half * h_tilde ** 2 / 2
    form_3 = -(sp.sqrt(q) + 1 / sp.sqrt(q)) * (sp.sqrt(q) - 1 / sp.sqrt(q)) ** 2 / 2

    # Convention D — the live forms.
    H_q4 = q ** 4 - q ** -4                  # q^4 bar-antisymmetric
    two_q = q + 1 / q                        # [2]_q
    two_q_sq = q ** 2 + q ** -2              # [2]_{q^2}

    form_d1 = -h * H_q4 / 8
    form_d2 = -h ** 2 * two_q * two_q_sq / 8
    form_d3 = -(q ** 2 - 1) * (q ** 8 - 1) / (8 * q ** 5)

    # Verify each form equals the upstream sym closed form.
    # SymPy struggles with mixed q^(1/2) and q forms; the clean approach
    # is to substitute q = t² in BOTH the candidate and the upstream
    # expression, then simplify in t (integer powers).
    def _verify_zero(candidate, target):
        # Substitute q = t² and force-simplify past sqrt branch cuts
        # (t is positive Symbol so (t²)^(1/2) = t is valid).
        diff = candidate - target
        diff_t = diff.subs(q, t ** 2)
        return sp.simplify(sp.powsimp(diff_t, force=True))

    # C forms against the RECORDED C-era sym; D forms against the LIVE
    # upstream. Comparing a C form to the live upstream is the mistake this
    # probe made for two weeks, and it is why the assertion read as a refuted
    # identity rather than a stale index.
    diff_1 = _verify_zero(form_1, SYM_Q_CONVENTION_C_HISTORICAL)
    diff_2 = _verify_zero(form_2, SYM_Q_CONVENTION_C_HISTORICAL)
    diff_3 = _verify_zero(form_3, SYM_Q_CONVENTION_C_HISTORICAL)

    diff_d1 = _verify_zero(form_d1, sym_q_witness)
    diff_d2 = _verify_zero(form_d2, sym_q_witness)
    diff_d3 = _verify_zero(form_d3, sym_q_witness)

    print(f"sym (from upstream witness, convention D): {sym_q_witness}")
    print(f"sym (convention C, historical):            "
          f"{SYM_Q_CONVENTION_C_HISTORICAL}")
    print()
    print("  convention D — live:")
    print(f"    Form D1: -h·(q⁴-q⁻⁴)/8 = {form_d1}")
    print(f"      diff = {diff_d1}")
    print(f"    Form D2: -h²·[2]_q·[2]_{{q²}}/8 = {form_d2}")
    print(f"      diff = {diff_d2}")
    print(f"    Form D3: -(q²-1)(q⁸-1)/(8q⁵) = {form_d3}")
    print(f"      diff = {diff_d3}")
    print()
    print("  convention C — historical, checked against the recorded C sym:")
    print(f"    Form 1: -h·(q-1)/(2·q^(1/2)) = {form_1}")
    print(f"      diff = {diff_1}")
    print(f"    Form 2: -[2]_{{q^(1/2)}}·h̃²/2 = {form_2}")
    print(f"      diff = {diff_2}")
    print(f"    Form 3: -(q^(1/2)+q^(-1/2))·(q^(1/2)-q^(-1/2))²/2 = {form_3}")
    print(f"      diff = {diff_3}")
    print()

    all_match = (str(diff_d1) == "0" and str(diff_d2) == "0"
                 and str(diff_d3) == "0")
    all_match_c = (str(diff_1) == "0" and str(diff_2) == "0"
                   and str(diff_3) == "0")

    builder.add_data("upstream_sym_q", str(sym_q_witness))
    builder.add_data("convention", "D")
    # Convention D — the live identity.
    builder.add_data("hecke_natural_form_D1_h_times_H_q4", str(form_d1))
    builder.add_data("hecke_natural_form_D2_h_sq_two_q_two_qsq", str(form_d2))
    builder.add_data("hecke_natural_form_D3_cyclotomic", str(form_d3))
    builder.add_data("diff_form_D1", str(diff_d1))
    builder.add_data("diff_form_D2", str(diff_d2))
    builder.add_data("diff_form_D3", str(diff_d3))
    builder.add_data("all_three_forms_match", all_match)
    # Convention C — historical, still checked, never compared to the live sym.
    builder.add_data("sym_q_convention_C_historical",
                     str(SYM_Q_CONVENTION_C_HISTORICAL))
    builder.add_data("hecke_natural_form_1_h_times_qm1_convention_C",
                     str(form_1))
    builder.add_data("hecke_natural_form_2_two_q_half_h_tilde_sq_convention_C",
                     str(form_2))
    builder.add_data("hecke_natural_form_3_explicit_t_basis_convention_C",
                     str(form_3))
    builder.add_data("diff_form_1_convention_C", str(diff_1))
    builder.add_data("diff_form_2_convention_C", str(diff_2))
    builder.add_data("diff_form_3_convention_C", str(diff_3))
    builder.add_data("all_three_forms_match_convention_C", all_match_c)

    builder.add_data("hecke_natural_reading", {
        "h_full_q": "q - q^(-1) — full-q bar-antisymmetric",
        "h_tilde_half_q": "q^(1/2) - q^(-1/2) — half-q bar-antisymmetric",
        "two_q_half": "q^(1/2) + q^(-1/2) — [2]_{q^(1/2)}",
        "sym_factorization": "PRODUCT of two bar-antisymmetric Hecke quantities ⟹ bar-symmetric under t ↔ 1/t",
        "candidate_categorical_reading": (
            "Wedge / antisymmetrized product of two Hecke bar-derivatives "
            "(h at full q, h̃ at half q). Suggests categorical reading "
            "as Lie bracket [h, h̃] or equivalently a 2-form curvature "
            "structure of the Hecke bar-involution. UNVERIFIED — "
            "requires identifying the categorical object that produces "
            "this projection in the canonical chain."
        ),
    })

    builder.add_data("anti_pattern_guard", (
        "This identifies the ALGEBRAIC FORM of sym, NOT a c_k closure. "
        "Numerical relation Q_β/m_e ≈ 140 · |sym| at q_proton would "
        "require a substrate constant ~140 (1/h² ≈ 102, [2]_q/h² ≈ 195 "
        "— neither hits cleanly). DO NOT wire as a derivation. To use "
        "this identity for Q_β requires identifying the CATEGORICAL "
        "OBJECT producing the sym projection — open research."
    ))

    builder.add_assertion(
        name="three_hecke_natural_forms_all_match_upstream_sym",
        # bool, not 1.0/0.0: this is a proof obligation, not a measurement,
        # and floats here were 3 of the raw-float64 fields the ratchet counts
        # against this witness for no informational gain.
        computed=bool(all_match),
        expected=True,
        tolerance=0,
        source="Exact algebraic identity (convention D): "
               "sym = -h·(q⁴-q⁻⁴)/8 = -h²·[2]_q·[2]_{q²}/8 "
               "= -(q²-1)(q⁸-1)/(8q⁵), verified via sympy after q→t² "
               "substitution against the LIVE upstream sym",
    )
    builder.add_assertion(
        name="convention_C_forms_still_match_the_recorded_C_sym",
        computed=bool(all_match_c),
        expected=True,
        tolerance=0,
        source="The three original (convention-C) forms against the recorded "
               "2026-08-08 C-era sym. Gated so the historical claim stays "
               "falsifiable instead of becoming folklore — it is NOT compared "
               "against the live upstream, which is convention D.",
    )

    out = builder.save()
    print(f"✓ Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
