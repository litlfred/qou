#!/usr/bin/env python3
"""Probe: hecke-markov-transition (`prop:hecke-markov-transition`).

Verifies the spectral-idempotent and transition-probability content
of the proposition, which gives a probabilistic interpretation to
each Hecke generator σ_i:

  (i) Spectral idempotents
        e_+^(i) = (σ_i + q⁻¹) / (q + q⁻¹)
        e_-^(i) = (q − σ_i)  / (q + q⁻¹)
      satisfy
        e_+ + e_-   = 𝟙
        (e_±)²      = e_±        (idempotent)
        e_+ · e_-   = 0           (orthogonal)
        σ_i         = q · e_+ − q⁻¹ · e_-     (spectral reconstruction)

  (ii) Transition probabilities
        p_+ = q  / (q + q⁻¹) = q² / (q² + 1)
        p_- = q⁻¹/ (q + q⁻¹) = 1  / (q² + 1)
      satisfy
        p_+ + p_- = 1
        p_+ / p_-  = q²

Each identity is checked numerically at q = q_0 in three Hoefsmit
reps: (3), (2,1), and (1,1,1) of H_3.  All residues at ~1e-50
(mpmath 50 dps).

Emits `hecke-markov-transition-probe.witness.json`.
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the `probes/` cluster subdirectory. The bridge
# module also puts every other cluster subdir on sys.path so
# cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))

from mpmath import mp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402
# `build_hoefsmit_mpfr` moved: it lived in
# `_deprecated/probes/probe_staircase_ew_k3_categorical.py`, root-level agent
# scratch untracked wholesale by 0763606e4, so this import has raised
# ModuleNotFoundError and THIS PRODUCER COULD NOT RUN AT ALL since. Recovered
# from history into hecke_character_symbolic, beside the symbolic twin and the
# standard_young_tableaux it is built on.
from hecke_character_symbolic import build_hoefsmit_mpfr  # noqa: E402
from q_parameter import Q_MP, Q_50_DIGIT_STR  # noqa: E402
from _precision import set_compute_dps  # noqa: E402


def _matrix_max_abs(M, dim: int) -> "mp.mpf":
    """Max |M[i,j]| across all entries (matrix-norm-like)."""
    return max(mp.fabs(M[i, j]) for i in range(dim) for j in range(dim))


def main() -> int:
    builder = WitnessBuilder(
        "hecke-markov-transition-probe",
        engine="mpmath",
    )
    set_compute_dps()

    q = Q_MP
    qi = 1 / q
    two_q = q + qi              # q + q⁻¹
    h = q - qi                  # h = q − q⁻¹

    # (ii) Transition probabilities — scalar identities.
    p_plus = q / two_q
    p_minus = qi / two_q
    # Keep residues at mp.mpf precision (flagged by
    # compute_no_mpf_to_float_cast — float() dropped).
    p_sum_residue = mp.fabs(p_plus + p_minus - mp.mpf(1))
    p_ratio_residue = mp.fabs(p_plus / p_minus - q * q)
    p_plus_alt_form = q * q / (q * q + 1)
    p_plus_form_residue = mp.fabs(p_plus - p_plus_alt_form)
    p_minus_alt_form = 1 / (q * q + 1)
    p_minus_form_residue = mp.fabs(p_minus - p_minus_alt_form)

    # (i) Spectral idempotents — check in three H_3 irreps.
    per_rep: list[dict] = []
    max_idem_residue = mp.mpf(0)
    for shape in [(3,), (2, 1), (1, 1, 1)]:
        sigmas, dim = build_hoefsmit_mpfr(shape, q)
        sigma = sigmas[0]
        I = mp.eye(dim)

        e_plus = (sigma + qi * I) / two_q
        e_minus = (q * I - sigma) / two_q

        # e_+ + e_- = I
        sum_check = e_plus + e_minus - I
        r_sum = float(_matrix_max_abs(sum_check, dim))

        # e_+² = e_+
        sq_plus = e_plus * e_plus - e_plus
        r_sq_plus = float(_matrix_max_abs(sq_plus, dim))

        # e_-² = e_-
        sq_minus = e_minus * e_minus - e_minus
        r_sq_minus = float(_matrix_max_abs(sq_minus, dim))

        # e_+ · e_- = 0
        cross = e_plus * e_minus
        r_cross = float(_matrix_max_abs(cross, dim))

        # σ = q · e_+ − q⁻¹ · e_-
        spec = q * e_plus - qi * e_minus - sigma
        r_spec = float(_matrix_max_abs(spec, dim))

        max_idem_residue = max(
            max_idem_residue,
            mp.mpf(r_sum), mp.mpf(r_sq_plus), mp.mpf(r_sq_minus),
            mp.mpf(r_cross), mp.mpf(r_spec),
        )
        per_rep.append({
            "shape": str(shape),
            "dim": dim,
            "completeness_e_plus_plus_e_minus_minus_I":
                r_sum,
            "idempotency_e_plus_sq_minus_e_plus": r_sq_plus,
            "idempotency_e_minus_sq_minus_e_minus": r_sq_minus,
            "orthogonality_e_plus_times_e_minus": r_cross,
            "spectral_reconstruction_residue": r_spec,
        })

    (
        builder
        .set_description(
            "I1 probe for prop:hecke-markov-transition.  Verifies "
            "(i) spectral idempotents e_± = (σ ± q^{∓1}) / (q + q⁻¹) "
            "satisfy completeness, idempotency, orthogonality, and "
            "spectral reconstruction σ = q · e_+ − q⁻¹ · e_-, in "
            "three H_3 irreps {(3), (2,1), (1^3)}; and "
            "(ii) transition probabilities p_+ = q/(q+q⁻¹), "
            "p_- = q⁻¹/(q+q⁻¹) satisfy p_+ + p_- = 1, p_+/p_- = q², "
            "with alternative forms p_+ = q²/(q²+1), p_- = 1/(q²+1).  "
            "All residues at ~1e-50 (mpmath 50 dps)."
        )
        .set_content_block("prop:hecke-markov-transition")
        .add_parameter("q_0_50dps", Q_50_DIGIT_STR)
        .add_parameter("p_plus_at_q0", float(p_plus))
        .add_parameter("p_minus_at_q0", float(p_minus))
        .add_parameter("p_sum_residue", p_sum_residue)
        .add_parameter("p_ratio_minus_q_squared_residue", p_ratio_residue)
        .add_parameter("p_plus_form_residue", p_plus_form_residue)
        .add_parameter("p_minus_form_residue", p_minus_form_residue)
        .add_parameter("max_idempotent_residue_across_3_reps",
                       float(max_idem_residue))
        .add_data("per_rep_idempotent_checks", per_rep)
        .add_data("transition_probabilities", {
            "p_plus": float(p_plus),
            "p_minus": float(p_minus),
            "p_plus_plus_p_minus": float(p_plus + p_minus),
            "p_plus_over_p_minus": float(p_plus / p_minus),
            "q_squared": float(q * q),
        })
        .add_assertion(
            name="transition_probabilities_sum_to_one",
            computed=p_sum_residue,
            expected=0.0, tolerance=1e-40,
            unit="|p_+ + p_- − 1|",
            source="prop:hecke-markov-transition (ii).",
        )
        .add_assertion(
            name="transition_probabilities_ratio_equals_q_squared",
            computed=p_ratio_residue,
            expected=0.0, tolerance=1e-40,
            unit="|p_+/p_- − q²|",
            source="prop:hecke-markov-transition (ii).",
        )
        .add_assertion(
            name="transition_p_plus_alt_form",
            computed=p_plus_form_residue,
            expected=0.0, tolerance=1e-40,
            unit="|q/(q+q⁻¹) − q²/(q²+1)|",
            source="prop:hecke-markov-transition (ii) closed form.",
        )
        .add_assertion(
            name="transition_p_minus_alt_form",
            computed=p_minus_form_residue,
            expected=0.0, tolerance=1e-40,
            unit="|q⁻¹/(q+q⁻¹) − 1/(q²+1)|",
            source="prop:hecke-markov-transition (ii) closed form.",
        )
        .add_assertion(
            name="spectral_idempotents_satisfy_all_identities",
            computed=float(max_idem_residue),
            expected=0.0, tolerance=1e-40,
            unit=(
                "max over {(3), (2,1), (1^3)} × {completeness, "
                "idempotency e_+, idempotency e_-, orthogonality, "
                "spectral reconstruction} of the matrix-entry residue"
            ),
            source=(
                "prop:hecke-markov-transition (i) — completeness, "
                "idempotency, orthogonality, and σ = q·e_+ − q⁻¹·e_- "
                "on the three H_3 Hoefsmit-seminormal irreps."
            ),
        )
    )

    out = builder.save()
    print(f"\nWitness: {out}")
    print()
    print("Transition probabilities at q_0:")
    print(f"  p_+         = {float(p_plus):.12f}")
    print(f"  p_-         = {float(p_minus):.12f}")
    print(f"  p_+ + p_-   = {float(p_plus + p_minus):.12f}  (residue {p_sum_residue:.2e})")
    print(f"  p_+/p_-     = {float(p_plus / p_minus):.12f}  (vs q² = {float(q*q):.12f})")
    print()
    print("Spectral idempotents per rep (matrix-entry residues):")
    for r in per_rep:
        print(f"  {r['shape']:<12} dim={r['dim']}:")
        print(f"    e_+ + e_-  = I:   {r['completeness_e_plus_plus_e_minus_minus_I']:.2e}")
        print(f"    e_+² = e_+:        {r['idempotency_e_plus_sq_minus_e_plus']:.2e}")
        print(f"    e_-² = e_-:        {r['idempotency_e_minus_sq_minus_e_minus']:.2e}")
        print(f"    e_+ · e_- = 0:     {r['orthogonality_e_plus_times_e_minus']:.2e}")
        print(f"    σ = q·e_+ − q⁻¹·e_-: {r['spectral_reconstruction_residue']:.2e}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
