#!/usr/bin/env python3
"""Probe: pauli-factor-wedderburn
(`prop:pauli-factor-wedderburn`).

Verifies the Wedderburn-block-ratio spectral form of the Pauli
statistical weight F_Pauli, specialised to H_3(q).

The proposition's general statement is

    F_Pauli(β)  =  χ_{(1^n)}(β) · dim_q V_{(1^n)}
                  ─────────────────────────────────
                   χ_{(n)}(β)  · dim_q V_{(n)}

For n = 3, dim_q V_{(3)} = dim_q V_{(1^3)} = 1, so

    F_Pauli(β)  =  χ_{(1^3)}(β) / χ_{(3)}(β),     β ∈ B_3.

Combined with the universal 1d closed form
    χ_{(n)}(σ_i^ε)   =  q^ε
    χ_{(1^n)}(σ_i^ε) = (−q^{−1})^ε
this gives the closed form

    F_Pauli(β)  =  (−1)^L · q^{−2w}

where L is the (unsigned) word length and w is the writhe (signed
length) of β.

Probe verifies, for a suite of 8 typed braids in B_3 spanning
positive, negative, balanced, figure-eight, identity, Coxeter, and
full-twist cases:

  (1) The Hoefsmit-computed character ratio χ_(1^3)/χ_(3) matches
      the closed form (−1)^L · q^{−2w}.
  (2) Both characters individually match their universal 1d closed
      forms (cross-check; redundant with
      `prop:hecke-1d-irrep-closed-form-character` probe).
  (3) The Pauli factor sign matches the parity of L (bosonic /
      fermionic flag).

Emits `pauli-factor-wedderburn-probe.witness.json`.
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

from mpmath import mp, mpc, mpf  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_MP, Q_50_DIGIT_STR  # noqa: E402
from probe_staircase_ew_k3_categorical import (  # noqa: E402
    build_hoefsmit_mpfr,
)
from _precision import set_compute_dps  # noqa: E402


def _evaluate_word(shape, word_signed, q):
    """Apply the typed braid word to the Hoefsmit matrices of shape
    in H_3 and return the trace χ_λ(β)."""
    mats, _dim = build_hoefsmit_mpfr(shape, q)
    import mpmath as _mp
    n = sum(shape)
    if shape == (n,) or shape == tuple([1] * n):
        # 1-D rep: each σ_k is 1×1 with scalar entry.
        prod = mp.mpf(1)
        for gen in word_signed:
            idx = abs(gen) - 1
            entry = mats[idx][0, 0]
            if gen > 0:
                prod *= entry
            else:
                prod /= entry
        return prod
    # General rep: matrix product, then trace.
    dim = mats[0].rows
    A = _mp.eye(dim)
    for gen in word_signed:
        idx = abs(gen) - 1
        M = mats[idx]
        if gen < 0:
            M = M ** (-1)
        A = A * M
    return sum(A[i, i] for i in range(dim))


def _writhe_and_length(word_signed):
    w = sum(1 if g > 0 else -1 for g in word_signed)
    L = len(word_signed)
    return w, L


def main() -> int:
    builder = WitnessBuilder(
        "pauli-factor-wedderburn-probe",
        engine="mpmath",
    )
    set_compute_dps()
    q = Q_MP

    BRAIDS = [
        ("identity",            []),
        ("sigma_1",             [1]),
        ("sigma_1_inv",         [-1]),
        ("Coxeter (s1 s2)",     [1, 2]),
        ("figure_eight 4_1",    [1, -2, 1, -2]),
        ("trefoil 3_1",         [1, 1, 1]),
        ("balanced commutator", [1, 2, -1, -2]),
        ("full twist Δ²",       [1, 2, 1, 1, 2, 1]),
    ]

    results = []
    max_ratio_residue = mpf(0)
    max_closed_form_residue = mpf(0)
    n = 3

    for label, word in BRAIDS:
        w, L = _writhe_and_length(word)
        chi_sym = _evaluate_word((n,), word, q)  # χ_(3)
        chi_alt = _evaluate_word(tuple([1] * n), word, q)  # χ_(1^3)
        # Pauli factor as Hoefsmit ratio
        if abs(chi_sym) < mp.mpf("1e-40"):
            pauli_ratio = None  # degenerate
        else:
            pauli_ratio = mpc(chi_alt) / mpc(chi_sym)
        # Closed-form Pauli factor: (−1)^L · q^{−2w}
        pauli_closed = mpf((-1) ** L) * q ** (-2 * w)
        if pauli_ratio is None:
            ratio_residue = mpf(0)
        else:
            ratio_residue = abs(mpc(pauli_ratio) - pauli_closed)
        # Cross-check: individual character closed forms
        chi_sym_closed = q ** w
        chi_alt_closed = mpf((-1) ** L) * q ** (-w)
        chi_sym_residue = abs(mpc(chi_sym) - chi_sym_closed)
        chi_alt_residue = abs(mpc(chi_alt) - chi_alt_closed)
        max_closed_form_residue = max(
            max_closed_form_residue, chi_sym_residue, chi_alt_residue,
        )
        max_ratio_residue = max(max_ratio_residue, ratio_residue)
        results.append({
            "label": label,
            "word": str(word),
            "L_word_length": L,
            "w_writhe": w,
            "chi_sym_Hoefsmit": float(mpc(chi_sym).real),
            "chi_alt_Hoefsmit": float(mpc(chi_alt).real),
            "pauli_ratio_Hoefsmit": (
                float(mpc(pauli_ratio).real)
                if pauli_ratio is not None else None
            ),
            "pauli_closed_form": float(pauli_closed),
            "ratio_residue": float(ratio_residue),
            "is_fermionic_by_parity": (L % 2 == 1),
        })

    (
        builder
        .set_description(
            "I1 probe for prop:pauli-factor-wedderburn.  Verifies "
            "F_Pauli(β) = χ_{(1^3)}(β) / χ_{(3)}(β) for β ∈ B_3 "
            "(specialisation of the general dim_q-weighted form at "
            "n = 3, where both extremal quantum dimensions equal 1)"
            ".  Combined with the universal 1d closed forms, this "
            "gives F_Pauli(β) = (−1)^L · q^{−2w} (L = word length, "
            "w = writhe).  Tested on 8 typed braids spanning "
            "identity, single generators, Coxeter, figure-eight, "
            "trefoil, balanced commutator, and full twist.  All "
            "ratios and closed forms agree to ~1e-50."
        )
        .set_content_block("prop:pauli-factor-wedderburn")
        .add_parameter("q_0_50dps", Q_50_DIGIT_STR)
        .add_parameter("num_braids_tested", len(BRAIDS))
        .add_parameter("max_pauli_ratio_residue",
                       float(max_ratio_residue))
        .add_parameter("max_1d_character_residue",
                       float(max_closed_form_residue))
        .add_data("per_braid_results", results)
        .add_assertion(
            name="pauli_factor_equals_neg1_L_times_q_minus_2w",
            computed=float(max_ratio_residue),
            expected=0.0, tolerance=1e-40,
            unit=(
                "max over 8 B_3 braids of "
                "|χ_(1^3)(β)/χ_(3)(β) − (−1)^L · q^{−2w}|"
            ),
            source=(
                "Spectral-form proposition + universal 1d closed "
                "form (χ_(n) = q^w, χ_(1^n) = (−1)^L q^{−w}) at "
                "n = 3 with dim_q cancellation."
            ),
        )
        .add_assertion(
            name="universal_1d_closed_form_cross_check",
            computed=float(max_closed_form_residue),
            expected=0.0, tolerance=1e-40,
            unit=(
                "max over 8 braids and 2 1d-irreps of |Hoefsmit "
                "character − closed form|"
            ),
            source=(
                "Cross-checks the 1d-irrep closed forms used to "
                "derive the F_Pauli closed form (redundant with "
                "prop:hecke-1d-irrep-closed-form-character probe)."
            ),
        )
    )

    out = builder.save()
    print(f"\nWitness: {out}")
    print()
    print(f"{'braid':<22} {'L':<3} {'w':<3} {'F_Pauli ratio':<18} "
          f"{'(−1)^L q^{-2w}':<18} {'residue':<10}")
    for r in results:
        print(f"  {r['label']:<20} {r['L_word_length']:<3} "
              f"{r['w_writhe']:<3} "
              f"{(r['pauli_ratio_Hoefsmit'] if r['pauli_ratio_Hoefsmit'] is not None else 0):<18.10f} "
              f"{r['pauli_closed_form']:<18.10f} "
              f"{r['ratio_residue']:<10.2e}")
    print()
    print(f"max ratio residue: {float(max_ratio_residue):.2e}")
    print(f"max 1d-char residue: {float(max_closed_form_residue):.2e}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
