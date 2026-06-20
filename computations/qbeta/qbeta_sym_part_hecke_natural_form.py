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
        "Hecke-natural closed form for sym(Δtr_M)(q): "
        "exact algebraic identity sym = -h·(q-1)/(2·q^(1/2)) = "
        "-[2]_{q^(1/2)}·h̃²/2 with h = q-q⁻¹, h̃ = q^(1/2)-q^(-1/2)."
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

    # Three equivalent forms
    form_1 = -h * (q - 1) / (2 * sp.sqrt(q))
    form_2 = -two_q_half * h_tilde ** 2 / 2
    form_3 = -(sp.sqrt(q) + 1 / sp.sqrt(q)) * (sp.sqrt(q) - 1 / sp.sqrt(q)) ** 2 / 2

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

    diff_1 = _verify_zero(form_1, sym_q_witness)
    diff_2 = _verify_zero(form_2, sym_q_witness)
    diff_3 = _verify_zero(form_3, sym_q_witness)

    print(f"sym (from upstream witness): {sym_q_witness}")
    print(f"Form 1: -h·(q-1)/(2·q^(1/2)) = {form_1}")
    print(f"  diff = {diff_1}")
    print(f"Form 2: -[2]_{{q^(1/2)}}·h̃²/2 = {form_2}")
    print(f"  diff = {diff_2}")
    print(f"Form 3: -(q^(1/2)+q^(-1/2))·(q^(1/2)-q^(-1/2))²/2 = {form_3}")
    print(f"  diff = {diff_3}")
    print()

    all_match = (str(diff_1) == "0" and str(diff_2) == "0" and str(diff_3) == "0")

    builder.add_data("upstream_sym_q", str(sym_q_witness))
    builder.add_data("hecke_natural_form_1_h_times_qm1", str(form_1))
    builder.add_data("hecke_natural_form_2_two_q_half_h_tilde_sq", str(form_2))
    builder.add_data("hecke_natural_form_3_explicit_t_basis", str(form_3))
    builder.add_data("diff_form_1", str(diff_1))
    builder.add_data("diff_form_2", str(diff_2))
    builder.add_data("diff_form_3", str(diff_3))
    builder.add_data("all_three_forms_match", all_match)

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
        computed=1.0 if all_match else 0.0,
        expected=1.0,
        tolerance=0.0,
        source="Exact algebraic identity verified via sympy after q→t² substitution",
    )

    out = builder.save()
    print(f"✓ Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
